"""
License:
PyIIDES
Copyright 2024 Carnegie Mellon University.
NO WARRANTY. THIS CARNEGIE MELLON UNIVERSITY AND SOFTWARE ENGINEERING INSTITUTE MATERIAL IS FURNISHED ON AN "AS-IS" BASIS. CARNEGIE MELLON UNIVERSITY MAKES NO WARRANTIES OF ANY KIND, EITHER EXPRESSED OR IMPLIED, AS TO ANY MATTER INCLUDING, BUT NOT LIMITED TO, WARRANTY OF FITNESS FOR PURPOSE OR MERCHANTABILITY, EXCLUSIVITY, OR RESULTS OBTAINED FROM USE OF THE MATERIAL. CARNEGIE MELLON UNIVERSITY DOES NOT MAKE ANY WARRANTY OF ANY KIND WITH RESPECT TO FREEDOM FROM PATENT, TRADEMARK, OR COPYRIGHT INFRINGEMENT.
Licensed under a MIT (SEI)-style license, please see license.txt or contact permission@sei.cmu.edu for full terms.
[DISTRIBUTION STATEMENT A] This material has been approved for public release and unlimited distribution.  Please see Copyright notice for non-US Government use and distribution.
DM24-1597
"""
import json
import uuid
import datetime
import random
import string
import copy

from pyiides import (
    Bundle,
    Person,
    Accomplice,
    Incident,
    Insider,
    Organization,
    Job,
    Detection,
    Response,
    TTP,
    Target,
    Impact,
    LegalResponse,
    CourtCase,
    Charge,
    Sentence,
    Sponsor,
    Source,
    Stressor,
    Note,
    Collusion,
    OrgRelationship,
)
def json_to_Bundle(data):
    """
    Converts JSON objects in the `objects` attribute to Python classes.

    This method iterates over the JSON objects, converts them to corresponding Python classes,
    and handles special relationships (collusion, orgRelationship) between the objects.

    Args:
        data (json.loads): Loaded json data from an IIDES json bundle.

    Returns:
        Bundle: The Bundle instance with all initializations and relationships set.

    Example:
        b = json_to_Bundle("Examples/fake_example.json")
    """
    
    # Get the objects from the Json
    json_objects = data.get("objects")
    
    all_classes = {}
    relationships = []
    special_relationships = []

    # Iterate through each object in the bundle's objects
    for json_object in json_objects:
        tag, pyiides_class = object_to_class(json_object)
        if tag == "Other":
            special_relationships.append(json_object)
        elif tag == "relationship":
            relationships.append(json_object)
        else:
            all_classes.setdefault(tag, []).append(pyiides_class)
    
    # Handle special relationships (e.g., collusion, orgRelationship)
    for special_relationship in special_relationships:
        full_id = special_relationship.get("id")
        index = full_id.find("--")
        tag = full_id[:index]
        relationship_id = full_id[index + 2:]

        if tag == "collusion":
            insiders = []
            for class_list in all_classes.values():
                for class_instance in class_list:
                    if len(insiders) == 2:
                        break
                    if isinstance(class_instance, Insider) and (class_instance.id == special_relationship.get("insider1").id or class_instance.id == special_relationship.get("insider2").id):
                        #TODO: The indexing above fails.
                        insiders.append(class_instance)
            if len(insiders) == 2:
                collusion = Collusion(id=relationship_id, insider1=insiders[0], insider2=insiders[1], relationship=special_relationship.get("relationship"), recruitment=special_relationship.get("recruitment"))
                all_classes.setdefault(tag, []).append(collusion)
        else:
            organizations = []
            for class_list in all_classes.values():
                for class_instance in class_list:
                    if len(organizations) == 2:
                        break
                    org1 = special_relationship.get("org1")
                    org2 = special_relationship.get("org2")
                    if isinstance(class_instance, Organization) and (class_instance.id == org1[0:org1.find("--")] or class_instance.id == org2[0:org2.find("--")]):
                        organizations.append(class_instance)
            if len(organizations) == 2:
                org_relationship = OrgRelationship(id=relationship_id, org1=organizations[0], org2=organizations[1], relationship=special_relationship.get("relationship"))
                all_classes.setdefault(tag, []).append(org_relationship)

    # Establish relationships if incident exists
    incident = all_classes.get("incident", [None])[0]

    if incident:
        detection = all_classes.get("detection")
        if detection:
            incident.detection = detection[0]

        targets = all_classes.get("target")
        if targets:
            incident.targets = targets

        sources = all_classes.get("source")
        if sources:
            incident.sources = sources
        
        notes = all_classes.get("note")
        if notes:
            incident.notes = notes
        
        ttps = all_classes.get("ttp")
        if ttps:
            incident.ttps = ttps

        # Establish response chain
        response = all_classes.get("response", [None])[0]
        if response:
            incident.response = response
            
            legal_response = all_classes.get("legal-response", [None])[0]
            if legal_response:
                response.legal_response = legal_response
                
                court_cases = all_classes.get("court-case")
                if court_cases and len(court_cases) == 1:
                    legal_response.court_cases = court_cases

                    charges = all_classes.get("charge")
                    if charges:
                        court_cases[0].charges = charges 

                    sentences = all_classes.get("sentence")
                    if sentences:
                        court_cases[0].sentences = sentences
                elif court_cases:
                    legal_response.court_cases = court_cases

        impacts = all_classes.get("impact")
        if impacts:
            incident.impacts = impacts 
        
        insiders = all_classes.get("insider")
        if insiders:
            incident.insiders = insiders 
        
        organizations = all_classes.get("organization")
        if organizations:
            incident.organizations = organizations

    # Add user-defined relationships using the relationships list
    for relationship in relationships:
        object1_id = relationship.get("object1")
        object2_id = relationship.get("object2")
        add_relation(all_classes, object1_id, object2_id)
    
    return Bundle(objects=all_classes)

