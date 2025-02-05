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
from datetime import datetime, timedelta
sys.path.append(os.getcwd())
from pyiides import Job, Insider, Organization # Adjust the import path as necessary

class TestJobInitialization(unittest.TestCase):
    def setUp(self):
        self.valid_job_function = [
            "11", "13", "15", "17", "19", "21", "22", "23", "25", "27",
            "29", "31", "33", "35", "37", "39", "41", "43", "45", "47",
            "49", "51", "53", "55", "99"
        ]
        self.valid_occupation = [
            "11.1", "11.2", "11.3", "11.9", "13.1", "13.2", "15.1", "15.2",
            "17.1", "17.2", "17.3", "19.1", "19.2", "19.3", "19.4", "19.5",
            "21.1", "21.2", "23.1", "23.2", "25.2", "25.3", "25.4", "25.9",
            "27.1", "27.2", "27.3", "27.4", "29.1", "29.2", "29.9", "31.1",
            "31.2", "31.9", "33.1", "33.2", "33.3", "33.9", "35.1", "35.2",
            "35.3", "35.9", "37.1", "37.2", "37.3", "39.1", "39.2", "39.3",
            "39.4", "39.5", "39.6", "39.7", "39.9", "41.1", "41.2", "41.3",
            "41.4", "41.9", "43.1", "43.2", "43.3", "43.4", "43.5", "43.6",
            "43.9", "45.1", "45.2", "45.3", "45.4", "47.1", "47.2", "47.3",
            "47.4", "47.5", "49.1", "49.2", "49.3", "49.9", "51.1", "51.2",
            "51.3", "51.4", "51.5", "51.6", "51.7", "51.8", "51.9", "53.1",
            "53.2", "53.3", "53.4", "53.5", "53.6", "53.7", "55.1", "55.2",
            "55.3", "99.1", "99.9"
        ]
        self.valid_access_authorization = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.valid_employment_type = ["CTR", "FLT", "PRT", "INT", "TMP", "VOL", "OTH"]
        
        self.job_data = {
            "id": str(uuid.uuid4()),
            "job_function": "15",
            "occupation": "15.1",
            "title": "Software Developer",
            "position_technical": True,
            "access_authorization": "3",
            "employment_type": "FLT",
            "hire_date": datetime(2020, 1, 1),
            "departure_date": datetime(2022, 1, 1),
            "tenure": timedelta(731),
            "comment": "This is a test job."
        }
        self.job = Job(**self.job_data)

    def test_initialization(self):
        # Check all fields are set correctly upon initialization
        self.assertEqual(self.job.id, self.job_data['id'])
        self.assertEqual(self.job.job_function, self.job_data['job_function'])
        self.assertEqual(self.job.occupation, self.job_data['occupation'])
        self.assertEqual(self.job.title, self.job_data['title'])
        self.assertEqual(self.job.position_technical, self.job_data['position_technical'])
        self.assertEqual(self.job.access_authorization, self.job_data['access_authorization'])
        self.assertEqual(self.job.employment_type, self.job_data['employment_type'])
        self.assertEqual(self.job.hire_date, self.job_data['hire_date'])
        self.assertEqual(self.job.departure_date, self.job_data['departure_date'])
        self.assertEqual(self.job.tenure, self.job_data['tenure'])
        self.assertEqual(self.job.comment, self.job_data['comment'])

    def test_invalid_job_function_vocabulary(self):
        for invalid_value in ["100", "invalid"]:
            with self.subTest(job_function=invalid_value):
                self.job_data['job_function'] = invalid_value
                with self.assertRaises(ValueError):
                    Job(**self.job_data)

    def test_invalid_occupation_vocabulary(self):
        for invalid_value in ["100.1", "invalid"]:
            with self.subTest(occupation=invalid_value):
                self.job_data['occupation'] = invalid_value
                with self.assertRaises(ValueError):
                    Job(**self.job_data)

    def test_invalid_access_authorization_vocabulary(self):
        for invalid_value in ["10", "invalid"]:
            with self.subTest(access_authorization=invalid_value):
                self.job_data['access_authorization'] = invalid_value
                with self.assertRaises(ValueError):
                    Job(**self.job_data)

    def test_invalid_employment_type_vocabulary(self):
        for invalid_value in ["XYZ", "invalid"]:
            with self.subTest(employment_type=invalid_value):
                self.job_data['employment_type'] = invalid_value
                with self.assertRaises(ValueError):
                    Job(**self.job_data)

    def test_type_errors(self):
        # Check type errors on initialization
        invalid_data = {
            "id": 123,  # should be str
            "job_function": 15,  # should be str
            "occupation": 15.1,  # should be str
            "title": 123,  # should be str
            "position_technical": "True",  # should be bool
            "access_authorization": 3,  # should be str
            "employment_type": 123,  # should be str
            "hire_date": "2020-01-01",  # should be datetime
            "departure_date": "2022-01-01",  # should be datetime
            "tenure": 123,  # should be timedelta (ISO 8601 duration)
            "comment": 123  # should be str
        }
        for key, value in invalid_data.items():
            with self.subTest(field=key):
                self.job_data[key] = value
                with self.assertRaises(TypeError):
                    Job(**self.job_data)

