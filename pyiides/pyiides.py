"""
License:
PyIIDES
Copyright 2024 Carnegie Mellon University.
NO WARRANTY. THIS CARNEGIE MELLON UNIVERSITY AND SOFTWARE ENGINEERING INSTITUTE
MATERIAL IS FURNISHED ON AN "AS-IS" BASIS. CARNEGIE MELLON UNIVERSITY MAKES NO
WARRANTIES OF ANY KIND, EITHER EXPRESSED OR IMPLIED, AS TO ANY MATTER
INCLUDING, BUT NOT LIMITED TO, WARRANTY OF FITNESS FOR PURPOSE OR
MERCHANTABILITY, EXCLUSIVITY, OR RESULTS OBTAINED FROM USE OF THE MATERIAL.
CARNEGIE MELLON UNIVERSITY DOES NOT MAKE ANY WARRANTY OF ANY KIND WITH RESPECT
TO FREEDOM FROM PATENT, TRADEMARK, OR COPYRIGHT INFRINGEMENT.
Licensed under a MIT (SEI)-style license, please see license.txt or contact
permission@sei.cmu.edu for full terms.
[DISTRIBUTION STATEMENT A] This material has been approved for public release
and unlimited distribution.  Please see Copyright notice for non-US Government
use and distribution.
DM24-1597
"""
import uuid
from datetime import datetime, timedelta
from datetime import date as dt
from pyiides.utils.helper_functions import (
    check_tenure, check_subtype, check_subtype_list, check_uuid, check_type, check_vocab, check_iides, check_tuple_list)


# --- Priority Content ---
class Person:
    """
    Initialize a Person instance.

    Args:
        first_name (str): The first, or given, name of the individual.
        middle_name (str): The middle name of the individual.
        last_name (str): The last, or family, name of the individual.
        suffix (str): The name suffix of the individual. A constant from 
                      `suffix-vocab <./vocab/suffix-vocab.html>`_.
        alias (list): A list of aliases (other names) the individual has used, and/or 
                      the anonymized names of the individual in court records. One or more string values.
        city (str): The city (or county/district) that the person resided in at the time of the incident.
        state (str): The state (or region) that the person resided in at the time of the incident.
        country (str): The country that the person resided in at the time of the incident. 
                       Public implementations should use the standard codes provided by ISO 3166-1 alpha-2.
        postal_code (int): The postal code that the person resided in at the time of the incident.
        country_of_citizenship (list): Citizenship(s) of the person. Public implementations 
                                       should use the standard codes provided by ISO 3166-1 alpha-2. One or more string values.
        nationality (list): The nationality or nationalities of the person. Public implementations 
                            should use the standard codes provided by ISO 3166-1 alpha-2. One or more string values.
        residency (str): Residency status if the person was not a citizen of the country where 
                         they resided during the incident. A constant from 
                         `residency-vocab <./vocab/residency-vocab.html>`_.
        gender (str): Sex or gender at the time of the incident. A constant from 
                      `gender-vocab <./vocab/gender-vocab.html>`_.
        age (int): Age at the time that the incident began.
        education (str): Highest level of education at the time the incident began. A constant from 
                         `education-vocab <./vocab/education-vocab.html>`_.
        marital_status (str): The marital status at the time of the incident. A constant from 
                              `marital-status-vocab <./vocab/marital-status-vocab.html>`_.
        number_of_children (int): The number of children that the person is responsible for, at the time of the incident.
        comment (str): Comments or clarifications regarding any of the Person properties.
        **kwargs (dict): Additional attributes for the person.

    Raises:
        TypeError: If any provided attribute is of the incorrect type.
        ValueError: If any provided attribute is of the incorrect vocabulary. 
    
    Examples:
        >>> from pyiides import Person
        >>> person = Person(first_name="John", last_name="Doe", city="New York", country="US")
        >>> print(person.first_name)
        John
        >>> print(person.city)
        New York
    """
    def __init__(self, first_name=None, middle_name=None, last_name=None, suffix=None, alias=None, city=None, state=None, country=None, postal_code=None, country_of_citizenship=None, nationality=None, residency=None, gender=None, age=None, education=None, marital_status=None, number_of_children=None, comment=None, **kwargs):
        check_type(first_name, str)
        self._first_name = first_name

        check_type(middle_name, str)
        self._middle_name = middle_name

        check_type(last_name, str)
        self._last_name = last_name

        check_type(suffix, str)
        check_vocab(suffix, 'suffix-vocab')
        self._suffix = suffix

        check_type(alias, list)
        if alias != None:
            for s in alias:
                check_type(s, str)
        self._alias = alias

        check_type(city, str)
        self._city = city

        check_type(state, str)
        check_vocab(state, 'state-vocab-us')
        self._state = state

        check_type(country, str)
        check_vocab(kwargs.get("country"), 'country-vocab')
        self._country = country

        check_type(postal_code, int)
        self._postal_code = postal_code

        check_type(country_of_citizenship, list)
        if country_of_citizenship != None:
            for s in country_of_citizenship:
                check_type(s, str)
        self._country_of_citizenship = country_of_citizenship

        check_type(nationality, list)
        if nationality != None:
            for s in nationality:
                check_type(s, str)
        self._nationality = nationality

        check_type(residency, str)
        check_vocab(residency, 'residency-vocab')
        self._residency = residency

        check_type(gender, str)
        check_vocab(gender, 'gender-vocab')
        self._gender = gender

        check_type(age, int)
        self._age = age

        check_type(education, str)
        check_vocab(education, 'education-vocab')
        self._education = education

        check_type(marital_status, str)
        check_vocab(marital_status, 'marital-status-vocab')
        self._marital_status = marital_status

        check_type(number_of_children, int)
        self._number_of_children = number_of_children

        check_type(comment, str)
        self._comment = comment

    def __repr__(self):
        return (f"Person("
                f"first_name={self.first_name}, "
                f"middle_name={self.middle_name}, "
                f"last_name={self.last_name}, "
                f"suffix={self.suffix}, "
                f"alias={self.alias}, "
                f"city={self.city}, "
                f"state={self.state}, "
                f"country={self.country}, "
                f"postal_code={self.postal_code}, "
                f"country_of_citizenship={self.country_of_citizenship}, "
                f"nationality={self.nationality}, "
                f"residency={self.residency}, "
                f"gender={self.gender}, "
                f"age={self.age}, "
                f"education={self.education}, "
                f"marital_status={self.marital_status}, "
                f"number_of_children={self.number_of_children}, "
                f"comment={self.comment})")
    
    def to_dict(self):
        class_dict_copy = self.__dict__.copy()
        return ({
                    key.lstrip('_'): value for key, value in class_dict_copy.items()
                }, None)

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        check_type(value, str, allow_none=False)
        self._first_name = value

    @first_name.deleter
    def first_name(self):
        self._first_name = None

    @property
    def middle_name(self):
        return self._middle_name

    @middle_name.setter
    def middle_name(self, value):
        check_type(value, str, allow_none=False)
        self._middle_name = value

    @middle_name.deleter
    def middle_name(self):
        self._middle_name = None

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        check_type(value, str, allow_none=False)
        self._last_name = value

    @last_name.deleter
    def last_name(self):
        self._last_name = None

    @property
    def suffix(self):
        return self._suffix

    @suffix.setter
    def suffix(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'suffix-vocab')
        self._suffix = value

    @suffix.deleter
    def suffix(self):
        self._suffix = None

    @property
    def alias(self):
        return self._alias

    @alias.setter
    def alias(self, value):
        check_type(value, list, allow_none=False)
        for s in value:
            check_type(s, str, allow_none=False)
        self._alias = value

    def append_alias(self, item):
        check_type(item, str, allow_none=False)
        self._alias.append(item)

    @alias.deleter
    def alias(self):
        self._alias = None

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        check_type(value, str, allow_none=False)
        self._city = value

    @city.deleter
    def city(self):
        self._city = None

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'state-vocab-us')
        self._state = value

    @state.deleter
    def state(self):
        self._state = None

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'country-vocab')
        self._country = value

    @country.deleter
    def country(self):
        self._country = None

    @property
    def postal_code(self):
        return self._postal_code

    @postal_code.setter
    def postal_code(self, value):
        check_type(value, int, allow_none=False)
        self._postal_code = value

    @postal_code.deleter
    def postal_code(self):
        self._postal_code = None

    @property
    def country_of_citizenship(self):
        return self._country_of_citizenship

    @country_of_citizenship.setter
    def country_of_citizenship(self, value):
        check_type(value, list, allow_none=False)
        for s in value:
            check_type(s, str, allow_none=False)
        self._country_of_citizenship = value

    def append_country_of_citizenship(self, item):
        check_type(item, str, allow_none=False)
        self._country_of_citizenship.append(item)

    @country_of_citizenship.deleter
    def country_of_citizenship(self):
        self._country_of_citizenship = None

    @property
    def nationality(self):
        return self._nationality

    @nationality.setter
    def nationality(self, value):
        check_type(value, list, allow_none=False)
        for s in value:
            check_type(s, str, allow_none=False)
        self._nationality = value

    def append_nationality(self, item):
        check_type(item, str, allow_none=False)
        self._nationality.append(item)

    @nationality.deleter
    def nationality(self):
        self._nationality = None

    @property
    def residency(self):
        return self._residency

    @residency.setter
    def residency(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'residency-vocab')
        self._residency = value

    @residency.deleter
    def residency(self):
        self._residency = None

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'gender-vocab')
        self._gender = value

    @gender.deleter
    def gender(self):
        self._gender = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        check_type(value, int, allow_none=False)
        self._age = value

    @age.deleter
    def age(self):
        self._age = None

    @property
    def education(self):
        return self._education

    @education.setter
    def education(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'education-vocab')
        self._education = value

    @education.deleter
    def education(self):
        self._education = None

    @property
    def marital_status(self):
        return self._marital_status

    @marital_status.setter
    def marital_status(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'marital-status-vocab')
        self._marital_status = value

    @marital_status.deleter
    def marital_status(self):
        self._marital_status = None

    @property
    def number_of_children(self):
        return self._number_of_children

    @number_of_children.setter
    def number_of_children(self, value):
        check_type(value, int, allow_none=False)
        self._number_of_children = value

    @number_of_children.deleter
    def number_of_children(self):
        self._number_of_children = None

    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, value):
        check_type(value, str, allow_none=False)
        self._comment = value

    @comment.deleter
    def comment(self):
        self._comment = None



# --- Merged Content ---
class Bundle:
    """
    A class used to represent a Bundle of IIDES objects.

    Attributes:
        id (str): A unique identifier for the Bundle instance. If not provided,
            a new UUID is generated.
        objects (list): A list of objects contained within the bundle.
    """

    def __init__(self, id=None, objects=None):
        if id is None:
            id = str(uuid.uuid4())

        check_uuid(id)
        self._id = id

        # Add a type checking that the objects are IIDES objects or atleast follow the format
        check_iides(objects)
        self._objects = objects

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        check_uuid(value)
        self._id = value

    @property
    def objects(self):
        return self._objects

    @objects.setter
    def objects(self, value):
        check_iides(value)
        self._objects = value

    @objects.deleter
    def objects(self):
        self._objects = None


class Detection:
    """
    Initialize a Detection instance.

    Args:
        id (str): Unique identifier for the detection. Defaults to a new UUIDv4 string if not provided.
        first_detected (datetime): The date and time the victim organization first became aware of the incident.
        who_detected (list): The individual entities or teams that first detected the incident. One or more constants from 
                             `detection-team-vocab <./vocab/detection-team-vocab.html>`_.
        detected_method (list): The system or process that led to the first detection of the incident. One or more constants from 
                                `detection-method-vocab <./vocab/detection-method-vocab.html>`_.
        logs (list): The type(s) of logs used by the detection team and/or method to first detect the incident. One or more constants from 
                     `detection-log-vocab <./vocab/detection-log-vocab.html>`_.
        comment (str): Clarifying comments about who, what, when, or how the incident was detected.
        **kwargs (dict): Additional attributes for the detection.
    
    Raises:
        TypeError: If any provided attribute is of the incorrect type.
        ValueError: If any provided attribute is of the incorrect vocabulary. 
    
    Examples:
        >>> from datetime import datetime
        >>> from pyiides.pyiides.detection import Detection
        >>> detection = detection = Detection(
        ...     first_detected= datetime(2023, 1, 1, 0, 0, 0),
        ...     who_detected=["LE"],
        ...     detected_method=["1"],
        ...     logs=["AC"],
        ...     comment="Additional details about the detection."
        ... )
        >>> print(detection.first_detected)
        2023-01-1 00:00:00
    """
    def __init__(self, id=None, first_detected=None, who_detected=None, detected_method=None, logs=None, comment=None, **kwargs):
        if id == None:
            id = str(uuid.uuid4())

        check_uuid(id)
        self._id = id

        check_type(first_detected, datetime)
        self._first_detected = first_detected

        check_type(who_detected, list)
        check_vocab(who_detected, 'detection-team-vocab')
        self._who_detected = who_detected

        check_type(detected_method, list)
        check_vocab(detected_method, 'detection-method-vocab')
        self._detected_method = detected_method

        check_type(logs, list)
        check_vocab(logs, 'detection-log-vocab')
        self._logs = logs

        check_type(comment, str)
        self._comment = comment

        # RELATIONSHIPS
        self._incident = None  # belongs to incident

    def __repr__(self):
        return (f"Detection(id={self.id}, "
                f"first_detected={self.first_detected}, "
                f"who_detected={self.who_detected}, "
                f"detected_method={self.detected_method}, "
                f"logs={self.logs}, "
                f"comment={self.comment})")

    def to_dict(self):
        class_dict_copy = self.__dict__.copy()

        relationships = {'_incident'}

        class_dict_copy["_id"] = f"detection--{self.id}"
        if self.first_detected != None:
            class_dict_copy["_first_detected"] = str(self.first_detected)
        return ({
                    key.lstrip('_'): value 
                    for key, value in class_dict_copy.items()
                    if key not in relationships
                }, None)

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        check_uuid(value)
        self._id = value
    
    @property
    def first_detected(self):
        return self._first_detected

    @first_detected.setter
    def first_detected(self, value):   
        check_type(value, datetime, allow_none=False)
        self._first_detected = value
    
    @first_detected.deleter
    def first_detected(self):
        self._first_detected = None
    
    @property
    def who_detected(self):
        return self._who_detected
    
    @who_detected.setter
    def who_detected(self, value):
        check_type(value, list, allow_none=False)
        check_vocab(value, 'detection-team-vocab')
        self._who_detected = value
    
    def append_who_detected(self, item):
        check_type(item, str, allow_none=False)
        check_vocab(item, 'detection-team-vocab')
        self._who_detected.append(item)
    
    @who_detected.deleter
    def who_detected(self):
        self._who_detected = None
    
    @property
    def detected_method(self):
        return self._detected_method
    
    @detected_method.setter
    def detected_method(self, value):
        check_type(value, list, allow_none=False)
        check_vocab(value, 'detection-method-vocab')
        self._detected_method = value
    
    def append_detected_method(self, item):
        check_type(item, str, allow_none=False)
        check_vocab(item, 'detection-method-vocab')
        self._detected_method.append(item)
    
    @detected_method.deleter
    def detected_method(self):
        self._detected_method = None

    @property
    def logs(self):
        return self._logs
    
    @logs.setter
    def logs(self, value):
        check_type(value, list, allow_none=False)
        check_vocab(value, 'detection-log-vocab')
        self._logs = value
    
    def append_logs(self, item):
        check_type(item, str, allow_none=False)
        check_vocab(item, 'detection-log-vocab')
        self._logs.append(item)
    
    @logs.deleter
    def logs(self):
        self._logs = None
    
    @property
    def comment(self):
        return self._comment
    
    @comment.setter
    def comment(self, value):
        check_type(value, str, allow_none=False)
        self._comment = value

    @comment.deleter
    def comment(self):
        self._comment = None

    # - - - - - - - RELATIONSHIPS - - - - - - 
    @property
    def incident(self):
        return self._incident
    
    @incident.setter
    def incident(self, value):
        
        check_type(value, Incident, allow_none=False)
        self._incident = value
        if value.detection != self:
            value.detection = self
    
    @incident.deleter
    def incident(self):
        temp = self._incident
        self._incident = None
        if temp != None:
            del temp.detection


class Collusion:
    """
    Initializes a Collusion instance

    Args:
        id (string) : Unique identifier for the collusion. Defaults to a new UUIDv4 string if not provided.
        insider1 (required) (Insider) : The first insider involved in the collusion.
        insider2 (required) (Insider) : The second insider involved in the collusion.
        relationship (required) (string) : The relationship between the two insiders.
            A constant from `insider-relationship-vocab <./vocab/insider-relationship-vocab.html>`_.
        recruitment (required) (string) : The recruitment method or relationship between the insiders.
            A constant from `insider-recruitment-vocab <./vocab/insider-recruitment-vocab.html>`_.
    
    Raises:
        TypeError: If any provided attribute is of the incorrect type.
        ValueError: If any provided attribute is of the incorrect vocabulary.

    Example:
        >>> from pyiides.utils.helper_functions import Collusion
        >>> 
        >>> insider1 = Insider(first_name="John", last_name="Doe")
        >>> insider2 = Insider(first_name="Jane", last_name="Smith")
        >>> collusion = Collusion(
        ...     insider1=insider1,
        ...     insider2=insider2,
        ...     relationship="1",
        ...     recruitment="2"
        ... )
        >>> print(collusion.relationship)
        1
        >>> print(collusion.recruitment)
        2
    """
    def __init__(self, insider1, insider2, relationship, recruitment, id=None):
        if id == None:
            id = str(uuid.uuid4())

        check_uuid(id)
        self._id = id
        
        
        check_type(insider1, Insider)
        self._insider1 = insider1

        check_type(insider2, Insider)
        self._insider2 = insider2 

        check_type(relationship, str)
        check_vocab(relationship, 'insider-relationship-vocab')
        self._relationship = relationship

        check_type(recruitment, str)
        check_vocab(recruitment, 'insider-recruitment-vocab')
        self._recruitment = recruitment 
    
    def __repr__(self):
        return (f"Collusion(id={self.id}, "
                f"insider1={self.insider1!r}, "
                f"insider2={self.insider2!r}, "
                f"relationship={self.relationship}, "
                f"recruitment={self.recruitment})")

    def to_dict(self):
        class_dict_copy = self.__dict__.copy()
        class_dict_copy["_id"] = f"collusion--{self.id}"
        return ({ 
                    key.lstrip('_'): value for key, value in class_dict_copy.items() 
                }, None)

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        check_uuid(value)
        self._id = value
    
    @property 
    def insider1(self):
        return self._insider1

    @insider1.setter
    def insider1(self, value):
        
        check_type(value, Insider)
        self._insider1 = value

    @insider1.deleter
    def insider1(self):
        self._insider1 = None
    
    @property 
    def insider2(self):
        return self._insider2

    @insider2.setter
    def insider2(self, value):
        
        check_type(value, Insider)
        self._insider2 = value

    @insider2.deleter
    def insider2(self):
        self._insider2 = None
    
    @property
    def relationship(self):
        return self._relationship
    
    @relationship.setter
    def relationship(self, value):
        check_type(value, str)
        check_vocab(value, 'insider-relationship-vocab')
        self._relationship = value
    
    @relationship.deleter
    def relationship(self):
        self._relationship = None
    
    @property 
    def recruitment(self):
        return self._recruitment

    @recruitment.setter
    def recruitment(self, value):
        check_type(value, str)
        check_vocab(value, 'insider-recruitment-vocab')
        self._recruitment = value

    @recruitment.deleter
    def recruitment(self):
        self._recruitment = None