def Bundle_to_json(bundle):
    """
    Converts Python classes in the `objects` attribute back to JSON objects and writes to a file.

    This method processes the Python classes in the `objects` attribute, converting them back into JSON objects, including any relationships between them, and writes the JSON representation to a specified file.

    Args:
        path (str): The file path where the JSON object will be written.
    """
    json_objects = []
    all_instances = []

    # Collect all class instances from the dictionary
    for obj in bundle.objects.values():
        all_instances.extend(obj)

    # Convert each class instance to a JSON object
    for class_instance in all_instances:
        json_object, relationships = class_instance.to_dict()
        json_objects.append(json_object)

        object1_id = json_object.get("id")
        if relationships:
            for object2_id in relationships:
                relationship_struct = {
                    "id": f"relationship--{uuid.uuid4()}",
                    "object1": object1_id,
                    "object2": object2_id
                }
                json_objects.append(relationship_struct)

    # Create the final bundle dictionary
    bundle_dict = {
        "id": f"bundle--{bundle.id}",
        "objects": json_objects
    }

    # Convert the bundle dictionary to a JSON string
    json_string = json.dumps(bundle_dict, indent=4)

    # Write the JSON string to the specified file
    return json_string


def date_str_to_obj(s: str) -> datetime.date:
    if s == None:
        return None

    return datetime.datetime.fromisoformat(s)


def datetime_str_to_obj(s: str) -> datetime.datetime:
    if s == None:
        return None

    return datetime.datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ")