class TestJobTypeChecking(unittest.TestCase):
    def setUp(self):
        self.job = Job(
            id=str(uuid.uuid4()),
            job_function="15",
            occupation="15.1",
            title="Software Developer",
            position_technical=True,
            access_authorization="3",
            employment_type="FLT",
            hire_date=datetime(2020, 1, 1),
            departure_date=datetime(2022, 1, 1),
            tenure=timedelta(days=731),  # 2 years
            comment="This is a test job."
        )

    def test_set_id_type(self):
        with self.assertRaises(TypeError):
            self.job.id = 123  # should be str

    def test_set_job_function_type(self):
        with self.assertRaises(TypeError):
            self.job.job_function = 15  # should be str

    def test_set_occupation_type(self):
        with self.assertRaises(TypeError):
            self.job.occupation = 15.1  # should be str

    def test_set_title_type(self):
        with self.assertRaises(TypeError):
            self.job.title = 123  # should be str

    def test_set_position_technical_type(self):
        with self.assertRaises(TypeError):
            self.job.position_technical = "True"  # should be bool

    def test_set_access_authorization_type(self):
        with self.assertRaises(TypeError):
            self.job.access_authorization = 3  # should be str

    def test_set_employment_type_type(self):
        with self.assertRaises(TypeError):
            self.job.employment_type = 123  # should be str

    def test_set_hire_date_type(self):
        with self.assertRaises(TypeError):
            self.job.hire_date = "2020-01-01"  # should be datetime

    def test_set_departure_date_type(self):
        with self.assertRaises(TypeError):
            self.job.departure_date = "2022-01-01"  # should be datetime

    def test_set_tenure_type(self):
        with self.assertRaises(TypeError):
            self.job.tenure = "P2Y"  # should be timedelta

    def test_set_comment_type(self):
        with self.assertRaises(TypeError):
            self.job.comment = 123  # should be str

class TestJobVocabChecking(unittest.TestCase):
    def setUp(self):
        self.valid_job_function = [
            "11", "13", "15", "17", "19", "21", "22", "23", "25", "27",
            "29", "31", "33", "35", "37", "39", "41", "43", "45", "47",
            "49", "51", "53", "55", "99"
        ]
        self.valid_occupation = [
            "11.1", "11.2", "11.3", "11.9", "13.1", "13.2", "15.1", "15.2",
            "17.1", "17.2", "17.3", "19.1", "19.2", "19.3", "19.4", "19.5",
            "21.1", "21.2", "23.1", "23.2", "25.2", "25.3", "25.4", "25.9",
            "27.1", "27.2", "27.3", "27.4", "29.1", "29.2", "29.9", "31.1",
            "31.2", "31.9", "33.1", "33.2", "33.3", "33.9", "35.1", "35.2",
            "35.3", "35.9", "37.1", "37.2", "37.3", "39.1", "39.2", "39.3",
            "39.4", "39.5", "39.6", "39.7", "39.9", "41.1", "41.2", "41.3",
            "41.4", "41.9", "43.1", "43.2", "43.3", "43.4", "43.5", "43.6",
            "43.9", "45.1", "45.2", "45.3", "45.4", "47.1", "47.2", "47.3",
            "47.4", "47.5", "49.1", "49.2", "49.3", "49.9", "51.1", "51.2",
            "51.3", "51.4", "51.5", "51.6", "51.7", "51.8", "51.9", "53.1",
            "53.2", "53.3", "53.4", "53.5", "53.6", "53.7", "55.1", "55.2",
            "55.3", "99.1", "99.9"
        ]
        self.valid_access_authorization = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.valid_employment_type = ["CTR", "FLT", "PRT", "INT", "TMP", "VOL", "OTH"]
        
        self.job = Job(
            id=str(uuid.uuid4()),
            job_function="15",
            occupation="15.1",
            title="Software Developer",
            position_technical=True,
            access_authorization="3",
            employment_type="FLT",
            hire_date=datetime(2020, 1, 1),
            departure_date=datetime(2022, 1, 1),
            tenure=timedelta(days=731),  # 2 years
            comment="This is a test job."
        )

