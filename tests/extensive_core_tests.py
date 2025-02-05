"""
License:
PyIIDES
Copyright 2024 Carnegie Mellon University.
NO WARRANTY. THIS CARNEGIE MELLON UNIVERSITY AND SOFTWARE ENGINEERING INSTITUTE MATERIAL IS FURNISHED ON AN "AS-IS" BASIS. CARNEGIE MELLON UNIVERSITY MAKES NO WARRANTIES OF ANY KIND, EITHER EXPRESSED OR IMPLIED, AS TO ANY MATTER INCLUDING, BUT NOT LIMITED TO, WARRANTY OF FITNESS FOR PURPOSE OR MERCHANTABILITY, EXCLUSIVITY, OR RESULTS OBTAINED FROM USE OF THE MATERIAL. CARNEGIE MELLON UNIVERSITY DOES NOT MAKE ANY WARRANTY OF ANY KIND WITH RESPECT TO FREEDOM FROM PATENT, TRADEMARK, OR COPYRIGHT INFRINGEMENT.
Licensed under a MIT (SEI)-style license, please see license.txt or contact permission@sei.cmu.edu for full terms.
[DISTRIBUTION STATEMENT A] This material has been approved for public release and unlimited distribution.  Please see Copyright notice for non-US Government use and distribution.
DM24-1597
"""
import unittest
import uuid
from pyiides import Person, Incident, Detection, Response, TTP, Organization, Job, Insider, Accomplice
from datetime import date, datetime, timedelta

class TestPerson(unittest.TestCase):
    def test_initialization(self):
        person = Person(
            first_name="John",
            middle_name="A",
            last_name="Doe",
            suffix="Jr",
            alias=["JD", "Johnny"],
            city="New York",
            state="NY",
            country="US",
            postal_code=10001,
            country_of_citizenship=["US"],
            nationality=["American"],
            residency="P",
            gender="M",
            age=30,
            education="5",
            marital_status="2",
            number_of_children=2,
            comment="Test comment"
        )
        self.assertEqual(person.first_name, "John")
        self.assertEqual(person.middle_name, "A")
        self.assertEqual(person.last_name, "Doe")
        self.assertEqual(person.suffix, "Jr")
        self.assertEqual(person.alias, ["JD", "Johnny"])
        self.assertEqual(person.city, "New York")
        self.assertEqual(person.state, "NY")
        self.assertEqual(person.country, "US")
        self.assertEqual(person.postal_code, 10001)
        self.assertEqual(person.country_of_citizenship, ["US"])
        self.assertEqual(person.nationality, ["American"])
        self.assertEqual(person.residency, "P")
        self.assertEqual(person.gender, "M")
        self.assertEqual(person.age, 30)
        self.assertEqual(person.education, "5")
        self.assertEqual(person.marital_status, "2")
        self.assertEqual(person.number_of_children, 2)
        self.assertEqual(person.comment, "Test comment")

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- TYPE  CHECKING -=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    def test_invalid_first_name(self):
        with self.assertRaises(TypeError):
            Person(first_name=123)  # first_name should be a string

    def test_invalid_middle_name(self):
        with self.assertRaises(TypeError):
            Person(middle_name=456)  # middle_name should be a string

    def test_invalid_last_name(self):
        with self.assertRaises(TypeError):
            Person(last_name=789)  # last_name should be a string

    def test_invalid_suffix(self):
        with self.assertRaises(TypeError):
            Person(suffix=123)  # suffix should be a string

    def test_invalid_alias(self):
        with self.assertRaises(TypeError):
            Person(alias="JD")  # alias should be a list of strings

        with self.assertRaises(TypeError):
            Person(alias=[123, "Johnny"])  # each alias should be a string

    def test_invalid_city(self):
        with self.assertRaises(TypeError):
            Person(city=123)  # city should be a string

    def test_invalid_state(self):
        with self.assertRaises(TypeError):
            Person(state=456)  # state should be a string

    def test_invalid_country(self):
        with self.assertRaises(TypeError):
            Person(country=789)  # country should be a string

    def test_invalid_postal_code(self):
        with self.assertRaises(TypeError):
            Person(postal_code="10001")  # postal_code should be an integer

    def test_invalid_country_of_citizenship(self):
        with self.assertRaises(TypeError):
            Person(country_of_citizenship="US")  # country_of_citizenship should be a list of strings

        with self.assertRaises(TypeError):
            Person(country_of_citizenship=[123])  # each entry should be a string

    def test_invalid_nationality(self):
        with self.assertRaises(TypeError):
            Person(nationality="American")  # nationality should be a list of strings

        with self.assertRaises(TypeError):
            Person(nationality=[123])  # each entry should be a string

    def test_invalid_residency(self):
        with self.assertRaises(TypeError):
            Person(residency=123)  # residency should be a string

    def test_invalid_gender(self):
        with self.assertRaises(TypeError):
            Person(gender=123)  # gender should be a string

    def test_invalid_age(self):
        with self.assertRaises(TypeError):
            Person(age="30")  # age should be an integer

    def test_invalid_education(self):
        with self.assertRaises(TypeError):
            Person(education=123)  # education should be a string

    def test_invalid_marital_status(self):
        with self.assertRaises(TypeError):
            Person(marital_status=123)  # marital_status should be a string

    def test_invalid_number_of_children(self):
        with self.assertRaises(TypeError):
            Person(number_of_children="2")  # number_of_children should be an integer

    def test_invalid_comment(self):
        with self.assertRaises(TypeError):
            Person(comment=123)  # comment should be a string

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- VOCAB CHECKING -=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    def test_suffix_vocabulary(self):
        valid_suffixes = ["Jr", "Sr", "III", "IV"]
        for suffix in valid_suffixes:
            person = Person(suffix=suffix)
            self.assertEqual(person.suffix, suffix)
 
    def test_invalid_suffix_vocabulary(self):
        with self.assertRaises(ValueError):
            Person(suffix="InvalidSuffix")

    def test_residency_vocabulary(self):
        valid_residencies = ["N", "P", "R"]
        for residency in valid_residencies:
            person = Person(residency=residency)
            self.assertEqual(person.residency, residency)

    def test_invalid_residency_vocabulary(self):
        with self.assertRaises(ValueError):
            Person(residency="InvalidResidency")

    def test_gender_vocabulary(self):
        valid_genders = ["F", "M", "N", "O"]
        for gender in valid_genders:
            person = Person(gender=gender)
            self.assertEqual(person.gender, gender)

    def test_invalid_gender_vocabulary(self):
        with self.assertRaises(ValueError):
            Person(gender="InvalidGender")

    def test_education_vocabulary(self):
        valid_educations = ["4", "5", "8", "2", "7", "6", "3", "1"]
        for ed_val in valid_educations:
            person = Person(education=ed_val)
            self.assertEqual(person.education, ed_val)

    def test_invalid_education_vocabulary(self):
        with self.assertRaises(ValueError):
            Person(education="InvalidEducation")

    def test_marital_status_vocabulary(self):
        valid_marital_statuses = ["1", "2", "3", "4", "5"]
        for status in valid_marital_statuses:
            person = Person(marital_status=status)
            self.assertEqual(person.marital_status, status)

    def test_invalid_marital_status_vocabulary(self):
        with self.assertRaises(ValueError):
            Person(marital_status="InvalidMaritalStatus")

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-  FUNCTION CHECKING -=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def setUp(self):
        self.person = Person(
            first_name="John",
            middle_name="A",
            last_name="Doe",
            suffix="Jr",
            alias=["JD", "Johnny"],
            city="New York",
            state="NY",
            country="US",
            postal_code=10001,
            country_of_citizenship=["US"],
            nationality=["American"],
            residency="P",
            gender="M",
            age=30,
            education="5",
            marital_status="2",
            number_of_children=2,
            comment="Test comment"
        )

    # Test setters
    def test_setters(self):
        self.person.first_name = "Jane"
        self.assertEqual(self.person.first_name, "Jane")

        self.person.last_name = "Smith"
        self.assertEqual(self.person.last_name, "Smith")

    # Test append function using person's append methods
    def test_append_functions(self):
        self.person.append_alias("JohnnyD")
        self.assertIn("JohnnyD", self.person.alias)

        self.person.append_country_of_citizenship("CA")
        self.assertIn("CA", self.person.country_of_citizenship)

        self.person.append_nationality("Canadian")
        self.assertIn("Canadian", self.person.nationality)

    # Test append with type checking and vocab checking
    def test_append_type_and_vocab_check(self):
        with self.assertRaises(TypeError):
            self.person.append_alias(123)  # Invalid type

        with self.assertRaises(TypeError):
            self.person.append_country_of_citizenship(123)  # Invalid type

        with self.assertRaises(TypeError):
            self.person.append_nationality(123)  # Invalid type

    # Test delete function
    def test_delete_functions(self):
        self.person.alias = []
        self.assertEqual(self.person.alias, [])

        self.person.country_of_citizenship = []
        self.assertEqual(self.person.country_of_citizenship, [])

        self.person.nationality = []
        self.assertEqual(self.person.nationality, [])

    # Test clear function
    def test_clear_functions(self):
        self.person.alias.clear()
        self.assertEqual(self.person.alias, [])

        self.person.country_of_citizenship.clear()
        self.assertEqual(self.person.country_of_citizenship, [])

        self.person.nationality.clear()
        self.assertEqual(self.person.nationality, [])

    # Test remove function
    def test_remove_functions(self):
        self.person.alias.remove("JD")
        self.assertNotIn("JD", self.person.alias)

        self.person.country_of_citizenship.remove("US")
        self.assertNotIn("US", self.person.country_of_citizenship)

        self.person.nationality.remove("American")
        self.assertNotIn("American", self.person.nationality)

    # Test all attributes' functions
    def test_all_attributes_functions(self):
        # First Name
        self.person.first_name = "Jane"
        self.assertEqual(self.person.first_name, "Jane")

        # Middle Name
        self.person.middle_name = "B"
        self.assertEqual(self.person.middle_name, "B")

        # Last Name
        self.person.last_name = "Smith"
        self.assertEqual(self.person.last_name, "Smith")

        # Suffix
        self.person.suffix = "Sr"
        self.assertEqual(self.person.suffix, "Sr")

        # Alias
        self.person.append_alias("JohnnyD")
        self.assertIn("JohnnyD", self.person.alias)
        self.person.alias.remove("JD")
        self.assertNotIn("JD", self.person.alias)
        self.person.alias.clear()
        self.assertEqual(self.person.alias, [])
        self.person.alias = ["JD", "Johnny"]

        # City
        self.person.city = "Los Angeles"
        self.assertEqual(self.person.city, "Los Angeles")

        # State
        self.person.state = "CA"
        self.assertEqual(self.person.state, "CA")

        # Country
        self.person.country = "CA"
        self.assertEqual(self.person.country, "CA")

        # Postal Code
        self.person.postal_code = 90210
        self.assertEqual(self.person.postal_code, 90210)

        # Country of Citizenship
        self.person.append_country_of_citizenship("CA")
        self.assertIn("CA", self.person.country_of_citizenship)
        self.person.country_of_citizenship.remove("US")
        self.assertNotIn("US", self.person.country_of_citizenship)
        self.person.country_of_citizenship.clear()
        self.assertEqual(self.person.country_of_citizenship, [])
        self.person.country_of_citizenship = ["US"]

        # Nationality
        self.person.append_nationality("Canadian")
        self.assertIn("Canadian", self.person.nationality)
        self.person.nationality.remove("American")
        self.assertNotIn("American", self.person.nationality)
        self.person.nationality.clear()
        self.assertEqual(self.person.nationality, [])
        self.person.nationality = ["American"]

        # Residency
        self.person.residency = "N"
        self.assertEqual(self.person.residency, "N")

        # Gender
        self.person.gender = "F"
        self.assertEqual(self.person.gender, "F")

        # Age
        self.person.age = 35
        self.assertEqual(self.person.age, 35)

        # Education
        self.person.education = "6"
        self.assertEqual(self.person.education, "6")

        # Marital Status
        self.person.marital_status = "3"
        self.assertEqual(self.person.marital_status, "3")

        # Number of Children
        self.person.number_of_children = 3
        self.assertEqual(self.person.number_of_children, 3)

        # Comment
        self.person.comment = "Updated comment"
        self.assertEqual(self.person.comment, "Updated comment")