class LegalResponse:
    """
    Initializes a LegalResponse instance

    Args:
        id (required) (string) : Unique identifier for the legal response. Defaults to a new UUIDv4 string if not provided.
        law_enforcement_contacted (date) : Organization contacts law enforcement to aid in the investigation of the incident. E.g., Police are called to respond to the Insider's violent behavior in the workplace).
        insider_arrested (date) : Insider is taken into custody. E.g., Police arrest insider in their home.
        insider_charged (date) : Insider is formally charged. Charges must relate to the incident. This category also covers a waiver of indictment and subsequent filing of information. E.g., Insider was indicted on computer fraud charges.
        insider_pleads (date) : Insider puts forth a plea to the court, including guilty, not guilty, nolo contendere (no contest). E.g., Insider pleads guilty to computer intrusion.
        insider_judgment (date) : Insider is found guilty, not guilty, or liable or not liable in a court of law. E.g., Insider is found guilty in a jury trial.
        insider_sentenced (date) : Insider is given a legally mandated punishment. E.g., Insider sentenced to 5 months in jail, then supervised release, community service, and restitution.
        insider_charges_dropped (date) : The plaintiff drops their case against the insider. E.g., The organization in a civil suit decides to drop the suit.
        insider_charges_dismissed (date) : The plaintiff dismiss their case against the insider. E.g., Upon discovery of further evidence, the judge decided to drop the charges against the insider.
        insider_settled (date) : The case against the insider is settled outside of the courtroom. E.g., The victim organization reached an agreement with the insider to not file formal charges in return for financial compensation.
        comment (string) : Comments clarifying the details or dates of the legal response.
    
    Raises:
        TypeError: If any provided attribute is of the incorrect type.
        ValueError: If any provided attribute is of the incorrect vocabulary. 
    
    Example:
        >>> from pyiides.utils.helper_functions import LegalResponse
        >>> legal_response = LegalResponse(
        ...     id="6eaf8e6c-8c4d-4d9d-8f8e-6c8c4d4d9d8f",
        ...     law_enforcement_contacted=datetime.date(2023, 1, 1),
        ...     insider_arrested=datetime.date(2023, 1, 2),
        ...     insider_charged=datetime.date(2023, 1, 3),
        ...     insider_pleads=datetime.date(2023, 1, 4),
        ...     insider_judgment=datetime.date(2023, 1, 5),
        ...     insider_sentenced=datetime.date(2023, 1, 6),
        ...     insider_charges_dropped=datetime.date(2023, 1, 7),
        ...     insider_charges_dismissed=datetime.date(2023, 1, 8),
        ...     insider_settled=datetime.date(2023, 1, 9),
        ...     comment="This is a sample comment."
        ... )
        >>> print(legal_response.id)
        6eaf8e6c-8c4d-4d9d-8f8e-6c8c4d4d9d8f
        >>> print(legal_response.comment)
        This is a sample comment.
    """
    def __init__(self, id=None, law_enforcement_contacted=None, insider_arrested=None, insider_charged=None, insider_pleads=None, insider_judgment=None, insider_sentenced=None, insider_charges_dropped=None, insider_charges_dismissed=None, insider_settled=None, comment=None):
        if id is None:
            id = str(uuid.uuid4())
        check_uuid(id)
        self._id = id

        check_type(law_enforcement_contacted, dt)
        self._law_enforcement_contacted = law_enforcement_contacted

        check_type(insider_arrested, dt)
        self._insider_arrested = insider_arrested

        check_type(insider_charged, dt)
        self._insider_charged = insider_charged

        check_type(insider_pleads, dt)
        self._insider_pleads = insider_pleads

        check_type(insider_judgment, dt)
        self._insider_judgment = insider_judgment

        check_type(insider_sentenced, dt)
        self._insider_sentenced = insider_sentenced

        check_type(insider_charges_dropped, dt)
        self._insider_charges_dropped = insider_charges_dropped

        check_type(insider_charges_dismissed, dt)
        self._insider_charges_dismissed = insider_charges_dismissed

        check_type(insider_settled, dt)
        self._insider_settled = insider_settled

        check_type(comment, str)
        self._comment = comment

        # Relationship
        self._response = None
        self._court_cases = None

    def __repr__(self):
        return (f"LegalResponse(id={self.id}, "
                f"law_enforcement_contacted={self.law_enforcement_contacted}, "
                f"insider_arrested={self.insider_arrested}, "
                f"insider_charged={self.insider_charged}, "
                f"insider_pleads={self.insider_pleads}, "
                f"insider_judgment={self.insider_judgment}, "
                f"insider_sentenced={self.insider_sentenced}, "
                f"insider_charges_dropped={self.insider_charges_dropped}, "
                f"insider_charges_dismissed={self.insider_charges_dismissed}, "
                f"insider_settled={self.insider_settled}, "
                f"comment={self.comment})")

    def to_dict(self):
        class_dict_copy = self.__dict__.copy()
        relationships = {'_response', '_court_cases'}

        if self.law_enforcement_contacted != None:
            class_dict_copy["_law_enforcement_contacted"] = str(self.law_enforcement_contacted)

        if self.insider_arrested != None:
            class_dict_copy["_insider_arrested"] = str(self.insider_arrested)

        if self.insider_charged != None:
            class_dict_copy["_insider_charged"] = str(self.insider_charged)

        if self.insider_pleads != None:
            class_dict_copy["_insider_pleads"] = str(self.insider_pleads)

        if self.insider_judgment != None:
            class_dict_copy["_insider_judgment"] = str(self.insider_judgment)

        if self.insider_sentenced != None:
            class_dict_copy["_insider_sentenced"] = str(self.insider_sentenced)

        if self.insider_charges_dropped != None:
            class_dict_copy["_insider_charges_dropped"] = str(self.insider_charges_dropped)

        if self.insider_charges_dismissed != None:
            class_dict_copy["_insider_charges_dismissed"] = str(self.insider_charges_dismissed)

        if self.insider_settled != None:
            class_dict_copy["_insider_settled"] = str(self.insider_settled)

        class_dict_copy["_id"] = f"legal-response--{self.id}"
        return ({
                    key.lstrip('_'): value 
                    for key, value in class_dict_copy.items()
                    if key not in relationships
                }, None)

    @property
    def id(self):
        return self._id  

    @id.setter
    def id(self, value):
        check_uuid(value)
        self._id = value

    @property
    def law_enforcement_contacted(self):
        return self._law_enforcement_contacted
    
    @law_enforcement_contacted.setter
    def law_enforcement_contacted(self, value):
        check_type(value, dt, allow_none=False)
        self._law_enforcement_contacted = value
    
    @law_enforcement_contacted.deleter
    def law_enforcement_contacted(self):
        self._law_enforcement_contacted = None
    
    @property
    def insider_arrested(self):
        return self._insider_arrested

    @insider_arrested.setter
    def insider_arrested(self, value):
        check_type(value, dt, allow_none=False)
        self._insider_arrested = value

    @insider_arrested.deleter
    def insider_arrested(self):
        self._insider_arrested = None

    @property
    def insider_charged(self):
        return self._insider_charged

    @insider_charged.setter
    def insider_charged(self, value):
        check_type(value, dt, allow_none=False)
        self._insider_charged = value

    @insider_charged.deleter
    def insider_charged(self):
        self._insider_charged = None

    @property
    def insider_pleads(self):
        return self._insider_pleads

    @insider_pleads.setter
    def insider_pleads(self, value):
        check_type(value, dt, allow_none=False)
        self._insider_pleads = value

    @insider_pleads.deleter
    def insider_pleads(self):
        self._insider_pleads = None

    @property
    def insider_judgment(self):
        return self._insider_judgment

    @insider_judgment.setter
    def insider_judgment(self, value):
        check_type(value, dt, allow_none=False)
        self._insider_judgment = value

    @insider_judgment.deleter
    def insider_judgment(self):
        self._insider_judgment = None

    @property
    def insider_sentenced(self):
        return self._insider_sentenced

    @insider_sentenced.setter
    def insider_sentenced(self, value):
        check_type(value, dt, allow_none=False)
        self._insider_sentenced = value

    @insider_sentenced.deleter
    def insider_sentenced(self):
        self._insider_sentenced = None

    @property
    def insider_charges_dropped(self):
        return self._insider_charges_dropped

    @insider_charges_dropped.setter
    def insider_charges_dropped(self, value):
        check_type(value, dt, allow_none=False)
        self._insider_charges_dropped = value

    @insider_charges_dropped.deleter
    def insider_charges_dropped(self):
        self._insider_charges_dropped = None

    @property
    def insider_charges_dismissed(self):
        return self._insider_charges_dismissed

    @insider_charges_dismissed.setter
    def insider_charges_dismissed(self, value):
        check_type(value, dt, allow_none=False)
        self._insider_charges_dismissed = value

    @insider_charges_dismissed.deleter
    def insider_charges_dismissed(self):
        self._insider_charges_dismissed = None

    @property
    def insider_settled(self):
        return self._insider_settled

    @insider_settled.setter
    def insider_settled(self, value):
        check_type(value, dt, allow_none=False)
        self._insider_settled = value

    @insider_settled.deleter
    def insider_settled(self):
        self._insider_settled = None

    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, value):
        check_type(value, str, allow_none=False)
        self._comment = value

    @comment.deleter
    def comment(self):
        self._comment = None

    # relationships 
    @property
    def response(self):
        return self._response
    
    @response.setter
    def response(self, value):
        
        check_type(value, Response)
        self._response = value
        if value.legal_response != self:
            value.legal_response = self

    @response.deleter
    def response(self):
        temp = self._response
        self._response = None
        if temp != None:
            del temp.legal_response

    @property
    def court_cases(self):
        return self._court_cases

    @court_cases.setter
    def court_cases(self, value):
        check_type(value, list, allow_none=False)

        # check that all elements are court case objects
        for obj in value:
            
            check_type(obj, CourtCase, allow_none=False)

        # set new court case list
        # making sure to remove older relationships before
        # setting the new ones 
        if self._court_cases != None:
            # use list() to create a copy
            for cc in list(self._court_cases):
                del cc.legal_response
        self._court_cases = value

        # connect them back to this instance of legal response
        for obj in value: 
            if obj.legal_response != self:
                obj.legal_response = self
    
    def append_court_case(self, item):
        
        check_type(item, CourtCase, allow_none=False)

        if self._court_cases == None:
            self._court_cases = [item]
        else:
            self._court_cases.append(item)

        item.legal_response = self

    def remove_court_case(self, item):
        
        check_type(item, CourtCase, allow_none=False)
        if self._court_cases != None:
            del item.legal_response

    @court_cases.deleter
    def court_cases(self):
        # adding list() creates a copy so that we don't
        # run into any issues with removing elements
        # from the list we are iterating over
        for obj in list(self._court_cases):
            del obj.legal_response
        self._court_cases = None


class Stressor:
    """
    Initialize a Stressor instance

    Args:
        id (required) (string) : Unique identifier for the stressor. Defaults to a new UUIDv4 string if not provided.
        date (date) : The date the stressor first occurred.
        category (string) : The category to which the stressor belongs. 
            A constant from `stressor-category-vocab <./vocab/stressor-category-vocab.html>`_.
            Required if subcategory exists.
        subcategory (string) : The subcategory to which the stressor belongs. When subcategory is specified, category MUST also be specified. The subcategory constant MUST map to the specified category constant.
            A constant from `stressor-subcategory-vocab <./vocab/stressor-subcategory-vocab.html>`_.
        comment (string) : Clarifying comments about the stressor.

    Raises:
        TypeError: If any provided attribute is of the incorrect type.
        ValueError: If any provided attribute is of the incorrect vocabulary. 
    
    Example:
        >>> from pyiides import Stressor
        >>> stressor = Stressor(date=datetime.date(2023, 6, 14), category="2", subcategory="2.12", comment="High-pressure project deadline")
        >>> print(stressor.id)
        ac386e51-2f66-40fe-bfb7-c791019b2b97
        >>> print(stressor.date)
        2023-06-14
        >>> print(stressor.category)
        2
        >>> print(stressor.subcategory)
        2.12
        >>> print(stressor.comment)
        High-pressure project deadline
    """
    def __init__(self, id=None, date=None, category=None, subcategory=None, comment=None):
        if id == None:
            id = str(uuid.uuid4())

        check_uuid(id)
        self._id = id

        check_type(date, dt)
        self._date = date

        check_type(subcategory, str)
        check_vocab(subcategory, 'stressor-subcategory-vocab')
        self._subcategory = subcategory

        check_type(category, str)
        check_vocab(category, 'stressor-category-vocab')
        if self._subcategory != None and category == None:
            raise ReferenceError("The attribute category is required if subcategory exists")
        self._category = category

        check_type(comment, str)
        self._comment = comment

        # relationships 
        self._organization = None
        self._insider = None
    
    def __repr__(self):
        return (f"Stressor(id={self.id}, "
                f"date={self.date}, "
                f"category={self.category}, "
                f"subcategory={self.subcategory}, "
                f"comment={self.comment})")

    def to_dict(self):
        class_dict_copy = self.__dict__.copy()
        relationships = {'_organization', '_insider'}

        if self.date != None:
            class_dict_copy["date"] = str(self.date)

        class_dict_copy["_id"] = f"stressor--{self.id}"
        return ({
                    key.lstrip('_'): value 
                    for key, value in class_dict_copy.items()
                    if key not in relationships
                }, None)

    @property
    def id(self):
        return self._id  

    @id.setter
    def id(self, value):
        check_uuid(value)
        self._id = value
    
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        check_type(value, dt, allow_none=False)
        self._date = value
    
    @date.deleter
    def date(self):
        self._date = None
    
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'stressor-category-vocab')
        self._category = value

    @category.deleter
    def category(self):
        if self.subcategory != None:
            raise ReferenceError("The attribute category is required if subcategory exists")
        self._category = None

    @property
    def subcategory(self):
        return self._subcategory

    @subcategory.setter
    def subcategory(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'stressor-subcategory-vocab')
        self._subcategory = value

    @subcategory.deleter
    def subcategory(self):
        self._subcategory = None

    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, value):
        check_type(value, str, allow_none=False)
        self._comment = value

    @comment.deleter
    def comment(self):
        self._comment = None

    # - - - - - - - RELATIONSHIPS - - - - - - 

    @property
    def organization(self):
        return self._organization

    @organization.setter
    def organization(self, value):
        
        check_type(value, Organization, allow_none=False)

        # set the organization
        # first remove all old relationships 
        if self._organization != None:
            self._organization.stressors.remove(self)
        self._organization = value

        # add it to the organization's stressor list
        if value.stressors == None:
            value.stressors = [self]
        elif self not in value.stressors:
            value.stressors.append(self)

    @organization.deleter
    def organization(self):
        if self._organization != None:
            self._organization.stressors.remove(self)
            self._organization = None
    
    @property
    def insider(self):
        return self._insider
    
    @insider.setter
    def insider(self, value):
        
        check_type(value, Insider, allow_none=False)
        
        # set the insider 
        # first remove old relationships if they exist
        if self._insider != None:
            self._insider.stressors.remove(self)
        self._insider = value 

        # add it to the insider's stressor list 
        if value.stressors == None:
            value.stressors = [self]
        elif self not in value.stressors: 
            value.stressors.append(self)
    
    @insider.deleter
    def insider(self):
        if self._insider != None:
            self._insider.stressors.remove(self)
            self._insider = None