class TestJobRelationships(unittest.TestCase):
    def setUp(self):
        self.job = Job(
            id=str(uuid.uuid4()),
            job_function="15",
            occupation="15.1",
            title="Software Developer",
            position_technical=True,
            access_authorization="3",
            employment_type="FLT",
            hire_date=datetime(2020, 1, 1),
            departure_date=datetime(2022, 1, 1),
            tenure=timedelta(days=731),  # 2 years including the end date
            comment="This is a test job."
        )
        self.insider = Insider(id=str(uuid.uuid4()), incident_role="1")
        self.organization = Organization(id=str(uuid.uuid4()))

    def test_set_insider_to_job(self):
        self.job.insider = self.insider
        self.assertEqual(self.job.insider, self.insider)
        self.assertIn(self.job, self.insider.jobs)

    def test_remove_job_from_insider(self):
        self.job.insider = self.insider
        self.insider.remove_job(self.job)
        self.assertIsNone(self.job.insider)
        self.assertNotIn(self.job, self.insider.jobs)

    def test_set_organization_to_job(self):
        self.job.organization = self.organization
        self.assertEqual(self.job.organization, self.organization)
        self.assertIn(self.job, self.organization.jobs)

    def test_remove_job_from_organization(self):
        self.job.organization = self.organization
        self.organization.remove_job(self.job)
        self.assertIsNone(self.job.organization)
        self.assertNotIn(self.job, self.organization.jobs)
    
    def test_set(self):
        o1 = Organization()
        o2 = Organization()
        
        self.job.organization = o1 
        self.assertIn(self.job, o1.jobs)
        self.assertEqual(self.job.organization, o1)

        self.job.organization = o2 
        self.assertNotIn(self.job, o1.jobs)

        self.assertIn(self.job, o2.jobs)
        self.assertEqual(self.job.organization, o2)

class TestJobSetting(unittest.TestCase):
    def setUp(self):
        self.job = Job(
            id=str(uuid.uuid4()),
            job_function="15",
            occupation="15.1",
            title="Software Developer",
            position_technical=True,
            access_authorization="3",
            employment_type="FLT",
            hire_date=datetime(2020, 1, 1),
            departure_date=datetime(2022, 1, 1),
            tenure=timedelta(days=731),  # 2 years including the end date
            comment="This is a test job."
        )

    def test_set_id(self):
        new_id = str(uuid.uuid4())
        self.job.id = new_id
        self.assertEqual(self.job.id, new_id)

    def test_set_job_function(self):
        new_job_function = "17"
        self.job.job_function = new_job_function
        self.assertEqual(self.job.job_function, new_job_function)

    def test_set_occupation(self):
        new_occupation = "17.1"
        self.job.occupation = new_occupation
        self.assertEqual(self.job.occupation, new_occupation)

    def test_set_title(self):
        new_title = "Senior Software Developer"
        self.job.title = new_title
        self.assertEqual(self.job.title, new_title)

    def test_set_position_technical(self):
        new_position_technical = False
        self.job.position_technical = new_position_technical
        self.assertEqual(self.job.position_technical, new_position_technical)

    def test_set_access_authorization(self):
        new_access_authorization = "5"
        self.job.access_authorization = new_access_authorization
        self.assertEqual(self.job.access_authorization, new_access_authorization)

    def test_set_employment_type(self):
        new_employment_type = "PRT"
        self.job.employment_type = new_employment_type
        self.assertEqual(self.job.employment_type, new_employment_type)

    def test_set_hire_date(self):
        new_hire_date = datetime(2019, 1, 1)
        self.job.hire_date = new_hire_date
        self.assertEqual(self.job.hire_date, new_hire_date)

    def test_set_departure_date(self):
        new_departure_date = datetime(2021, 1, 1)
        self.job.departure_date = new_departure_date
        self.assertEqual(self.job.departure_date, new_departure_date)

    def test_set_comment(self):
        new_comment = "Updated comment for the job."
        self.job.comment = new_comment
        self.assertEqual(self.job.comment, new_comment)


if __name__ == '__main__':
    unittest.main()
