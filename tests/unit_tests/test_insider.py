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
from uuid import uuid4
sys.path.append(os.getcwd())
from pyiides import Insider, Incident, Sponsor, Job, Stressor, Accomplice

class TestInsiderInitialization(unittest.TestCase):
    def setUp(self):
        self.valid_incident_role = ["1", "2", "3", "4"]
        self.valid_motive = ["1", "2", "3", "4", "5", "6", "7", "8", "99"]
        self.valid_psych_issues = ["1", "2", "3", "4", "5", "99"]
        self.valid_predispositions = [
            ("1", "1.1"), ("2", "2.1"), ("3", "3.1"), ("4", "4.1")
        ]
        self.valid_concerning_behaviors = [
            ("3", "3.1"), ("3", "3.2"), ("3", "3.3"), ("3", "3.4")
        ]
        self.insider_data = {
            "id": str(uuid.uuid4()),
            "incident_role": "1",
            "motive": ["1"],
            "substance_use_during_incident": True,
            "psychological_issues": ["1"],
            "predispositions": [("1", "1.1"), ("2", "2.1")],
            "concerning_behaviors": [("3", "3.1"), ("3", "3.2")]
        }
        self.insider = Insider(**self.insider_data)

    def test_initialization(self):
        # Check all fields are set correctly upon initialization
        self.assertEqual(self.insider.id, self.insider_data['id'])
        self.assertEqual(self.insider.incident_role, self.insider_data['incident_role'])
        self.assertEqual(self.insider.motive, self.insider_data['motive'])
        self.assertEqual(self.insider.substance_use_during_incident, self.insider_data['substance_use_during_incident'])
        self.assertEqual(self.insider.psychological_issues, self.insider_data['psychological_issues'])
        self.assertEqual(self.insider.predispositions, self.insider_data['predispositions'])
        self.assertEqual(self.insider.concerning_behaviors, self.insider_data['concerning_behaviors'])

    def test_invalid_incident_role_vocabulary(self):
        for invalid_value in ["0", "invalid"]:
            with self.subTest(incident_role=invalid_value):
                self.insider_data['incident_role'] = invalid_value
                with self.assertRaises(ValueError):
                    Insider(**self.insider_data)

    def test_invalid_motive_vocabulary(self):
        for invalid_value in ["0", "invalid"]:
            with self.subTest(motive=invalid_value):
                self.insider_data['motive'] = [invalid_value]
                with self.assertRaises(ValueError):
                    Insider(**self.insider_data)

    def test_invalid_psychological_issues_vocabulary(self):
        for invalid_value in ["0", "invalid"]:
            with self.subTest(psychological_issues=invalid_value):
                self.insider_data['psychological_issues'] = [invalid_value]
                with self.assertRaises(ValueError):
                    Insider(**self.insider_data)

    def test_invalid_predispositions_vocabulary(self):
        for invalid_value in [("0", "0.0"), ("invalid", "invalid")]:
            with self.subTest(predispositions=invalid_value):
                self.insider_data['predispositions'] = [invalid_value]
                with self.assertRaises(ValueError):
                    Insider(**self.insider_data)

    def test_invalid_concerning_behaviors_vocabulary(self):
        for invalid_value in [("0", "0.0"), ("invalid", "invalid")]:
            with self.subTest(concerning_behaviors=invalid_value):
                self.insider_data['concerning_behaviors'] = [invalid_value]
                with self.assertRaises(ValueError):
                    Insider(**self.insider_data)

    def test_type_errors(self):
        # Check type errors on initialization
        invalid_data = {
            "id": 123,  # should be str
            "incident_role": 1,  # should be str
            "motive": "1",  # should be list
            "substance_use_during_incident": "True",  # should be bool
            "psychological_issues": "1",  # should be list
            "predispositions": "1",  # should be list of tuples
            "concerning_behaviors": "3.1"  # should be list of tuples
        }
        for key, value in invalid_data.items():
            with self.subTest(field=key):
                self.insider_data[key] = value
                with self.assertRaises(TypeError):
                    Insider(**self.insider_data)

class TestInsiderTypeChecking(unittest.TestCase):
    def setUp(self):
        self.insider = Insider(
            id=str(uuid.uuid4()),
            incident_role="1",
            motive=["1"],
            substance_use_during_incident=True,
            psychological_issues=["1"],
            predispositions=[("1", "1.1"), ("2", "2.1")],
            concerning_behaviors=[("3", "3.1"), ("3", "3.2")]
        )

    def test_set_id_type(self):
        with self.assertRaises(TypeError):
            self.insider.id = 123  # should be str

    def test_set_incident_role_type(self):
        with self.assertRaises(TypeError):
            self.insider.incident_role = 1  # should be str

    def test_set_motive_type(self):
        with self.assertRaises(TypeError):
            self.insider.motive = "1"  # should be list

    def test_set_substance_use_during_incident_type(self):
        with self.assertRaises(TypeError):
            self.insider.substance_use_during_incident = "True"  # should be bool

    def test_set_psychological_issues_type(self):
        with self.assertRaises(TypeError):
            self.insider.psychological_issues = "1"  # should be list

    def test_set_predispositions_type(self):
        with self.assertRaises(TypeError):
            self.insider.predispositions = "1"  # should be list of lists

    def test_set_concerning_behaviors_type(self):
        with self.assertRaises(TypeError):
            self.insider.concerning_behaviors = "3.1"  # should be list of lists