class Organization:
    """
    Initialize an Organization instance.
    
    Args:
        id (str): Unique identifier for the Organization. Defaults to a new UUIDv4 string if not provided.
        name (str): The name of the organization. E.g., "Company XYZ, Inc."
        city (str): The city where the organization is located. Use the address of the headquarters if the whole
                    organization was affected or use the address of the local branch if only that local branch was affected.
        state (str): The state where the organization is located. Use the address of the headquarters if the whole
                     organization was affected or use the address of the local branch if only that local branch was affected.
        country (str): The country where the organization is located. Use the address of the headquarters if the whole
                       organization was affected or use the address of the local branch if only that local branch was affected.
                       Public implementations should use the standard codes provided by ISO 3166-1 alpha-2.
        postal_code (int): The postal code of the organization. Use the address of the headquarters if the whole
                           organization was affected or use the address of the local branch if only that local branch was affected.
        small_business (bool): TRUE if the organization is a privately owned business with 500 or fewer employees.
        industry_sector (str): Top-level category for the economic sector the organization belongs to. Note, sectors
                               are derived from the North American Industry Classification System (NAICS) version 2022
                               published by the United States Office of Management and Budget. A constant from 
                               `industry-sector-vocab <./vocab/industry-sector-vocab.html>`_. Required if industry_subsector exists.
        industry_subsector (str): Second-level category for the economic sector the organization belongs to. This value
                                  MUST map back to industry_sector. E.g., if sector is "9", subsector must be "9.x". A constant
                                  from `industry-subsector-vocab <./vocab/industry-subsector-vocab.html>`_.
        business (str): Description of the organization's business.
        parent_company (str): Name of the organization's parent company, if applicable.
        incident_role (str): The organization's role in the incident. A constant from 
                             `org-role-vocab <./vocab/org-role-vocab.html>`_.
        **kwargs (dict): Additional attributes for the Organization.

    Raises:
        TypeError: If any provided attribute is of the incorrect type.
        ValueError: If any provided attribute is of the incorrect vocabulary. 
    
    Example:
        >>> organization = Organization(
        ...     id="123e4567-e89b-12d3-a456-426614174000",
        ...     name="Company XYZ, Inc.",
        ...     city="New York",
        ...     state="NY",
        ...     country="US",
        ...     postal_code=10001,
        ...     small_business=True,
        ...     industry_sector="51",
        ...     industry_subsector="51.2",
        ...     business="Software Development",
        ...     parent_company="Parent Company ABC",
        ...     incident_role="V"
        ... )
        >>> print(organization.id)
        123e4567-e89b-12d3-a456-426614174000
        >>> print(organization.name)
        Company XYZ, Inc.
    """
    def __init__(self, id=None, name=None, city=None, state=None, country=None, postal_code=None, small_business=None, industry_sector=None, industry_subsector=None, business=None, parent_company=None, incident_role=None, **kwargs):
        if id is None:
            id = str(uuid.uuid4())
        check_uuid(id)
        self._id = id

        check_type(name, str)
        self._name = name

        check_type(city, str)
        self._city = city

        check_type(state, str)
        check_vocab(state, 'state-vocab-us')
        self._state = state

        check_type(country, str)
        check_vocab(country, 'country-vocab')
        self._country = country

        check_type(postal_code, int)
        self._postal_code = postal_code

        check_type(small_business, bool)
        self._small_business = small_business

        check_type(industry_sector, str)
        check_vocab(industry_sector, 'industry-sector-vocab')
        self._industry_sector = industry_sector

        check_type(industry_subsector, str)
        check_vocab(industry_subsector, 'industry-subsector-vocab')
        check_subtype(industry_sector, industry_subsector)
        self._industry_subsector = industry_subsector

        check_type(business, str)
        self._business = business

        check_type(parent_company, str)
        self._parent_company = parent_company

        check_type(incident_role, str)
        check_vocab(kwargs.get("incident_role"), 'org-role-vocab')
        self._incident_role = incident_role

        # Relationships
        self._incident = None
        self._jobs = None
        self._stressors = None
    
    def __repr__(self):
        return (f"Organization(id={self.id}, "
                f"name={self.name}, "
                f"city={self.city}, "
                f"state={self.state}, "
                f"country={self.country}, "
                f"postal_code={self.postal_code}, "
                f"small_business={self.small_business}, "
                f"industry_sector={self.industry_sector}, "
                f"industry_subsector={self.industry_subsector}, "
                f"business={self.business}, "
                f"parent_company={self.parent_company}, "
                f"incident_role={self.incident_role})")

    def to_dict(self):
        class_dict_copy = self.__dict__.copy()

        relationships = {'_incident', '_jobs', '_stressors'}

        children_ids = None 

        if self.jobs != None:
            children_ids = ["job--" + x.id for x in self.jobs]
        
        if self.stressors != None:
            stressors = ["stressor--" + x.id for x in self.stressors]
            if children_ids == None:
                children_ids = stressors 
            else:
                children_ids.extend(stressors)
        
        class_dict_copy["_id"] = f"organization--{self.id}"
        return ({
                    key.lstrip('_'): value 
                    for key, value in class_dict_copy.items()
                    if key not in relationships
                }, children_ids)

    @property
    def id(self):
        return self._id  

    @id.setter
    def id(self, value):
        check_uuid(value)
        self._id = value
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        check_type(value, str, allow_none=False)
        self._name = value
    
    @name.deleter
    def name(self):
        self._name = None
    
    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, value):
        check_type(value, str, allow_none=False)
        self._city = value
    
    @city.deleter
    def city(self):
        self._city = None
    
    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'state-vocab-us')
        self._state = value
    
    @state.deleter
    def state(self):
        self._state = None
    
    @property
    def country(self):
        return self._country
    
    @country.setter
    def country(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'country-vocab')
        self._country = value
    
    @country.deleter
    def country(self):
        self._country = None
    
    @property
    def postal_code(self):
        return self._postal_code
    
    @postal_code.setter
    def postal_code(self, value):
        check_type(value, int, allow_none=False)
        self._postal_code = value
    
    @postal_code.deleter
    def postal_code(self):
        self._postal_code = None
    
    @property
    def small_business(self):
        return self._small_business
    
    @small_business.setter
    def small_business(self, value):
        check_type(value, bool, allow_none=False)
        self._small_business = value
    
    @small_business.deleter
    def small_business(self):
        self._small_business = None
    
    @property
    def industry_sector(self):
        return self._industry_sector
    
    @industry_sector.setter
    def industry_sector(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'industry-sector-vocab')
        self._industry_sector = value
    
    @industry_sector.deleter
    def industry_sector(self):
        self._industry_sector = None
    
    @property
    def industry_subsector(self):
        return self._industry_subsector
    
    @industry_subsector.setter
    def industry_subsector(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'industry-subsector-vocab')
        check_subtype(self._industry_sector, value)
        self._industry_subsector = value
    
    @industry_subsector.deleter
    def industry_subsector(self):
        self._industry_subsector = None
    
    @property
    def business(self):
        return self._business
    
    @business.setter
    def business(self, value):
        check_type(value, str, allow_none=False)
        self._business = value
    
    @business.deleter
    def business(self):
        self._business = None
    
    @property
    def parent_company(self):
        return self._parent_company
    
    @parent_company.setter
    def parent_company(self, value):
        check_type(value, str, allow_none=False)
        self._parent_company = value
    
    @parent_company.deleter
    def parent_company(self):
        self._parent_company = None
    
    @property
    def incident_role(self):
        return self._incident_role
    
    @incident_role.setter
    def incident_role(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'org-role-vocab')
        self._incident_role = value
    
    @incident_role.deleter
    def incident_role(self):
        self._incident_role = None

    # - - - - - - - RELATIONSHIPS - - - - - - 
    @property
    def incident(self):
        return self._incident
    
    @incident.setter
    def incident(self, value):
        
        check_type(value, Incident, allow_none=False)
        
        # set the incident
        # making sure to remove any old relationships first
        if self._incident != None:
            self._incident.organizations.remove(self)
        self._incident = value

        # add it to the incident's organization list
        if value.organizations == None:
            value.organizations = [self]
        elif self not in value.organizations:
            value.organizations.append(self)
    
    @incident.deleter
    def incident(self):
        if self._incident != None:
            self._incident.organizations.remove(self)
            self._incident = None

    @property
    def jobs(self):
        return self._jobs
    
    @jobs.setter
    def jobs(self, value):
        check_type(value, list, allow_none=False)

        # check all elements of the list are Job 
        # objects
        for obj in value:
            
            check_type(obj, Job, allow_none=False)
        
        # set new job list
        # making sure to remove any old relationships first
        if self._jobs != None:
            # use list() to create a copy
            for j in list(self._jobs):
                del j.organization
        self._jobs = value

        # connect those back to this
        # organization instance
        for obj in value: 
            if obj.organization != self:
                obj.organization = self

    def append_job(self, item):
        
        check_type(item, Job)
        
        if self._jobs == None:
            self._jobs = [item]
        else:
            self._jobs.append(item)
        
        item.organization = self
    
    def remove_job(self, item):
        
        check_type(item, Job, allow_none=False)
        if self._jobs != None:
            del item.organization    

    @jobs.deleter
    def jobs(self):
        # adding list() creates a copy so that we don't
        # run into any issues with removing elements 
        # from the list we are iterating over
        for obj in list(self._jobs):
            del obj.organization
        self._jobs = None
    
    @property
    def stressors(self):
        return self._stressors
    
    @stressors.setter
    def stressors(self, value):
        check_type(value, list, allow_none=False)

        # check that all elements are stressor object
        for obj in value:
            
            check_type(obj, Stressor, allow_none=False)
        
        # set the new stressor value 
        # making sure to delete any old relationships first
        if self._stressors != None:
            # use list() to create a copy
            for s in list(self._stressors):
                del s.organization
        self._stressors = value

        # connect those back to this organization instance
        for obj in value: 
            if obj.organization != self:
                obj.organization = self

    def append_stressor(self, item):
        
        check_type(item, Stressor)
        
        if self._stressors == None:
            self._stressors = [item]
        else:
            self._stressors.append(item)
        
        item.organization = self
    
    def remove_stressor(self, item):
        
        check_type(item, Stressor, allow_none=False)
        if self._stressors != None:
            del item.organization    

    @stressors.deleter
    def stressors(self):
        # adding list() creates a copy so that we don't
        # run into any issues with removing elements 
        # from the list we are iterating over
        for obj in list(self._stressors):
            del obj.organization
        self._stressors = None


class Incident:
    """
    Initialize an Incident instance.

    Args:
        id (str): Unique identifier for the incident. Defaults to a new UUIDv4 string if not provided.
        cia_effect (list): CIA triad components which were affected. One or more constants from 
                           `cia-vocab <./vocab/cia-vocab.html>`_.
        incident_type (list): Categorization of the incident. One or more constants from 
                              `incident-type-vocabulary <./vocab/incident-type-vocab.html>`_. 
                              Required if incident_subtype exists.
        incident_subtype (list): The subtype that the incident fits. MUST match the specified incident_type.
                                 One or more constants from 
                                 `incident-subtype-vocabulary <./vocab/incident-subtype-vocab.html>`_.
        outcome (list): Consequences suffered by the victim organization as a result of the insider's attack.
                        This is NOT the outcome or consequences imposed on the insider.
                        One or more constants from 
                        `outcome-type-vocabulary <./vocab/outcome-type-vocab.html>`_.
        status (str): The current status of the incident. A constant from 
                      `incident-status-vocabulary <./vocab/incident-status-vocab.html>`_.
        summary (str): A brief prose explanation of the incident. This summary should serve as a stand-alone 
                       explanation of the incident and should include the following information as a general rule: 
                       who, what, when, where, why, and how.
        brief_summary (str): A shortened version of the summary (2-4 sentences, max 500 characters) with 
                             anonymized data.
        comment (str): Clarifying details about the incident or any of the above properties.
        **kwargs (dict): Additional attributes for the incident.

    Raises:
        TypeError: If any provided attribute is of the incorrect type.
        ValueError: If any provided attribute is of the incorrect vocabulary. 
    
    Examples:
        >>> incident = Incident(
        ...     cia_effect=["C", "I"],
        ...     incident_type=["F"],
        ...     incident_subtype=["F.1"],
        ...     outcome=["BR"],
        ...     status="P",
        ...     summary="An insider incident involving data theft.",
        ...     brief_summary="Insider data theft.",
        ...     comment="Additional details about the incident."
        ... )
        >>> print(incident.id)
        123e4567-e89b-12d3-a456-426614174000
        >>> print(incident.incident_type)
        ['F']
    """
    def __init__(self, id=None, cia_effect=None, incident_type=None, incident_subtype=None, outcome=None, status=None, summary=None, brief_summary=None, comment=None, **kwargs):
        if id == None:
            id = str(uuid.uuid4())

        check_uuid(id)
        self._id = id
        
        check_type(cia_effect, list)
        check_vocab(cia_effect, 'cia-vocab')
        self._cia_effect = cia_effect

        check_type(incident_type, list)
        check_vocab(incident_type, 'incident-type-vocab')
        self._incident_type = incident_type

        check_type(incident_subtype, list)
        check_vocab(incident_subtype, 'incident-subtype-vocab')
        check_subtype_list(self._incident_type, incident_subtype)
        self._incident_subtype = incident_subtype

        check_type(outcome, list)
        check_vocab(outcome, 'outcome-type-vocab')
        self._outcome = outcome

        check_type(status, str)
        check_vocab(status, 'incident-status-vocab')
        self._status = status

        check_type(summary, str)
        self._summary = summary

        check_type(brief_summary, str)
        self._brief_summary = brief_summary

        check_type(comment, str)
        self._comment = comment

        # - - - - - - RELATIONSHIPS - - - - - - - # 
        self._detection = None
        self._response = None 
        self._ttps = None
        self._organizations = None
        self._insiders = None
        self._impacts = None
        self._targets = None
        self._notes = None
        self._sources = None

    def __repr__(self):
        return (f"Incident(id={self.id}, "
                f"cia_effect={self.cia_effect}, "
                f"incident_type={self.incident_type}, "
                f"incident_subtype={self.incident_subtype}, "
                f"outcome={self.outcome}, "
                f"status={self.status}, "
                f"summary={self.summary}, "
                f"brief_summary={self.brief_summary}, "
                f"comment={self.comment})")

    def to_dict(self):
        class_dict_copy = self.__dict__.copy()
        relationships = {'_detection', '_response', '_ttps', '_organizations', '_insiders', '_impacts', '_targets', '_notes', '_sources'}
        class_dict_copy["_id"] = f"incident--{self.id}"
        return ({
                    key.lstrip('_'): value 
                    for key, value in class_dict_copy.items()
                    if key not in relationships
                }, None)

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        check_uuid(value)
        self._id = value

    @property
    def cia_effect(self):
        return self._cia_effect
    
    @cia_effect.setter
    def cia_effect(self, value):
        check_type(value, list, allow_none=False)
        check_vocab(value, 'cia-vocab')
        self._cia_effect = value
    
    def append_cia(self, item):
        check_type(item, str, allow_none=False)
        check_vocab(item, 'cia-vocab')
        self._cia_effect.append(item)

    @cia_effect.deleter
    def cia_effect(self):
        self._cia_effect = None
    
    @property
    def incident_type(self):
        return self._incident_type
    
    @incident_type.setter
    def incident_type(self, value):
        check_type(value, list, allow_none=False)
        check_vocab(value, 'incident-type-vocab')
        self._incident_type = value
    
    def append_type(self, item):
        check_type(item, str, allow_none=False)
        check_vocab(item, 'incident-type-vocab')        
        self._incident_type.append(item)

    @incident_type.deleter
    def incident_type(self):
        self._incident_type = None

    @property
    def incident_subtype(self):
        return self._incident_subtype
    
    @incident_subtype.setter
    def incident_subtype(self, value):
        check_type(value, list, allow_none=False)
        check_vocab(value, 'incident-subtype-vocab')
        check_subtype_list(self._incident_type, value)
        self._incident_subtype = value
    
    def append_subtype(self, item):
        check_type(item, str, allow_none=False)
        check_vocab(item, 'incident-subtype-vocab')
        check_subtype_list(self._incident_type, item)
        self._incident_subtype.append(item)

    @incident_subtype.deleter
    def incident_subtype(self):
        self._incident_subtype = None
    
    @property 
    def outcome(self):
        return self._outcome
    
    @outcome.setter
    def outcome(self, value):
        check_type(value, list, allow_none=False)
        check_vocab(value, 'outcome-type-vocab')
        self._outcome = value
    
    def append_outcome(self, item):
        check_type(item, str, allow_none=False)
        check_vocab(item, 'outcome-type-vocab')
        self._outcome.append(item)

    @outcome.deleter
    def outcome(self):
        self._outcome = None
    
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'incident-status-vocab')
        self._status = value
    
    @status.deleter 
    def status(self):
        self._status = None
    
    @property
    def summary(self):
        return self._summary

    @summary.setter
    def summary(self, value):
        check_type(value, str, allow_none=False)
        self._summary = value
    
    @summary.deleter 
    def summary(self):
        self._summary = None
    
    @property
    def brief_summary(self):
        return self._brief_summary

    @brief_summary.setter
    def brief_summary(self, value):
        check_type(value, str, allow_none=False)
        self._brief_summary = value
    
    @brief_summary.deleter 
    def brief_summary(self):
        self._brief_summary = None
    
    @property
    def comment(self):
        return self._comment
    
    @comment.setter
    def comment(self, value):
        check_type(value, str, allow_none=False)
        self._comment = value

    @comment.deleter
    def comment(self):
        self._comment = None

    # - - - - - - - RELATIONSHIPS - - - - - - - -

    @property
    def detection(self):
        return self._detection
    
    @detection.setter
    def detection(self, value):
        
        check_type(value, Detection, allow_none=False)
        self._detection = value
        if value.incident != self:
            value.incident = self
    
    @detection.deleter
    def detection(self):
        temp = self._detection
        self._detection = None
        if temp != None:
            del temp.incident
    
    @property
    def response(self):
        return self._response
    
    @response.setter
    def response(self, value):
        
        check_type(value, Response, allow_none=False)
        self._response = value
        if value.incident != self:
            value.incident = self 
    
    @response.deleter
    def response(self):
        temp = self._response
        self._response = None
        if temp != None:
            del temp.incident
    
    @property
    def ttps(self):
        return self._ttps
    
    @ttps.setter
    def ttps(self, value):
        check_type(value, list, allow_none=False)

        # check that all elements inside the list are
        # a TTP object
        for obj in value:
            check_type(obj, TTP, allow_none=False)
        
        # set the ttps attribute to the new list
        # if it isn't None, we want to remove all old 
        # relationships before setting the new ones
        if self._ttps != None:
            # using list() creates a copy
            for t in list(self._ttps):
                del t.incident
        self._ttps = value

        # set each incident attribute of the TTP list
        # to this instance of Incident 
        for obj in value: 
            if obj.incident != self:
                obj.incident = self

    def append_ttp(self, item):
        
        check_type(item, TTP, allow_none=False)
         
        if self._ttps == None:
            self._ttps = [item]
        else:
            self._ttps.append(item)

        item.incident = self   
    
    def remove_ttp(self, item):
        
        check_type(item, TTP, allow_none=False)
        if self._ttps != None:
            del item.incident 

    @ttps.deleter
    def ttps(self):
        # adding list() creates a copy so that we don't
        # run into any issues with removing elements 
        # from the list we are iterating over
        for obj in list(self._ttps):
            del obj.incident
        self._ttps = None
    
    @property
    def organizations(self):
        return self._organizations
    
    @organizations.setter
    def organizations(self, value):
        check_type(value, list, allow_none=False)

        # check that all elements of list are Organization objects
        for obj in value:
            
            check_type(obj, Organization, allow_none=False)
        
        # set the organizations list
        # if it is not None, then we want to remove all the old 
        # relationships
        if self._organizations != None:
            # using list() creates a copy
            for o in list(self._organizations):
                del o.incident
        self._organizations = value

        # set the rest of the relationships for the newly set
        # organizations
        for obj in value: 
            if obj.incident != self:
                obj.incident = self
    
    def append_organization(self, item):
        
        check_type(item, Organization)
        if self._organizations == None:
            self._organizations = [item]
        else:
            self._organizations.append(item)

        item.incident = self
    
    def remove_organization(self, item):
        
        check_type(item, Organization, allow_none=False)
        if self._organizations != None:
            del item.incident  

    @organizations.deleter
    def organizations(self):
        # adding list() creates a copy so that we don't
        # run into any issues with removing elements 
        # from the list we are iterating over
        for obj in list(self._organizations):
            del obj.incident
        self._organizations = None
    
    @property
    def insiders(self):
        return self._insiders
    
    @insiders.setter
    def insiders(self, value):
        check_type(value, list, allow_none=False)

        # check that all elements in this list are 
        # Insider objects 
        for obj in value:
            
            check_type(obj, Insider, allow_none=False)
        
        # set the new insider list:
        # if a insiders list already exists, we want
        # to remove the relationships before setting  
        # a new one
        if self._insiders != None:
            # using list() creates a copy
            for i in list(self._insiders):
                del i.incident
        self._insiders = value

        # connect each insider object to this instance
        # of the incident
        for obj in value: 
            if obj.incident != self:
                obj.incident = self

    def append_insider(self, item):
        
        check_type(item, Insider, allow_none=False)
        if self._insiders == None:
            self._insiders = [item]
        else:
            self._insiders.append(item)
        
        item.incident = self
    
    def remove_insider(self, item):
        
        check_type(item, Insider, allow_none=False)
        if self._insiders != None:
            del item.incident  

    @insiders.deleter
    def insiders(self):
        # adding list() creates a copy so that we don't
        # run into any issues with removing elements 
        # from the list we are iterating over
        for obj in list(self._insiders):
            del obj.incident
        self._insiders = None
    
    @property
    def impacts(self):
        return self._impacts
    
    @impacts.setter
    def impacts(self, value):
        check_type(value, list, allow_none=False)

        # check that all elements in the list are
        # Impact objects
        for obj in value:
            
            check_type(obj, Impact, allow_none=False)
        
        # set the new impact list:
        # making sure to remove all old relationships first
        if self._impacts != None:
            # using list() creates a copy
            for i in list(self._impacts):
                del i.incident
        self._impacts = value

        # connect each impact to this incident instance
        for obj in value: 
            if obj.incident != self:
                obj.incident = self

    def append_impact(self, item):
        
        check_type(item, Impact, allow_none=False)
        if self._impacts == None:
            self._impacts = [item]
        else:
            self._impacts.append(item)
        
        item.incident = self
    
    def remove_impact(self, item):
        
        check_type(item, Impact, allow_none=False)
        if self._impacts != None:
            del item.incident  

    @impacts.deleter
    def impacts(self):
        # adding list() creates a copy so that we don't
        # run into any issues with removing elements 
        # from the list we are iterating over
        for obj in list(self._impacts):
            del obj.incident
        self._impacts = None

    @property
    def targets(self):
        return self._targets
    
    @targets.setter
    def targets(self, value):
        check_type(value, list, allow_none=False)

        # check that all elements are target objects 
        for obj in value:
            
            check_type(obj, Target, allow_none=False)
        
        # set the new targets list:
        # making sure to remove old relationships first
        if self._targets != None:
            # using list() creates a copy
            for t in list(self._targets):
                del t.incident
        self._targets = value

        # connect those back to this instance of incident
        for obj in value: 
            if obj.incident != self:
                obj.incident = self

    def append_target(self, item):
        
        check_type(item, Target, allow_none=False)
        if self._targets == None:
            self._targets = [item]
        else:
            self._targets.append(item)
        
        item.incident = self
    
    def remove_target(self, item):
        
        check_type(item, Target, allow_none=False)
        if self._targets != None:
            del item.incident  

    @targets.deleter
    def targets(self):
        # adding list() creates a copy so that we don't
        # run into any issues with removing elements 
        # from the list we are iterating over
        for obj in list(self._targets):
            del obj.incident
        self._targets = None

    
    # - - - - - - -
    @property
    def notes(self):
        return self._notes
    
    @notes.setter
    def notes(self, value):
        check_type(value, list, allow_none=False)

        # check that all elements are target objects 
        for obj in value:
            
            check_type(obj, Note, allow_none=False)
        
        # set the new notes list:
        # making sure to remove old relationships first
        if self._notes != None:
            # using list() creates a copy
            for t in list(self._notes):
                del t.incident
        self._notes = value

        # connect those back to this instance of incident
        for obj in value: 
            if obj.incident != self:
                obj.incident = self

    def append_note(self, item):
        
        check_type(item, Note, allow_none=False)
        if self._notes == None:
            self._notes = [item]
        else:
            self._notes.append(item)
        
        item.incident = self
    
    def remove_note(self, item):
        
        check_type(item, Note, allow_none=False)
        if self._notes != None:
            del item.incident  

    @notes.deleter
    def notes(self):
        # adding list() creates a copy so that we don't
        # run into any issues with removing elements 
        # from the list we are iterating over
        for obj in list(self._notes):
            del obj.incident
        self._notes = None
    
    # - - - - - - -
    @property
    def sources(self):
        return self._sources
    
    @sources.setter
    def sources(self, value):
        check_type(value, list, allow_none=False)

        # check that all elements are target objects 
        for obj in value:
            
            check_type(obj, Source, allow_none=False)
        
        # set the new sources list:
        # making sure to remove old relationships first
        if self._sources != None:
            # using list() creates a copy
            for t in list(self._sources):
                del t.incident
        self._sources = value

        # connect those back to this instance of incident
        for obj in value: 
            if obj.incident != self:
                obj.incident = self

    def append_source(self, item):
        
        check_type(item, Source, allow_none=False)
        if self._sources == None:
            self._sources = [item]
        else:
            self._sources.append(item)
        
        item.incident = self
    
    def remove_source(self, item):
        
        check_type(item, Source, allow_none=False)
        if self._sources != None:
            del item.incident  

    @sources.deleter
    def sources(self):
        # adding list() creates a copy so that we don't
        # run into any issues with removing elements 
        # from the list we are iterating over
        for obj in list(self._sources):
            del obj.incident
        self._sources = None