class TestIncident(unittest.TestCase):

    def test_initialization(self):
        incident = Incident(
            id="123e4567-e89b-12d3-a456-426614174000",
            cia_effect=["C", "I"],
            incident_type=["F"],
            incident_subtype=["F.1"],
            outcome=["BR"],
            status="P",
            summary="An insider incident involving data theft.",
            brief_summary="Insider data theft.",
            comment="Additional details about the incident."
        )
        self.assertEqual(incident.id, "123e4567-e89b-12d3-a456-426614174000")
        self.assertEqual(incident.cia_effect, ["C", "I"])
        self.assertEqual(incident.incident_type, ["F"])
        self.assertEqual(incident.incident_subtype, ["F.1"])
        self.assertEqual(incident.outcome, ["BR"])
        self.assertEqual(incident.status, "P")
        self.assertEqual(incident.summary, "An insider incident involving data theft.")
        self.assertEqual(incident.brief_summary, "Insider data theft.")
        self.assertEqual(incident.comment, "Additional details about the incident.")

    # Invalid type checks
    def test_invalid_id(self):
        with self.assertRaises(ValueError):
            Incident(id="123e4567-e89b-12d3-a456-f")  # Invalid format

    def test_invalid_cia_effect(self):
        with self.assertRaises(TypeError):
            Incident(cia_effect="C")  # Should be a list
        with self.assertRaises(ValueError):
            Incident(cia_effect=["Invalid"])  # Invalid vocabulary

    def test_invalid_incident_type(self):
        with self.assertRaises(TypeError):
            Incident(incident_type="F")  # Should be a list
        with self.assertRaises(ValueError):
            Incident(incident_type=["Invalid"])  # Invalid vocabulary

    def test_invalid_incident_subtype(self):
        with self.assertRaises(TypeError):
            Incident(incident_subtype="F.1")  # Should be a list
        with self.assertRaises(ValueError):
            Incident(incident_subtype=["Invalid"])  # Invalid vocabulary

    def test_invalid_outcome(self):
        with self.assertRaises(TypeError):
            Incident(outcome="BR")  # Should be a list
        with self.assertRaises(ValueError):
            Incident(outcome=["Invalid"])  # Invalid vocabulary

    def test_invalid_status(self):
        with self.assertRaises(ValueError):
            Incident(status="Invalid")  # Invalid vocabulary

    def test_invalid_summary(self):
        with self.assertRaises(TypeError):
            Incident(summary=123)  # Should be a string

    def test_invalid_brief_summary(self):
        with self.assertRaises(TypeError):
            Incident(brief_summary=123)  # Should be a string

    def test_invalid_comment(self):
        with self.assertRaises(TypeError):
            Incident(comment=123)  # Should be a string

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- VOCAB CHECKING -=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    def test_cia_vocabulary(self):
        valid_cia_effects = ["C", "I", "A"]
        for cia in valid_cia_effects:
            incident = Incident(cia_effect=[cia])
            self.assertIn(cia, incident.cia_effect)

    def test_invalid_cia_vocabulary(self):
        with self.assertRaises(ValueError):
            Incident(cia_effect=["X"])

    def test_incident_type_vocabulary(self):
        valid_incident_types = ["F", "S", "E", "V", "U"]
        for incident_type in valid_incident_types:
            incident = Incident(incident_type=[incident_type])
            self.assertIn(incident_type, incident.incident_type)

    def test_invalid_incident_type_vocabulary(self):
        with self.assertRaises(ValueError):
            Incident(incident_type=["X"])

    def test_incident_subtype_vocabulary(self):
        valid_incident_subtypes = ["F.1", "F.2", "F.3", "S.1", "S.2", "E.1", "E.2", "V.1", "V.2", "U.1", "U.2"]
        for incident_subtype in valid_incident_subtypes:
            incident = Incident(incident_type=[incident_subtype[0:incident_subtype.rfind('.')]], incident_subtype=[incident_subtype])
            self.assertIn(incident_subtype, incident.incident_subtype)

    def test_invalid_incident_subtype_vocabulary(self):
        with self.assertRaises(ValueError):
            Incident(incident_subtype=["X"])

    def test_outcome_vocabulary(self):
        valid_outcomes = ["BR", "DC", "DD", "DR", "DS", "MD", "ML", "MS", "NN", "OT", "RO", "SI", "IT"]
        for outcome in valid_outcomes:
            incident = Incident(outcome=[outcome])
            self.assertIn(outcome, incident.outcome)

    def test_invalid_outcome_vocabulary(self):
        with self.assertRaises(ValueError):
            Incident(outcome=["X"])

    def test_status_vocabulary(self):
        valid_statuses = ["P", "I", "R", "C"]
        for status in valid_statuses:
            incident = Incident(status=status)
            self.assertEqual(incident.status, status)

    def test_invalid_status_vocabulary(self):
        with self.assertRaises(ValueError):
            Incident(status="X")

    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- TYPE-SUBTYPE CHECKING -=-=-=-=-=-=-=-=-=-=-=
    # The following tests are designed to validate that incident_subtype values are
    # consistent with their corresponding incident_type values. Each incident_subtype
    # must match the pattern of one of the provided incident_type values.
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    def test_valid_type_subtype_combinations(self):
        valid_combinations = {
            "F": ["F.1", "F.2", "F.3"],
            "S": ["S.1", "S.2"],
            "E": ["E.1", "E.2"],
            "V": ["V.1", "V.2"],
            "U": ["U.1", "U.2"]
        }
        for incident_type, incident_subtypes in valid_combinations.items():
            incident = Incident(incident_type=[incident_type], incident_subtype=incident_subtypes)
            self.assertEqual(incident.incident_type, [incident_type])
            self.assertEqual(incident.incident_subtype, incident_subtypes)

    def test_invalid_type_subtype_combinations(self):
        invalid_combinations = [
            (["F"], ["S.1"]),
            (["S"], ["F.1"]),
            (["E"], ["V.1"]),
            (["V"], ["U.1"]),
            (["U"], ["E.1"]),
            (["F", "S"], ["F.1", "E.1"]),  # E.1 is not valid for F or S
        ]
        for incident_type, incident_subtype in invalid_combinations:
            with self.assertRaises(ValueError):
                Incident(incident_type=incident_type, incident_subtype=incident_subtype)

    def test_valid_combination_of_types_with_subtypes(self):
        valid_types = ["F", "S"]
        valid_subtypes = ["F.1", "F.2", "S.1", "S.2"]
        incident = Incident(incident_type=valid_types, incident_subtype=valid_subtypes)
        self.assertEqual(incident.incident_type, valid_types)
        self.assertEqual(incident.incident_subtype, valid_subtypes)

    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- FUNCTION     CHECKING -=-=-=-=-=-=-=-=-=-=-=
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    def setUp(self):
        self.incident = Incident(
            id="123e4567-e89b-12d3-a456-426614174000",
            cia_effect=["C"],
            incident_type=["F"],
            incident_subtype=["F.1"],
            outcome=["BR"],
            status="P",
            summary="A brief explanation of the incident.",
            brief_summary="A short summary.",
            comment="Additional details about the incident."
        )

    # Test setters
    def test_setters(self):
        self.incident.status = "I"
        self.assertEqual(self.incident.status, "I")

        self.incident.summary = "Updated summary"
        self.assertEqual(self.incident.summary, "Updated summary")

    # Test append function using incident's append methods
    def test_append_functions(self):
        self.incident.append_cia("I")
        self.assertIn("I", self.incident.cia_effect)

        self.incident.append_type("S")
        self.assertIn("S", self.incident.incident_type)

        self.incident.append_subtype("S.1")
        self.assertIn("S.1", self.incident.incident_subtype)

        self.incident.append_outcome("DC")
        self.assertIn("DC", self.incident.outcome)

    # Test append with type checking and vocab checking
    def test_append_type_and_vocab_check(self):
        with self.assertRaises(TypeError):
            self.incident.append_cia(123)  # Invalid type

        with self.assertRaises(ValueError):
            self.incident.append_cia("X")  # Invalid vocab

        with self.assertRaises(TypeError):
            self.incident.append_type(123)  # Invalid type

        with self.assertRaises(ValueError):
            self.incident.append_type("X")  # Invalid vocab

        with self.assertRaises(TypeError):
            self.incident.append_subtype(123)  # Invalid type

        with self.assertRaises(ValueError):
            self.incident.append_subtype("X")  # Invalid vocab

        with self.assertRaises(TypeError):
            self.incident.append_outcome(123)  # Invalid type

        with self.assertRaises(ValueError):
            self.incident.append_outcome("X")  # Invalid vocab

    # Test delete function
    def test_delete_functions(self):
        self.incident.cia_effect = []
        self.assertEqual(self.incident.cia_effect, [])

        self.incident.incident_type = []
        self.assertEqual(self.incident.incident_type, [])

        self.incident.incident_subtype = []
        self.assertEqual(self.incident.incident_subtype, [])

        self.incident.outcome = []
        self.assertEqual(self.incident.outcome, [])

    # Test clear function
    def test_clear_functions(self):
        self.incident.cia_effect.clear()
        self.assertEqual(self.incident.cia_effect, [])

        self.incident.incident_type.clear()
        self.assertEqual(self.incident.incident_type, [])

        self.incident.incident_subtype.clear()
        self.assertEqual(self.incident.incident_subtype, [])

        self.incident.outcome.clear()
        self.assertEqual(self.incident.outcome, [])

    # Test remove function
    def test_remove_functions(self):
        self.incident.cia_effect.remove("C")
        self.assertNotIn("C", self.incident.cia_effect)

        self.incident.incident_type.remove("F")
        self.assertNotIn("F", self.incident.incident_type)

        self.incident.incident_subtype.remove("F.1")
        self.assertNotIn("F.1", self.incident.incident_subtype)

        self.incident.outcome.remove("BR")
        self.assertNotIn("BR", self.incident.outcome)
    
    def test_all_attributes_functions(self):
        # ID
        self.incident.id = "123e4567-e89b-12d3-a456-426614174001"
        self.assertEqual(self.incident.id, "123e4567-e89b-12d3-a456-426614174001")

        # CIA Effect
        self.incident.append_cia("I")
        self.assertIn("I", self.incident.cia_effect)
        self.incident.cia_effect.remove("C")
        self.assertNotIn("C", self.incident.cia_effect)
        self.incident.cia_effect.clear()
        self.assertEqual(self.incident.cia_effect, [])
        self.incident.cia_effect = ["C"]

        # Incident Type
        self.incident.append_type("S")
        self.assertIn("S", self.incident.incident_type)
        self.incident.incident_type.remove("F")
        self.assertNotIn("F", self.incident.incident_type)
        self.incident.incident_type.clear()
        self.assertEqual(self.incident.incident_type, [])
        self.incident.incident_type = ["F", "S"]

        # Incident Subtype
        self.incident.append_subtype("S.1")
        self.assertIn("S.1", self.incident.incident_subtype)
        self.incident.incident_subtype.remove("F.1")
        self.assertNotIn("F.1", self.incident.incident_subtype)
        self.incident.incident_subtype.clear()
        self.assertEqual(self.incident.incident_subtype, [])
        self.incident.incident_subtype = ["F.1"]

        # Outcome
        self.incident.append_outcome("DC")
        self.assertIn("DC", self.incident.outcome)
        self.incident.outcome.remove("BR")
        self.assertNotIn("BR", self.incident.outcome)
        self.incident.outcome.clear()
        self.assertEqual(self.incident.outcome, [])
        self.incident.outcome = ["BR"]

        # Status
        self.incident.status = "I"
        self.assertEqual(self.incident.status, "I")

        # Summary
        self.incident.summary = "Updated summary"
        self.assertEqual(self.incident.summary, "Updated summary")

        # Brief Summary
        self.incident.brief_summary = "Updated brief summary"
        self.assertEqual(self.incident.brief_summary, "Updated brief summary")

        # Comment
        self.incident.comment = "Updated comment"
        self.assertEqual(self.incident.comment, "Updated comment")


