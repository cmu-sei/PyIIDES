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
sys.path.append(os.getcwd())
from pyiides import Charge, CourtCase

class TestChargeInitialization(unittest.TestCase):
    def setUp(self):
        self.valid_pleas = ["1", "2", "3", "4"]
        self.valid_dispositions = [str(i) for i in range(1, 12)]
        self.charge_data = {
            "id": str(uuid.uuid4()),
            "title": "Test Charge",
            "section": "18:343",
            "nature_of_offense": "Wire Fraud",
            "count": 1,
            "plea": "1",
            "plea_bargain": False,
            "disposition": "2"
        }
        self.charge = Charge(**self.charge_data)

    def test_initialization(self):
        # Check all fields are set correctly upon initialization
        self.assertEqual(self.charge.id, self.charge_data['id'])
        self.assertEqual(self.charge.title, self.charge_data['title'])
        self.assertEqual(self.charge.section, self.charge_data['section'])
        self.assertEqual(self.charge.nature_of_offense, self.charge_data['nature_of_offense'])
        self.assertEqual(self.charge.count, self.charge_data['count'])
        self.assertEqual(self.charge.plea, self.charge_data['plea'])
        self.assertEqual(self.charge.plea_bargain, self.charge_data['plea_bargain'])
        self.assertEqual(self.charge.disposition, self.charge_data['disposition'])

    def test_invalid_plea_vocabulary(self):
        for invalid_plea in ["0", "5", "invalid"]:
            with self.subTest(plea=invalid_plea):
                self.charge_data['plea'] = invalid_plea
                with self.assertRaises(ValueError):
                    Charge(**self.charge_data)

    def test_invalid_disposition_vocabulary(self):
        for invalid_disposition in ["0", "12", "invalid"]:
            with self.subTest(disposition=invalid_disposition):
                self.charge_data['disposition'] = invalid_disposition
                with self.assertRaises(ValueError):
                    Charge(**self.charge_data)

    def test_type_errors(self):
        # Check type errors on initialization
        invalid_data = {
            "id": 123,  # should be str
            "title": 123,  # should be str
            "section": 123,  # should be str
            "nature_of_offense": 123,  # should be str
            "count": "1",  # should be int
            "plea": 1,  # should be str
            "plea_bargain": "False",  # should be bool
            "disposition": 2  # should be str
        }
        for key, value in invalid_data.items():
            with self.subTest(field=key):
                self.charge_data[key] = value
                with self.assertRaises(TypeError):
                    Charge(**self.charge_data)


class TestChargeTypeChecking(unittest.TestCase):
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

    def test_set_id_type(self):
        with self.assertRaises(TypeError):
            self.charge.id = 123  # should be str

    def test_set_title_type(self):
        with self.assertRaises(TypeError):
            self.charge.title = 123  # should be str

    def test_set_section_type(self):
        with self.assertRaises(TypeError):
            self.charge.section = 123  # should be str

    def test_set_nature_of_offense_type(self):
        with self.assertRaises(TypeError):
            self.charge.nature_of_offense = 123  # should be str

    def test_set_count_type(self):
        with self.assertRaises(TypeError):
            self.charge.count = "1"  # should be int

    def test_set_plea_type(self):
        with self.assertRaises(TypeError):
            self.charge.plea = 1  # should be str

    def test_set_plea_bargain_type(self):
        with self.assertRaises(TypeError):
            self.charge.plea_bargain = "False"  # should be bool

    def test_set_disposition_type(self):
        with self.assertRaises(TypeError):
            self.charge.disposition = 2  # should be str


class TestChargeVocabChecking(unittest.TestCase):
    def setUp(self):
        self.valid_pleas = ["1", "2", "3", "4"]
        self.valid_dispositions = [str(i) for i in range(1, 12)]
        self.charge_data = {
            "id": str(uuid.uuid4()),
            "title": "Test Charge",
            "section": "18:343",
            "nature_of_offense": "Wire Fraud",
            "count": 1,
            "plea": "1",
            "plea_bargain": False,
            "disposition": "2"
        }
        self.charge = Charge(**self.charge_data)

    def test_valid_plea_values(self):
        for plea in self.valid_pleas:
            with self.subTest(plea=plea):
                self.charge.plea = plea
                self.assertEqual(self.charge.plea, plea)

    def test_invalid_plea_values(self):
        for invalid_plea in ["0", "5", "invalid"]:
            with self.subTest(plea=invalid_plea):
                with self.assertRaises(ValueError):
                    self.charge.plea = invalid_plea

    def test_valid_disposition_values(self):
        for disposition in self.valid_dispositions:
            with self.subTest(disposition=disposition):
                self.charge.disposition = disposition
                self.assertEqual(self.charge.disposition, disposition)

    def test_invalid_disposition_values(self):
        for invalid_disposition in ["0", "12", "invalid"]:
            with self.subTest(disposition=invalid_disposition):
                with self.assertRaises(ValueError):
                    self.charge.disposition = invalid_disposition


