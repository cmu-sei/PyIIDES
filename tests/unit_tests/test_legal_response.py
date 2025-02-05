"""
License:
PyIIDES
Copyright 2024 Carnegie Mellon University.
NO WARRANTY. THIS CARNEGIE MELLON UNIVERSITY AND SOFTWARE ENGINEERING INSTITUTE MATERIAL IS FURNISHED ON AN "AS-IS" BASIS. CARNEGIE MELLON UNIVERSITY MAKES NO WARRANTIES OF ANY KIND, EITHER EXPRESSED OR IMPLIED, AS TO ANY MATTER INCLUDING, BUT NOT LIMITED TO, WARRANTY OF FITNESS FOR PURPOSE OR MERCHANTABILITY, EXCLUSIVITY, OR RESULTS OBTAINED FROM USE OF THE MATERIAL. CARNEGIE MELLON UNIVERSITY DOES NOT MAKE ANY WARRANTY OF ANY KIND WITH RESPECT TO FREEDOM FROM PATENT, TRADEMARK, OR COPYRIGHT INFRINGEMENT.
Licensed under a MIT (SEI)-style license, please see license.txt or contact permission@sei.cmu.edu for full terms.
[DISTRIBUTION STATEMENT A] This material has been approved for public release and unlimited distribution.  Please see Copyright notice for non-US Government use and distribution.
DM24-1597
"""
import unittest, sys, os
import uuid
from datetime import datetime
sys.path.append(os.getcwd())
from pyiides import LegalResponse, CourtCase, Sentence  # Adjust the import path as necessary

class TestLegalResponseInitialization(unittest.TestCase):
    def setUp(self):
        self.legal_response_data = {
            "id": str(uuid.uuid4()),
            "law_enforcement_contacted": datetime(2020, 1, 1),
            "insider_arrested": datetime(2020, 1, 2),
            "insider_charged": datetime(2020, 1, 3),
            "insider_pleads": datetime(2020, 1, 4),
            "insider_judgment": datetime(2020, 1, 5),
            "insider_sentenced": datetime(2020, 1, 6),
            "insider_charges_dropped": datetime(2020, 1, 7),
            "insider_charges_dismissed": datetime(2020, 1, 8),
            "insider_settled": datetime(2020, 1, 9),
            "comment": "This is a test legal response."
        }
        self.legal_response = LegalResponse(**self.legal_response_data)

    def test_initialization(self):
        # Check all fields are set correctly upon initialization
        self.assertEqual(self.legal_response.id, self.legal_response_data['id'])
        self.assertEqual(self.legal_response.law_enforcement_contacted, self.legal_response_data['law_enforcement_contacted'])
        self.assertEqual(self.legal_response.insider_arrested, self.legal_response_data['insider_arrested'])
        self.assertEqual(self.legal_response.insider_charged, self.legal_response_data['insider_charged'])
        self.assertEqual(self.legal_response.insider_pleads, self.legal_response_data['insider_pleads'])
        self.assertEqual(self.legal_response.insider_judgment, self.legal_response_data['insider_judgment'])
        self.assertEqual(self.legal_response.insider_sentenced, self.legal_response_data['insider_sentenced'])
        self.assertEqual(self.legal_response.insider_charges_dropped, self.legal_response_data['insider_charges_dropped'])
        self.assertEqual(self.legal_response.insider_charges_dismissed, self.legal_response_data['insider_charges_dismissed'])
        self.assertEqual(self.legal_response.insider_settled, self.legal_response_data['insider_settled'])
        self.assertEqual(self.legal_response.comment, self.legal_response_data['comment'])

    def test_type_errors(self):
        # Check type errors on initialization
        invalid_data = {
            "id": 123,  # should be str
            "law_enforcement_contacted": "2020-01-01",  # should be datetime
            "insider_arrested": "2020-01-02",  # should be datetime
            "insider_charged": "2020-01-03",  # should be datetime
            "insider_pleads": "2020-01-04",  # should be datetime
            "insider_judgment": "2020-01-05",  # should be datetime
            "insider_sentenced": "2020-01-06",  # should be datetime
            "insider_charges_dropped": "2020-01-07",  # should be datetime
            "insider_charges_dismissed": "2020-01-08",  # should be datetime
            "insider_settled": "2020-01-09",  # should be datetime
            "comment": 123  # should be str
        }
        for key, value in invalid_data.items():
            with self.subTest(field=key):
                self.legal_response_data[key] = value
                with self.assertRaises(TypeError):
                    LegalResponse(**self.legal_response_data)