class Job:
    """
    Initialize a Job instance.

    Args:
        id (str): Unique identifier for the Job. Defaults to a new UUIDv4 string if not provided.
        job_function (str): Functional category of the individual's job. Based on the 2018 Standard Occupational Classification system published by the Bureau of Labor Statistics. A constant from 
                            `job-function-vocab <./vocab/job-function-vocab.html>`_. Required if occupation exists.
        occupation (str): The subcategory of the individual's job. Must match the constant for job_function. A constant from 
                          `occupation-vocab <./vocab/occupation-vocab.html>`_. Required if title exists.
        title (str): The individual's job title. If title is specified, occupation should be as well.
        position_technical (bool): The individual had access to technical areas of the organization as part of their job role. E.g. IT admin, network engineer, help desk associate, etc.
        access_authorization (str): The level of access control given by this job role. A constant from 
                                    `access-auth-vocab <./vocab/access-auth-vocab.html>`_.
        employment_type (str): The individual's employment arrangement at the time of the incident. A constant from 
                               `employment-type-vocab <./vocab/employment-type-vocab.html>`_.
        hire_date (date): Date the individual is hired into this position.
        departure_date (date): Date the individual departed from this position.
        tenure (timedelta): The amount of time the individual spent in this particular job role.
        comment (str): Clarifying comments or details about the job or the individual's employment with the organization.
        **kwargs (dict): Additional attributes for the Job.

    Raises:
        TypeError: If any provided attribute is of the incorrect type.
        ValueError: If any provided attribute is of the incorrect vocabulary. 
    
    Example:
        >>> job = Job(
        ...     id="123e4567-e89b-12d3-a456-426614174000",
        ...     job_function="15",
        ...     occupation="15.1",
        ...     title="Software Developer",
        ...     position_technical=True,
        ...     access_authorization="2",
        ...     employment_type="FLT",
        ...     hire_date=date(2020, 1, 1),
        ...     departure_date=date(2023, 1, 1),
        ...     tenure=timedelta(days=1096),
        ...     comment="This is a comment"
        ... )
        >>> print(job.id)
        123e4567-e89b-12d3-a456-426614174000
        >>> print(job.title)
        Software Developer
        >>> print(access_authorization)
        2
    """
    def __init__(self, id=None, job_function=None, occupation=None, title=None, position_technical=None, access_authorization=None, employment_type=None, hire_date=None, departure_date=None, tenure=None, comment=None, **kwargs):
        if id is None:
            id = str(uuid.uuid4())
        check_uuid(id)
        self._id = id

        check_type(job_function, str)
        check_vocab(job_function, 'job-function-vocab')
        self._job_function = job_function

        check_type(occupation, str)
        check_vocab(occupation, 'occupation-vocab')
        check_subtype(self._job_function, occupation)
        self._occupation = occupation

        check_type(title, str)
        self._title = title

        check_type(position_technical, bool)
        self._position_technical = position_technical

        check_type(access_authorization, str)
        check_vocab(access_authorization, 'access-auth-vocab')
        self._access_authorization = access_authorization

        check_type(employment_type, str)
        check_vocab(employment_type, 'employment-type-vocab')
        self._employment_type = employment_type

        check_type(hire_date, dt)
        self._hire_date = hire_date
        
        check_type(departure_date, dt)
        self._departure_date = departure_date

        check_type(tenure, timedelta)
        check_tenure(self._hire_date, self._departure_date, tenure)
        self._tenure = tenure
        
        check_type(comment, str)
        self._comment = comment

        # Relationships 
        self._organization = None
        self._insider = None
        self._accomplice = None
    
    def __repr__(self):
        return (f"Job(id={self.id}, "
                f"job_function={self.job_function}, "
                f"occupation={self.occupation}, "
                f"title={self.title}, "
                f"position_technical={self.position_technical}, "
                f"access_authorization={self.access_authorization}, "
                f"employment_type={self.employment_type}, "
                f"hire_date={self.hire_date}, "
                f"departure_date={self.departure_date}, "
                f"tenure={self.tenure}, "
                f"comment={self.comment})")

    def to_dict(self):
        class_dict_copy = self.__dict__.copy()
        relationships = {'_organization', '_insider', '_accomplice'}
        self.__dict__["id"] = f"job--{self.id}"

        if self.hire_date != None:
            class_dict_copy["_hire_date"] = str(self.hire_date)
        
        if self.departure_date != None:
            class_dict_copy["_departure_date"] = str(self.departure_date)

        if self.tenure != None:
            class_dict_copy["_tenure"] = str(self.tenure)

        return ({
                    key.lstrip('_'): value 
                    for key, value in class_dict_copy.items()
                    if key not in relationships
                }, None)

    @property
    def id(self):
        return self._id  

    @id.setter
    def id(self, value):
        check_uuid(value)
        self._id = value

    @property
    def job_function(self):
        return self._job_function

    @job_function.setter
    def job_function(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'job-function-vocab')
        self._job_function = value
    
    @job_function.deleter
    def job_function(self):
        self._job_function = None

    @property
    def occupation(self):
        return self._occupation

    @occupation.setter
    def occupation(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'occupation-vocab')
        self._occupation = value
    
    @occupation.deleter
    def occupation(self):
        self._occupation = None

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        check_type(value, str, allow_none=False)
        self._title = value

    @title.deleter
    def title(self):
        self._title = None

    @property
    def position_technical(self):
        return self._position_technical

    @position_technical.setter
    def position_technical(self, value):
        check_type(value, bool, allow_none=False)
        self._position_technical = value
    
    @position_technical.deleter
    def position_technical(self):
        self._position_technical = None

    @property
    def access_authorization(self):
        return self._access_authorization

    @access_authorization.setter
    def access_authorization(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'access-auth-vocab')
        self._access_authorization = value
    
    @access_authorization.deleter
    def access_authorization(self):
        self._access_authorization = None

    @property
    def employment_type(self):
        return self._employment_type

    @employment_type.setter
    def employment_type(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'employment-type-vocab')
        self._employment_type = value
    
    @employment_type.deleter
    def employment_type(self):
        self._employment_type = None
    
    @property 
    def hire_date(self):
        return self._hire_date

    @hire_date.setter
    def hire_date(self, value):   
        check_type(value, dt, allow_none=False)
        self._hire_date = value
        if (self._hire_date != None and self._departure_date != None):
            self._tenure = self._departure_date - self._hire_date
    
    @hire_date.deleter
    def hire_date(self):
        self._hire_date = None

    @property
    def departure_date(self):
        return self._departure_date

    @departure_date.setter
    def departure_date(self, value):
        check_type(value, dt, allow_none=False)
        self._departure_date = value
        if (self._hire_date != None and self._departure_date != None):
            self._tenure = self._departure_date - self._hire_date
    
    @departure_date.deleter
    def departure_date(self):
        self._departure_date = None
    
    @property
    def tenure(self):
        return self._tenure

    @tenure.setter
    def tenure(self, value):
        check_type(value, timedelta, allow_none=False)
        if (self._hire_date == None or self._departure_date == None):
            raise ReferenceError("You must set the hire date and departure date in order to set the tenure")
        td = self._departure_date - self._hire_date
        if (td != value):
            raise ValueError("Incorrect value for the given hire date and departure date")
        self._tenure = value
    
    @tenure.deleter
    def tenure(self):
        self._tenure = None
    
    @property
    def comment(self):
        return self._comment
    
    @comment.setter
    def comment(self, value):
        check_type(value, str, allow_none=False)
        self._comment = value

    @comment.deleter
    def comment(self):
        self._comment = None

    # - - - - - - - RELATIONSHIPS - - - - - - 
    @property
    def organization(self):
        return self._organization
    
    @organization.setter
    def organization(self, value):
        
        check_type(value, Organization, allow_none=False)
        
        # set the organization 
        # making sure to remove any old relationships first
        if self._organization != None:
            self._organization.jobs.remove(self)
        self._organization = value

        # add it to the organization's job list
        if value.jobs == None:
            value.jobs = [self]
        elif self not in value.jobs: 
            value.jobs.append(self)
    
    @organization.deleter
    def organization(self):
        if self._organization != None:
            self._organization.jobs.remove(self)
            self._organization = None
    
    @property
    def insider(self):
        return self._insider
    
    @insider.setter
    def insider(self, value):
        
        check_type(value, Insider, allow_none=False)
        
        # set the insider 
        # making sure to remove any old relationships first
        if self._insider != None:
            self._insider.jobs.remove(self)
        self._insider = value

        # add it to the insiders's job list
        if value.jobs == None:
            value.jobs = [self]
        elif self not in value.jobs: 
            value.jobs.append(self)
    
    @insider.deleter
    def insider(self):
        if self._insider != None:
            self._insider.jobs.remove(self)
            self._insider = None

    @property
    def accomplice(self):
        return self._accomplice
    
    @accomplice.setter
    def accomplice(self, value):
        
        check_type(value, Accomplice, allow_none=False)
        
        # set the accomplice
        # making sure to remove old relationships first
        if self._accomplice != None:
            self._accomplice.jobs.remove(self)
        self._accomplice = value

        # add it to the insiders's job list
        if value.jobs == None:
            value.jobs = [self]
        elif self not in value.jobs: 
            value.jobs.append(self)
    
    @accomplice.deleter
    def accomplice(self):
        if self._accomplice != None:
            self._accomplice.jobs.remove(self)
            self._accomplice = None