class TestDetection(unittest.TestCase):

    def test_initialization(self):
        detection = Detection(
            id="123e4567-e89b-12d3-a456-426614174000",
            first_detected= datetime(2023, 1, 1, 0, 0, 0),
            who_detected=["LE"],
            detected_method=["1"],
            logs=["AC"],
            comment="Additional details about the detection."
        )
        self.assertEqual(detection.id, "123e4567-e89b-12d3-a456-426614174000")
        self.assertEqual(detection.first_detected, datetime(2023, 1, 1, 0, 0, 0))
        self.assertEqual(detection.who_detected, ["LE"])
        self.assertEqual(detection.detected_method, ["1"])
        self.assertEqual(detection.logs, ["AC"])
        self.assertEqual(detection.comment, "Additional details about the detection.")

    # Invalid type checks
    def test_invalid_id(self):
        with self.assertRaises(TypeError):
            Detection(id=123)

    def test_invalid_first_detected(self):
        with self.assertRaises(TypeError):
            Detection(first_detected=123)

    def test_invalid_who_detected(self):
        with self.assertRaises(TypeError):
            Detection(who_detected="LE")

    def test_invalid_detected_method(self):
        with self.assertRaises(TypeError):
            Detection(detected_method="1")

    def test_invalid_logs(self):
        with self.assertRaises(TypeError):
            Detection(logs="AC")

    def test_invalid_comment(self):
        with self.assertRaises(TypeError):
            Detection(comment=123)

    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- VOCAB CHECKING -=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    def test_who_detected_vocabulary(self):
        valid_who_detected = ["LE", "OR", "CU", "CO", "AU", "SR", "IR", "ST", "MG", "II", "RR"]
        for who in valid_who_detected:
            detection = Detection(who_detected=[who])
            self.assertIn(who, detection.who_detected)

    def test_invalid_who_detected_vocabulary(self):
        with self.assertRaises(ValueError):
            Detection(who_detected=["Invalid"])

    def test_detected_method_vocabulary(self):
        valid_detected_methods = ["1", "2", "3", "4", "5"]
        for method in valid_detected_methods:
            detection = Detection(detected_method=[method])
            self.assertIn(method, detection.detected_method)

    def test_invalid_detected_method_vocabulary(self):
        with self.assertRaises(ValueError):
            Detection(detected_method=["Invalid"])

    def test_logs_vocabulary(self):
        valid_logs = ["AC", "AU", "BR", "DB", "EM", "FS", "IS", "RA", "SF", "VD", "WB"]
        for log in valid_logs:
            detection = Detection(logs=[log])
            self.assertIn(log, detection.logs)

    def test_invalid_logs_vocabulary(self):
        with self.assertRaises(ValueError):
            Detection(logs=["Invalid"])

    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= FUNCTION CHECKING -=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def setUp(self):
        self.detection = Detection(
            id="123e4567-e89b-12d3-a456-426614174000",
            first_detected=datetime(2023, 1, 1, 0, 0, 0),
            who_detected=["LE"],
            detected_method=["1"],
            logs=["AC"],
            comment="Initial comment"
        )

    # Test setters
    def test_setters(self):
        self.detection.first_detected = datetime(2024, 1, 1, 0, 0, 0)
        self.assertEqual(self.detection.first_detected, datetime(2024, 1, 1, 0, 0, 0))

        self.detection.comment = "Updated comment"
        self.assertEqual(self.detection.comment, "Updated comment")

    # Test append function using detection's append methods
    def test_append_functions(self):
        self.detection.append_who_detected("OR")
        self.assertIn("OR", self.detection.who_detected)

        self.detection.append_detected_method("2")
        self.assertIn("2", self.detection.detected_method)

        self.detection.append_logs("AU")
        self.assertIn("AU", self.detection.logs)

    # Test append with type checking and vocab checking
    def test_append_type_and_vocab_check(self):
        with self.assertRaises(TypeError):
            self.detection.append_who_detected(123)  # Invalid type

        with self.assertRaises(ValueError):
            self.detection.append_who_detected("Invalid")  # Invalid vocab

        with self.assertRaises(TypeError):
            self.detection.append_detected_method(123)  # Invalid type

        with self.assertRaises(ValueError):
            self.detection.append_detected_method("Invalid")  # Invalid vocab

        with self.assertRaises(TypeError):
            self.detection.append_logs(123)  # Invalid type

        with self.assertRaises(ValueError):
            self.detection.append_logs("Invalid")  # Invalid vocab

    # Test delete function
    def test_delete_functions(self):
        self.detection.who_detected = []
        self.assertEqual(self.detection.who_detected, [])

        self.detection.detected_method = []
        self.assertEqual(self.detection.detected_method, [])

        self.detection.logs = []
        self.assertEqual(self.detection.logs, [])

    # Test clear function
    def test_clear_functions(self):
        self.detection.who_detected.clear()
        self.assertEqual(self.detection.who_detected, [])

        self.detection.detected_method.clear()
        self.assertEqual(self.detection.detected_method, [])

        self.detection.logs.clear()
        self.assertEqual(self.detection.logs, [])

    # Test remove function
    def test_remove_functions(self):
        self.detection.who_detected.remove("LE")
        self.assertNotIn("LE", self.detection.who_detected)

        self.detection.detected_method.remove("1")
        self.assertNotIn("1", self.detection.detected_method)

        self.detection.logs.remove("AC")
        self.assertNotIn("AC", self.detection.logs)

    # Test all attributes' functions
    def test_all_attributes_functions(self):
        # ID
        self.detection.id = "123e4567-e89b-12d3-a456-426614174001"
        self.assertEqual(self.detection.id, "123e4567-e89b-12d3-a456-426614174001")

        # First Detected
        self.detection.first_detected = datetime(2024, 1, 1, 0, 0, 0)
        self.assertEqual(self.detection.first_detected, datetime(2024, 1, 1, 0, 0, 0))

        # Who Detected
        self.detection.append_who_detected("OR")
        self.assertIn("OR", self.detection.who_detected)
        self.detection.who_detected.remove("LE")
        self.assertNotIn("LE", self.detection.who_detected)
        self.detection.who_detected.clear()
        self.assertEqual(self.detection.who_detected, [])
        self.detection.who_detected = ["LE"]

        # Detected Method
        self.detection.append_detected_method("2")
        self.assertIn("2", self.detection.detected_method)
        self.detection.detected_method.remove("1")
        self.assertNotIn("1", self.detection.detected_method)
        self.detection.detected_method.clear()
        self.assertEqual(self.detection.detected_method, [])
        self.detection.detected_method = ["1"]

        # Logs
        self.detection.append_logs("AU")
        self.assertIn("AU", self.detection.logs)
        self.detection.logs.remove("AC")
        self.assertNotIn("AC", self.detection.logs)
        self.detection.logs.clear()
        self.assertEqual(self.detection.logs, [])
        self.detection.logs = ["AC"]

        # Comment
        self.detection.comment = "Updated comment"
        self.assertEqual(self.detection.comment, "Updated comment")