class TestLegalResponseTypeChecking(unittest.TestCase):
    def setUp(self):
        self.legal_response = LegalResponse(
            id=str(uuid.uuid4()),
            law_enforcement_contacted=datetime(2020, 1, 1),
            insider_arrested=datetime(2020, 1, 2),
            insider_charged=datetime(2020, 1, 3),
            insider_pleads=datetime(2020, 1, 4),
            insider_judgment=datetime(2020, 1, 5),
            insider_sentenced=datetime(2020, 1, 6),
            insider_charges_dropped=datetime(2020, 1, 7),
            insider_charges_dismissed=datetime(2020, 1, 8),
            insider_settled=datetime(2020, 1, 9),
            comment="This is a test legal response."
        )

    def test_set_id_type(self):
        with self.assertRaises(TypeError):
            self.legal_response.id = 123  # should be str

    def test_set_law_enforcement_contacted_type(self):
        with self.assertRaises(TypeError):
            self.legal_response.law_enforcement_contacted = "2020-01-01"  # should be datetime

    def test_set_insider_arrested_type(self):
        with self.assertRaises(TypeError):
            self.legal_response.insider_arrested = "2020-01-02"  # should be datetime

    def test_set_insider_charged_type(self):
        with self.assertRaises(TypeError):
            self.legal_response.insider_charged = "2020-01-03"  # should be datetime

    def test_set_insider_pleads_type(self):
        with self.assertRaises(TypeError):
            self.legal_response.insider_pleads = "2020-01-04"  # should be datetime

    def test_set_insider_judgment_type(self):
        with self.assertRaises(TypeError):
            self.legal_response.insider_judgment = "2020-01-05"  # should be datetime

    def test_set_insider_sentenced_type(self):
        with self.assertRaises(TypeError):
            self.legal_response.insider_sentenced = "2020-01-06"  # should be datetime

    def test_set_insider_charges_dropped_type(self):
        with self.assertRaises(TypeError):
            self.legal_response.insider_charges_dropped = "2020-01-07"  # should be datetime

    def test_set_insider_charges_dismissed_type(self):
        with self.assertRaises(TypeError):
            self.legal_response.insider_charges_dismissed = "2020-01-08"  # should be datetime

    def test_set_insider_settled_type(self):
        with self.assertRaises(TypeError):
            self.legal_response.insider_settled = "2020-01-09"  # should be datetime

    def test_set_comment_type(self):
        with self.assertRaises(TypeError):
            self.legal_response.comment = 123  # should be str

class TestLegalResponseRelationships(unittest.TestCase):
    def setUp(self):
        self.legal_response = LegalResponse(
            id=str(uuid.uuid4()),
            law_enforcement_contacted=datetime(2020, 1, 1),
            insider_arrested=datetime(2020, 1, 2),
            insider_charged=datetime(2020, 1, 3),
            insider_pleads=datetime(2020, 1, 4),
            insider_judgment=datetime(2020, 1, 5),
            insider_sentenced=datetime(2020, 1, 6),
            insider_charges_dropped=datetime(2020, 1, 7),
            insider_charges_dismissed=datetime(2020, 1, 8),
            insider_settled=datetime(2020, 1, 9),
            comment="This is a test legal response."
        )
        self.court_case1 = CourtCase(id=str(uuid.uuid4()))
        self.court_case2 = CourtCase(id=str(uuid.uuid4()))

    def test_append_court_case_to_legal_response(self):
        self.legal_response.append_court_case(self.court_case1)
        self.assertIn(self.court_case1, self.legal_response.court_cases)
        self.assertEqual(self.court_case1.legal_response, self.legal_response)

    def test_remove_court_case_from_legal_response(self):
        self.legal_response.append_court_case(self.court_case1)
        self.legal_response.remove_court_case(self.court_case1)
        self.assertNotIn(self.court_case1, self.legal_response.court_cases)
        self.assertIsNone(self.court_case1.legal_response)

    def test_append_multiple_court_cases(self):
        self.legal_response.append_court_case(self.court_case1)
        self.legal_response.append_court_case(self.court_case2)
        self.assertIn(self.court_case1, self.legal_response.court_cases)
        self.assertIn(self.court_case2, self.legal_response.court_cases)
        self.assertEqual(self.court_case1.legal_response, self.legal_response)
        self.assertEqual(self.court_case2.legal_response, self.legal_response)

    def test_remove_one_of_multiple_court_cases(self):
        self.legal_response.append_court_case(self.court_case1)
        self.legal_response.append_court_case(self.court_case2)
        self.legal_response.remove_court_case(self.court_case1)
        self.assertNotIn(self.court_case1, self.legal_response.court_cases)
        self.assertIn(self.court_case2, self.legal_response.court_cases)
        self.assertIsNone(self.court_case1.legal_response)
        self.assertEqual(self.court_case2.legal_response, self.legal_response)
    
    def test_set_court_case(self):
        cc1 = CourtCase()
        cc2 = CourtCase()
        cc3 = CourtCase()
        cc4 = CourtCase()

        self.legal_response.court_cases = [cc1, cc2]
        self.assertIn(cc1, self.legal_response.court_cases)
        self.assertIn(cc2, self.legal_response.court_cases)
        self.assertEqual(cc1.legal_response, self.legal_response)
        self.assertEqual(cc2.legal_response, self.legal_response)

        self.legal_response.court_cases = [cc3, cc4]
        self.assertIsNone(cc1.legal_response)
        self.assertIsNone(cc2.legal_response)
        self.assertNotIn(cc1, self.legal_response.court_cases)
        self.assertNotIn(cc2, self.legal_response.court_cases)

        self.assertIn(cc3, self.legal_response.court_cases)
        self.assertIn(cc4, self.legal_response.court_cases)
        self.assertEqual(cc3.legal_response, self.legal_response)
        self.assertEqual(cc4.legal_response, self.legal_response)