def object_to_class(json_object):
    """
    Converts a JSON object to its corresponding Python class based on its ID tag.

    Args:
        json_object (dict): The JSON object to be converted.

    Returns:
        tuple: A tuple containing the tag and the corresponding Python class instance.
    """
    full_id = json_object.get("id")
    separator_index = full_id.find("--")
    tag = full_id[:separator_index]
    object_id = full_id[separator_index + 2:]

    json_object["id"] = object_id

    if tag == "accomplice":
        return tag, Accomplice(**json_object)

    if tag == "charge":
        return tag, Charge(**json_object)

    if tag == "court-case":
        return tag, CourtCase(**json_object)

    if tag == "detection":
        json_object["first_detected"] = datetime_str_to_obj(json_object.get("first_detected"))
        return tag, Detection(**json_object)

    if tag == "impact":
        return tag, Impact(**json_object)

    if tag == "incident":
        return tag, Incident(**json_object)

    if tag == "insider":
        predispositions = json_object.get("predispositions")
        if predispositions:
            json_object["predispositions"] = [tuple(item) for item in predispositions]

        concerning_behaviors = json_object.get("concerning_behaviors")
        if concerning_behaviors:
            json_object["concerning_behaviors"] = [tuple(item) for item in concerning_behaviors]

        return tag, Insider(**json_object)

    if tag == "job":
        json_object["hire_date"] = date_str_to_obj(json_object.get("hire_date"))
        json_object["departure_date"] = date_str_to_obj(json_object.get("departure_date"))

        if json_object.get("hire_date") and json_object.get("departure_date"):
            json_object["tenure"] = json_object["departure_date"] - json_object["hire_date"]

        return tag, Job(**json_object)

    if tag == "legal-response":
        json_object["law_enforcement_contacted"] = date_str_to_obj(json_object.get("law_enforcement_contacted"))
        json_object["insider_arrested"] = date_str_to_obj(json_object.get("insider_arrested"))
        json_object["insider_charged"] = date_str_to_obj(json_object.get("insider_charged"))
        json_object["insider_pleads"] = date_str_to_obj(json_object.get("insider_pleads"))
        json_object["insider_judgment"] = date_str_to_obj(json_object.get("insider_judgment"))
        json_object["insider_sentenced"] = date_str_to_obj(json_object.get("insider_sentenced"))
        json_object["insider_charges_dropped"] = date_str_to_obj(json_object.get("insider_charges_dropped"))
        json_object["insider_charges_dismissed"] = date_str_to_obj(json_object.get("insider_charges_dismissed"))
        json_object["insider_settled"] = date_str_to_obj(json_object.get("insider_settled"))

        return tag, LegalResponse(**json_object)
    
    if tag == "note":
        date_str = json_object.get("date")
        if date_str:
            json_object["date"] = datetime.datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
        return tag, Note(**json_object)

    if tag == "organization":
        return tag, Organization(**json_object)

    if tag == "person":
        return tag, Person(**json_object)
        #TODO, fix, insider holds a lot of person attributes, and needs them imported here

    if tag == "response":
        return tag, Response(**json_object)

    if tag == "sentence":
        return tag, Sentence(**json_object)

    if tag == "source":
        json_object["date"] = datetime_str_to_obj(json_object.get("date"))
        return tag, Source(**json_object)

    if tag == "sponsor":
        return tag, Sponsor(**json_object)

    if tag == "stressor":
        date_str = json_object.get("date")
        if date_str:
            json_object["date"] = datetime.datetime.fromisoformat(date_str)
        return tag, Stressor(**json_object)

    if tag == "target":
        return tag, Target(**json_object)

    if tag == "ttp":
        date_str = json_object.get("date")
        if date_str:
            json_object["date"] = datetime.datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
        return tag, TTP(**json_object)

    if tag == "relationship":
        json_object["id"] = f"{tag}--{object_id}"
        return "relationship", None

    json_object["id"] = f"{tag}--{object_id}"
    return "Other", None