class Insider(Person):
    """
    Initialize an Insider instance.

    Args:
        id (str): Unique identifier for the Job. Defaults to a new UUIDv4 string if not provided.
        incident_role (str): The insider's role in the incident. Whether the insider was the primary actor or had a different role in the incident. A constant from 
                             `incident-role-vocab <./vocab/incident-role-vocab.html>`_.
        motive (list): The insider's motive(s) for the incident. One or more constants from 
                       `motive-vocab <./vocab/motive-vocab.html>`_.
        substance_use_during_incident (bool): Indicates if the insider was using or abusing substances at the time they took one or more actions related to the incident.
        psychological_issues (list): Psychological issue(s) the insider experienced during or before the incident. One or more constants from 
                                     `psych-issues-vocab <./vocab/psych-issues-vocab.html>`_.
        predispositions (list): The insider's tendency toward certain actions or qualities. One or more array values.
        concerning_behaviors (list): The insider's history of past behavior that could indicate future issues. One or more array values.
        **kwargs (dict): Additional attributes for the Job.

    Raises:
        TypeError: If any provided attribute is of the incorrect type.
        ValueError: If any provided attribute is of the incorrect vocabulary. 
    
    Example:
        >>> from pyiides.pyiides.insider import Insider
        >>> insider = Insider(
        ...     id="123e4567-e89b-12d3-a456-426614174000",
        ...     incident_role="1",
        ...     motive=["1"],
        ...     substance_use_during_incident=True,
        ...     psychological_issues=["1"],
        ...     predispositions=[("1", "1.1")],
        ...     concerning_behaviors=[("3.1", "3.1.1")]
        ... )
        >>> print(insider.id)
        123e4567-e89b-12d3-a456-426614174000
        >>> print(insider.incident_role)
        1
    """
    def __init__(self, incident_role, id=None, motive=None, substance_use_during_incident=None, psychological_issues=None, predispositions=None, concerning_behaviors=None, **kwargs):
        # inherit everything from Person
        super().__init__(**kwargs)

        if id is None:
            id = str(uuid.uuid4())
        check_uuid(id)
        self._id = id

        check_type(incident_role, str)
        check_vocab(incident_role, 'incident-role-vocab')
        self._incident_role = incident_role

        check_type(motive, list)
        check_vocab(motive, 'motive-vocab')
        self._motive = motive

        check_type(substance_use_during_incident, bool)
        self._substance_use_during_incident = substance_use_during_incident

        check_type(psychological_issues, list)
        check_vocab(psychological_issues, 'psych-issues-vocab')
        self._psychological_issues = psychological_issues

        check_type(predispositions, list)
        check_tuple_list(predispositions, 'predisposition-type-vocab', 'predisposition-subtype-vocab')
        self._predispositions = predispositions

        check_type(concerning_behaviors, list)
        check_tuple_list(concerning_behaviors, 'concerning-behavior-vocab', 'cb-subtype-vocab')
        self._concerning_behaviors = concerning_behaviors

        # relationships
        self._incident = None
        self._sponsor = None
        self._jobs = None
        self._stressors = None
        self._accomplices = None

    def __repr__(self):
        return (f"Insider(id={self.id}, "
                f"incident_role={self.incident_role}, "
                f"motive={self.motive}, "
                f"substance_use_during_incident={self.substance_use_during_incident}, "
                f"psychological_issues={self.psychological_issues}, "
                f"predispositions={self.predispositions}, "
                f"concerning_behaviors={self.concerning_behaviors}) ")

    def to_dict(self):
        class_dict_copy = self.__dict__.copy()

        relationships = {'_incident', '_sponsor', '_jobs', '_stressors', '_accomplices'}

        children_ids = None 

        if self.jobs != None:
            children_ids = ["job--" + x.id for x in self.jobs]
        
        if self.stressors != None:
            stressors = ["stressor--" + x.id for x in self.stressors]
            if children_ids == None:
                children_ids = stressors 
            else:
                children_ids.extend(stressors)
        
        if self.accomplices != None:
            accomplices = ["accomplice--" + x.id for x in self.accomplices]
            if children_ids == None:
                children_ids = accomplices 
            else:
                children_ids.extend(accomplices)

        class_dict_copy["_id"] = f"insider--{self.id}"
        return ({
                    key.lstrip('_'): value 
                    for key, value in class_dict_copy.items()
                    if key not in relationships
                }, children_ids)

    @property
    def id(self):
        return self._id  

    @id.setter
    def id(self, value):
        check_uuid(value)
        self._id = value
    
    @property
    def incident_role(self):
        return self._incident_role
    
    @incident_role.setter
    def incident_role(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'incident-role-vocab')
        self._incident_role = value
    
    @incident_role.deleter
    def incident_role(self):
        self._incident_role = None

    @property
    def motive(self):
        return self._motive

    @motive.setter
    def motive(self, value):
        check_type(value, list, allow_none=False)
        check_vocab(value, 'motive-vocab')
        self._motive = value

    def append_motive(self, item):
        check_type(item, str, allow_none=False)
        check_vocab(item, 'motive-vocab')
        self._motive.append(item)

    @motive.deleter
    def motive(self):
        self._motive = None

    @property
    def substance_use_during_incident(self):
        return self._substance_use_during_incident

    @substance_use_during_incident.setter
    def substance_use_during_incident(self, value):
        check_type(value, bool, allow_none=False)
        self._substance_use_during_incident = value

    @substance_use_during_incident.deleter
    def substance_use_during_incident(self):
        self._substance_use_during_incident = None

    @property
    def psychological_issues(self):
        return self._psychological_issues

    @psychological_issues.setter
    def psychological_issues(self, value):
        check_type(value, list, allow_none=False)
        check_vocab(value, 'psych-issues-vocab')
        self._psychological_issues = value
    
    def append_psychological_issues(self, item):
        check_type(item, str, allow_none=False)
        check_vocab(item, 'psych-issues-vocab')
        self._psychological_issues.append(item)

    @psychological_issues.deleter
    def psychological_issues(self):
        self._psychological_issues = None

    @property
    def predispositions(self):
        return self._predispositions

    @predispositions.setter
    def predispositions(self, value):
        check_type(value, list, allow_none=False)
        check_tuple_list(value, 'predisposition-type-vocab', 'predisposition-subtype-vocab')
        self._predispositions = value
    
    def append_predispositions(self, elem):
        check_tuple_list(elem, 'predisposition-type-vocab', 'predisposition-subtype-vocab')
        self._predispositions.append(elem)

    @predispositions.deleter
    def predispositions(self):
        self._predispositions = None

    @property
    def concerning_behaviors(self):
        return self._concerning_behaviors

    @concerning_behaviors.setter
    def concerning_behaviors(self, value):
        check_type(value, list, allow_none=False)
        check_tuple_list(value, 'concerning-behavior-vocab', 'cb-subtype-vocab')
        self._concerning_behaviors = value

    def append_concerning_behaviors(self, elem):
        check_tuple_list(elem, 'concerning-behavior-vocab', 'cb-subtype-vocab')
        self._concerning_behaviors.append(elem) 

    @concerning_behaviors.deleter
    def concerning_behaviors(self):
        self._concerning_behaviors = None

    # - - - - - - - - - - RELATIONSHIPS - - - - - - - - - -
    @property
    def incident(self):
        return self._incident
    
    @incident.setter
    def incident(self, value):
        
        check_type(value, Incident, allow_none=False)
        
        # set incident 
        # first though, we need to remove old 
        # relationships if there exist any
        if self._incident != None:
            self._incident.insiders.remove(self)
        self._incident = value

        # add the insider to the incident's insider list
        if value.insiders == None:
            value.insiders = [self]
        elif self not in value.insiders:
            value.insiders.append(self)

    @incident.deleter
    def incident(self):
        if self._incident != None:
            self._incident.insiders.remove(self)
            self._incident = None
    
    @property
    def sponsor(self):
        return self._sponsor
    
    @sponsor.setter
    def sponsor(self, value):
        
        check_type(value, Sponsor, allow_none=False)
        
        # set the sponsor 
        # first though, we must remove any old relationships
        if self._sponsor != None:
            self._sponsor.insiders.remove(self)
        self._sponsor = value

        # add this insider instance to the sponsor's 
        # insiders list
        if value.insiders == None:
            value.insiders = [self]
        elif self not in value.insiders:
            value.insiders.append(self)
    
    @sponsor.deleter
    def sponsor(self):
        if self._sponsor != None:
            self._sponsor.insiders.remove(self)
            self._sponsor = None

    @property
    def jobs(self):
        return self._jobs
    
    @jobs.setter
    def jobs(self, value):
        check_type(value, list, allow_none=False)

        # check that all elements are a Job object
        for obj in value:
            
            check_type(obj, Job, allow_none=False)
        
        # set the new job list 
        # making sure to remove old relationships first
        if self._jobs != None:
            # use list() to create a copy 
            for j in list(self._jobs):
                del j.insider
        self._jobs = value

        # connect each job back to this instance 
        # of insider
        for obj in value: 
            if obj.insider != self:
                obj.insider = self
    
    def append_job(self, item):
        
        check_type(item, Job, allow_none=False)
         
        if self._jobs == None:
            self._jobs = [item]
        else:
            self._jobs.append(item)
        
        item.insider = self   
    
    def remove_job(self, item):
        
        check_type(item, Job, allow_none=False)
        if self._jobs != None:
            del item.insider    

    @jobs.deleter
    def jobs(self):
        # adding list() creates a copy so that we don't
        # run into any issues with removing elements 
        # from the list we are iterating over
        for obj in list(self._jobs):
            del obj.insider
        self._jobs = None
    
    @property
    def stressors(self):
        return self._stressors
    
    @stressors.setter
    def stressors(self, value):
        check_type(value, list, allow_none=False)

        # check that all elements are stressor objects
        for obj in value:
            
            check_type(obj, Stressor, allow_none=False)
        
        # set the new stressor list 
        # making sure to remove old relationships first
        if self._stressors != None:
            # using list() to create a copy
            for s in list(self._stressors):
                del s.insider
        self._stressors = value

        # connect those back to this instance of insider
        for obj in value: 
            if obj.insider != self:
                obj.insider = self

    def append_stressor(self, item):
        
        check_type(item, Stressor, allow_none=False)
          
        if self._stressors == None:
            self._stressors = [item]
        else:
            self._stressors.append(item)

        item.insider = self
    
    def remove_stressor(self, item):
        
        check_type(item, Stressor, allow_none=False)
        if self._stressors != None:
            del item.insider    

    @stressors.deleter
    def stressors(self):
        # adding list() creates a copy so that we don't
        # run into any issues with removing elements 
        # from the list we are iterating over
        for obj in list(self._stressors):
            del obj.insider
        self._stressors = None
    
    @property
    def accomplices(self):
        return self._accomplices
    
    @accomplices.setter
    def accomplices(self, value):
        check_type(value, list, allow_none=False)

        # check that all elements in the list are Accomplice
        # objects
        for obj in value:
            
            check_type(obj, Accomplice, allow_none=False)

        # set the accomplices list
        # making sure to remove any old relationships first
        if self._accomplices != None:
            for a in list(self._accomplices):
                del a.insider
        self._accomplices = value

        # connect each accomplice back to this insider instance
        for obj in value: 
            if obj.insider != self:
                obj.insider = self

    def append_accomplice(self, item):
        
        check_type(item, Accomplice, allow_none=False)
        
        if self._accomplices == None:
            self._accomplices = [item]
        else:
            self._accomplices.append(item)
        
        item.insider = self
    
    def remove_accomplice(self, item):
        
        check_type(item, Accomplice, allow_none=False)
        if self._accomplices != None:
            del item.insider  

    @accomplices.deleter
    def accomplices(self):
        # adding list() creates a copy so that we don't
        # run into any issues with removing elements 
        # from the list we are iterating over
        for obj in list(self._accomplices):
            del obj.insider
        self._accomplices = None


class Charge:
    """
    Initializes a Charge instance

    Args:
        id (required) (string) : Unique identifier for the charge. Defaults to a new UUIDv4 string if not provided.
        title (required) (string) : Broad subject matter area of the legal code. For U.S. cases, these are often title '18 U.S.C.'.
        section (string) : Section (and subsection) of the law the subject is accused of violating. For U.S. cases for example, Wire Fraud is section 1343 of Title 18.
        nature_of_offense (string) : Description of the title and section of the law being violated.
        count (integer) : Number of times the subject is accused of violating the law associated with this charge. Note that multiple violations of a law are often listed as a range of counts (e.g. 'Count 2-6' would have count=5 for this property).
        plea (string) : Plea entered by the defendant for this charge.
            A constant from `charge-plea-vocab <./vocab/charge-plea-vocab.html>`_.
        plea_bargain (boolean) : Whether the charge indicated here is a lesser charge based on a previous plea agreement.
        disposition (string) : The decision in the case or the final result.
            A constant from `charge-disposition-vocab <./vocab/charge-disposition-vocab.html>`_.
    
    Raises:
        TypeError: If any provided attribute is of the incorrect type.
        ValueError: If any provided attribute is of the incorrect vocabulary. 

    Example:
        >>> from pyiides.utils.helper_functions import Charge
        >>> charge = Charge(
        ...     title="18 U.S.C.",
        ...     id="6eaf8e6c-8c4d-4d9d-8f8e-6c8c4d4d9d8f",
        ...     section="1343",
        ...     nature_of_offense="Wire Fraud",
        ...     count=5,
        ...     plea="1",
        ...     plea_bargain=False,
        ...     disposition="2"
        ... )
        >>> print(charge.title)
        18 U.S.C.
        >>> print(charge.section)
        1343
    """
    def __init__(self, title, id=None, section=None, nature_of_offense=None, count=None, plea=None, plea_bargain=None, disposition=None):
        if id == None:
            id = str(uuid.uuid4())

        check_uuid(id)
        self._id = id

        check_type(title, str)
        self._title = title

        check_type(section, str)
        self._section = section

        check_type(nature_of_offense, str)
        self._nature_of_offense = nature_of_offense

        check_type(count, int)
        self._count = count

        check_type(plea, str)
        check_vocab(plea, 'charge-plea-vocab')
        self._plea = plea

        check_type(plea_bargain, bool)
        self._plea_bargain = plea_bargain

        check_type(disposition, str)
        check_vocab(disposition, 'charge-disposition-vocab')
        self._disposition = disposition

        # relationships
        self._court_case = None
    
    def __repr__(self):
        return (f"Charge(id={self.id}, "
                f"title={self.title}, "
                f"section={self.section}, "
                f"nature_of_offense={self.nature_of_offense}, "
                f"count={self.count}, plea={self.plea}, "
                f"plea_bargain={self.plea_bargain}, "
                f"disposition={self.disposition})")

    def to_dict(self):
        class_dict_copy = self.__dict__.copy()
        relationships = {'_court_case'}
        class_dict_copy["_id"] = f"charge--{self.id}"
        return ({ 
                    key.lstrip('_'): value 
                    for key, value in class_dict_copy.items() 
                    if key not in relationships
                }, None)  
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        check_uuid(value)
        self._id = value

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        check_type(value, str, allow_none=False)
        self._title = value

    @title.deleter
    def title(self):
        self._title = None
    
    @property
    def section(self):
        return self._section

    @section.setter
    def section(self, value):
        check_type(value, str, allow_none=False)
        self._section = value

    @section.deleter
    def section(self):
        self._section = None

    @property
    def nature_of_offense(self):
        return self._nature_of_offense

    @nature_of_offense.setter
    def nature_of_offense(self, value):
        check_type(value, str, allow_none=False)
        self._nature_of_offense = value

    @nature_of_offense.deleter
    def nature_of_offense(self):
        self._nature_of_offense = None

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        check_type(value, int, allow_none=False)
        self._count = value

    @count.deleter
    def count(self):
        self._count = None

    @property
    def plea(self):
        return self._plea

    @plea.setter
    def plea(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'charge-plea-vocab')
        self._plea = value

    @plea.deleter
    def plea(self):
        self._plea = None

    @property
    def plea_bargain(self):
        return self._plea_bargain

    @plea_bargain.setter
    def plea_bargain(self, value):
        check_type(value, bool, allow_none=False)
        self._plea_bargain = value

    @plea_bargain.deleter
    def plea_bargain(self):
        self._plea_bargain = None

    @property
    def disposition(self):
        return self._disposition

    @disposition.setter
    def disposition(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'charge-disposition-vocab')
        self._disposition = value

    @disposition.deleter
    def disposition(self):
        self._disposition = None
    
    # - - - - - - - RELATIONSHIPS - - - - - - 
    @property
    def court_case(self):
        return self._court_case
    
    @court_case.setter
    def court_case(self, value):
        
        check_type(value, CourtCase, allow_none=False)
        
        # if the court case was already set, we have to remove
        # its current relationships before setting the new one
        if self._court_case != None:
            self._court_case.charges.remove(self)
        self._court_case = value
        
        # then add this charge instance to the court 
        # case's charge list 
        if value.charges == None:
            value.charges = [self]
        elif self not in value.charges:
            value.charges.append(self)
    
    @court_case.deleter
    def court_case(self):
        if self._court_case != None:
            self._court_case.charges.remove(self)
            self._court_case = None


class Response:
    """
    Initialize a Response instance.

    Args:
        id (str): Unique identifier for the response. Defaults to a new UUIDv4 string if not provided.
        technical_controls (list): Controls put in place to limit or monitor the insider's access to devices, data,
                                   or the network, or to limit/monitor network/device access for the user population more generally. One or more list values.
        behavioral_controls (list): Controls put in place to limit, monitor, or correct the insider's behavior
                                    within the organization. One or more list values.
        investigated_by (list): The organization(s) or entity(s) that investigated the incident.
                                One or more constants from 
                                `investigator-vocab <./vocab/investigator-vocab.html>`_.
        investigation_events (list): Specific events that happened during the course of the investigation into the incident.
                                     One or more array values.
        comment (str): Clarifying comments or additional details about the organization's response.
        **kwargs (dict): Additional attributes for the response.

    Raises:
        TypeError: If any provided attribute is of the incorrect type.
        ValueError: If any provided attribute is of the incorrect vocabulary. 
    
    Example:
        >>> response = Response(
        ...     id="123e4567-e89b-12d3-a456-426614174000",
        ...     technical_controls=[("1", date(2023, 1, 1))],
        ...     behavioral_controls=[("4", date(2023, 1, 2))],
        ...     investigated_by=["1", "2"],
        ...     investigation_events=[("2", date(2023, 1, 3))],
        ...     comment="Initial comment"
        ... )
        >>> print(response.id)
        123e4567-e89b-12d3-a456-426614174000
        >>> print(response.technical_controls)
        [("1", "2023-01-01")]
    """
    def __init__(self, id=None, technical_controls=None, behavioral_controls=None, investigated_by=None, investigation_events=None, comment=None, **kwargs):
        if id == None:
            id = str(uuid.uuid4())

        check_uuid(id)
        self._id = id

        check_type(technical_controls, list)
        check_vocab(technical_controls, 'technical-control-vocab')
        self._technical_controls = technical_controls

        check_type(behavioral_controls, list)
        check_vocab(behavioral_controls, 'behavioral-control-vocab')
        self._behavioral_controls = behavioral_controls

        check_type(investigated_by, list)
        check_vocab(investigated_by, 'investigator-vocab')
        self._investigated_by = investigated_by

        check_type(investigation_events, list)
        check_vocab(investigation_events, 'investigation-vocab')
        self._investigation_events = investigation_events

        check_type(comment, str)
        self._comment = comment

        # RELATIONSHIPS
        self._incident = None    # belongs to incident
        self._legal_response = None

    def __repr__(self):
        return (f"Response(id={self.id}, "
                f"technical_controls={self.technical_controls}, "
                f"behavioral_controls={self.behavioral_controls}, "
                f"investigated_by={self.investigated_by}, "
                f"investigation_events={self.investigation_events}, "
                f"comment={self.comment})")

    def to_dict(self):
        class_dict_copy = self.__dict__.copy()
        relationships = {'_incident', '_legal_response'}

        if self.technical_controls != None:
            for (_, date) in class_dict_copy["_technical_controls"]:
                date = str(date)
                
        if self.behavioral_controls != None:
            for (_, date) in class_dict_copy["_behavioral_controls"]:
                date = str(date)
        
        if self.investigation_events != None:
            for (_, date) in class_dict_copy["_investigation_events"]:
                date = str(date)

        class_dict_copy["_id"] = f"response--{self.id}"
        return ({
                    key.lstrip('_'): value 
                    for key, value in class_dict_copy.items()
                    if key not in relationships
                }, None)

    @property
    def id(self):
        return self._id  

    @id.setter
    def id(self, value):
        check_uuid(value)
        self._id = value
    
    @property 
    def technical_controls(self):
        return self._technical_controls
    
    @technical_controls.setter
    def technical_controls(self, value):
        check_type(value, list, allow_none=False)
        check_vocab(value, 'technical-control-vocab')
        self._technical_controls = value
    
    def append_technical_controls(self, item):
        check_type(item, tuple, allow_none=False)
        check_vocab(item, 'technical-control-vocab')
        self._technical_controls.append(item)
    
    @technical_controls.deleter
    def technical_controls(self):
        self._technical_controls = None
    
    @property
    def behavioral_controls(self):
        return self._behavioral_controls
    
    @behavioral_controls.setter
    def behavioral_controls(self, value):
        check_type(value, list, allow_none=False)
        check_vocab(value, 'behavioral-control-vocab')
        self._behavioral_controls = value
    
    def append_behavioral_controls(self, item):
        check_type(item, tuple, allow_none=False)
        check_vocab(item, 'behavioral-control-vocab')
        self._behavioral_controls.append(item)
    
    @behavioral_controls.deleter
    def behavioral_controls(self):
        self._behavioral_controls = None

    @property
    def investigated_by(self):
        return self._investigated_by
    
    @investigated_by.setter
    def investigated_by(self, value):
        check_type(value, list, allow_none=False)
        check_vocab(value, 'investigator-vocab')
        self._investigated_by = value
    
    def append_investigated_by(self, item):
        check_type(item, str, allow_none=False)
        check_vocab(item, 'investigator-vocab')
        self._investigated_by.append(item)

    @investigated_by.deleter
    def investigated_by(self):
        self._investigated_by = None
    
    @property
    def investigation_events(self):
        return self._investigation_events
    
    @investigation_events.setter
    def investigation_events(self, value):
        check_type(value, list, allow_none=False)
        check_vocab(value, 'investigation-vocab')
        self._investigation_events = value
    
    def append_investigation_events(self, item):
        check_type(item, tuple, allow_none=False)
        check_vocab(item, 'investigation-vocab')
        self._investigation_events.append(item)

    @investigation_events.deleter
    def investigation_events(self):
        self._investigation_events = None

    @property
    def comment(self):
        return self._comment
    
    @comment.setter
    def comment(self, value):
        check_type(value, str, allow_none=False)
        self._comment = value

    @comment.deleter
    def comment(self):
        self._comment = None
    
    # - - - - - - - RELATIONSHIPS - - - - - - 
    @property
    def incident(self):
        return self._incident
    
    @incident.setter
    def incident(self, value):
        
        check_type(value, Incident, allow_none=False)
        self._incident = value
        if value.response != self:
            value.response = self
    
    @incident.deleter
    def incident(self):
        temp = self._incident
        self._incident = None
        if temp != None:
            del temp.response
    
    @property
    def legal_response(self):
        return self._legal_response
    
    @legal_response.setter
    def legal_response(self, value):
        
        check_type(value, LegalResponse)
        self._legal_response = value
        if value.response != self:
            value.response = self

    @legal_response.deleter
    def legal_response(self):
        temp = self._legal_response
        self._legal_response = None
        if temp != None:
            del temp.response