class TestLegalResponseSetting(unittest.TestCase):
    def setUp(self):
        self.legal_response = LegalResponse(
            id=str(uuid.uuid4()),
            law_enforcement_contacted=datetime(2020, 1, 1),
            insider_arrested=datetime(2020, 1, 2),
            insider_charged=datetime(2020, 1, 3),
            insider_pleads=datetime(2020, 1, 4),
            insider_judgment=datetime(2020, 1, 5),
            insider_sentenced=datetime(2020, 1, 6),
            insider_charges_dropped=datetime(2020, 1, 7),
            insider_charges_dismissed=datetime(2020, 1, 8),
            insider_settled=datetime(2020, 1, 9),
            comment="This is a test legal response."
        )

    def test_set_id(self):
        new_id = str(uuid.uuid4())
        self.legal_response.id = new_id
        self.assertEqual(self.legal_response.id, new_id)

    def test_set_law_enforcement_contacted(self):
        new_date = datetime(2021, 1, 1)
        self.legal_response.law_enforcement_contacted = new_date
        self.assertEqual(self.legal_response.law_enforcement_contacted, new_date)

    def test_set_insider_arrested(self):
        new_date = datetime(2021, 1, 2)
        self.legal_response.insider_arrested = new_date
        self.assertEqual(self.legal_response.insider_arrested, new_date)

    def test_set_insider_charged(self):
        new_date = datetime(2021, 1, 3)
        self.legal_response.insider_charged = new_date
        self.assertEqual(self.legal_response.insider_charged, new_date)

    def test_set_insider_pleads(self):
        new_date = datetime(2021, 1, 4)
        self.legal_response.insider_pleads = new_date
        self.assertEqual(self.legal_response.insider_pleads, new_date)

    def test_set_insider_judgment(self):
        new_date = datetime(2021, 1, 5)
        self.legal_response.insider_judgment = new_date
        self.assertEqual(self.legal_response.insider_judgment, new_date)

    def test_set_insider_sentenced(self):
        new_date = datetime(2021, 1, 6)
        self.legal_response.insider_sentenced = new_date
        self.assertEqual(self.legal_response.insider_sentenced, new_date)

    def test_set_insider_charges_dropped(self):
        new_date = datetime(2021, 1, 7)
        self.legal_response.insider_charges_dropped = new_date
        self.assertEqual(self.legal_response.insider_charges_dropped, new_date)

    def test_set_insider_charges_dismissed(self):
        new_date = datetime(2021, 1, 8)
        self.legal_response.insider_charges_dismissed = new_date
        self.assertEqual(self.legal_response.insider_charges_dismissed, new_date)

    def test_set_insider_settled(self):
        new_date = datetime(2021, 1, 9)
        self.legal_response.insider_settled = new_date
        self.assertEqual(self.legal_response.insider_settled, new_date)

    def test_set_comment(self):
        new_comment = "Updated comment for the legal response."
        self.legal_response.comment = new_comment
        self.assertEqual(self.legal_response.comment, new_comment)

        
if __name__ == '__main__':
    unittest.main()