class TestInsider(unittest.TestCase):

    def setUp(self):
        self.insider = Insider(
            id="123e4567-e89b-12d3-a456-426614174000",
            incident_role="1",
            motive=["1"],
            substance_use_during_incident=True,
            psychological_issues=["1"],
            predispositions=[("1", "1.1")],
            concerning_behaviors=[("3", "3.1")]
        )

    # Initialization test
    def test_initialization(self):
        self.assertEqual(self.insider.id, "123e4567-e89b-12d3-a456-426614174000")
        self.assertEqual(self.insider.incident_role, "1")
        self.assertEqual(self.insider.motive, ["1"])
        self.assertTrue(self.insider.substance_use_during_incident)
        self.assertEqual(self.insider.psychological_issues, ["1"])
        self.assertEqual(self.insider.predispositions, [("1", "1.1")])
        self.assertEqual(self.insider.concerning_behaviors, [("3", "3.1")])

    # Test setters
    def test_setters(self):
        self.insider.incident_role = "2"
        self.assertEqual(self.insider.incident_role, "2")

        self.insider.substance_use_during_incident = False
        self.assertEqual(self.insider.substance_use_during_incident, False)

    # Test append function using insider's append methods
    def test_append_functions(self):
        self.insider.append_motive("2")
        self.assertIn("2", self.insider.motive)

        self.insider.append_psychological_issues("2")
        self.assertIn("2", self.insider.psychological_issues)

        self.insider.append_predispositions(("2", "2.1"))
        self.assertIn(("2", "2.1"), self.insider.predispositions)

        self.insider.append_concerning_behaviors(("3", "3.2"))
        self.assertIn(("3", "3.2"), self.insider.concerning_behaviors)

    # Type checking
    def test_type_checking(self):
        with self.assertRaises(TypeError):
            self.insider.id = 123

        with self.assertRaises(TypeError):
            self.insider.substance_use_during_incident = "True"

        with self.assertRaises(TypeError):
            self.insider.motive = "1"

        with self.assertRaises(TypeError):
            self.insider.psychological_issues = "1"

        with self.assertRaises(TypeError):
            self.insider.predispositions = ["1", "1.1"]

        with self.assertRaises(TypeError):
            self.insider.concerning_behaviors = ["3", "3.1"]

    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- VOCAB CHECKING -=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    def test_vocab_checking_incident_role(self):
        valid_incident_roles = ["1", "2", "3", "4"]
        for role in valid_incident_roles:
            insider = Insider(incident_role=role)
            self.assertEqual(insider.incident_role, role)

    def test_vocab_checking_motive(self):
        valid_motives = ["1", "2", "3", "4", "5", "6", "7", "8", "99"]
        for motive in valid_motives:
            insider = Insider(incident_role = '1', motive=[motive])
            self.assertIn(motive, insider.motive)

    def test_vocab_checking_psychological_issues(self):
        valid_psych_issues = ["1", "2", "3", "4", "5", "99"]
        for issue in valid_psych_issues:
            insider = Insider(incident_role = '1', psychological_issues=[issue])
            self.assertIn(issue, insider.psychological_issues)

    def test_vocab_checking_predispositions(self):
        valid_predispositions = [
            ("1", "1.1"), ("1", "1.2"), ("1", "1.3"), ("1", "1.4"), ("1", "1.5"), ("1", "1.6"), ("1", "1.7"),
            ("2", "2.1"), ("2", "2.2"), ("2", "2.3"), ("2", "2.4"), ("2", "2.5"), ("2", "2.6"), ("2", "2.7"),
            ("3", "3.1"), ("3", "3.2"),
            ("4", "4.1"), ("4", "4.2"), ("4", "4.3"), ("4", "4.4")
        ]
        for predisposition in valid_predispositions:
            insider = Insider(incident_role = '1', predispositions=[predisposition])
            self.assertIn(predisposition, insider.predispositions)

    def test_vocab_checking_concerning_behaviors(self):
        valid_behaviors = [
            # Type 1: Misuse of Company Resources
            ("1", "1.1"), ("1", "1.2"), ("1", "1.3"),
            
            # Type 2: Technical Policy Abuse
            ("2", "2.1"), ("2", "2.2"), ("2", "2.3"), ("2", "2.4"),
            ("2", "2.5"), ("2", "2.6"),
            
            # Type 3: Interpersonal Issues
            ("3", "3.1"), ("3", "3.2"), ("3", "3.3"), ("3", "3.4"), 
            ("3", "3.5"), ("3", "3.6"), ("3", "3.7"), ("3", "3.8"), 
            ("3", "3.9"), ("3", "3.10"), ("3", "3.11"), ("3", "3.12"), ("3", "3.13"),
            
            # Type 4: Financial
            ("4", "4.1"), ("4", "4.2"), ("4", "4.3"),
            
            # Type 5: Organizational Conflict
            ("5", "5.1"), ("5", "5.2"), ("5", "5.3"), ("5", "5.4"), 
            ("5", "5.5"), ("5", "5.6"),
            
            # Type 6: Suspicious Contact
            ("6", "6.1"), ("6", "6.2"), ("6", "6.3"), ("6", "6.4"),
            
            # Type 7: Relocation
            ("7", "7.1")
        ]
        for behavior in valid_behaviors:
            insider = Insider(incident_role = '1', concerning_behaviors=[behavior])
            self.assertIn(behavior, insider.concerning_behaviors)
    
    def test_vocab_checking(self):
        with self.assertRaises(ValueError):
            self.insider.incident_role = "Invalid"

        with self.assertRaises(ValueError):
            self.insider.motive = ["Invalid"]

        with self.assertRaises(ValueError):
            self.insider.psychological_issues = ["Invalid"]

        with self.assertRaises(ValueError):
            self.insider.predispositions = [("Invalid", "1.1")]

        with self.assertRaises(ValueError):
            self.insider.concerning_behaviors = [("Invalid", "3.1")]


    # Test delete function
    def test_delete_functions(self):
        self.insider.motive = []
        self.assertEqual(self.insider.motive, [])

        self.insider.psychological_issues = []
        self.assertEqual(self.insider.psychological_issues, [])

        self.insider.predispositions = []
        self.assertEqual(self.insider.predispositions, [])

        self.insider.concerning_behaviors = []
        self.assertEqual(self.insider.concerning_behaviors, [])

    # Test clear function
    def test_clear_functions(self):
        self.insider.motive.clear()
        self.assertEqual(self.insider.motive, [])

        self.insider.psychological_issues.clear()
        self.assertEqual(self.insider.psychological_issues, [])

        self.insider.predispositions.clear()
        self.assertEqual(self.insider.predispositions, [])

        self.insider.concerning_behaviors.clear()
        self.assertEqual(self.insider.concerning_behaviors, [])

    # Test remove function
    def test_remove_functions(self):
        self.insider.motive.remove("1")
        self.assertNotIn("1", self.insider.motive)

        self.insider.psychological_issues.remove("1")
        self.assertNotIn("1", self.insider.psychological_issues)

        self.insider.predispositions.remove(("1", "1.1"))
        self.assertNotIn(("1", "1.1"), self.insider.predispositions)

        self.insider.concerning_behaviors.remove(("3", "3.1"))
        self.assertNotIn(("3", "3.1"), self.insider.concerning_behaviors)

    # Test all attributes' functions
    def test_all_attributes_functions(self):
        # ID
        self.insider.id = "123e4567-e89b-12d3-a456-426614174001"
        self.assertEqual(self.insider.id, "123e4567-e89b-12d3-a456-426614174001")

        # Incident Role
        self.insider.incident_role = "2"
        self.assertEqual(self.insider.incident_role, "2")

        # Motive
        self.insider.append_motive("2")
        self.assertIn("2", self.insider.motive)
        self.insider.motive.remove("1")
        self.assertNotIn("1", self.insider.motive)
        self.insider.motive.clear()
        self.assertEqual(self.insider.motive, [])
        self.insider.motive = ["1"]

        # Substance Use During Incident
        self.insider.substance_use_during_incident = False
        self.assertEqual(self.insider.substance_use_during_incident, False)

        # Psychological Issues
        self.insider.append_psychological_issues("2")
        self.assertIn("2", self.insider.psychological_issues)
        self.insider.psychological_issues.remove("1")
        self.assertNotIn("1", self.insider.psychological_issues)
        self.insider.psychological_issues.clear()
        self.assertEqual(self.insider.psychological_issues, [])
        self.insider.psychological_issues = ["1"]

        # Predispositions
        self.insider.append_predispositions(("2", "2.1"))
        self.assertIn(("2", "2.1"), self.insider.predispositions)
        self.insider.predispositions.remove(("1", "1.1"))
        self.assertNotIn(("1", "1.1"), self.insider.predispositions)
        self.insider.predispositions.clear()
        self.assertEqual(self.insider.predispositions, [])
        self.insider.predispositions = [("1", "1.1")]

        # Concerning Behaviors
        self.insider.append_concerning_behaviors(("3", "3.2"))
        self.assertIn(("3", "3.2"), self.insider.concerning_behaviors)
        self.insider.concerning_behaviors.remove(("3", "3.1"))
        self.assertNotIn(("3", "3.1"), self.insider.concerning_behaviors)
        self.insider.concerning_behaviors.clear()
        self.assertEqual(self.insider.concerning_behaviors, [])
        self.insider.concerning_behaviors = [("3", "3.1")]