class TTP:
    """
    Initialize a TTP instance.

    Args:
        id (str): Unique identifier for the TTP. Defaults to a new UUIDv4 string if not provided.
        date (datetime): The date and time the action happened. If over a range of time, the start time of the action.
        sequence_num (int): The sequence number of this action in the overall timeline of actions. Helpful if the sequence of events is known, but the dates are unknown.
        observed (bool): Whether the action was observed by the victim organization or investigative team at the time it happened.
        number_of_times (int): The number of times this particular action took place. E.g., subject issued "5" fraudulent checks over the course of three weeks.
        ttp_vocab (str): A reference to the TTP framework being used by this TTP. Common options are IIDES, ATT&CK, CAPEC, etc. Default is "IIDES". Required if tactic exists.
        tactic (str): The high-level category or goal of the action. A constant from 
                     `tactic-vocab <./vocab/tactic-vocab.html>`_. Required if technique exists.
        technique (str): The general action taken. If technique exists, tactic should as well. A constant from 
                         `technique-vocab <./vocab/technique-vocab.html>`_.
        location (list): Whether the action was taken on-site or remotely.
        hours (list): Whether the action was taken during work hours.
        device (list): The device where this action either took place or a device that was affected by the action. A device where the action could be detected. One or more constants from 
                       `device-vocab <./vocab/device-vocab.html>`_.
        channel (list): Methods used to transmit information outside, or into, the victim organization. One or more constants from 
                        `channel-vocab <./vocab/channel-vocab.html>`_.
        description (str): Description of the action/procedure.
        **kwargs (dict): Additional attributes for the TTP.

    Raises:
        TypeError: If any provided attribute is of the incorrect type.
        ValueError: If any provided attribute is of the incorrect vocabulary.

    Example:
        >>> ttp = TTP(
        ...     id="123e4567-e89b-12d3-a456-426614174000",
        ...     date=datetime(2023, 1, 1, 0, 0, 0),
        ...     sequence_num=1,
        ...     observed=True,
        ...     number_of_times=5,
        ...     ttp_vocab="IIDES",
        ...     tactic="1",
        ...     technique="1.1",
        ...     location=["1"],
        ...     hours=["1"],
        ...     device=["1"],
        ...     channel=["1"],
        ...     description="Initial description"
        ... )
        >>> print(ttp.id)
        123e4567-e89b-12d3-a456-426614174000
        >>> print(ttp.date)
        2020-01-01 00:00:00
    """
    def __init__(self, id=None, date=None, sequence_num=None, observed=None, number_of_times=None, ttp_vocab=None, tactic=None, technique=None, location=None, hours=None, device=None, channel=None, description=None, **kwargs):
        if id is None:
            id = str(uuid.uuid4())
        check_uuid(id)
        self._id = id

        check_type(date, datetime)
        self._date = date

        check_type(sequence_num, int)
        self._sequence_num = sequence_num

        check_type(observed, bool)
        self._observed = observed

        check_type(number_of_times, int)
        self._number_of_times = number_of_times

        check_type(ttp_vocab, str)
        self._ttp_vocab = ttp_vocab

        check_type(tactic, str)
        check_vocab(tactic, 'tactic-vocab')
        self._tactic = tactic

        check_type(technique, str)
        check_vocab(technique, 'technique-vocab')
        self._technique = technique

        check_type(location, list)
        check_vocab(location, 'attack-location-vocab')
        self._location = location

        check_type(hours, list)
        check_vocab(hours, 'attack-hours-vocab')
        self._hours = hours

        check_type(device, list)
        check_vocab(device, 'device-vocab')
        self._device = device

        check_type(channel, list)
        check_vocab(channel, 'channel-vocab')
        self._channel = channel

        check_type(description, str)
        self._description = description

        # RELATIONSHIPS 
        self._incident = None
    
    def __repr__(self):
        return (f"TTP(id={self.id}, "
                f"date={self.date}, "
                f"sequence_num={self.sequence_num}, "
                f"observed={self.observed}, "
                f"number_of_times={self.number_of_times}, "
                f"ttp_vocab={self.ttp_vocab}, "
                f"tactic={self.tactic}, "
                f"technique={self.technique}, "
                f"location={self.location}, "
                f"hours={self.hours}, "
                f"device={self.device}, "
                f"channel={self.channel}, "
                f"description={self.description})")

    def to_dict(self):
        class_dict_copy = self.__dict__.copy()
        relationships = {'_incident'}

        if self.date != None:
            class_dict_copy["date"] = str(self.date)

        class_dict_copy["_id"] = f"ttp--{self.id}"
        return ({
                    key.lstrip('_'): value 
                    for key, value in class_dict_copy.items()
                    if key not in relationships
                }, None)

    @property
    def id(self):
        return self._id  

    @id.setter
    def id(self, value):
        check_uuid(value)
        self._id = value
    
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        check_type(value, datetime, allow_none=False)
        self._date = value
    
    @date.deleter
    def date(self):
        self._date = None
    
    @property
    def sequence_num(self):
        return self._sequence_num

    @sequence_num.setter
    def sequence_num(self, value):
        check_type(value, int, allow_none=False)
        self._sequence_num = value
    
    @sequence_num.deleter
    def sequence_num(self):
        self._sequence_num = None
    
    @property
    def observed(self):
        return self._observed
    
    @observed.setter
    def observed(self, value):
        check_type(value, bool, allow_none=False)
        self._observed = value
    
    @observed.deleter
    def observed(self):
        self._observed = None
    
    @property
    def number_of_times(self):
        return self._number_of_times
    
    @number_of_times.setter
    def number_of_times(self, value):
        check_type(value, int, allow_none=False)
        self._number_of_times = value
    
    @number_of_times.deleter
    def number_of_times(self):
        self._number_of_times = None
    
    @property
    def ttp_vocab(self):
        return self._ttp_vocab
    
    @ttp_vocab.setter
    def ttp_vocab(self, value):
        check_type(value, str, allow_none=False)
        self._ttp_vocab = value
    
    @ttp_vocab.deleter
    def ttp_vocab(self):
        self._ttp_vocab = None
    
    @property
    def tactic(self):
        return self._tactic
    
    @tactic.setter
    def tactic(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'tactic-vocab')
        self._tactic = value
    
    @tactic.deleter
    def tactic(self):
        self._tactic = None
    
    @property
    def technique(self):
        return self._technique
    
    @technique.setter
    def technique(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'technique-vocab')
        self._technique = value
    
    @technique.deleter
    def technique(self):
        self._technique = None
    
    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, value):
        check_type(value, list, allow_none=False)
        check_vocab(value, 'attack-location-vocab')
        self._location = value
    
    def append_location(self, item):
        check_type(item, str, allow_none=False)
        check_vocab(item, 'attack-location-vocab')
        self._location.append(item)
    
    @location.deleter
    def location(self):
        self._location = None
    
    @property
    def hours(self):
        return self._hours
    
    @hours.setter
    def hours(self, value):
        check_type(value, list, allow_none=False)
        check_vocab(value, 'attack-hours-vocab')
        self._hours = value
    
    def append_hours(self, item):
        check_type(item, str, allow_none=False)
        check_vocab(item, 'attack-hours-vocab')
        self._hours.append(item)

    @hours.deleter
    def hours(self):
        self._hours = None
    
    @property
    def device(self):
        return self._device
    
    @device.setter
    def device(self, value):
        check_type(value, list, allow_none=False)
        check_vocab(value, 'device-vocab')
        self._device = value
    
    def append_device(self, item):
        check_type(item, str, allow_none=False)
        check_vocab(item, 'device-vocab')
        self._device.append(item)

    @device.deleter
    def device(self):
        self._device = None
    
    @property
    def channel(self):
        return self._channel
    
    @channel.setter
    def channel(self, value):
        check_type(value, list, allow_none=False)
        check_vocab(value, 'channel-vocab')
        self._channel = value
    
    def append_channel(self, item):
        check_type(item, str, allow_none=False)
        check_vocab(item, 'channel-vocab')
        self._channel.append(item)

    @channel.deleter
    def channel(self):
        self._channel = None
    
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        check_type(value, str, allow_none=False)
        self._description = value
    
    @description.deleter
    def description(self):
        self._description = None

    # - - - - - - - RELATIONSHIPS - - - - - - 
    @property
    def incident(self):
        return self._incident
    
    @incident.setter
    def incident(self, value):
        check_type(value, Incident, allow_none=False)
        
        # set the incident
        # first remove all old relationships if they exist
        if self._incident != None:
            self._incident.ttps.remove(self)
        self._incident = value

        # add it to the incident's ttp list
        if value.ttps == None:
            value.ttps = [self]
        elif self not in value.ttps:
            value.ttps.append(self)
    
    @incident.deleter
    def incident(self):
        # remove the ttpfrom incident ttp list, as well as 
        # set the incident attribute to none
        if self._incident != None:
            self._incident.ttps.remove(self)
            self._incident = None


class Sentence:
    """
    Initializes a Sentence instance
    
    Args:
        id (required) (string) : Unique identifier for the sentence. Defaults to a new UUIDv4 string if not provided.
        sentence_type (required) (string) : The type of sentence that was ordered.
            A constant from `sentence-type-vocab <./vocab/sentence-type-vocab.html>`_.
        quantity (integer) : The quantity of the sentence type imposed. MUST be used with the metric property if used.
            Required if metric exists.
        metric (string) : The measurement type of the sentence imposed. MUST be used with the quantity property if used.
            A constant from `sentence-metric-vocab <./vocab/sentence-metric-vocab.html>`_.
            Required if quantity exists.
        concurrency (boolean) : Whether the sentence is to run concurrently (at the same time as) other sentences within the same case.
    
    Raises:
        TypeError: If any provided attribute is of the incorrect type.
        ValueError: If any provided attribute is of the incorrect vocabulary. 
    
    Example:
        >>> from pyiides.utils.helper_functions import Sentence
        >>> sentence = Sentence(
        ...     id="6eaf8e6c-8c4d-4d9d-8f8e-6c8c4d4d9d8f",
        ...     sentence_type="9",
        ...     quantity=5,
        ...     metric="Years",
        ...     concurrency=True
        ... )
        >>> print(sentence.sentence_type)
        9
        >>> print(sentence.quantity)
        5
    """
    def __init__(self, sentence_type, id=None, quantity=None, metric=None, concurrency=None) -> None:
        if id is None:
            id = str(uuid.uuid4())
        check_uuid(id)
        self._id = id

        check_type(sentence_type, str)
        check_vocab(sentence_type, 'sentence-type-vocab')
        self._sentence_type = sentence_type

        if (quantity == None and metric != None or quantity != None and metric == None):
            raise ReferenceError("Either quantity and metric must coexist, or they are both None")
        
        check_type(quantity, int)
        self._quantity = quantity

        check_type(metric, str)
        check_vocab(metric, 'sentence-metric-vocab')
        self._metric = metric

        check_type(concurrency, bool)
        self._concurrency = concurrency

        # relationships
        self._court_case = None

    def __repr__(self):
        return (f"Sentence(id={self.id}, "
                f"sentence_type={self.sentence_type}, "
                f"quantity={self.quantity}, "
                f"metric={self.metric}, "
                f"concurrency={self.concurrency})")

    def to_dict(self):
        class_dict_copy = self.__dict__.copy()
        relationships = {'_court_case'}
        class_dict_copy["_id"] = f"sentence--{self.id}"
        return ({
                    key.lstrip('_'): value 
                    for key, value in class_dict_copy.items()
                    if key not in relationships
                }, None)

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        check_uuid(value)
        self._id = value
    
    @property
    def sentence_type(self):
        return self._sentence_type
    
    @sentence_type.setter
    def sentence_type(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'sentence-type-vocab')
        self._sentence_type = value

    @sentence_type.deleter
    def sentence_type(self):
        self._sentence_type = None

    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, value):
        check_type(value, int, allow_none=False)
        self._quantity = value

        if self._metric == None:
            val = input("Please enter an input for metric:\n")
            check_type(val, str)
            check_vocab(val, 'sentence-metric-vocab')
            self._metric = val
            if (self._metric == None):
                raise ReferenceError("Either quantity and metric must coexist, or they are both None")

    @quantity.deleter
    def quantity(self):
        self._quantity = None
        self._metric = None

    @property
    def metric(self):
        return self._metric
    
    @metric.setter
    def metric(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'sentence-metric-vocab')
        self._metric = value

        if self._quantity == None:
            val = input("Please enter an input for quantity:\n")
            check_type(val, int)
            self._quantity = val
            if (self._quantity == None):
                raise ReferenceError("Either quantity and metric must coexist, or they are both None")

    @metric.deleter
    def metric(self):
        self._metric = None
        self._quantity = None

    @property
    def concurrency(self):
        return self._concurrency
    
    @concurrency.setter
    def concurrency(self, value):
        check_type(value, bool, allow_none=True)
        self._concurrency = value

    @concurrency.deleter
    def concurrency(self):
        self._concurrency = None
    
    # - - - - - - - RELATIONSHIPS - - - - - - 
    @property
    def court_case(self):
        return self._court_case
    
    @court_case.setter
    def court_case(self, value):
        
        check_type(value, CourtCase, allow_none=False)
        
        # set the court case
        # making sure to remove old relationships
        if self._court_case != None:
            self._court_case.sentences.remove(self)
        self._court_case = value

        # add it to the court case's sentence list
        if value.sentences == None:
            value.sentences = [self]
        elif self not in value.sentences: 
            value.sentences.append(self)
    
    @court_case.deleter
    def court_case(self):
        if self._court_case != None:
            self._court_case.sentences.remove(self)
            self._court_case = None


class Target:
    """
    Initializes a Target instance 

    Args:
        id (required) (string) : Unique identifier for the target. Defaults to a new UUIDv4 string if not provided.
        asset_type (required) (string) : The type of target.
            A constant from `target-asset-vocab <./vocab/target-asset-vocab.html>`_.
            Required if category exists.
        category (required) (string) : The classification group a target belongs to.
            A constant from `target-category-vocab <./vocab/target-category-vocab.html>`_.
            Required if subcategory exists.
        subcategory (required) (string) : The lower-level classification group a target belongs to.
            A constant from `target-subcategory-vocab <./vocab/target-subcategory-vocab.html>`_.
        format (required) (string) : The data type of the target.
            A constant from `target-format-vocab <./vocab/target-format-vocab.html>`_.
        owner (required) (string) : Who the data is about. For assets, the owner of the asset. In cases where the owner and subject of the data/asset is unclear, pick the person/group most responsible for safeguarding the data/asset.
            A constant from `target-owner-vocab <./vocab/target-owner-vocab.html>`_.
        sensitivity (required) (array) : The level of sensitivity and controls applied to a target.
            One or more constants from `target-sensitivity-vocab <./vocab/target-sensitivity-vocab.html>`_.
        description (string) : Brief description of the target.
    
    Raises:
        TypeError: If any provided attribute is of the incorrect type.
        ValueError: If any provided attribute is of the incorrect vocabulary. 
    
    Example:
        >>> target = Target(
        ...     id="12345678-1234-1234-1234-123456789abc",
        ...     asset_type="4",
        ...     category="4.1",
        ...     subcategory="4.1.1",
        ...     format="1",
        ...     owner="O",
        ...     sensitivity=["25"],
        ...     description="Client list for manifold sales"
        ... )
        >>> print(target.id)
        12345678-1234-1234-1234-123456789abc
        >>> print(target.asset_type)
        4
        >>> print(target.category)
        4.1
        >>> print(target.subcategory)
        4.1.1
        >>> print(target.format)
        1
    """
    def __init__(self, asset_type, category, subcategory, format, owner, sensitivity, id=None, description=None):
        if id is None:
            id = str(uuid.uuid4())

        check_uuid(id)
        self._id = id

        check_type(asset_type, str)
        check_vocab(asset_type, 'target-asset-vocab')
        self._asset_type = asset_type

        check_type(category, str)
        check_vocab(category, 'target-category-vocab')
        self._category = category

        check_type(subcategory, str)
        check_vocab(subcategory, 'target-subcategory-vocab')
        self._subcategory = subcategory

        check_type(format, str)
        check_vocab(format, 'target-format-vocab')
        self._format = format

        check_type(owner, str)
        check_vocab(owner, 'target-owner-vocab')
        self._owner = owner

        check_type(sensitivity, list)
        check_vocab(sensitivity, 'target-sensitivity-vocab')
        self._sensitivity = sensitivity

        check_type(description, str)
        self._description = description

        # relationships
        self._incident = None
    
    def __repr__(self):
        return (f"Target(id={self.id}, "
                f"assert_type={self.asset_type}, "
                f"category={self.category}, "
                f"subcategory={self.subcategory}, "
                f"format={self.format}, "
                f"owner={self.owner}, "
                f"sensitivity={self.sensitivity}, "
                f"description={self.description})")
    
    def to_dict(self):
        class_dict_copy = self.__dict__.copy()
        relationships = {'_incident'}
        class_dict_copy["_id"] = f"target--{self.id}"
        return ({
                    key.lstrip('_'): value 
                    for key, value in class_dict_copy.items()
                    if key not in relationships
                }, None)

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        check_uuid(value)
        self._id = value
    
    @id.deleter
    def id(self):
        self._id = None

    @property
    def asset_type(self):
        return self._asset_type
    
    @asset_type.setter
    def asset_type(self, value):
        check_type(value, str)
        check_vocab(value, 'target-asset-vocab')
        self._asset_type = value
    
    @asset_type.deleter
    def asset_type(self):
        self._asset_type = None

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        check_type(value, str)
        check_vocab(value, 'target-category-vocab')
        self._category = value
    
    @category.deleter
    def category(self):
        self._category = None

    @property
    def subcategory(self):
        return self._subcategory
    
    @subcategory.setter
    def subcategory(self, value):
        check_type(value, str)
        check_vocab(value, 'target-subcategory-vocab')
        self._subcategory = value
    
    @subcategory.deleter
    def subcategory(self):
        self._subcategory = None

    @property
    def format(self):
        return self._format
    
    @format.setter
    def format(self, value):
        check_type(value, str)
        check_vocab(value, 'target-format-vocab')
        self._format = value
    
    @format.deleter
    def format(self):
        self._format = None

    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, value):
        check_type(value, str)
        check_vocab(value, 'target-owner-vocab')
        self._owner = value
    
    @owner.deleter
    def owner(self):
        self._owner = None

    @property
    def sensitivity(self):
        return self._sensitivity
    
    @sensitivity.setter
    def sensitivity(self, value):
        check_type(value, list)
        check_vocab(value, 'target-sensitivity-vocab')
        self._sensitivity = value
    
    @sensitivity.deleter
    def sensitivity(self):
        self._sensitivity = None

    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        check_type(value, str)
        self._description = value
    
    @description.deleter
    def description(self):
        self._description = None
    
    # - - - - - - - RELATIONSHIPS - - - - - - 
    @property
    def incident(self):
        return self._incident
    
    @incident.setter
    def incident(self, value):
        
        check_type(value, Incident, allow_none=False)
        
        # set the incident 
        # making sure to remove old relationships first
        if self._incident != None:
            self._incident.targets.remove(self)
        self._incident = value 

        # add this to the incident's target list 
        if value.targets == None:
            value.targets = [self]
        elif self not in value.targets: 
            value.targets.append(self)
    
    @incident.deleter
    def incident(self):
        if self._incident != None:
            self._incident.targets.remove(self)
            self._incident = None


