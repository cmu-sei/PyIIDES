"""
License:
PyIIDES
Copyright 2024 Carnegie Mellon University.
NO WARRANTY. THIS CARNEGIE MELLON UNIVERSITY AND SOFTWARE ENGINEERING INSTITUTE MATERIAL IS FURNISHED ON AN "AS-IS" BASIS. CARNEGIE MELLON UNIVERSITY MAKES NO WARRANTIES OF ANY KIND, EITHER EXPRESSED OR IMPLIED, AS TO ANY MATTER INCLUDING, BUT NOT LIMITED TO, WARRANTY OF FITNESS FOR PURPOSE OR MERCHANTABILITY, EXCLUSIVITY, OR RESULTS OBTAINED FROM USE OF THE MATERIAL. CARNEGIE MELLON UNIVERSITY DOES NOT MAKE ANY WARRANTY OF ANY KIND WITH RESPECT TO FREEDOM FROM PATENT, TRADEMARK, OR COPYRIGHT INFRINGEMENT.
Licensed under a MIT (SEI)-style license, please see license.txt or contact permission@sei.cmu.edu for full terms.
[DISTRIBUTION STATEMENT A] This material has been approved for public release and unlimited distribution.  Please see Copyright notice for non-US Government use and distribution.
DM24-1597
"""
import unittest, uuid, os, sys
from datetime import date
sys.path.append(os.getcwd())
from pyiides import Charge, CourtCase, LegalResponse, Sentence

class TestCourtCaseInitialization(unittest.TestCase):
    def setUp(self):
        self.valid_court_types = ["1", "2", "3"]
        self.valid_case_types = ["1", "2"]
        self.court_case_data = {
            "id": str(uuid.uuid4()),
            "case_number": "12345",
            "case_title": "US v. LastName",
            "court_country": "US",
            "court_state": "CA",
            "court_district": "CA Central District Court",
            "court_type": "1",
            "case_type": "2",
            "defendant": ["Defendant One"],
            "plaintiff": ["Plaintiff One"],
            "comment": "This is a test comment."
        }
        self.court_case = CourtCase(**self.court_case_data)

    def test_initialization(self):
        # Check all fields are set correctly upon initialization
        self.assertEqual(self.court_case.id, self.court_case_data['id'])
        self.assertEqual(self.court_case.case_number, self.court_case_data['case_number'])
        self.assertEqual(self.court_case.case_title, self.court_case_data['case_title'])
        self.assertEqual(self.court_case.court_country, self.court_case_data['court_country'])
        self.assertEqual(self.court_case.court_state, self.court_case_data['court_state'])
        self.assertEqual(self.court_case.court_district, self.court_case_data['court_district'])
        self.assertEqual(self.court_case.court_type, self.court_case_data['court_type'])
        self.assertEqual(self.court_case.case_type, self.court_case_data['case_type'])
        self.assertEqual(self.court_case.defendant, self.court_case_data['defendant'])
        self.assertEqual(self.court_case.plaintiff, self.court_case_data['plaintiff'])
        self.assertEqual(self.court_case.comment, self.court_case_data['comment'])

    def test_invalid_court_type_vocabulary(self):
        for invalid_court_type in ["0", "4", "invalid"]:
            with self.subTest(court_type=invalid_court_type):
                self.court_case_data['court_type'] = invalid_court_type
                with self.assertRaises(ValueError):
                    CourtCase(**self.court_case_data)

    def test_invalid_case_type_vocabulary(self):
        for invalid_case_type in ["0", "3", "invalid"]:
            with self.subTest(case_type=invalid_case_type):
                self.court_case_data['case_type'] = invalid_case_type
                with self.assertRaises(ValueError):
                    CourtCase(**self.court_case_data)

    def test_type_errors(self):
        # Check type errors on initialization
        invalid_data = {
            "id": 123,  # should be str
            "case_number": 12345,  # should be str
            "case_title": 123,  # should be str
            "court_country": 123,  # should be str
            "court_state": 123,  # should be str
            "court_district": 123,  # should be str
            "court_type": 1,  # should be str
            "case_type": 2,  # should be str
            "defendant": "Defendant One",  # should be list
            "plaintiff": "Plaintiff One",  # should be list
            "comment": 123  # should be str
        }
        for key, value in invalid_data.items():
            with self.subTest(field=key):
                self.court_case_data[key] = value
                with self.assertRaises(TypeError):
                    CourtCase(**self.court_case_data)