class TestInsiderVocabChecking(unittest.TestCase):
    def setUp(self):
        self.valid_incident_role = ["1", "2", "3", "4"]
        self.valid_motive = ["1", "2", "3", "4", "5", "6", "7", "8", "99"]
        self.valid_psych_issues = ["1", "2", "3", "4", "5", "99"]
        self.valid_predispositions = [
            ("1", "1.1"), ("2", "2.1"), ("3", "3.1"), ("4", "4.1")
        ]
        self.valid_concerning_behaviors = [
            ("3", "3.1"), ("3", "3.2"), ("3", "3.1"), ("3", "3.4")
        ]
        self.insider = Insider(
            id=str(uuid.uuid4()),
            incident_role="1",
            motive=["1"],
            substance_use_during_incident=True,
            psychological_issues=["1"],
            predispositions=[("1", "1.1"), ("2", "2.1")],
            concerning_behaviors=[("3", "3.1"), ("3", "3.2")]
        )

    def test_valid_incident_role_values(self):
        for incident_role in self.valid_incident_role:
            with self.subTest(incident_role=incident_role):
                self.insider.incident_role = incident_role
                self.assertEqual(self.insider.incident_role, incident_role)

    def test_invalid_incident_role_values(self):
        for invalid_value in ["0", "invalid"]:
            with self.subTest(incident_role=invalid_value):
                with self.assertRaises(ValueError):
                    self.insider.incident_role = invalid_value

    def test_valid_motive_values(self):
        for motive in self.valid_motive:
            with self.subTest(motive=motive):
                self.insider.motive = [motive]
                self.assertEqual(self.insider.motive, [motive])

    def test_invalid_motive_values(self):
        for invalid_value in ["0", "invalid"]:
            with self.subTest(motive=invalid_value):
                with self.assertRaises(ValueError):
                    self.insider.motive = [invalid_value]

    def test_valid_psychological_issues_values(self):
        for psychological_issues in self.valid_psych_issues:
            with self.subTest(psychological_issues=psychological_issues):
                self.insider.psychological_issues = [psychological_issues]
                self.assertEqual(self.insider.psychological_issues, [psychological_issues])

    def test_invalid_psychological_issues_values(self):
        for invalid_value in ["0", "invalid"]:
            with self.subTest(psychological_issues=invalid_value):
                with self.assertRaises(ValueError):
                    self.insider.psychological_issues = [invalid_value]

    def test_valid_predispositions_values(self):
        for predispositions in self.valid_predispositions:
            with self.subTest(predispositions=predispositions):
                self.insider.predispositions = [predispositions]
                self.assertEqual(self.insider.predispositions, [predispositions])

    def test_invalid_predispositions_values(self):
        for invalid_value in [("0", "0.0"), ("invalid", "invalid")]:
            with self.subTest(predispositions=invalid_value):
                with self.assertRaises(ValueError):
                    self.insider.predispositions = [invalid_value]

    def test_valid_concerning_behaviors_values(self):
        for concerning_behaviors in self.valid_concerning_behaviors:
            with self.subTest(concerning_behaviors=concerning_behaviors):
                self.insider.concerning_behaviors = [concerning_behaviors]
                self.assertEqual(self.insider.concerning_behaviors, [concerning_behaviors])

    def test_invalid_concerning_behaviors_values(self):
        for invalid_value in [("0", "0.0"), ("invalid", "invalid")]:
            with self.subTest(concerning_behaviors=invalid_value):
                with self.assertRaises(ValueError):
                    self.insider.concerning_behaviors = [invalid_value]