class TestAccomplice(unittest.TestCase):

    def setUp(self):
        self.accomplice = Accomplice(
            id=str(uuid.uuid4()),  # UUID
            relationship_to_insider="1"  # Acquaintance
        )

    # Initialization test
    def test_initialization(self):
        self.assertTrue(uuid.UUID(self.accomplice.id))  # Validate UUID format
        self.assertEqual(self.accomplice.relationship_to_insider, "1")

    # Test setters
    def test_setters(self):
        new_uuid = str(uuid.uuid4())
        self.accomplice.id = new_uuid
        self.assertEqual(self.accomplice.id, new_uuid)

        self.accomplice.relationship_to_insider = "2"  # Colleague
        self.assertEqual(self.accomplice.relationship_to_insider, "2")

    # Type checking
    def test_type_checking(self):
        with self.assertRaises(TypeError):
            self.accomplice.id = 123

        with self.assertRaises(TypeError):
            self.accomplice.relationship_to_insider = ["1"]

    # Vocab Checking
    def test_vocab_checking_relationship_to_insider(self):
        valid_relationships = ["1", "2", "3", "4", "5", "6", "8", "9"]
        for relationship in valid_relationships:
            accomplice = Accomplice(relationship_to_insider=relationship)
            self.assertEqual(accomplice.relationship_to_insider, relationship)

        with self.assertRaises(ValueError):
            self.accomplice.relationship_to_insider = "unknown"

    # Test delete function
    def test_delete_functions(self):
        del self.accomplice.relationship_to_insider
        self.assertIsNone(self.accomplice.relationship_to_insider)


class TestOrganization(unittest.TestCase):

    def setUp(self):
        self.organization = Organization(
            id="123e4567-e89b-12d3-a456-426614174000",
            name="Company XYZ, Inc.",
            city="New York",
            state="NY",
            country="US",
            postal_code=10001,
            small_business=True,
            industry_sector="51",
            industry_subsector="51.2",
            business="Software Development",
            parent_company="Parent Company ABC",
            incident_role="V"
        )

    # Initialization test
    def test_initialization(self):
        self.assertEqual(self.organization.id, "123e4567-e89b-12d3-a456-426614174000")
        self.assertEqual(self.organization.name, "Company XYZ, Inc.")
        self.assertEqual(self.organization.city, "New York")
        self.assertEqual(self.organization.state, "NY")
        self.assertEqual(self.organization.country, "US")
        self.assertEqual(self.organization.postal_code, 10001)
        self.assertTrue(self.organization.small_business)
        self.assertEqual(self.organization.industry_sector, "51")
        self.assertEqual(self.organization.industry_subsector, "51.2")
        self.assertEqual(self.organization.business, "Software Development")
        self.assertEqual(self.organization.parent_company, "Parent Company ABC")
        self.assertEqual(self.organization.incident_role, "V")

    # Test setters
    def test_setters(self):
        self.organization.name = "New Company"
        self.assertEqual(self.organization.name, "New Company")

        self.organization.city = "Los Angeles"
        self.assertEqual(self.organization.city, "Los Angeles")

        self.organization.state = "CA"
        self.assertEqual(self.organization.state, "CA")

        self.organization.country = "CA"
        self.assertEqual(self.organization.country, "CA")

        self.organization.postal_code = 90001
        self.assertEqual(self.organization.postal_code, 90001)

        self.organization.small_business = False
        self.assertFalse(self.organization.small_business)

        self.organization.industry_sector = "52"
        self.assertEqual(self.organization.industry_sector, "52")

        self.organization.industry_subsector = "52.1"
        self.assertEqual(self.organization.industry_subsector, "52.1")

        self.organization.business = "Financial Services"
        self.assertEqual(self.organization.business, "Financial Services")

        self.organization.parent_company = "New Parent Company"
        self.assertEqual(self.organization.parent_company, "New Parent Company")

        self.organization.incident_role = "T"
        self.assertEqual(self.organization.incident_role, "T")

    # Type checking
    def test_type_checking(self):
        with self.assertRaises(TypeError):
            self.organization.id = 123

        with self.assertRaises(TypeError):
            self.organization.postal_code = "10001"

        with self.assertRaises(TypeError):
            self.organization.small_business = "True"

    # Vocab Checking
    def test_vocab_checking_industry_sector(self):
        valid_industry_sectors = ["11", "22", "23", "31", "42", "44", "48", "51", "52", "53", "54", "55", "56", "61", "62", "71", "72", "81", "92", "99"]
        for sector in valid_industry_sectors:
            organization = Organization(industry_sector=sector)
            self.assertEqual(organization.industry_sector, sector)

        with self.assertRaises(ValueError):
            self.organization.industry_sector = "invalid"

    def test_vocab_checking_industry_subsector(self):
        valid_industry_subsectors = ["11.1", "11.2", "11.3", "11.4", "11.5", "21.1", "21.2", "21.3", "22.1", "23.6", "23.7", "23.8", "31.1", "31.2", "31.3", "31.4", "31.5", "31.6", "31.21", "31.22", "31.23", "31.24", "31.25", "31.26", "31.27", "31.31", "31.32", "31.33", "31.34", "31.35", "31.36", "31.37", "31.39", "42.3", "42.4", "42.5", "44.1", "44.4", "44.5", "44.9", "44.55", "44.56", "44.57", "44.58", "44.59", "48.1", "48.2", "48.3", "48.4", "48.5", "48.6", "48.7", "48.8", "48.91", "48.92", "48.93", "51.2", "51.3", "51.6", "51.7", "51.8", "51.9", "52.1", "52.2", "52.3", "52.4", "52.5", "53.1", "53.2", "53.3", "54.1", "55.1", "56.1", "56.2", "61.1", "62.1", "62.2", "62.3", "62.4", "71.1", "71.2", "71.3", "72.1", "72.2", "81.1", "81.2", "81.3", "81.4", "92.1", "92.2", "92.3", "92.4", "92.5", "92.6", "92.7", "92.811", "92.812"]
        for subsector in valid_industry_subsectors:
            organization = Organization(industry_sector=subsector[0:subsector.find('.')], industry_subsector=subsector)
            self.assertEqual(organization.industry_subsector, subsector)

        with self.assertRaises(ValueError):
            self.organization.industry_subsector = "invalid"

    def test_vocab_checking_incident_role(self):
        valid_incident_roles = ["B", "V", "S", "T", "O"]
        for role in valid_incident_roles:
            organization = Organization(incident_role=role)
            self.assertEqual(organization.incident_role, role)

        with self.assertRaises(ValueError):
            self.organization.incident_role = "invalid"

    # Test delete function
    def test_delete_functions(self):
        del self.organization.name
        self.assertIsNone(self.organization.name)

        del self.organization.city
        self.assertIsNone(self.organization.city)

        del self.organization.state
        self.assertIsNone(self.organization.state)

        del self.organization.country
        self.assertIsNone(self.organization.country)

        del self.organization.postal_code
        self.assertIsNone(self.organization.postal_code)

        del self.organization.small_business 
        self.assertIsNone(self.organization.small_business)

        del self.organization.industry_sector
        self.assertIsNone(self.organization.industry_sector)

        del self.organization.industry_subsector
        self.assertIsNone(self.organization.industry_subsector)

        del self.organization.business
        self.assertIsNone(self.organization.business)

        del self.organization.parent_company
        self.assertIsNone(self.organization.parent_company)

        del self.organization.incident_role 
        self.assertIsNone(self.organization.incident_role)


    # Test remove function
    def test_remove_functions(self):
        self.organization.name = "Company XYZ, Inc."
        del self.organization.name 
        self.assertIsNone(self.organization.name)

        self.organization.city = "New York"
        del self.organization.city 
        self.assertIsNone(self.organization.city)

        self.organization.state = "NY"
        del self.organization.state
        self.assertIsNone(self.organization.state)

        self.organization.country = "US"
        del self.organization.country
        self.assertIsNone(self.organization.country)

        self.organization.postal_code = 10001
        del self.organization.postal_code 
        self.assertIsNone(self.organization.postal_code)

        self.organization.small_business = True
        del self.organization.small_business
        self.assertIsNone(self.organization.small_business)

        self.organization.industry_subsector = "51.2"
        del self.organization.industry_subsector
        self.assertIsNone(self.organization.industry_subsector)

        self.organization.industry_sector = "51"
        del self.organization.industry_sector 
        self.assertIsNone(self.organization.industry_sector)

        self.organization.business = "Software Development"
        del self.organization.business 
        self.assertIsNone(self.organization.business)

        self.organization.parent_company = "Parent Company ABC"
        del self.organization.parent_company
        self.assertIsNone(self.organization.parent_company)

        self.organization.incident_role = "V"
        del self.organization.incident_role
        self.assertIsNone(self.organization.incident_role)