class TestCourtCaseTypeChecking(unittest.TestCase):
    def setUp(self):
        self.court_case = CourtCase(
            id=str(uuid.uuid4()),
            case_number="12345",
            case_title="US v. LastName",
            court_country="US",
            court_state="CA",
            court_district="CA Central District Court",
            court_type="1",
            case_type="2",
            defendant=["Defendant One"],
            plaintiff=["Plaintiff One"],
            comment="This is a test comment."
        )

    def test_set_id_type(self):
        with self.assertRaises(TypeError):
            self.court_case.id = 123  # should be str

    def test_set_case_number_type(self):
        with self.assertRaises(TypeError):
            self.court_case.case_number = 12345  # should be str

    def test_set_case_title_type(self):
        with self.assertRaises(TypeError):
            self.court_case.case_title = 123  # should be str

    def test_set_court_country_type(self):
        with self.assertRaises(TypeError):
            self.court_case.court_country = 123  # should be str

    def test_set_court_state_type(self):
        with self.assertRaises(TypeError):
            self.court_case.court_state = 123  # should be str

    def test_set_court_district_type(self):
        with self.assertRaises(TypeError):
            self.court_case.court_district = 123  # should be str

    def test_set_court_type_type(self):
        with self.assertRaises(TypeError):
            self.court_case.court_type = 1  # should be str

    def test_set_case_type_type(self):
        with self.assertRaises(TypeError):
            self.court_case.case_type = 2  # should be str

    def test_set_defendant_type(self):
        with self.assertRaises(TypeError):
            self.court_case.defendant = "Defendant One"  # should be list

    def test_set_plaintiff_type(self):
        with self.assertRaises(TypeError):
            self.court_case.plaintiff = "Plaintiff One"  # should be list

    def test_set_comment_type(self):
        with self.assertRaises(TypeError):
            self.court_case.comment = 123  # should be str


class TestCourtCaseVocabChecking(unittest.TestCase):
    def setUp(self):
        self.valid_court_types = ["1", "2", "3"]
        self.valid_case_types = ["1", "2"]
        self.court_case_data = {
            "id": str(uuid.uuid4()),
            "case_number": "12345",
            "case_title": "US v. LastName",
            "court_country": "US",
            "court_state": "CA",
            "court_district": "CA Central District Court",
            "court_type": "1",
            "case_type": "2",
            "defendant": ["Defendant One"],
            "plaintiff": ["Plaintiff One"],
            "comment": "This is a test comment."
        }
        self.court_case = CourtCase(**self.court_case_data)

    def test_valid_court_type_values(self):
        for court_type in self.valid_court_types:
            with self.subTest(court_type=court_type):
                self.court_case.court_type = court_type
                self.assertEqual(self.court_case.court_type, court_type)

    def test_invalid_court_type_values(self):
        for invalid_court_type in ["0", "4", "invalid"]:
            with self.subTest(court_type=invalid_court_type):
                with self.assertRaises(ValueError):
                    self.court_case.court_type = invalid_court_type

    def test_valid_case_type_values(self):
        for case_type in self.valid_case_types:
            with self.subTest(case_type=case_type):
                self.court_case.case_type = case_type
                self.assertEqual(self.court_case.case_type, case_type)

    def test_invalid_case_type_values(self):
        for invalid_case_type in ["0", "3", "invalid"]:
            with self.subTest(case_type=invalid_case_type):
                with self.assertRaises(ValueError):
                    self.court_case.case_type = invalid_case_type


