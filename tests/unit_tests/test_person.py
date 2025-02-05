"""
License:
PyIIDES
Copyright 2024 Carnegie Mellon University.
NO WARRANTY. THIS CARNEGIE MELLON UNIVERSITY AND SOFTWARE ENGINEERING INSTITUTE MATERIAL IS FURNISHED ON AN "AS-IS" BASIS. CARNEGIE MELLON UNIVERSITY MAKES NO WARRANTIES OF ANY KIND, EITHER EXPRESSED OR IMPLIED, AS TO ANY MATTER INCLUDING, BUT NOT LIMITED TO, WARRANTY OF FITNESS FOR PURPOSE OR MERCHANTABILITY, EXCLUSIVITY, OR RESULTS OBTAINED FROM USE OF THE MATERIAL. CARNEGIE MELLON UNIVERSITY DOES NOT MAKE ANY WARRANTY OF ANY KIND WITH RESPECT TO FREEDOM FROM PATENT, TRADEMARK, OR COPYRIGHT INFRINGEMENT.
Licensed under a MIT (SEI)-style license, please see license.txt or contact permission@sei.cmu.edu for full terms.
[DISTRIBUTION STATEMENT A] This material has been approved for public release and unlimited distribution.  Please see Copyright notice for non-US Government use and distribution.
DM24-1597
"""
from pyiides import Person
import unittest

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