class TestJob(unittest.TestCase):

    def setUp(self):
        self.job = Job(
            id="123e4567-e89b-12d3-a456-426614174000",
            job_function="15",
            occupation="15.1",
            title="Software Developer",
            position_technical=True,
            access_authorization="2",
            employment_type="FLT",
            hire_date=date(2020, 1, 1),
            departure_date=date(2023, 1, 1),
            tenure=timedelta(days=1096),
            comment="This is a comment"
        )

    # Initialization test
    def test_initialization(self):
        self.assertEqual(self.job.id, "123e4567-e89b-12d3-a456-426614174000")
        self.assertEqual(self.job.job_function, "15")
        self.assertEqual(self.job.occupation, "15.1")
        self.assertEqual(self.job.title, "Software Developer")
        self.assertTrue(self.job.position_technical)
        self.assertEqual(self.job.access_authorization, "2")
        self.assertEqual(self.job.employment_type, "FLT")
        self.assertEqual(self.job.hire_date, date(2020, 1, 1))
        self.assertEqual(self.job.departure_date, date(2023, 1, 1))
        self.assertEqual(self.job.tenure, timedelta(days=1096))
        self.assertEqual(self.job.comment, "This is a comment")

    # Test setters
    def test_setters(self):
        self.job.job_function = "17"
        self.assertEqual(self.job.job_function, "17")

        self.job.occupation = "17.1"
        self.assertEqual(self.job.occupation, "17.1")

        self.job.title = "Architect"
        self.assertEqual(self.job.title, "Architect")

        self.job.position_technical = False
        self.assertFalse(self.job.position_technical)

        self.job.access_authorization = "3"
        self.assertEqual(self.job.access_authorization, "3")

        self.job.employment_type = "PRT"
        self.assertEqual(self.job.employment_type, "PRT")

        self.job.hire_date = date(2021, 1, 1)
        self.assertEqual(self.job.hire_date, date(2021, 1, 1))

        self.job.departure_date = date(2022, 1, 1)
        self.assertEqual(self.job.departure_date, date(2022, 1, 1))

        self.job.tenure = timedelta(days=365)
        self.assertEqual(self.job.tenure, timedelta(days=365))

        self.job.comment = "Updated comment"
        self.assertEqual(self.job.comment, "Updated comment")

    # Type checking
    def test_type_checking(self):
        with self.assertRaises(TypeError):
            self.job.id = 123  # Should be a string

        with self.assertRaises(TypeError):
            self.job.job_function = 15  # Should be a string

        with self.assertRaises(TypeError):
            self.job.occupation = 15.1  # Should be a string

        with self.assertRaises(TypeError):
            self.job.title = 12345  # Should be a string

        with self.assertRaises(TypeError):
            self.job.position_technical = "True"  # Should be a boolean

        with self.assertRaises(TypeError):
            self.job.access_authorization = 2  # Should be a string

        with self.assertRaises(TypeError):
            self.job.employment_type = 3  # Should be a string

        with self.assertRaises(TypeError):
            self.job.hire_date = 20200101  # Should be a string in date format

        with self.assertRaises(TypeError):
            self.job.departure_date = 20230101  # Should be a string in date format

        with self.assertRaises(TypeError):
            self.job.tenure = 3  # Should be a string

        with self.assertRaises(TypeError):
            self.job.comment = 12345  # Should be a string

    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- VOCAB CHECKING -=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    def test_vocab_checking_job_function(self):
        valid_job_functions = ["11", "13", "15", "17", "19", "21", "23", "25", "27", "29", "31", "33", "35", "37", "39", "41", "43", "45", "47", "49", "51", "53", "55", "99"]
        for function in valid_job_functions:
            job = Job(job_function=function)
            self.assertEqual(job.job_function, function)

        with self.assertRaises(ValueError):
            self.job.job_function = "invalid"

    def test_vocab_checking_occupation(self):
        valid_occupations = [("11", "11.1"), ("11", "11.2"), ("11", "11.3"), ("11", "11.9"), ("13", "13.1"), ("13", "13.2"), ("15", "15.1"), ("15", "15.2"), ("17", "17.1"), ("17", "17.2"), ("17", "17.3"), ("19", "19.1"), ("19", "19.2"), ("19", "19.3"), ("19", "19.4"), ("19", "19.5"), ("21", "21.1"), ("21", "21.2"), ("23", "23.1"), ("23", "23.2"), ("25", "25.2"), ("25", "25.3"), ("25", "25.4"), ("25", "25.9"), ("27", "27.1"), ("27", "27.2"), ("27", "27.3"), ("27", "27.4"), ("29", "29.1"), ("29", "29.2"), ("29", "29.9"), ("31", "31.1"), ("31", "31.2"), ("31", "31.9"), ("33", "33.1"), ("33", "33.2"), ("33", "33.3"), ("33", "33.9"), ("35", "35.1"), ("35", "35.2"), ("35", "35.3"), ("35", "35.9"), ("37", "37.1"), ("37", "37.2"), ("37", "37.3"), ("39", "39.1"), ("39", "39.2"), ("39", "39.3"), ("39", "39.4"), ("39", "39.5"), ("39", "39.6"), ("39", "39.7"), ("39", "39.9"), ("41", "41.1"), ("41", "41.2"), ("41", "41.3"), ("41", "41.4"), ("41", "41.9"), ("43", "43.1"), ("43", "43.2"), ("43", "43.3"), ("43", "43.4"), ("43", "43.5"), ("43", "43.6"), ("43", "43.9"), ("45", "45.1"), ("45", "45.2"), ("45", "45.3"), ("45", "45.4"), ("47", "47.1"), ("47", "47.2"), ("47", "47.3"), ("47", "47.4"), ("47", "47.5"), ("49", "49.1"), ("49", "49.2"), ("49", "49.3"), ("49", "49.9"), ("51", "51.1"), ("51", "51.2"), ("51", "51.3"), ("51", "51.4"), ("51", "51.5"), ("51", "51.6"), ("51", "51.7"), ("51", "51.8"), ("51", "51.9"), ("53", "53.1"), ("53", "53.2"), ("53", "53.3"), ("53", "53.4"), ("53", "53.5"), ("53", "53.6"), ("53", "53.7"), ("55", "55.1"), ("55", "55.2"), ("55", "55.3"), ("99", "99.1"), ("99", "99.9")]        
        for jf, occupation in valid_occupations:
            job = Job(job_function=jf, occupation=occupation)
            self.assertEqual(job.occupation, occupation)

        with self.assertRaises(ValueError):
            self.job.occupation = "invalid"
    
    def test_occupation_is_subtype_of_job_function(self):
        valid_combinations = [
            ("13", "13.1"), ("13", "13.2"), ("15", "15.1"), ("15", "15.2"),
            ("17", "17.1"), ("17", "17.2"), ("17", "17.3")
        ]
        for job_function, occupation in valid_combinations:
            job = Job(job_function=job_function, occupation=occupation)
            self.assertEqual(job.job_function, job_function)
            self.assertEqual(job.occupation, occupation)

        # Invalid combinations
        invalid_combinations = [
            ("13", "15.1"), ("15", "17.2"), ("17", "19.1")
        ]
        for job_function, occupation in invalid_combinations:
            with self.assertRaises(ValueError):
                Job(job_function=job_function, occupation=occupation)


    def test_vocab_checking_access_authorization(self):
        valid_access_auth = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for auth in valid_access_auth:
            job = Job(access_authorization=auth)
            self.assertEqual(job.access_authorization, auth)

        with self.assertRaises(ValueError):
            self.job.access_authorization = "invalid"

    def test_vocab_checking_employment_type(self):
        valid_employment_types = ["CTR", "FLT", "PRT", "INT", "TMP", "VOL", "OTH"]
        for emp_type in valid_employment_types:
            job = Job(employment_type=emp_type)
            self.assertEqual(job.employment_type, emp_type)

        with self.assertRaises(ValueError):
            self.job.employment_type = "invalid"

    # Test delete function
    def test_delete_functions(self):
        del self.job.job_function
        self.assertIsNone(self.job.job_function)

        del self.job.occupation
        self.assertIsNone(self.job.occupation)

        del self.job.title
        self.assertIsNone(self.job.title)

        del self.job.position_technical
        self.assertIsNone(self.job.position_technical)

        del self.job.access_authorization
        self.assertIsNone(self.job.access_authorization)

        del self.job.employment_type
        self.assertIsNone(self.job.employment_type)

        del self.job.hire_date
        self.assertIsNone(self.job.hire_date)

        del self.job.departure_date
        self.assertIsNone(self.job.departure_date)

        del self.job.comment
        self.assertIsNone(self.job.comment)

    # Test remove function
    def test_remove_functions(self):
        self.job.job_function = "15"
        del self.job.job_function 
        self.assertIsNone(self.job.job_function)

        self.job.occupation = "15.1"
        del self.job.occupation 
        self.assertIsNone(self.job.occupation)

        self.job.title = "Software Developer"
        del self.job.title 
        self.assertIsNone(self.job.title)

        self.job.position_technical = True
        del self.job.position_technical 
        self.assertIsNone(self.job.position_technical)

        self.job.access_authorization = "2"
        del self.job.access_authorization 
        self.assertIsNone(self.job.access_authorization)

        self.job.employment_type = "FLT"
        del self.job.employment_type 
        self.assertIsNone(self.job.employment_type)

        del self.job.hire_date 
        self.assertIsNone(self.job.hire_date)
        self.job.hire_date = date(2020, 1, 1)

        del self.job.departure_date 
        self.assertIsNone(self.job.departure_date)
        self.job.departure_date = date(2023, 1, 1)

        self.job.tenure = timedelta(days=1096)

        self.job.comment = "This is a comment"
        del self.job.comment 
        self.assertIsNone(self.job.comment)