class TestCourtCaseRelationships(unittest.TestCase):
    def setUp(self):
        self.charge = Charge(
            id=str(uuid.uuid4()),
            title="Test Charge",
            section="18:343",
            nature_of_offense="Wire Fraud",
            count=1,
            plea="1",
            plea_bargain=False,
            disposition="2"
        )
        self.sentence = Sentence(id=str(uuid.uuid4()), sentence_type="2")
        self.legal_response = LegalResponse(id=str(uuid.uuid4()))

        self.court_case_data = {
            "id": str(uuid.uuid4()),
            "case_number": "12345",
            "case_title": "US v. LastName",
            "court_country": "US",
            "court_state": "CA",
            "court_district": "CA Central District Court",
            "court_type": "1",
            "case_type": "2",
            "defendant": ["Defendant One"],
            "plaintiff": ["Plaintiff One"],
            "comment": "This is a test comment."
        }
        self.court_case = CourtCase(**self.court_case_data)
        self.court_case.legal_response = self.legal_response

    def test_append_charge_to_court_case(self):
        self.court_case.append_charge(self.charge)
        self.assertIn(self.charge, self.court_case.charges)
        self.assertEqual(self.charge.court_case, self.court_case)

    def test_remove_charge_from_court_case(self):
        self.court_case.append_charge(self.charge)
        self.court_case.remove_charge(self.charge)
        self.assertNotIn(self.charge, self.court_case.charges)
        self.assertIsNone(self.charge.court_case)

    def test_multiple_charges(self):
        charge2 = Charge(
            id=str(uuid.uuid4()),
            title="Test Charge 2",
            section="18:344",
            nature_of_offense="Bank Fraud",
            count=2,
            plea="2",
            plea_bargain=True,
            disposition="3"
        )
        self.court_case.append_charge(self.charge)
        self.court_case.append_charge(charge2)
        self.assertIn(self.charge, self.court_case.charges)
        self.assertIn(charge2, self.court_case.charges)
        self.assertEqual(self.charge.court_case, self.court_case)
        self.assertEqual(charge2.court_case, self.court_case)
        self.court_case.remove_charge(self.charge)
        self.assertNotIn(self.charge, self.court_case.charges)
        self.assertIsNone(self.charge.court_case)
        self.assertIn(charge2, self.court_case.charges)
        self.assertEqual(charge2.court_case, self.court_case)

    def test_append_invalid_type_charge(self):
        with self.assertRaises(TypeError):
            self.court_case.append_charge("Invalid Charge")  # should raise TypeError
    
    def test_set_sentence(self):
        sentence2 = Sentence(sentence_type="1")
        sentence3 = Sentence(sentence_type="1")
        sentence4 = Sentence(sentence_type="1")

        self.court_case.sentences = [self.sentence, sentence2]
        self.assertIn(self.sentence, self.court_case.sentences)
        self.assertIn(sentence2, self.court_case.sentences)
        self.assertEqual(self.sentence.court_case, self.court_case)
        self.assertEqual(sentence2.court_case, self.court_case)

        self.court_case.sentences = [sentence3, sentence4]
        self.assertIn(sentence3, self.court_case.sentences)
        self.assertIn(sentence4, self.court_case.sentences)
        self.assertEqual(sentence3.court_case, self.court_case)
        self.assertEqual(sentence4.court_case, self.court_case)
    
    def test_set_charge(self):
        charge1 = Charge(title="title1")
        charge2 = Charge(title="title2")
        charge3 = Charge(title="title3")
        charge4 = Charge(title="title4")

        self.court_case.charges = [charge1, charge2]
        self.assertIn(charge1, self.court_case.charges)
        self.assertIn(charge2, self.court_case.charges)
        self.assertEqual(charge1.court_case, self.court_case)
        self.assertEqual(charge2.court_case, self.court_case)

        self.court_case.charges = [charge3, charge4]
        self.assertIsNone(charge1.court_case)
        self.assertIsNone(charge2.court_case)
        self.assertNotIn(charge1, self.court_case.charges)
        self.assertNotIn(charge2, self.court_case.charges)

        self.assertIn(charge3, self.court_case.charges)
        self.assertIn(charge4, self.court_case.charges)
        self.assertEqual(charge3.court_case, self.court_case)
        self.assertEqual(charge4.court_case, self.court_case)

    def test_append_sentence_to_court_case(self):
        self.court_case.append_sentence(self.sentence)
        self.assertIn(self.sentence, self.court_case.sentences)
        self.assertEqual(self.sentence.court_case, self.court_case)

    def test_remove_sentence_from_court_case(self):
        self.court_case.append_sentence(self.sentence)
        self.court_case.remove_sentence(self.sentence)
        self.assertNotIn(self.sentence, self.court_case.sentences)
        self.assertIsNone(self.sentence.court_case)

    def test_multiple_sentences(self):
        sentence2 = Sentence(id=str(uuid.uuid4()), sentence_type="1")
        self.court_case.append_sentence(self.sentence)
        self.court_case.append_sentence(sentence2)
        self.assertIn(self.sentence, self.court_case.sentences)
        self.assertIn(sentence2, self.court_case.sentences)
        self.assertEqual(self.sentence.court_case, self.court_case)
        self.assertEqual(sentence2.court_case, self.court_case)
        self.court_case.remove_sentence(self.sentence)
        self.assertNotIn(self.sentence, self.court_case.sentences)
        self.assertIsNone(self.sentence.court_case)
        self.assertIn(sentence2, self.court_case.sentences)
        self.assertEqual(sentence2.court_case, self.court_case)

    def test_append_invalid_type_sentence(self):
        with self.assertRaises(TypeError):
            self.court_case.append_sentence("Invalid Sentence")  # should raise TypeError

    def test_set_legal_response_to_court_case(self):
        self.court_case.legal_response = self.legal_response
        self.assertEqual(self.court_case.legal_response, self.legal_response)
        self.assertIn(self.court_case, self.legal_response.court_cases)

    def test_set_another_legal_response(self):
        self.court_case.legal_response = self.legal_response
        another_legal_response = LegalResponse(id=str(uuid.uuid4()))
        self.assertIn(self.court_case, self.legal_response.court_cases)
        self.assertEqual(self.legal_response, self.court_case.legal_response)

        self.court_case.legal_response = another_legal_response
        self.assertIn(self.court_case, another_legal_response.court_cases)
        self.assertEqual(another_legal_response, self.court_case.legal_response)

        self.assertNotIn(self.court_case, self.legal_response.court_cases)
        self.assertNotEqual(self.legal_response, self.court_case.legal_response)

    def test_remove_legal_response_from_court_case(self):
        self.court_case.legal_response = self.legal_response
        del self.court_case.legal_response
        self.assertIsNone(self.court_case.legal_response)
        self.assertNotIn(self.court_case, self.legal_response.court_cases)

    def test_set_invalid_type_legal_response(self):
        with self.assertRaises(TypeError):
            self.court_case.legal_response = "Invalid Legal Response"  # should raise TypeError