class TestChargeRelationships(unittest.TestCase):
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
        self.court_case = CourtCase(id=str(uuid.uuid4()))

    def test_add_charge_to_court_case(self):
        self.court_case.append_charge(self.charge)
        self.assertIn(self.charge, self.court_case.charges)
        self.assertEqual(self.charge.court_case, self.court_case)

    def test_remove_charge_from_court_case(self):
        self.court_case.append_charge(self.charge)
        self.court_case.remove_charge(self.charge)
        self.assertNotIn(self.charge, self.court_case.charges)
        self.assertIsNone(self.charge.court_case)
    # TODO: RELATIONSHIP CHECKS ON INIT and TYPE CHECK RELATIONSHIPS ADDITIONS ON INIT, SET, APPEND
    def test_set_court_case(self):
        self.charge.court_case = self.court_case
        self.assertIn(self.charge, self.court_case.charges)
        self.assertEqual(self.court_case, self.charge.court_case)

        new_court_case = CourtCase()
        self.charge.court_case = new_court_case
        self.assertIn(self.charge, new_court_case.charges)
        self.assertEqual(new_court_case, self.charge.court_case)

        self.assertNotIn(self.charge, self.court_case.charges)
        self.assertNotEqual(self.court_case, self.charge.court_case)


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

class TestChargeSetters(unittest.TestCase):
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

    def test_set_id(self):
        new_id = str(uuid.uuid4())
        self.charge.id = new_id
        self.assertEqual(self.charge.id, new_id)
        with self.assertRaises(TypeError):
            self.charge.id = 123  # should be str

    def test_set_title(self):
        new_title = "Updated Charge"
        self.charge.title = new_title
        self.assertEqual(self.charge.title, new_title)
        with self.assertRaises(TypeError):
            self.charge.title = 123  # should be str

    def test_set_section(self):
        new_section = "18:344"
        self.charge.section = new_section
        self.assertEqual(self.charge.section, new_section)
        with self.assertRaises(TypeError):
            self.charge.section = 123  # should be str

    def test_set_nature_of_offense(self):
        new_nature_of_offense = "Bank Fraud"
        self.charge.nature_of_offense = new_nature_of_offense
        self.assertEqual(self.charge.nature_of_offense, new_nature_of_offense)
        with self.assertRaises(TypeError):
            self.charge.nature_of_offense = 123  # should be str

    def test_set_count(self):
        new_count = 3
        self.charge.count = new_count
        self.assertEqual(self.charge.count, new_count)
        with self.assertRaises(TypeError):
            self.charge.count = "1"  # should be int

    def test_set_plea(self):
        new_plea = "2"
        self.charge.plea = new_plea
        self.assertEqual(self.charge.plea, new_plea)
        with self.assertRaises(TypeError):
            self.charge.plea = 1  # should be str
        with self.assertRaises(ValueError):
            self.charge.plea = "invalid"  # should raise ValueError for invalid vocab

    def test_set_plea_bargain(self):
        new_plea_bargain = True
        self.charge.plea_bargain = new_plea_bargain
        self.assertEqual(self.charge.plea_bargain, new_plea_bargain)
        with self.assertRaises(TypeError):
            self.charge.plea_bargain = "False"  # should be bool

    def test_set_disposition(self):
        new_disposition = "3"
        self.charge.disposition = new_disposition
        self.assertEqual(self.charge.disposition, new_disposition)
        with self.assertRaises(TypeError):
            self.charge.disposition = 2  # should be str
        with self.assertRaises(ValueError):
            self.charge.disposition = "invalid"  # should raise ValueError for invalid vocab