class TestResponse(unittest.TestCase):

    def setUp(self):
        self.response = Response(
            id="123e4567-e89b-12d3-a456-426614174000",
            technical_controls=[("1", date(2023, 1, 1))],
            behavioral_controls=[("4", date(2023, 1, 2))],
            investigated_by=["1", "2"],
            investigation_events=[("2", date(2023, 1, 3))],
            comment="Initial comment"
        )

    # Initialization test
    def test_initialization(self):
        self.assertEqual(self.response.id, "123e4567-e89b-12d3-a456-426614174000")
        self.assertEqual(self.response.technical_controls, [("1", date(2023, 1, 1))])
        self.assertEqual(self.response.behavioral_controls, [("4", date(2023, 1, 2))])
        self.assertEqual(self.response.investigated_by, ["1", "2"])
        self.assertEqual(self.response.investigation_events, [("2", date(2023, 1, 3))])
        self.assertEqual(self.response.comment, "Initial comment")

    # Test setters
    def test_setters(self):
        self.response.technical_controls = [("2", date(2023, 2, 1))]
        self.assertEqual(self.response.technical_controls, [("2", date(2023, 2, 1))])

        self.response.behavioral_controls = [("1", date(2023, 2, 2))]
        self.assertEqual(self.response.behavioral_controls, [("1", date(2023, 2, 2))])

        self.response.investigated_by = ["3", "4"]
        self.assertEqual(self.response.investigated_by, ["3", "4"])

        self.response.investigation_events = [("3", date(2023, 2, 3))]
        self.assertEqual(self.response.investigation_events, [("3", date(2023, 2, 3))])

        self.response.comment = "Updated comment"
        self.assertEqual(self.response.comment, "Updated comment")

    # Extensive type checking
    def test_type_checking(self):
        with self.assertRaises(TypeError):
            self.response.id = 123  # Should be a string

        with self.assertRaises(TypeError):
            self.response.technical_controls = "invalid"  # Should be a list

        with self.assertRaises(TypeError):
            self.response.behavioral_controls = "invalid"  # Should be a list

        with self.assertRaises(TypeError):
            self.response.investigated_by = "invalid"  # Should be a list

        with self.assertRaises(TypeError):
            self.response.investigation_events = "invalid"  # Should be a list

        with self.assertRaises(TypeError):
            self.response.comment = 12345  # Should be a string

    # Vocab Checking
    def test_vocab_checking_technical_controls(self):
        valid_technical_controls = [("1", date(2023, 1, 1)), ("2", date(2023, 1, 2))]
        for control in valid_technical_controls:
            response = Response(technical_controls=[control])
            self.assertEqual(response.technical_controls, [control])

        with self.assertRaises(ValueError):
            self.response.technical_controls = [("invalid", date(2023, 1, 1))]

    def test_vocab_checking_behavioral_controls(self):
        valid_behavioral_controls = [
            ("1", date(2023, 1, 1)), ("2", date(2023, 1, 2)), ("3", date(2023, 1, 3)), ("4", date(2023, 1, 4)), ("5", date(2023, 1, 5)),
            ("6", date(2023, 1, 6)), ("7", date(2023, 1, 7)), ("8", date(2023, 1, 8)), ("9", date(2023, 1, 9)), ("10", date(2023, 1, 10)),
            ("11", date(2023, 1, 11)), ("12", date(2023, 1, 12))
        ]
        for control in valid_behavioral_controls:
            response = Response(behavioral_controls=[control])
            self.assertEqual(response.behavioral_controls, [control])

        with self.assertRaises(ValueError):
            self.response.behavioral_controls = [("invalid", date(2023, 1, 1))]

    def test_vocab_checking_investigated_by(self):
        valid_investigators = ["1", "2", "3", "4", "5", "6", "7", "99"]
        for investigator in valid_investigators:
            response = Response(investigated_by=[investigator])
            self.assertEqual(response.investigated_by, [investigator])

        with self.assertRaises(ValueError):
            self.response.investigated_by = ["invalid"]

    def test_vocab_checking_investigation_events(self):
        valid_events = [("1", date(2023, 1, 1)), ("2", date(2023, 1, 2)), ("3", date(2023, 1, 3))]
        for event in valid_events:
            response = Response(investigation_events=[event])
            self.assertEqual(response.investigation_events, [event])

        with self.assertRaises(ValueError):
            self.response.investigation_events = [("invalid", date(2023, 1, 1))]

    # Append functionality tests
    def test_append_technical_controls(self):
        self.response.append_technical_controls(("2", date(2023, 2, 1)))
        self.assertIn(("2", date(2023, 2, 1)), self.response.technical_controls)

    def test_append_behavioral_controls(self):
        self.response.append_behavioral_controls(("5", date(2023, 2, 2)))
        self.assertIn(("5", date(2023, 2, 2)), self.response.behavioral_controls)

    def test_append_investigated_by(self):
        self.response.append_investigated_by("3")
        self.assertIn("3", self.response.investigated_by)

    def test_append_investigation_evens(self):
        self.response.append_investigation_events(("3", date(2023, 2, 3)))
        self.assertIn(("3", date(2023, 2, 3)), self.response.investigation_events)

    # Test delete function
    def test_delete_functions(self):
        del self.response.technical_controls
        self.assertIsNone(self.response.technical_controls)

        del self.response.behavioral_controls
        self.assertIsNone(self.response.behavioral_controls)

        del self.response.investigated_by 
        self.assertIsNone(self.response.investigated_by)

        del self.response.investigation_events 
        self.assertIsNone(self.response.investigation_events)

        del self.response.comment
        self.assertIsNone(self.response.comment)

    # Test clear function
    def test_clear_functions(self):
        self.response.technical_controls = []
        self.assertEqual(self.response.technical_controls, [])

        self.response.behavioral_controls = []
        self.assertEqual(self.response.behavioral_controls, [])

        self.response.investigated_by = []
        self.assertEqual(self.response.investigated_by, [])

        self.response.investigation_events = []
        self.assertEqual(self.response.investigation_events, [])

        self.response.comment = ""
        self.assertEqual(self.response.comment, "")

    # Test remove function
    def test_remove_functions(self):
        self.response.technical_controls = [("1", date(2023, 1, 1))]
        del self.response.technical_controls 
        self.assertIsNone(self.response.technical_controls)

        self.response.behavioral_controls = [("4", date(2023, 1, 2))]
        del self.response.behavioral_controls 
        self.assertIsNone(self.response.behavioral_controls)

        self.response.investigated_by = ["1", "2"]
        del self.response.investigated_by 
        self.assertIsNone(self.response.investigated_by)

        self.response.investigation_events = [("2", date(2023, 1, 3))]
        del self.response.investigation_events 
        self.assertIsNone(self.response.investigation_events)

        self.response.comment = "Initial comment"
        del self.response.comment 
        self.assertIsNone(self.response.comment)