class Accomplice(Person):
    """
    Initialize an Accomplice instance, inheriting from Person.

    Args:
        id (str): Unique identifier for the accomplice. Defaults to a new
            UUIDv4 string if not provided.
        relationship_to_insider (str): The relationship of the accomplice to
            the insider. Must be a valid constant from
            `insider-relationship-vocab <./vocab/insider-relationship-vocab.html>`_.
        **kwargs (dict): Additional attributes inherited from the Person class.

    Raises:
        TypeError: If any provided attribute is of the incorrect type.
        ValueError: If any provided attribute is of the incorrect vocabulary.

    Examples:
        >>> from pyiides.pyiides.accomplice import Accomplice
        >>> accomplice = Accomplice(
        ...     first_name="John",
        ...     last_name="Doe",
        ...     relationship_to_insider="1"
        ... )
        >>> print(accomplice.id)
        e6d8b622-8d6a-4f5b-8b9a-d7c93c6ee6b6
        >>> print(accomplice.relationship_to_insider)
        1
    """
    def __init__(self, id=None, relationship_to_insider=None, **kwargs):
        # inherit everything from Person
        super().__init__(**kwargs)

        if id is None:
            id = str(uuid.uuid4())

        check_uuid(id)
        self._id = id

        check_type(relationship_to_insider, str)
        check_vocab(relationship_to_insider, 'insider-relationship-vocab')
        self._relationship_to_insider = relationship_to_insider

        # Relationships:
        self._insider = None
        self._jobs = None
        self._sponsor = None

    def __repr__(self):
        return (f"Accomplice(id={self.id}, "
                f"relationship_to_insider={self.relationship_to_insider})")

    def to_dict(self):
        """
        returns tuple: (dict of class itself, list containing child id's to connect)
        """
        class_dict_copy = self.__dict__.copy()

        relationships = {'_insider', '_jobs', '_sponsor'}

        children_ids = None
        if self.jobs != None:
            children_ids = ["jobs--" + x.id for x in self.jobs]

        class_dict_copy["_id"] = f"accomplice--{self.id}"
        return ({
                    key.lstrip('_'): value
                    for key, value in class_dict_copy.items()
                    if key not in relationships
                },
                children_ids
                )

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        check_uuid(value)
        self._id = value

    @property
    def relationship_to_insider(self):
        return self._relationship_to_insider

    @relationship_to_insider.setter
    def relationship_to_insider(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'insider-relationship-vocab')
        self._relationship_to_insider = value

    @relationship_to_insider.deleter
    def relationship_to_insider(self):
        self._relationship_to_insider = None

    # - - - - - - - - - - RELATIONSHIPS - - - - - - - - - -
    @property
    def insider(self):
        return self._insider

    @insider.setter
    def insider(self, value):
        
        check_type(value, Insider, allow_none=False)

        # set the insider
        # making sure to remove all old relationships first if they exist
        if self._insider != None:
            self._insider.accomplices.remove(self)
        self._insider = value

        # add this accomplice to the insider's accomplice list
        if value.accomplices == None:
            value.accomplices = [self]
        elif self not in value.accomplices:
            value.accomplices.append(self)

    @insider.deleter
    def insider(self):
        if self._insider != None:
            self._insider.accomplices.remove(self)
            self._insider = None

    @property
    def jobs(self):
        return self._jobs

    @jobs.setter
    def jobs(self, value):
        # to the future dev: im sorry i didnt modularize these setters/getters,
        # they could be made into one cute little helper function
        # you got it :)
        check_type(value, list)

        # check that all elements are Job objects
        for obj in value:
            
            check_type(obj, Job, allow_none=False)

        # set the new job list
        # making sure to remove old relationships first if they exist
        if self._jobs != None:
            for j in list(self._jobs):
                del j.accomplice
        self._jobs = value

        # connect those jobs back to this instance of accomplice
        for obj in value:
            if obj.accomplice != self:
                obj.accomplice = self

    def append_job(self, item):
        
        check_type(item, Job, allow_none=False)

        if self._jobs == None:
            self._jobs = [item]
        else:
            self._jobs.append(item)

        item.accomplice = self

    def remove_job(self, item):
        
        check_type(item, Job, allow_none=False)
        if self._jobs != None:
            del item.accomplice

    @jobs.deleter
    def jobs(self):
        # need to create a copy using list() since we
        # are removing from the list we are also
        # iterating over
        for obj in list(self._jobs):
            del obj.accomplice
        self._jobs = None

    @property
    def sponsor(self):
        return self._sponsor

    @sponsor.setter
    def sponsor(self, value):
        
        check_type(value, Sponsor, allow_none=False)

        # set the sponsor
        # making sure to remove old relationships first
        if self._sponsor != None:
            self._sponsor.accomplices.remove(self)
        self._sponsor = value

        # add it to the sponsor's accomplice list
        if value.accomplices == None:
            value.accomplices = [self]
        elif self not in value.accomplices:
            value.accomplices.append(self)

    @sponsor.deleter
    def sponsor(self):
        if self._sponsor != None:
            self._sponsor.accomplices.remove(self)
            self._sponsor = None


class OrgRelationship:
    """
    Initializes an OrgRelationship instance

    Args:
        id (string) : Unique identifier for the organization relationship. Defaults to a new UUIDv4 string if not provided.
        org1 (required) (Organization) : The first organization involved in the relationship.
        org2 (required) (Organization) : The second organization involved in the relationship.
        relationship (required) (string) : The type of relationship between the two organizations.
            A constant from `org-relationship-vocab <./vocab/org-relationship-vocab.html>`_.
    
    Raises:
        TypeError: If any provided attribute is of the incorrect type.
        ValueError: If any provided attribute is of the incorrect vocabulary. 
    
    Example:
        >>> from pyiides.utils.helper_functions import OrgRelationship
        >>> 
        >>> org1 = Organization(name="Org One")
        >>> org2 = Organization(name="Org Two")
        >>> org_relationship = OrgRelationship(
        ...     org1=org1,
        ...     org2=org2,
        ...     relationship="C",
        ...     id="org-relationship--6eaf8e6c-8c4d-4d9d-8f8e-6c8c4d4d9d8f"
        ... )
        >>> print(org_relationship.org1)
        Org One
        >>> print(org_relationship.relationship)
        C
    """
    def __init__(self, org1, org2, relationship, id=None):
        if id == None:
            id = str(uuid.uuid4())

        check_uuid(id)
        self._id = id
        
        
        check_type(org1, Organization)
        self._org1 = org1 

        check_type(org2, Organization)
        self._org2 = org2 

        check_type(relationship, str)
        check_vocab(relationship, 'org-relationship-vocab')
        self._relationship = relationship

    def __repr__(self):
        return (f"OrgRelationship(id={self.id}, "
                f"org1={self.org1}, "
                f"org2={self.org2}, "
                f"relationship={self.relationship})")

    def to_dict(self):
        class_dict_copy = self.__dict__.copy()
        class_dict_copy["_id"] = f"org-relationship--{self.id}"
        return ({
                    key.lstrip('_'): value for key, value in class_dict_copy.items()
                }, None)

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        check_uuid(value)
        self._id = value
    
    @property
    def org1(self):
        return self.org1

    @org1.setter
    def org1(self, value):
        
        check_type(value, Organization)
        self._org1 = value
    
    @org1.deleter
    def org1(self):
        self._org1 = None
    
    @property
    def org2(self):
        return self.org2

    @org2.setter
    def org2(self, value):
        
        check_type(value, Organization)
        self._org2 = value
    
    @org2.deleter
    def org2(self):
        self._org2 = None
    
    @property
    def relationship(self):
        return self._relationship
    
    @relationship.setter
    def relationship(self, value):
        check_type(value, str)
        check_vocab(value, 'org-relationship-vocab')
        self._relationship = value
    
    @relationship.deleter
    def relationship(self):
        self._relationship = None


class Sponsor:
    """
    Initializes a Sponsor instance

    Args:
        id (required) (string) : Unique identifier for the sponsor. Defaults to a new UUIDv4 string if not provided.
        name (string) : The name of the individual or entity sponsoring the insider's actions.
        sponsor_type (string) : The type of sponsor.
            A constant from `sponsor-type-vocab <./vocab/sponsor-type-vocab.html>`_.
    
    Raises:
        TypeError: If any provided attribute is of the incorrect type.
        ValueError: If any provided attribute is of the incorrect vocabulary. 
    
    Example:
        >>> from pyiides.utils.helper_functions import Sponsor
        >>> sponsor = Sponsor(
        ...     id="6eaf8e6c-8c4d-4d9d-8f8e-6c8c4d4d9d8f",
        ...     name="Foreign Government",
        ...     sponsor_type="SS"
        ... )
        >>> print(sponsor.name)
        Foreign Government
        >>> print(sponsor.sponsor_type)
        SS
    """
    
    def __init__(self, id=None, name=None, sponsor_type=None):  
        if id is None:
            id = str(uuid.uuid4())
        check_uuid(id)
        self._id = id

        check_type(name, str)
        self._name = name

        check_type(sponsor_type, str)
        check_vocab(sponsor_type, 'sponsor-type-vocab')
        self._sponsor_type = sponsor_type

        # Relationships
        self._accomplices = None
        self._insiders = None
    
    def __repr__(self):
        return (f"Sponsor(id={self.id}, "
                f"name={self.name}, "
                f"sponsor_type={self.sponsor_type})")

    def to_dict(self):
        class_dict_copy = self.__dict__.copy()

        relationships = {'_accomplices', '_insiders'}

        children_ids = None

        if self.accomplices != None:
            children_ids = ["accomplice--" + x.id for x in self.accomplices]
        
        if self.insiders != None:
            insiders = ["insider--" + x.id for x in self.insiders]
            if children_ids == None: 
                children_ids = insiders
            else:
                children_ids.extend(insiders)

        class_dict_copy["_id"] = f"sponsor--{self.id}"
        return ({
                    key.lstrip('_'): value 
                    for key, value in class_dict_copy.items()
                    if key not in relationships
                }, children_ids)
    @property
    def id(self):
        return self._id  

    @id.setter
    def id(self, value):
        check_uuid(value)
        self._id = value

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        check_type(value, str, allow_none=False)
        self._name = value

    @name.deleter 
    def name(self):
        self._name = None
    
    @property
    def sponsor_type(self):
        return self._sponsor_type
    
    @sponsor_type.setter
    def sponsor_type(self, value):
        check_type(value, str)
        check_vocab(value, 'sponsor-type-vocab')
        self._sponsor_type = value
    
    @sponsor_type.deleter
    def sponsor_type(self):
        self._sponsor_type = None

    # - - - - - - - - - - RELATIONSHIPS - - - - - - - - - -

    @property
    def accomplices(self):
        return self._accomplices
    
    @accomplices.setter
    def accomplices(self, value):
        check_type(value, list, allow_none=False)

        # check that all elements are accomplice objects
        for obj in value:
            
            check_type(obj, Accomplice, allow_none=False)
        
        # set to new accomplice list
        # making sure to remove old relationships first
        if self._accomplices != None:
            # use list to create a copy
            for a in list(self._accomplices):
                del a.sponsor
        self._accomplices = value

        # connect those back to this instance of sponsor
        for obj in value: 
            if obj.sponsor != self:
                obj.sponsor = self

    def append_accomplice(self, item):
        
        check_type(item, Accomplice, allow_none=False)
        if self._accomplices == None:
            self._accomplices = [item]
        else:
            self._accomplices.append(item)

        # need to connect this after, or else it adds self twice
        item.sponsor = self
    
    def remove_accomplice(self, item):
        
        check_type(item, Accomplice, allow_none=False)
        if self._accomplices != None:
            del item.sponsor  

    @accomplices.deleter
    def accomplices(self):
        # adding list() creates a copy so that we don't
        # run into any issues with removing elements 
        # from the list we are iterating over
        for obj in list(self._accomplices):
            del obj.sponsor
        self._accomplices = None

    @property
    def insiders(self):
        return self._insiders
    
    @insiders.setter
    def insiders(self, value):
        check_type(value, list, allow_none=False)

        # check that all elements inside are Insider objects
        for obj in value:
            
            check_type(obj, Insider, allow_none=False)

        # set new insider list
        # making sure to remove the old relationships first
        if self._insiders != None:
            # using list() to create a copy
            for i in list(self._insiders):
                del i.sponsor
        self._insiders = value

        # connect those insiders to this sponsor instance
        for obj in value: 
            if obj.sponsor != self:
                obj.sponsor = self

    def append_insider(self, item):
        
        check_type(item, Insider, allow_none=False)
        if self._insiders == None:
            self._insiders = [item]
        else:
            self._insiders.append(item)
        
        # need to set this after, or else it may add self twice
        item.sponsor = self
    
    def remove_insider(self, item):
        
        check_type(item, Insider, allow_none=False)
        if self._insiders != None:
            del item.sponsor  

    @insiders.deleter
    def insiders(self):
        # adding list() creates a copy so that we don't
        # run into any issues with removing elements 
        # from the list we are iterating over
        for obj in list(self._insiders):
            del obj.sponsor
        self._insiders = None