class TestCourtCaseSetting(unittest.TestCase):
    def setUp(self):
        self.court_case = CourtCase(
            id=str(uuid.uuid4()),
            case_number="12345",
            case_title="USA v. LastName",
            court_country="US",
            court_state="CA",
            court_district="CA Central District Court",
            court_type="1",
            case_type="2",
            defendant=["Defendant One"],
            plaintiff=["Plaintiff One"],
            comment="This is a test comment."
        )
        self.charge = Charge(
            id=str(uuid.uuid4()),
            title="Test Charge",
            section="18:343",
            nature_of_offense="Wire Fraud",
            count=1,
            plea="1",
            plea_bargain=False,
            disposition="2"
        )
        self.sentence = Sentence(id=str(uuid.uuid4()), sentence_type="1")
        self.legal_response = LegalResponse(id=str(uuid.uuid4()))

    def test_set_case_number(self):
        new_case_number = "67890"
        self.court_case.case_number = new_case_number
        self.assertEqual(self.court_case.case_number, new_case_number)

    def test_set_case_title(self):
        new_case_title = "State v. Someone"
        self.court_case.case_title = new_case_title
        self.assertEqual(self.court_case.case_title, new_case_title)

    def test_set_court_country(self):
        new_court_country = "CA"
        self.court_case.court_country = new_court_country
        self.assertEqual(self.court_case.court_country, new_court_country)

    def test_set_court_state(self):
        new_court_state = "CA"
        self.court_case.court_state = new_court_state
        self.assertEqual(self.court_case.court_state, new_court_state)

    def test_set_court_district(self):
        new_court_district = "CA Central District Court"
        self.court_case.court_district = new_court_district
        self.assertEqual(self.court_case.court_district, new_court_district)

    def test_set_court_type(self):
        new_court_type = "3"
        self.court_case.court_type = new_court_type
        self.assertEqual(self.court_case.court_type, new_court_type)
        with self.assertRaises(ValueError):
            self.court_case.court_type = "invalid"

    def test_set_case_type(self):
        new_case_type = "1"
        self.court_case.case_type = new_case_type
        self.assertEqual(self.court_case.case_type, new_case_type)
        with self.assertRaises(ValueError):
            self.court_case.case_type = "invalid"

    def test_set_defendant(self):
        new_defendant = ["New Defendant"]
        self.court_case.defendant = new_defendant
        self.assertEqual(self.court_case.defendant, new_defendant)

    def test_set_plaintiff(self):
        new_plaintiff = ["New Plaintiff"]
        self.court_case.plaintiff = new_plaintiff
        self.assertEqual(self.court_case.plaintiff, new_plaintiff)

    def test_set_comment(self):
        new_comment = "New comment for the case"
        self.court_case.comment = new_comment
        self.assertEqual(self.court_case.comment, new_comment)

    def test_set_invalid_type(self):
        with self.assertRaises(TypeError):
            self.court_case.case_number = 12345  # should be str

        with self.assertRaises(TypeError):
            self.court_case.case_title = 123  # should be str

        with self.assertRaises(TypeError):
            self.court_case.court_country = 123  # should be str

        with self.assertRaises(TypeError):
            self.court_case.court_state = 123  # should be str

        with self.assertRaises(TypeError):
            self.court_case.court_district = 123  # should be str

        with self.assertRaises(TypeError):
            self.court_case.court_type = 3  # should be str

        with self.assertRaises(TypeError):
            self.court_case.case_type = 1  # should be str

        with self.assertRaises(TypeError):
            self.court_case.defendant = "Invalid Defendant"  # should be list

        with self.assertRaises(TypeError):
            self.court_case.plaintiff = "Invalid Plaintiff"  # should be list

        with self.assertRaises(TypeError):
            self.court_case.comment = 123  # should be str

    def test_multiple_properties_integrity(self):
        charge2 = Charge(
            id=str(uuid.uuid4()),
            title="Test Charge 2",
            section="18:344",
            nature_of_offense="Bank Fraud",
            count=2,
            plea="2",
            plea_bargain=True,
            disposition="3"
        )
        sentence2 = Sentence(id=str(uuid.uuid4()), sentence_type="3")
        self.court_case.append_charge(self.charge)
        self.court_case.append_charge(charge2)
        self.court_case.append_sentence(self.sentence)
        self.court_case.append_sentence(sentence2)

        self.court_case.remove_charge(self.charge)
        self.assertNotIn(self.charge, self.court_case.charges)
        self.assertIn(charge2, self.court_case.charges)
        self.assertEqual(charge2.court_case, self.court_case)

        self.court_case.remove_sentence(self.sentence)
        self.assertNotIn(self.sentence, self.court_case.sentences)
        self.assertIn(sentence2, self.court_case.sentences)
        self.assertEqual(sentence2.court_case, self.court_case)

class TestCourtCaseSpecialCases(unittest.TestCase):
    def setUp(self):
        self.court_case = CourtCase(
            id=str(uuid.uuid4()),
            case_number="12345",
            case_title="USA v. LastName",
            court_country="US",
            court_state="CA",
            court_district="CA Central District Court",
            court_type="1",
            case_type="2",
            defendant=["Defendant One"],
            plaintiff=["Plaintiff One"],
            comment="This is a test comment."
        )
        self.charge = Charge(
            id=str(uuid.uuid4()),
            title="Test Charge",
            section="18:343",
            nature_of_offense="Wire Fraud",
            count=1,
            plea="1",
            plea_bargain=False,
            disposition="2"
        )
        self.sentence = Sentence(id=str(uuid.uuid4()), sentence_type="1")
        self.legal_response = LegalResponse(id=str(uuid.uuid4()))

if __name__ == '__main__':
    unittest.main()