def find_class(classes_dict, tag, id):
    """
    Finds and returns a class instance from a dictionary based on the tag and id.

    Args:
        classes_dict (dict): Dictionary containing lists or single instances of classes, keyed by tag.
        tag (str): The tag associated with the class to find.
        id (str): The unique identifier of the class instance to find.

    Returns:
        object: The class instance with the matching id, or None if not found.
    """
    class_list_or_instance = classes_dict.get(tag)

    if class_list_or_instance is None:
        return None

    if isinstance(class_list_or_instance, list):
        for class_instance in class_list_or_instance:
            if class_instance.id == id:
                return class_instance
    elif class_list_or_instance.id == id:
        return class_list_or_instance
    
    return None

def add_relation(classes_dict, id1, id2):
    """
    Adds a relationship between two class instances based on their IDs.

    Args:
        classes_dict (dict): Dictionary containing lists or single instances of classes, keyed by tag.
        id1 (str): The unique identifier of the first class instance.
        id2 (str): The unique identifier of the second class instance.

    Raises:
        ReferenceError: If one of the classes for the specified IDs does not exist.
    """
    # Extract tag and UUID from id1
    index1 = id1.find("--")
    tag1 = id1[:index1]
    uuid1 = id1[index1 + 2:]

    # Extract tag and UUID from id2
    index2 = id2.find("--")
    tag2 = id2[:index2]
    uuid2 = id2[index2 + 2:]

    # Find the corresponding class instances
    class1 = find_class(classes_dict, tag1, uuid1)
    class2 = find_class(classes_dict, tag2, uuid2)

    # Check if either class instance does not exist
    if class1 is None or class2 is None:
        raise ReferenceError(f"One of the classes for the specified IDs does not exist. id1: {class1}, id2: {class2}")

    # Define the set of tags to identify the type of relationship
    relation = {tag1, tag2}

    # Establish relationships based on tags
    if "organization" in relation and "job" in relation:
        if tag1 == "job":
            class1.organization = class2
        else:
            class2.organization = class1
    elif "job" in relation and "accomplice" in relation:
        if tag1 == "job":
            class1.accomplice = class2
        else:
            class2.accomplice = class1
    elif "insider" in relation and "accomplice" in relation:
        if tag1 == "accomplice":
            class1.insider = class2 
        else:
            class2.insider = class1 
    elif "insider" in relation and "stressor" in relation:
        if tag1 == "stressor":
            class1.insider = class2
        else:
            class2.insider = class1 
    elif "organization" in relation and "stressor" in relation:
        if tag1 == "stressor":
            class1.organization = class2
        else:
            class2.organization = class1 
    elif "sponsor" in relation and "insider" in relation:
        if tag1 == "insider":
            class1.sponsor = class2
        else:
            class2.sponsor = class1 
    elif "sponsor" in relation and "accomplice" in relation:
        if tag1 == "accomplice":
            class1.sponsor = class2 
        else:
            class2.sponsor = class1 
    elif "court-case" in relation and "sentence" in relation:
        if tag1 == "sentence":
            class1.court_case = class2 
        else:
            class2.court_case = class1 
    elif "court-case" in relation and "charge" in relation:
        if tag1 == "charge":
            class1.court_case = class2 
        else:
            class2.court_case = class1 