class CourtCase:
    """
    Initializes a CourtCase instance

    Args:
        id (required) (string) : Unique identifier for the court case. Defaults to a new UUIDv4 string if not provided.
        case_number (string) : A case number assigned by the court system in which the case is being tried.
        case_title (string) : Title provided by the court system (e.g., 'USA v. LastName' or 'USA v. LastName, et al.').
        court_country (string) : Country where the case was tried.
            A constant from `country-vocab <./vocab/country-vocab.html>`_.
        court_state (string) : State or region where the case was tried.
            A constant from `state-vocab-us <./vocab/state-vocab-us.html>`_.
        court_district (string) : District where the case was tried, if applicable (e.g., "CA Central District Court").
        court_type (string) : Type or level of the court where the case is tried.
            A constant from `court-type-vocab <./vocab/court-type-vocab.html>`_.
        case_type (string) : Type of case.
            A constant from `case-type-vocab <./vocab/case-type-vocab.html>`_.
        defendant (array) : The names of all the defendants (or respondents, or appellees) in the case.
            One or more string values.
        plaintiff (array) : The names of all the plaintiffs (or petitioners, or appellants) in the case.
            One or more string values.
        comment (string) : Clarifying comments about any of the court case details, or its associated charges and sentences, 
                          such as which sentences run concurrently, the structure of a plea deal, or the status of the case.
    
    Raises:
        TypeError: If any provided attribute is of the incorrect type.
        ValueError: If any provided attribute is of the incorrect vocabulary. 

    Example:
        >>> from pyiides.utils.helper_functions import CourtCase
        >>> court_case = CourtCase(
        ...     case_number="1:22-cr-00123-JMF",
        ...     case_title="USA v. Smith",
        ...     court_country="US",
        ...     court_state="NY",
        ...     court_district="Southern District of New York",
        ...     court_type="Federal",
        ...     case_type="Criminal",
        ...     defendant=["John Smith"],
        ...     plaintiff=["United States of America"],
        ...     comment="This case involved multiple charges including espionage and unauthorized disclosure of classified information."
        ... )
        >>> print(court_case.case_title)
        USA v. Smith
        >>> print(court_case.court_country)
        US
    """
    def __init__(self, id=None, case_number=None, case_title=None, court_country=None, court_state=None, court_district=None, court_type=None, case_type=None, defendant=None, plaintiff=None, comment=None):
        if id == None:
            id = str(uuid.uuid4())

        check_uuid(id)
        self._id = id

        check_type(case_number, str)
        self._case_number = case_number

        check_type(case_title, str)
        self._case_title = case_title

        check_type(court_country, str)
        check_vocab(court_country, 'country-vocab')
        self._court_country = court_country

        check_type(court_state, str)
        check_vocab(court_state, 'state-vocab-us')
        self._court_state = court_state

        check_type(court_district, str)
        self._court_district = court_district

        check_type(court_type, str)
        check_vocab(court_type, 'court-type-vocab')
        self._court_type = court_type

        check_type(case_type, str)
        check_vocab(case_type, 'case-type-vocab')
        self._case_type = case_type

        check_type(defendant, list)
        if defendant != None:
            for s in defendant:
                check_type(s, str)
        self._defendant = defendant

        check_type(plaintiff, list)
        if plaintiff != None:
            for s in plaintiff:
                check_type(s, str)
        self._plaintiff = plaintiff

        check_type(comment, str)
        self._comment = comment

        # Relationships:
        self._legal_response = None
        self._sentences = None
        self._charges = None

    def __repr__(self):
        return (f"CourtCase(id={self.id}, "
                f"case_number={self.case_number}, "
                f"case_title={self.case_title}, "
                f"court_country={self.court_country}, "
                f"court_state={self.court_state}, "
                f"court_district={self.court_district}, "
                f"court_type={self.court_type}, "
                f"case_type={self.case_type}, "
                f"defendant={self.defendant}, "
                f"plaintiff={self.plaintiff}, "
                f"comment={self.comment}) ")
    
    def to_dict(self):
        class_dict_copy = self.__dict__.copy()

        relationships = {'_legal_response', '_sentences', '_charges'}

        children_ids = None 

        if self.charges != None:
            children_ids = ["charge--" + x.id for x in self.charges]

        if self.sentences != None:
            sentences = ["sentence--" + x.id for x in self.sentences]
            if children_ids == None: 
                children_ids = sentences
            else:
                children_ids.extend(sentences)
        
        class_dict_copy["_id"] = f"court-case--{self.id}"
        return ({
                    key.lstrip('_'): value 
                    for key, value in class_dict_copy.items()
                    if key not in relationships
                }, children_ids)

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        check_uuid(value)
        self._id = value
    
    @property
    def case_number(self):
        return self._case_number
    
    @case_number.setter
    def case_number(self, value):
        check_type(value, str, allow_none=False)
        self._case_number = value
    
    @case_number.deleter
    def case_number(self):
        self._case_number = None

    @property
    def case_title(self):
        return self._case_title

    @case_title.setter
    def case_title(self, value):
        check_type(value, str, allow_none=False)
        self._case_title = value

    @case_title.deleter
    def case_title(self):
        self._case_title = None

    @property
    def court_country(self):
        return self._court_country
    
    @court_country.setter
    def court_country(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'country-vocab')
        self._court_country = value
    
    @court_country.deleter
    def court_country(self):
        self._court_country = None

    @property
    def court_state(self):
        return self._court_state
    
    @court_state.setter
    def court_state(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'state-vocab-us')
        self._court_state = value
    
    @court_state.deleter
    def court_state(self):
        self._court_state = None

    @property
    def court_district(self):
        return self._court_district
    
    @court_district.setter
    def court_district(self, value):
        check_type(value, str, allow_none=False)
        self._court_district = value
    
    @court_district.deleter
    def court_district(self):
        self._court_district = None

    @property
    def court_type(self):
        return self._court_type
    
    @court_type.setter
    def court_type(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'court-type-vocab')
        self._court_type = value
    
    @court_type.deleter
    def court_type(self):
        self._court_type = None

    @property
    def case_type(self):
        return self._case_type
    
    @case_type.setter
    def case_type(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'case-type-vocab')
        self._case_type = value
    
    @case_type.deleter
    def case_type(self):
        self._case_type = None

    @property
    def defendant(self):
        return self._defendant
    
    @defendant.setter
    def defendant(self, value):
        check_type(value, list, allow_none=False)
        if value is not None:
            for s in value:
                check_type(s, str, allow_none=False)
        self._defendant = value
    
    def append_defendant(self, item):
        check_type(item, str, allow_none=False)
        self._defendant.append(item)
    
    @defendant.deleter
    def defendant(self):
        self._defendant = None

    @property
    def plaintiff(self):
        return self._plaintiff
    
    @plaintiff.setter
    def plaintiff(self, value):
        check_type(value, list, allow_none=False)
        if value is not None:
            for s in value:
                check_type(s, str, allow_none=False)
        self._plaintiff = value
    
    def append_plaintiff(self, item):
        check_type(item, str, allow_none=False)
        self._plaintiff.append(item)

    @plaintiff.deleter
    def plaintiff(self):
        self._plaintiff = None

    @property
    def comment(self):
        return self._comment
    
    @comment.setter
    def comment(self, value):
        check_type(value, str, allow_none=False)
        self._comment = value
    
    @comment.deleter
    def comment(self):
        self._comment = None

    # - - - - - - - RELATIONSHIPS - - - - - - 
    @property
    def legal_response(self):
        return self._legal_response
    
    @legal_response.setter
    def legal_response(self, value):
        
        check_type(value, LegalResponse, allow_none=False)
        
        # if the legal response was already set, we have to remove
        # its current relationships before setting the new one
        if self._legal_response != None:
            self._legal_response.court_cases.remove(self)
        self._legal_response = value

        # add court case to legal response's court case list
        if value.court_cases == None:
            value.court_cases = [self]
        elif self not in value.court_cases:
            value.court_cases.append(self)
    
    @legal_response.deleter
    def legal_response(self):
        if self._legal_response != None:
            self._legal_response.court_cases.remove(self)
            self._legal_response = None

    @property
    def sentences(self):
        return self._sentences
    
    @sentences.setter
    def sentences(self, value):
        check_type(value, list, allow_none=False)

        # check that all elements are sentence objects
        for obj in value:
            
            check_type(obj, Sentence, allow_none=False)
        
        # set the new sentences list:
        # if it is not None, we need to remove 
        # the old relationships first
        if self._sentences != None:
            for s in self._sentences:
                del s.court_case
        self._sentences = value

        # connect those sentences back to this 
        # instance of court case
        for obj in value: 
            if obj.court_case != self:
                obj.court_case = self
    
    def append_sentence(self, item):
        
        check_type(item, Sentence, allow_none=False)
        
        if self._sentences == None:
            self._sentences = [item]
        else:
            self._sentences.append(item)
        
        item.court_case = self    
    
    def remove_sentence(self, item):
        
        check_type(item, Sentence, allow_none=False)
        if self._sentences != None:
            del item.court_case 
    
    @sentences.deleter
    def sentences(self):
        # adding list() creates a copy so that we don't
        # run into any issues with removing elements 
        # from the list we are iterating over
        for obj in list(self._sentences):
            del obj.court_case
        self._sentences = None
    
    @property
    def charges(self):
        return self._charges
    
    @charges.setter
    def charges(self, value):
        check_type(value, list, allow_none=False)

        # check that all elements within the list
        # are Charge objects 
        for obj in value:
            
            check_type(obj, Charge, allow_none=False)

        # set the charges list
        # if it is not None, we need to remove 
        # the old relationships first
        if self._charges != None:
            # use list() to create a copy
            for c in list(self._charges):
                del c.court_case
        self._charges = value

        # connect each charge back to this court case
        # instance
        for obj in value: 
            if obj.court_case != self:
                obj.court_case = self
    
    def append_charge(self, item):
        
        check_type(item, Charge, allow_none=False)
          
        if self._charges == None:
            self._charges = [item]
        else:
            self._charges.append(item)
        
        item.court_case = self 
    
    def remove_charge(self, item):
        
        check_type(item, Charge, allow_none=False)
        if self._charges != None:
            del item.court_case 
 
    @charges.deleter
    def charges(self):
        # adding list() creates a copy so that we don't
        # run into any issues with removing elements 
        # from the list we are iterating over
        for obj in list(self._charges):
            del obj.court_case
        self._charges = None


class Source:
    """
    Initializes a Source instance

    Args:
        id (string) : Unique identifier for the source. Defaults to a new UUIDv4 string if not provided.
        title (required) (string) : The title of the source.
        source_type (string) : The type of the source.
        file_type (string) : The type of file (e.g., pdf, html).
        date (datetime) : The date the source was created or last modified.
        public (bool) : Indicates if the source is public.
        document (string) : The document or URL associated with the source.
        comment (string): Clarifying comments about the source.

    Raises:
        TypeError: If any provided attribute is of the incorrect type.
        ValueError: If any provided attribute is of the incorrect vocabulary.

    Example:
        >>> from datetime import datetime
        >>> source = Source(
        ...     title="Sample Title",
        ...     id="source--123e4567-e89b-12d3-a456-426614174000",
        ...     source_type="Type A",
        ...     file_type="pdf",
        ...     date=datetime(2023, 1, 1),
        ...     public=True,
        ...     document="http://example.com",
        ...     comment="Sample comments about the sample source."
        ... )
        >>> print(source.title)
        Sample Title
        >>> print(source.date)
        2023-01-01 00:00:00
    """
    def __init__(self, title, id=None, source_type=None, file_type=None, date=None, public=None, document=None, comment=None):
        if id is None:
            id = str(uuid.uuid4())
        check_uuid(id)
        self._id = id

        check_type(title, str)
        self._title = title 

        check_type(source_type, str)
        self._source_type = source_type

        check_type(file_type, str)
        self._file_type = file_type

        check_type(date, datetime)
        self._date = date

        check_type(public, bool)
        self._public = public

        check_type(document, str)
        self._document = document

        check_type(comment, str)
        self._comment = comment

        # relationships
        self._incident = None

    def __repr__(self):
        return (f"Source(id={self.id}, "
                f"title={self.title}, "
                f"source_type={self.source_type}, "
                f"file_type={self.file_type}, "
                f"date={self.date}, "
                f"public={self.public}, "
                f"document={self.document}), "
                f"comment={self.comment}")

    def to_dict(self):
        class_dict_copy = self.__dict__.copy()
        relationships = {'_incident'}

        if self.date != None:
            class_dict_copy["_date"] = str(self.date)

        class_dict_copy["_id"] = f"source--{self.id}"
        return ({
                    key.lstrip('_'): value 
                    for key, value in class_dict_copy.items()
                    if key not in relationships
                }, None)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        check_uuid(value)
        self._id = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        check_type(value, str)
        self._title = value

    @title.deleter
    def title(self):
        self._title = None

    @property
    def source_type(self):
        return self._source_type

    @source_type.setter
    def source_type(self, value):
        check_type(value, str)
        self._source_type = value

    @source_type.deleter
    def source_type(self):
        self._source_type = None

    @property
    def file_type(self):
        return self._file_type

    @file_type.setter
    def file_type(self, value):
        check_type(value, str)
        self._file_type = value

    @file_type.deleter
    def file_type(self):
        self._file_type = None

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        check_type(value, datetime)
        self._date = value

    @date.deleter
    def date(self):
        self._date = None

    @property
    def public(self):
        return self._public

    @public.setter
    def public(self, value):
        check_type(value, bool)
        self._public = value

    @public.deleter
    def public(self):
        self._public = None

    @property
    def document(self):
        return self._document

    @document.setter
    def document(self, value):
        check_type(value, str)
        self._document = value

    @document.deleter
    def document(self):
        self._document = None

    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, value):
        check_type(value, str)
        self._comment = value

    @comment.deleter
    def comment(self):
        self._comment = None

    # - - - - - - - - RELATIONSHIPS - - - - - - - - 
    @property
    def incident(self):
        return self._incident

    @incident.setter
    def incident(self, value):

        check_type(value, Incident, allow_none=False)

        # set the incident:
        # if there is already an incident set, we want to
        # remove this note instance from that incident
        # before setting the new one
        if self._incident != None:
            self._incident.sources.remove(self)
        self._incident = value

        # add this note instance to the incident's
        # sources list
        if value.sources == None:
            value.sources = [self]
        elif self not in value.sources:
            value.sources.append(self)

    @incident.deleter
    def incident(self):
        if self._incident != None:
            self._incident.sources.remove(self)
            self._incident = None


class Note:
    """
    Initialize a Note instance

    Args:
        id (required) (string) : A unique string that begins with "note--" and
            is appended with a UUIDv4.
        author (required) (string) : Individual, group, or organization that
            authored the note.
        date (required) (date-time) : Date and time the note was authored or
            most recently modified.
        comment (required) (string) : Notes, comments, details as needed.

    Raises:
        TypeError: If any provided attribute is of the incorrect type.
        ValueError: If any provided attribute is of the incorrect vocabulary.

    Example:
        >>> from pyiides.utils.helper_functions import Note
        >>> from datetime import date
        >>> note = Note(
        ...     author="John Doe",
        ...     date=date(2023, 1, 1),
        ...     comment="This is a sample comment.",
        ...     id="note--6eaf8e6c-8c4d-4d9d-8f8e-6c8c4d4d9d8f"
        ... )
        >>> print(note.author)
        John Doe
        >>> print(note.date)
        2023-01-01
    """
    def __init__(self, author, date, comment, id=None):
        if id == None:
            id = str(uuid.uuid4())

        check_uuid(id)
        self._id = id

        check_type(author, str)
        self._author = author

        check_type(date, dt)
        # There is a naming conflict between the date attribute and date type
        self._date = date

        check_type(comment, str)
        self._comment = comment

        # Relationships
        self._incident = None

    def __repr__(self):
        return (f"Note(id={self.id}, "
                f"author={self.author}, "
                f"date={self.date}, "
                f"comment={self.comment})")

    def to_dict(self):
        class_dict_copy = self.__dict__.copy()
        relationships = {'_incident'}

        if self.date != None:
            class_dict_copy["_date"] = str(self.date)

        class_dict_copy["_id"] = f"note--{self.id}"
        return ({
                    key.lstrip('_'): value 
                    for key, value in class_dict_copy.items()
                    if key not in relationships
                }, None)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        check_uuid(value)
        self._id = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        check_type(value, str, allow_none=False)
        self._author = value

    @author.deleter
    def author(self):
        self._author = None

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        check_type(value, dt)
        self._date = value

    @date.deleter
    def date(self):
        self._date = None

    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, value):
        check_type(value, str, allow_none=False)
        self._comment = value

    @comment.deleter
    def comment(self):
        self._comment = None

    # - - - - - - - - RELATIONSHIPS - - - - - - - -
    @property
    def incident(self):
        return self._incident

    @incident.setter
    def incident(self, value):
        
        check_type(value, Incident, allow_none=False)

        # set the incident: 
        # if there is already an incident set, we want to 
        # remove this note instance from that incident 
        # before setting the new one
        if self._incident != None:
            self._incident.notes.remove(self)
        self._incident = value

        # add this note instance to the incident's
        # notes list
        if value.notes == None:
            value.notes = [self]
        elif self not in value.notes:
            value.notes.append(self)
    
    @incident.deleter
    def incident(self):
        if self._incident != None:
            self._incident.notes.remove(self)
            self._incident = None


class Impact:
    """
    Initialize an Impact instance

    Args:
        id (required) (string) : Unique identifier for the impact. Defaults to
            a new UUIDv4 string if not provided.
        high (required) (number) : The quantity of the impact being measured.
            If a range, the high end of the range.
        low (number) : If a range, the low estimate of the range.
        metric (required) (string) : The type of impact being quantified.
            A constant from `impact-metric-vocab <./vocab/impact-metric-vocab.html>`_.
        estimated (required) (boolean) : True if the impact low and/or high is
            an estimated number or range.
        comment (string) : Clarifying comments.

    Raises:
        TypeError: If any provided attribute is of the incorrect type.
        ValueError: If any provided attribute is of the incorrect vocabulary.

    Example:
        >>> from pyiides import Impact
        >>> impact = Impact(high=5000, metric="dollars", estimated=True)
        >>> print(impact.high)
        5000
        >>> print(impact.metric)
        dollars
        >>> print(impact.estimated)
        True
    """
    def __init__(self, high, metric, estimated, id=None, low=None, comment=None):
        if id == None:
            id = str(uuid.uuid4())

        check_uuid(id)
        self._id = id

        check_type(high, float)
        self._high = high

        check_type(low, float)
        self._low = low

        check_type(metric, str)
        check_vocab(metric, 'impact-metric-vocab')
        self._metric = metric

        check_type(estimated, bool)
        self._estimated = estimated

        check_type(comment, str)
        self._comment = comment 

        # RELATIONSHIP

        self._incident = None

    def __repr__(self):
        return (f"Impact(id={self.id}, "
                f"high={self.high}, "
                f"low={self.low}, "
                f"metric={self.metric}, "
                f"estimated={self.estimated}, "
                f"comment={self.comment})")

    def to_dict(self):
        class_dict_copy = self.__dict__.copy()
        relationships = {'_incident'}
        class_dict_copy["_id"] = f"impact--{self.id}"
        return ({
                    key.lstrip('_'): value
                    for key, value in class_dict_copy.items()
                    if key not in relationships
                }, None)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        check_uuid(value)
        self._id = value

    @property
    def high(self):
        return self._high

    @high.setter
    def high(self, value):
        check_type(value, float, allow_none=False)
        self._high = value

    @high.deleter
    def high(self):
        self._high = None

    @property
    def low(self):
        return self._low

    @low.setter
    def low(self, value):
        check_type(value, float, allow_none=False)
        self._low = value

    @low.deleter
    def low(self):
        self._low = None

    @property
    def metric(self):
        return self._metric

    @metric.setter
    def metric(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'impact-metric-vocab')
        self._metric = value

    @metric.deleter
    def metric(self):
        self._metric = None

    @property
    def estimated(self):
        return self._estimated

    @estimated.setter
    def estimated(self, value):
        check_type(value, bool, allow_none=False)
        self._estimated = value

    @estimated.deleter
    def estimated(self):
        self._estimated = None

    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, value):
        check_type(value, str, allow_none=False)
        self._comment = value

    @comment.deleter
    def comment(self):
        self._comment = None

    # - - - - - - - RELATIONSHIPS - - - - - - 
    @property
    def incident(self):
        return self._incident

    @incident.setter
    def incident(self, value):
        
        check_type(value, Incident, allow_none=False)

        # set the incident:
        # if there is already an incident set, we want to
        # remove this impact instance from that incident
        # before setting the new one
        if self._incident != None:
            self._incident.impacts.remove(self)
        self._incident = value

        # add this impact instance to the incident's
        # impacts list
        if value.impacts == None:
            value.impacts = [self]
        elif self not in value.impacts:
            value.impacts.append(self)

    @incident.deleter
    def incident(self):
        if self._incident != None:
            self._incident.impacts.remove(self)
            self._incident = None


