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
from pyiides import Impact, Incident  # Adjust the import path as necessary

class TestImpactInitialization(unittest.TestCase):
    def setUp(self):
        self.valid_metrics = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"]
        self.impact_data = {
            "id":  str(uuid.uuid4()),
            "high": 1000.0,
            "low": 500.0,
            "metric": "5",
            "estimated": True,
            "comment": "This is a test comment."
        }
        self.impact = Impact(**self.impact_data)

    def test_initialization(self):
        # Check all fields are set correctly upon initialization
        self.assertEqual(self.impact.id, self.impact_data['id'])
        self.assertEqual(self.impact.high, self.impact_data['high'])
        self.assertEqual(self.impact.low, self.impact_data['low'])
        self.assertEqual(self.impact.metric, self.impact_data['metric'])
        self.assertEqual(self.impact.estimated, self.impact_data['estimated'])
        self.assertEqual(self.impact.comment, self.impact_data['comment'])

    def test_invalid_metric_vocabulary(self):
        for invalid_value in ["0", "17", "invalid"]:
            with self.subTest(metric=invalid_value):
                self.impact_data['metric'] = invalid_value
                with self.assertRaises(ValueError):
                    Impact(**self.impact_data)

    def test_type_errors(self):
        # Check type errors on initialization
        invalid_data = {
            "id": 123,  # should be str
            "high": "1000.0",  # should be number
            "low": "500.0",  # should be number
            "metric": 5,  # should be str
            "estimated": "True",  # should be bool
            "comment": 123  # should be str
        }
        for key, value in invalid_data.items():
            with self.subTest(field=key):
                self.impact_data[key] = value
                with self.assertRaises(TypeError):
                    Impact(**self.impact_data)

class TestImpactTypeChecking(unittest.TestCase):
    def setUp(self):
        self.impact = Impact(
            id= str(uuid.uuid4()),
            high=1000.0,
            low=500.0,
            metric="5",
            estimated=True,
            comment="This is a test comment."
        )

    def test_set_id_type(self):
        with self.assertRaises(TypeError):
            self.impact.id = 123  # should be str

    def test_set_high_type(self):
        with self.assertRaises(TypeError):
            self.impact.high = "1000.0"  # should be number

    def test_set_low_type(self):
        with self.assertRaises(TypeError):
            self.impact.low = "500.0"  # should be number

    def test_set_metric_type(self):
        with self.assertRaises(TypeError):
            self.impact.metric = 5  # should be str

    def test_set_estimated_type(self):
        with self.assertRaises(TypeError):
            self.impact.estimated = "True"  # should be bool

    def test_set_comment_type(self):
        with self.assertRaises(TypeError):
            self.impact.comment = 123  # should be str

class TestImpactVocabChecking(unittest.TestCase):
    def setUp(self):
        self.valid_metrics = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"]
        self.impact = Impact(
            id= str(uuid.uuid4()),
            high=1000.0,
            low=500.0,
            metric="5",
            estimated=True,
            comment="This is a test comment."
        )

    def test_valid_metric_values(self):
        for metric in self.valid_metrics:
            with self.subTest(metric=metric):
                self.impact.metric = metric
                self.assertEqual(self.impact.metric, metric)

    def test_invalid_metric_values(self):
        for invalid_value in ["0", "17", "invalid"]:
            with self.subTest(metric=invalid_value):
                with self.assertRaises(ValueError):
                    self.impact.metric = invalid_value

class TestImpactRelationships(unittest.TestCase):
    def setUp(self):
        self.impact = Impact(
            id= str(uuid.uuid4()),
            high=1000.0,
            low=500.0,
            metric="5",
            estimated=True,
            comment="This is a test comment."
        )
        self.incident = Incident(id= str(uuid.uuid4()))

    def test_add_incident_to_impact(self):
        self.impact.incident = self.incident
        self.assertEqual(self.incident, self.impact.incident)
        self.assertIn(self.impact, self.incident.impacts)

    def test_remove_incident_from_impact(self):
        self.impact.incident = self.incident
        del self.impact.incident
        self.assertNotIn(self.impact, self.incident.impacts)
        self.assertIsNone(self.impact.incident)
    
    def test_set_incident(self):
        i1 = Incident()
        i2 = Incident()

        self.impact.incident = i1 
        self.assertIn(self.impact, i1.impacts)
        self.assertEqual(self.impact.incident, i1)

        self.impact.incident = i2
        self.assertNotIn(self.impact, i1.impacts)
        self.assertIn(self.impact, i2.impacts)
        self.assertEqual(self.impact.incident, i2)

class TestImpactSetting(unittest.TestCase):
    def setUp(self):
        self.impact = Impact(
            id= str(uuid.uuid4()),
            high=1000.0,
            low=500.0,
            metric="5",
            estimated=True,
            comment="This is a test comment."
        )
        self.incident = Incident(id= str(uuid.uuid4()))

    def test_set_high(self):
        new_high = 2000.0
        self.impact.high = new_high
        self.assertEqual(self.impact.high, new_high)

    def test_set_comment(self):
        new_comment = "Updated comment for the impact"
        self.impact.comment = new_comment
        self.assertEqual(self.impact.comment, new_comment)

if __name__ == '__main__':
    unittest.main()