def anonymize_bundle(bundle):
    """
    Args:
        bundle (Bundle): The bundle to anonymize.

    Returns:
        Bundle: The anonymized bundle with all personally identifiable information removed.
    """
    from pyiides.utils.helper_functions import extract_constants
    import random, string, copy, datetime

    def anonymize_case_number():
        part1 = random.randint(1, 9)
        year = random.randint(20, 99)
        case_type = "cr"  # Fixed case type
        case_id = random.randint(10000, 99999)
        judge_initials = ''.join(random.choices(string.ascii_uppercase, k=3))

        return f"{part1}:{year}-{case_type}-{case_id}-{judge_initials}"

    def anonymize_date(reference: datetime.datetime = None, latest_date: datetime.datetime = None) -> datetime.datetime:
        if reference:
            return reference + datetime.timedelta(days=random.randint(-30, 30))
        if latest_date:
            return latest_date + datetime.timedelta(days=random.randint(1, 45))
        return datetime.datetime.now()

    anon_firstname = "John"
    anon_middlename = "A."
    anon_lastname = "Doe"
    anon_victimorg = "Company A"
    anon_orgname = "Company X"
    random_state = random.choice(extract_constants("state-vocab-us"))

    anon_bundle = Bundle(objects=copy.deepcopy(bundle.objects))
    org_count = len(anon_bundle.objects.get("organization"))

    for class_list in anon_bundle.objects.values():
        for obj in class_list:
            if isinstance(obj, CourtCase):
                if hasattr(obj, 'case_number'):
                    obj.case_number = anonymize_case_number()
                if hasattr(obj, 'case_title'):
                    obj.case_title = f"USA v. {anon_lastname}"
                if hasattr(obj, 'court_state'):
                    obj.court_state = random_state
                if hasattr(obj, 'court_district'):
                    obj.court_district = random.choice(
                        ["Western District", "Eastern District", "Northern District", "Southern District"])
                if hasattr(obj, 'defendant'):
                    obj.defendant = [f"{anon_firstname} {anon_lastname}"]
                if hasattr(obj, 'plaintiff'):
                    obj.plaintiff = ["United States of America"]
                if hasattr(obj, 'comment'):
                    obj.comment = "Redacted for anonymity."

            elif isinstance(obj, Detection):
                if hasattr(obj, 'first_detected') and obj.first_detected:
                    obj.first_detected = anonymize_date(reference=obj.first_detected)
                if hasattr(obj, 'comment'):
                    obj.comment = "Redacted for anonymity."

            elif isinstance(obj, Impact):
                if hasattr(obj, 'comment'):
                    obj.comment = "Redacted for anonymity."

            elif isinstance(obj, Incident):
                if hasattr(obj, 'summary'):
                    obj.summary = "Redacted for anonymity."
                if hasattr(obj, 'brief_summary'):
                    obj.brief_summary = "Redacted for anonymity."
                if hasattr(obj, 'comment'):
                    obj.comment = "Redacted for anonymity."

            elif isinstance(obj, Insider):
                if hasattr(obj, 'first_name'):
                    obj.first_name = anon_firstname
                if hasattr(obj, 'last_name'):
                    obj.last_name = anon_lastname
                if hasattr(obj, 'middle_name'):
                    obj.middle_name = anon_middlename
                if hasattr(obj, 'suffix'):
                    obj.suffix = random.choice(extract_constants("suffix-vocab"))
                if hasattr(obj, 'alias') and obj.alias:
                    del obj.alias
                if hasattr(obj, 'city'):
                    obj.city = "City A"
                if hasattr(obj, 'state'):
                    obj.state = random_state
                if hasattr(obj, 'postal_code') and obj.postal_code:
                    del obj.postal_code
                if hasattr(obj, 'age'):
                    obj.age = random.randint(18, 65)
                if hasattr(obj, 'comment'):
                    obj.comment = "Redacted for anonymity."

            elif isinstance(obj, Job):
                if hasattr(obj, 'hire_date'):
                    obj.hire_date = anonymize_date(reference=obj.hire_date)
                if hasattr(obj, 'departure_date'):
                    obj.departure_date = anonymize_date(reference=obj.departure_date, latest_date=obj.hire_date)
                if hasattr(obj, 'tenure'):
                    obj.tenure = obj.departure_date - obj.hire_date
                if hasattr(obj, 'comment'):
                    obj.comment = "Redacted for anonymity."

            elif isinstance(obj, LegalResponse):
                if hasattr(obj, 'law_enforcement_contacted'):
                    obj.law_enforcement_contacted = anonymize_date(reference=obj.law_enforcement_contacted)
                if hasattr(obj, 'insider_arrested'):
                    obj.insider_arrested = anonymize_date(reference=obj.insider_arrested, latest_date=obj.law_enforcement_contacted)
                if hasattr(obj, 'insider_charged'):
                    obj.insider_charged = anonymize_date(reference=obj.insider_charged, latest_date=obj.insider_arrested)
                if hasattr(obj, 'insider_pleads'):
                    obj.insider_pleads = anonymize_date(reference=obj.insider_pleads, latest_date=obj.insider_charged)
                if hasattr(obj, 'insider_judgment'):
                    obj.insider_judgment = anonymize_date(reference=obj.insider_judgment, latest_date=obj.insider_pleads)
                if hasattr(obj, 'insider_sentenced'):
                    obj.insider_sentenced = anonymize_date(reference=obj.insider_sentenced, latest_date=obj.insider_judgment)
                if hasattr(obj, 'comment'):
                    obj.comment = "Redacted for anonymity."
                
            elif isinstance(obj, Response):
                if hasattr(obj, 'comment'):
                    obj.comment = "Redacted for anonymity."
                if hasattr(obj, 'technical_controls'):
                    for control in obj.technical_controls:
                        control[1] = anonymize_date(reference=date_str_to_obj(control[1]))
                if hasattr(obj, 'behavioral_controls'):
                    for control in obj.behavioral_controls:
                        control[1] = anonymize_date(reference=date_str_to_obj(control[1]))
                if hasattr(obj, 'investigation_events'):
                    for event in obj.investigation_events:
                        event[1] = anonymize_date(reference=date_str_to_obj(event[1]))
            elif isinstance(obj, Note):
                if hasattr(obj, 'date'):
                    obj.date = anonymize_date(reference=obj.date)
                if hasattr(obj, 'comment'):
                    obj.comment = "Redacted for anonymity."
            elif isinstance(obj, Organization):
                if hasattr(obj, 'name'):
                    obj.name = anon_orgname
                if hasattr(obj, 'city'):
                    obj.city = "City X"
                if hasattr(obj, 'state'):
                    obj.state = random_state
                if hasattr(obj, 'postal_code') and obj.postal_code:
                    del obj.postal_code
                if hasattr(obj, 'comment'):
                    obj.comment = "Redacted for anonymity."
                if org_count == 1:
                    obj.name = anon_victimorg
                    org_count -= 1
                else:
                    obj.name = f"{anon_orgname} {org_count}"
                    org_count -= 1

            elif isinstance(obj, Stressor):
                if hasattr(obj, 'date'):
                    obj.date = anonymize_date(reference=obj.date)
                if hasattr(obj, 'comment'):
                    obj.comment = "Redacted for anonymity."

            elif isinstance(obj, Target):
                if hasattr(obj, 'comment'):
                    obj.comment = "Redacted for anonymity."

            elif isinstance(obj, TTP):
                if hasattr(obj, 'date'):
                    obj.date = anonymize_date(reference=obj.date)
                if hasattr(obj, 'description'):
                    obj.description = "Redacted for anonymity."

            elif isinstance(obj, Sponsor):
                if hasattr(obj, 'name'):
                    obj.name = anon_orgname
                if hasattr(obj, 'comment'):
                    obj.comment = "Redacted for anonymity."
            
            elif isinstance(obj, Source):
                if hasattr(obj, 'date'):
                    obj.date = anonymize_date(reference=obj.date)
                if hasattr(obj, 'title'):
                    obj.title = "Redacted for anonymity."
                if hasattr(obj, 'document'):
                    obj.document = "Redacted for anonymity."
    for anon_list, origin_list in zip(anon_bundle.objects.values(), bundle.objects.values()):
        for anon_obj, obj, in zip(anon_list, origin_list):
            print(f"ANONY:{anon_obj}\n----------------------------------------\nORIGINAL:{obj}\n\n")
    # print(f"{anon_bundle.objects} \n--------------------\n {bundle.objects}")
    print("Anonymized bundle successfully.")
    return anon_bundle