class TestTTP(unittest.TestCase):

    def setUp(self):
        self.ttp = TTP(
            id="123e4567-e89b-12d3-a456-426614174000",
            date=datetime(2023, 1, 1, 0, 0, 0),
            sequence_num=1,
            observed=True,
            number_of_times=5,
            ttp_vocab="IIDES",
            tactic="1",
            technique="1.1",
            location=["1"],
            hours=["1"],
            device=["1"],
            channel=["1"],
            description="Initial description"
        )

    # Initialization test
    def test_initialization(self):
        self.assertEqual(self.ttp.id, "123e4567-e89b-12d3-a456-426614174000")
        self.assertEqual(self.ttp.date, datetime(2023, 1, 1, 0, 0, 0))
        self.assertEqual(self.ttp.sequence_num, 1)
        self.assertTrue(self.ttp.observed)
        self.assertEqual(self.ttp.number_of_times, 5)
        self.assertEqual(self.ttp.ttp_vocab, "IIDES")
        self.assertEqual(self.ttp.tactic, "1")
        self.assertEqual(self.ttp.technique, "1.1")
        self.assertEqual(self.ttp.location, ["1"])
        self.assertEqual(self.ttp.hours, ["1"])
        self.assertEqual(self.ttp.device, ["1"])
        self.assertEqual(self.ttp.channel, ["1"])
        self.assertEqual(self.ttp.description, "Initial description")

    # Test setters
    def test_setters(self):
        self.ttp.date = datetime(2023, 2, 1, 0, 0, 0)
        self.assertEqual(self.ttp.date, datetime(2023, 2, 1, 0, 0, 0))

        self.ttp.sequence_num = 2
        self.assertEqual(self.ttp.sequence_num, 2)

        self.ttp.observed = False
        self.assertFalse(self.ttp.observed)

        self.ttp.number_of_times = 10
        self.assertEqual(self.ttp.number_of_times, 10)

        self.ttp.ttp_vocab = "ATT&CK"
        self.assertEqual(self.ttp.ttp_vocab, "ATT&CK")

        self.ttp.tactic = "2"
        self.assertEqual(self.ttp.tactic, "2")

        self.ttp.technique = "2.1"
        self.assertEqual(self.ttp.technique, "2.1")

        self.ttp.description = "Updated description"
        self.assertEqual(self.ttp.description, "Updated description")

    # Type checking
    def test_type_checking(self):
        with self.assertRaises(TypeError):
            self.ttp.date = 20230101  # Should be a string

        with self.assertRaises(TypeError):
            self.ttp.sequence_num = "1"  # Should be an integer

        with self.assertRaises(TypeError):
            self.ttp.observed = "True"  # Should be a boolean

        with self.assertRaises(TypeError):
            self.ttp.number_of_times = "5"  # Should be an integer

        with self.assertRaises(TypeError):
            self.ttp.tactic = 1  # Should be a string

        with self.assertRaises(TypeError):
            self.ttp.technique = 1.1  # Should be a string

        with self.assertRaises(TypeError):
            self.ttp.location = 1  # Should be a list of strings

        with self.assertRaises(TypeError):
            self.ttp.hours = 1  # Should be a list of strings

        with self.assertRaises(TypeError):
            self.ttp.device = 1  # Should be a list of strings

        with self.assertRaises(TypeError):
            self.ttp.channel = 1  # Should be a list of strings

        with self.assertRaises(TypeError):
            self.ttp.description = 12345  # Should be a string

    # Vocab Checking
    def test_vocab_checking_tactic(self):
        valid_tactics = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for tactic in valid_tactics:
            ttp = TTP(id=str(uuid.uuid4()), tactic=tactic)
            self.assertEqual(ttp.tactic, tactic)

        with self.assertRaises(ValueError):
            self.ttp.tactic = "invalid"

    def test_vocab_checking_technique(self):
        valid_techniques = ["1.1", "1.2", "1.3", "1.4", "1.5", "1.6", "1.7", "1.8", "1.9", "1.10", "1.11", "1.12", "1.13", "2.1", "2.2", "2.3", "2.4", "3.1", "3.2", "3.3", "3.4", "3.5", "3.6", "3.7", "4.1", "4.2", "4.3", "4.4", "4.5", "4.6", "4.7", "4.8", "4.9", "4.10", "4.11", "4.12", "4.13", "5.1", "5.2", "5.3", "5.4", "6.1", "6.2", "6.3", "6.4", "6.5", "6.6", "6.7", "6.8", "6.9", "6.10", "7.1", "7.2", "7.3", "7.4", "7.5", "7.6", "7.7", "7.8", "7.9", "7.10", "8.1", "8.2", "8.3", "8.4", "8.5", "8.6", "9.1", "9.2", "9.3", "9.4", "9.5"]
        for technique in valid_techniques:
            ttp = TTP(id=str(uuid.uuid4()), technique=technique)
            self.assertEqual(ttp.technique, technique)

        with self.assertRaises(ValueError):
            self.ttp.technique = "invalid"

    def test_vocab_checking_location(self):
        valid_locations = ["1", "2", "3", "4"]
        for location in valid_locations:
            ttp = TTP(id=str(uuid.uuid4()), location=[location])
            self.assertIn(location, ttp.location)

        with self.assertRaises(ValueError):
            self.ttp.location = ["invalid"]

    def test_vocab_checking_hours(self):
        valid_hours = ["1", "2"]
        for hour in valid_hours:
            ttp = TTP(id=str(uuid.uuid4()), hours=[hour])
            self.assertIn(hour, ttp.hours)

        with self.assertRaises(ValueError):
            self.ttp.hours = ["invalid"]

    def test_vocab_checking_device(self):
        valid_devices = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "99"]
        for device in valid_devices:
            ttp = TTP(id=str(uuid.uuid4()), device=[device])
            self.assertIn(device, ttp.device)

        with self.assertRaises(ValueError):
            self.ttp.device = ["invalid"]

    def test_vocab_checking_channel(self):
        valid_channels = ["1", "2", "3", "4", "5", "6", "9"]
        for channel in valid_channels:
            ttp = TTP(id=str(uuid.uuid4()), channel=[channel])
            self.assertIn(channel, ttp.channel)

        with self.assertRaises(ValueError):
            self.ttp.channel = ["invalid"]
    
    # TODO: def test_technique_is_subtype_of_tactic(self):
        # valid_combinations = [
        #     ("1", "1.1"), ("1", "1.2"), ("1", "1.3"), ("1", "1.4"), ("1", "1.5"),
        #     ("2", "2.1"), ("2", "2.2"), ("2", "2.3"), ("2", "2.4"),
        #     ("3", "3.1"), ("3", "3.2"), ("3", "3.3"), ("3", "3.4"), ("3", "3.5"),
        #     ("4", "4.1"), ("4", "4.2"), ("4", "4.3"), ("4", "4.4"), ("4", "4.5"),
        #     ("5", "5.1"), ("5", "5.2"), ("5", "5.3"), ("5", "5.4"),
        #     ("6", "6.1"), ("6", "6.2"), ("6", "6.3"), ("6", "6.4"), ("6", "6.5"),
        #     ("7", "7.1"), ("7", "7.2"), ("7", "7.3"), ("7", "7.4"), ("7", "7.5"),
        #     ("8", "8.1"), ("8", "8.2"), ("8", "8.3"), ("8", "8.4"), ("8", "8.5"),
        #     ("9", "9.1"), ("9", "9.2"), ("9", "9.3"), ("9", "9.4"), ("9", "9.5")
        # ]
        # for tactic, technique in valid_combinations:
        #     ttp = TTP(id=str(uuid.uuid4()), tactic=tactic, technique=technique)
        #     self.assertEqual(ttp.tactic, tactic)
        #     self.assertEqual(ttp.technique, technique)

        # # Invalid combinations
        # invalid_combinations = [
        #     ("1", "2.1"), ("2", "3.2"), ("3", "4.1")
        # ]
        # for tactic, technique in invalid_combinations:
        #     with self.assertRaises(ValueError):
        #         TTP(id=str(uuid.uuid4()), tactic=tactic, technique=technique)


    # Append functionality tests
    def test_append_location(self):
        self.ttp.append_location("2")
        self.assertIn("2", self.ttp.location)

    def test_append_hours(self):
        self.ttp.append_hours("2")
        self.assertIn("2", self.ttp.hours)

    def test_append_device(self):
        self.ttp.append_device("2")
        self.assertIn("2", self.ttp.device)

    def test_append_channel(self):
        self.ttp.append_channel("2")
        self.assertIn("2", self.ttp.channel)

if __name__ == "__main__":
    print("\n - - - - - - - - - - - - - - - -\n")
    print("Beginning Testing Suite:\n")

    unittest.main()

    print("Finished testing suite.")