class TestInsiderRelationships(unittest.TestCase):

    def setUp(self):
        self.insider = Insider(
            id=str(uuid4()),
            incident_role="1",
            motive=["1"],
            substance_use_during_incident=True,
            psychological_issues=["1"],
            predispositions=[("1", "1.1")],
            concerning_behaviors=[("3", "3.1")]
        )

    def test_incident_relationship(self):
        incident = Incident()
        
        self.insider.incident = incident
        self.assertEqual(self.insider.incident, incident)
        self.assertIn(self.insider, incident.insiders)

        del self.insider.incident
        self.assertIsNone(self.insider.incident)
        self.assertNotIn(self.insider, incident.insiders)

    def test_sponsor_relationship(self):
        sponsor = Sponsor()
        
        self.insider.sponsor = sponsor
        self.assertEqual(self.insider.sponsor, sponsor)
        self.assertIn(self.insider, sponsor.insiders)

        del self.insider.sponsor
        self.assertIsNone(self.insider.sponsor)
        self.assertNotIn(self.insider, sponsor.insiders)

    def test_jobs_relationship(self):
        job1 = Job()
        job2 = Job()

        self.insider.jobs = [job1, job2]
        self.assertEqual(len(self.insider.jobs), 2)
        self.assertIn(job1, self.insider.jobs)
        self.assertIn(job2, self.insider.jobs)
        self.assertEqual(job1.insider, self.insider)
        self.assertEqual(job2.insider, self.insider)

        job3 = Job()
        self.insider.append_job(job3)
        self.assertEqual(len(self.insider.jobs), 3)
        self.assertIn(job3, self.insider.jobs)
        self.assertEqual(job3.insider, self.insider)

        self.insider.remove_job(job2)
        self.assertEqual(len(self.insider.jobs), 2)
        self.assertNotIn(job2, self.insider.jobs)
        self.assertIsNone(job2.insider)

        del self.insider.jobs
        self.assertIsNone(self.insider.jobs)
        self.assertIsNone(job1.insider)
        self.assertIsNone(job3.insider)

    def test_stressors_relationship(self):
        stressor1 = Stressor()
        stressor2 = Stressor()

        self.insider.stressors = [stressor1, stressor2]
        self.assertEqual(len(self.insider.stressors), 2)
        self.assertIn(stressor1, self.insider.stressors)
        self.assertIn(stressor2, self.insider.stressors)
        self.assertEqual(stressor1.insider, self.insider)
        self.assertEqual(stressor2.insider, self.insider)

        stressor3 = Stressor()
        self.insider.append_stressor(stressor3)
        self.assertEqual(len(self.insider.stressors), 3)
        self.assertIn(stressor3, self.insider.stressors)
        self.assertEqual(stressor3.insider, self.insider)

        self.insider.remove_stressor(stressor2)
        self.assertEqual(len(self.insider.stressors), 2)
        self.assertNotIn(stressor2, self.insider.stressors)
        self.assertIsNone(stressor2.insider)

        del self.insider.stressors
        self.assertIsNone(self.insider.stressors)
        self.assertIsNone(stressor1.insider)
        self.assertIsNone(stressor3.insider)

    def test_accomplices_relationship(self):
        accomplice1 = Accomplice(id=str(uuid4()), relationship_to_insider="1")
        accomplice2 = Accomplice(id=str(uuid4()), relationship_to_insider="2")

        self.insider.accomplices = [accomplice1, accomplice2]
        self.assertEqual(len(self.insider.accomplices), 2)
        self.assertIn(accomplice1, self.insider.accomplices)
        self.assertIn(accomplice2, self.insider.accomplices)
        self.assertEqual(accomplice1.insider, self.insider)
        self.assertEqual(accomplice2.insider, self.insider)

        accomplice3 = Accomplice(id=str(uuid4()), relationship_to_insider="3")
        self.insider.append_accomplice(accomplice3)
        self.assertEqual(len(self.insider.accomplices), 3)
        self.assertIn(accomplice3, self.insider.accomplices)
        self.assertEqual(accomplice3.insider, self.insider)

        self.insider.remove_accomplice(accomplice2)
        self.assertEqual(len(self.insider.accomplices), 2)
        self.assertNotIn(accomplice2, self.insider.accomplices)
        self.assertIsNone(accomplice2.insider)

        del self.insider.accomplices
        self.assertIsNone(self.insider.accomplices)
        self.assertIsNone(accomplice1.insider)
        self.assertIsNone(accomplice3.insider)

class TestInsiderSetting(unittest.TestCase):
    def setUp(self):
        self.insider = Insider(
            id=str(uuid.uuid4()),
            incident_role="1",
            motive=["1"],
            substance_use_during_incident=True,
            psychological_issues=["1"],
            predispositions=[("1", "1.1"), ("2", "2.1")],
            concerning_behaviors=[("3", "3.1"), ("3", "3.2")]
        )
        self.incident = Incident(id=str(uuid.uuid4()))

    def test_set_id(self):
        new_id = str(uuid.uuid4())
        self.insider.id = new_id
        self.assertEqual(self.insider.id, new_id)

    def test_set_incident_role(self):
        new_incident_role = "2"
        self.insider.incident_role = new_incident_role
        self.assertEqual(self.insider.incident_role, new_incident_role)

    def test_set_motive(self):
        new_motive = ["2"]
        self.insider.motive = new_motive
        self.assertEqual(self.insider.motive, new_motive)

    def test_set_substance_use_during_incident(self):
        new_substance_use_during_incident = False
        self.insider.substance_use_during_incident = new_substance_use_during_incident
        self.assertEqual(self.insider.substance_use_during_incident, new_substance_use_during_incident)

    def test_set_psychological_issues(self):
        new_psychological_issues = ["2"]
        self.insider.psychological_issues = new_psychological_issues
        self.assertEqual(self.insider.psychological_issues, new_psychological_issues)

    def test_set_predispositions(self):
        new_predispositions = [("3", "3.1")]
        self.insider.predispositions = new_predispositions
        self.assertEqual(self.insider.predispositions, new_predispositions)

    def test_set_concerning_behaviors(self):
        new_concerning_behaviors = [("3", "3.4")]
        self.insider.concerning_behaviors = new_concerning_behaviors
        self.assertEqual(self.insider.concerning_behaviors, new_concerning_behaviors)

if __name__ == '__main__':
    unittest.main()
