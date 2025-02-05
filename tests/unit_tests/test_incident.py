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
import uuid, sys, os
from datetime import datetime
sys.path.append(os.getcwd())
from pyiides import Incident, Detection, Response, TTP, Organization, Insider, Impact, Target
from uuid import uuid4

class TestIncidentInitialization(unittest.TestCase):
    def setUp(self):
        self.valid_cia_effect = ["C", "I", "A"]
        self.valid_incident_type = ["F", "S", "E", "V", "U"]
        self.valid_incident_subtype = ["F.1", "S.1", "E.1", "V.1", "U.1"]
        self.valid_outcome = ["BR", "DC", "DD", "DR", "DS", "MD", "ML", "MS", "NN", "OT", "RO", "SI", "IT"]
        self.valid_status = ["P", "I", "R", "C"]
        self.incident_data = {
            "id": str(uuid.uuid4()),
            "cia_effect": ["C"],
            "incident_type": ["F"],
            "incident_subtype": ["F.1"],
            "outcome": ["BR"],
            "status": "P",
            "summary": "This is a test summary.",
            "brief_summary": "This is a brief test summary.",
            "comment": "This is a test comment."
        }
        self.incident = Incident(**self.incident_data)

    def test_initialization(self):
        # Check all fields are set correctly upon initialization
        self.assertEqual(self.incident.id, self.incident_data['id'])
        self.assertEqual(self.incident.cia_effect, self.incident_data['cia_effect'])
        self.assertEqual(self.incident.incident_type, self.incident_data['incident_type'])
        self.assertEqual(self.incident.incident_subtype, self.incident_data['incident_subtype'])
        self.assertEqual(self.incident.outcome, self.incident_data['outcome'])
        self.assertEqual(self.incident.status, self.incident_data['status'])
        self.assertEqual(self.incident.summary, self.incident_data['summary'])
        self.assertEqual(self.incident.brief_summary, self.incident_data['brief_summary'])
        self.assertEqual(self.incident.comment, self.incident_data['comment'])

    def test_invalid_cia_effect_vocabulary(self):
        for invalid_value in ["Z", "invalid"]:
            with self.subTest(cia_effect=invalid_value):
                self.incident_data['cia_effect'] = [invalid_value]
                with self.assertRaises(ValueError):
                    Incident(**self.incident_data)

    def test_invalid_incident_type_vocabulary(self):
        for invalid_value in ["Z", "invalid"]:
            with self.subTest(incident_type=invalid_value):
                self.incident_data['incident_type'] = [invalid_value]
                with self.assertRaises(ValueError):
                    Incident(**self.incident_data)

    def test_invalid_incident_subtype_vocabulary(self):
        for invalid_value in ["F.99", "invalid"]:
            with self.subTest(incident_subtype=invalid_value):
                self.incident_data['incident_subtype'] = [invalid_value]
                with self.assertRaises(ValueError):
                    Incident(**self.incident_data)

    def test_invalid_outcome_vocabulary(self):
        for invalid_value in ["ZZ", "invalid"]:
            with self.subTest(outcome=invalid_value):
                self.incident_data['outcome'] = [invalid_value]
                with self.assertRaises(ValueError):
                    Incident(**self.incident_data)

    def test_invalid_status_vocabulary(self):
        for invalid_value in ["Z", "invalid"]:
            with self.subTest(status=invalid_value):
                self.incident_data['status'] = invalid_value
                with self.assertRaises(ValueError):
                    Incident(**self.incident_data)

    def test_type_errors(self):
        # Check type errors on initialization
        invalid_data = {
            "id": 123,  # should be str
            "cia_effect": "C",  # should be list
            "incident_type": "F",  # should be list
            "incident_subtype": "F.1",  # should be list
            "outcome": "BR",  # should be list
            "status": 123,  # should be str
            "summary": 123,  # should be str
            "brief_summary": 123,  # should be str
            "comment": 123  # should be str
        }
        for key, value in invalid_data.items():
            with self.subTest(field=key):
                self.incident_data[key] = value
                with self.assertRaises(TypeError):
                    Incident(**self.incident_data)

class TestIncidentTypeChecking(unittest.TestCase):
    def setUp(self):
        self.incident = Incident(
            id=str(uuid.uuid4()),
            cia_effect=["C"],
            incident_type=["F"],
            incident_subtype=["F.1"],
            outcome=["BR"],
            status="P",
            summary="This is a test summary.",
            brief_summary="This is a brief test summary.",
            comment="This is a test comment."
        )

    def test_set_id_type(self):
        with self.assertRaises(TypeError):
            self.incident.id = 123  # should be str

    def test_set_cia_effect_type(self):
        with self.assertRaises(TypeError):
            self.incident.cia_effect = "C"  # should be list

    def test_set_incident_type_type(self):
        with self.assertRaises(TypeError):
            self.incident.incident_type = "F"  # should be list

    def test_set_incident_subtype_type(self):
        with self.assertRaises(TypeError):
            self.incident.incident_subtype = "F.1"  # should be list

    def test_set_outcome_type(self):
        with self.assertRaises(TypeError):
            self.incident.outcome = "BR"  # should be list

    def test_set_status_type(self):
        with self.assertRaises(TypeError):
            self.incident.status = 123  # should be str

    def test_set_summary_type(self):
        with self.assertRaises(TypeError):
            self.incident.summary = 123  # should be str

    def test_set_brief_summary_type(self):
        with self.assertRaises(TypeError):
            self.incident.brief_summary = 123  # should be str

    def test_set_comment_type(self):
        with self.assertRaises(TypeError):
            self.incident.comment = 123  # should be str


class TestIncidentVocabChecking(unittest.TestCase):
    def setUp(self):
        self.valid_cia_effect = ["C", "I", "A"]
        self.valid_incident_type = ["F", "S", "E", "V", "U"]
        self.valid_incident_subtype = ["F.1", "S.1", "E.1", "V.1", "U.1"]
        self.valid_outcome = ["BR", "DC", "DD", "DR", "DS", "MD", "ML", "MS", "NN", "OT", "RO", "SI", "IT"]
        self.valid_status = ["P", "I", "R", "C"]
        self.incident = Incident(
            id=str(uuid.uuid4()),
            cia_effect=["C"],
            incident_type=["F"],
            incident_subtype=["F.1"],
            outcome=["BR"],
            status="P",
            summary="This is a test summary.",
            brief_summary="This is a brief test summary.",
            comment="This is a test comment."
        )

    def test_valid_cia_effect_values(self):
        for cia_effect in self.valid_cia_effect:
            with self.subTest(cia_effect=cia_effect):
                self.incident.cia_effect = [cia_effect]
                self.assertEqual(self.incident.cia_effect, [cia_effect])

    def test_invalid_cia_effect_values(self):
        for invalid_value in ["Z", "invalid"]:
            with self.subTest(cia_effect=invalid_value):
                with self.assertRaises(ValueError):
                    self.incident.cia_effect = [invalid_value]

    def test_valid_incident_type_values(self):
        for incident_type in self.valid_incident_type:
            with self.subTest(incident_type=incident_type):
                self.incident.incident_type = [incident_type]
                self.assertEqual(self.incident.incident_type, [incident_type])

    def test_invalid_incident_type_values(self):
        for invalid_value in ["Z", "invalid"]:
            with self.subTest(incident_type=invalid_value):
                with self.assertRaises(ValueError):
                    self.incident.incident_type = [invalid_value]

    def test_valid_incident_subtype_values(self):
        for incident_subtype in self.valid_incident_subtype:
            with self.subTest(incident_subtype=incident_subtype):
                self.incident.incident_type = [incident_subtype[:incident_subtype.find(".")]]
                self.incident.incident_subtype = [incident_subtype]
                self.assertEqual(self.incident.incident_subtype, [incident_subtype])

    def test_invalid_incident_subtype_values(self):
        for invalid_value in ["F.99", "invalid"]:
            with self.subTest(incident_subtype=invalid_value):
                with self.assertRaises(ValueError):
                    self.incident.incident_subtype = [invalid_value]

    def test_valid_outcome_values(self):
        for outcome in self.valid_outcome:
            with self.subTest(outcome=outcome):
                self.incident.outcome = [outcome]
                self.assertEqual(self.incident.outcome, [outcome])

    def test_invalid_outcome_values(self):
        for invalid_value in ["ZZ", "invalid"]:
            with self.subTest(outcome=invalid_value):
                with self.assertRaises(ValueError):
                    self.incident.outcome = [invalid_value]

    def test_valid_status_values(self):
        for status in self.valid_status:
            with self.subTest(status=status):
                self.incident.status = status
                self.assertEqual(self.incident.status, status)

    def test_invalid_status_values(self):
        for invalid_value in ["Z", "invalid"]:
            with self.subTest(status=invalid_value):
                with self.assertRaises(ValueError):
                    self.incident.status = invalid_value


class TestIncidentRelationships(unittest.TestCase):
    def setUp(self):
        self.incident = Incident(
            id=str(uuid.uuid4()),
            cia_effect=["C"],
            incident_type=["F"],
            incident_subtype=["F.1"],
            outcome=["BR"],
            status="P",
            summary="This is a test summary.",
            brief_summary="This is a brief test summary.",
            comment="This is a test comment."
        )
        self.detection = Detection(id= str(uuid.uuid4()))

    def test_append_detection_to_incident(self):
        self.incident.detection = self.detection
        self.assertEqual(self.detection.incident, self.incident)
        self.assertEqual(self.incident.detection, self.detection)

    def test_remove_detection_from_incident(self):
        del self.incident.detection
        self.assertIsNone(self.incident.detection)

    def test_remove_incident_from_detection(self):
        del self.detection.incident
        self.assertIsNone(self.detection.incident)
    
    def add_response_to_incident_and_delete(self):
        r1 = Response()
        r2 = Response()

        self.incident.response = r1
        self.assertEqual(self.incident.response, r1)
        self.assertEqual(r1.incident, self.incident)

        self.incident.response = r2 
        self.assertIsNone(r1.incident)
        self.assertEqual(self.incident.response, r2)
        self.assertEqual(r2.incident, self.incident)

        del self.incident.response
        self.assertIsNone(r2.incident)
        self.assertIsNone(self.incident.response)

class TestMoreIncidentRelationships(unittest.TestCase):
    def setUp(self):
        self.incident = Incident(
            id=str(uuid4()),
            cia_effect=["C"],
            incident_type=["F"],
            incident_subtype=["F.1"],
            outcome=["BR"],
            status="P",
            summary="Test incident",
            brief_summary="Test",
            comment="Test comment"
        )

    def test_detection_relationship(self):
        detection = Detection(id=str(uuid4()))
        
        self.incident.detection = detection
        self.assertEqual(self.incident.detection, detection)
        self.assertEqual(detection.incident, self.incident)

        del self.incident.detection
        self.assertIsNone(self.incident.detection)
        self.assertIsNone(detection.incident)

    def test_response_relationship(self):
        response = Response(id=str(uuid4()))
        
        self.incident.response = response
        self.assertEqual(self.incident.response, response)
        self.assertEqual(response.incident, self.incident)

        del self.incident.response
        self.assertIsNone(self.incident.response)
        self.assertIsNone(response.incident)

    def test_ttps_relationship(self):
        ttp1 = TTP(id=str(uuid4()))
        ttp2 = TTP(id=str(uuid4()))

        self.incident.ttps = [ttp1, ttp2]
        self.assertEqual(len(self.incident.ttps), 2)
        self.assertIn(ttp1, self.incident.ttps)
        self.assertIn(ttp2, self.incident.ttps)
        self.assertEqual(ttp1.incident, self.incident)
        self.assertEqual(ttp2.incident, self.incident)

        ttp3 = TTP(id=str(uuid4()))
        self.incident.append_ttp(ttp3)
        self.assertEqual(len(self.incident.ttps), 3)
        self.assertIn(ttp3, self.incident.ttps)
        self.assertEqual(ttp3.incident, self.incident)

        self.incident.remove_ttp(ttp2)
        self.assertEqual(len(self.incident.ttps), 2)
        self.assertNotIn(ttp2, self.incident.ttps)
        self.assertIsNone(ttp2.incident)

        del self.incident.ttps
        self.assertIsNone(self.incident.ttps)
        self.assertIsNone(ttp1.incident)
        self.assertIsNone(ttp3.incident)
    
    def test_set_ttp(self):
        ttp1 = TTP()
        ttp2 = TTP()
        ttp3 = TTP()
        ttp4 = TTP()

        self.incident.ttps = [ttp1, ttp2]
        self.assertEqual(ttp1.incident, self.incident)
        self.assertEqual(ttp2.incident, self.incident)
        self.assertIn(ttp1, self.incident.ttps)
        self.assertIn(ttp2, self.incident.ttps)

        self.incident.ttps = [ttp3, ttp4]
        self.assertIsNone(ttp1.incident)
        self.assertIsNone(ttp2.incident)
        self.assertNotIn(ttp1, self.incident.ttps)
        self.assertNotIn(ttp2, self.incident.ttps)

        self.assertEqual(ttp3.incident, self.incident)
        self.assertEqual(ttp4.incident, self.incident)
        self.assertIn(ttp3, self.incident.ttps)
        self.assertIn(ttp4, self.incident.ttps)

    def test_organizations_relationship(self):
        org1 = Organization(id=str(uuid4()))
        org2 = Organization(id=str(uuid4()))

        self.incident.organizations = [org1, org2]
        self.assertEqual(len(self.incident.organizations), 2)
        self.assertIn(org1, self.incident.organizations)
        self.assertIn(org2, self.incident.organizations)
        self.assertEqual(org1.incident, self.incident)
        self.assertEqual(org2.incident, self.incident)

        org3 = Organization(id=str(uuid4()))
        self.incident.append_organization(org3)
        self.assertEqual(len(self.incident.organizations), 3)
        self.assertIn(org3, self.incident.organizations)
        self.assertEqual(org3.incident, self.incident)

        self.incident.remove_organization(org2)
        self.assertEqual(len(self.incident.organizations), 2)
        self.assertNotIn(org2, self.incident.organizations)
        self.assertIsNone(org2.incident)

        del self.incident.organizations
        self.assertIsNone(self.incident.organizations)
        self.assertIsNone(org1.incident)
        self.assertIsNone(org3.incident)

    def test_insiders_relationship(self):
        insider1 = Insider(incident_role="1")
        insider2 = Insider(incident_role="1")

        self.incident.insiders = [insider1, insider2]
        self.assertEqual(len(self.incident.insiders), 2)
        self.assertIn(insider1, self.incident.insiders)
        self.assertIn(insider2, self.incident.insiders)
        self.assertEqual(insider1.incident, self.incident)
        self.assertEqual(insider2.incident, self.incident)

        insider3 = Insider(incident_role="1")
        self.incident.append_insider(insider3)
        self.assertEqual(len(self.incident.insiders), 3)
        self.assertIn(insider3, self.incident.insiders)
        self.assertEqual(insider3.incident, self.incident)

        self.incident.remove_insider(insider2)
        self.assertEqual(len(self.incident.insiders), 2)
        self.assertNotIn(insider2, self.incident.insiders)
        self.assertIsNone(insider2.incident)

        del self.incident.insiders
        self.assertIsNone(self.incident.insiders)
        self.assertIsNone(insider1.incident)
        self.assertIsNone(insider3.incident)

    def test_impacts_relationship(self):
        impact1 = Impact(low=1.1, high=2.1, metric="1", estimated=True)
        impact2 = Impact(low=1.1, high=2.1, metric="1", estimated=True)

        self.incident.impacts = [impact1, impact2]
        self.assertEqual(len(self.incident.impacts), 2)
        self.assertIn(impact1, self.incident.impacts)
        self.assertIn(impact2, self.incident.impacts)
        self.assertEqual(impact1.incident, self.incident)
        self.assertEqual(impact2.incident, self.incident)

        impact3 = Impact(low=1.1, high=2.1, metric="1", estimated=True)
        self.incident.append_impact(impact3)
        self.assertEqual(len(self.incident.impacts), 3)
        self.assertIn(impact3, self.incident.impacts)
        self.assertEqual(impact3.incident, self.incident)

        self.incident.remove_impact(impact2)
        self.assertEqual(len(self.incident.impacts), 2)
        self.assertNotIn(impact2, self.incident.impacts)
        self.assertIsNone(impact2.incident)

        del self.incident.impacts
        self.assertIsNone(self.incident.impacts)
        self.assertIsNone(impact1.incident)
        self.assertIsNone(impact3.incident)

    def test_targets_relationship(self):
        target1 = Target(asset_type="1", category="1.1", subcategory="1.1.1", format="1", owner="C", sensitivity=["1"])
        target2 = Target(asset_type="1", category="1.1", subcategory="1.1.1", format="1", owner="C", sensitivity=["1"])

        self.incident.targets = [target1, target2]
        self.assertEqual(len(self.incident.targets), 2)
        self.assertIn(target1, self.incident.targets)
        self.assertIn(target2, self.incident.targets)
        self.assertEqual(target1.incident, self.incident)
        self.assertEqual(target2.incident, self.incident)

        target3 = Target(asset_type="1", category="1.1", subcategory="1.1.1", format="1", owner="C", sensitivity=["1"])
        self.incident.append_target(target3)
        self.assertEqual(len(self.incident.targets), 3)
        self.assertIn(target3, self.incident.targets)
        self.assertEqual(target3.incident, self.incident)

        self.incident.remove_target(target2)
        self.assertEqual(len(self.incident.targets), 2)
        self.assertNotIn(target2, self.incident.targets)
        self.assertIsNone(target2.incident)

        del self.incident.targets
        self.assertIsNone(self.incident.targets)
        self.assertIsNone(target1.incident)
        self.assertIsNone(target3.incident)

class TestIncidentSetting(unittest.TestCase):
    def setUp(self):
        self.incident = Incident(
            id=str(uuid.uuid4()),
            cia_effect=["C"],
            incident_type=["F"],
            incident_subtype=["F.1"],
            outcome=["BR"],
            status="P",
            summary="This is a test summary.",
            brief_summary="This is a brief test summary.",
            comment="This is a test comment."
        )
        self.detection = Detection(id=str(uuid.uuid4()))

    def test_set_id(self):
        new_id = str(uuid.uuid4())
        self.incident.id = new_id
        self.assertEqual(self.incident.id, new_id)

    def test_set_cia_effect(self):
        new_cia_effect = ["I"]
        self.incident.cia_effect = new_cia_effect
        self.assertEqual(self.incident.cia_effect, new_cia_effect)

    def test_set_incident_type(self):
        new_incident_type = ["S"]
        self.incident.incident_type = new_incident_type
        self.assertEqual(self.incident.incident_type, new_incident_type)

    def test_set_incident_subtype(self):
        new_incident_subtype = ["S.1"]
        self.incident.incident_type = ["S"]
        self.incident.incident_subtype = new_incident_subtype
        self.assertEqual(self.incident.incident_subtype, new_incident_subtype)

    def test_set_outcome(self):
        new_outcome = ["DS"]
        self.incident.outcome = new_outcome
        self.assertEqual(self.incident.outcome, new_outcome)

    def test_set_status(self):
        new_status = "C"
        self.incident.status = new_status
        self.assertEqual(self.incident.status, new_status)

    def test_set_summary(self):
        new_summary = "Updated summary for the incident"
        self.incident.summary = new_summary
        self.assertEqual(self.incident.summary, new_summary)

    def test_set_brief_summary(self):
        new_brief_summary = "Updated brief summary for the incident"
        self.incident.brief_summary = new_brief_summary
        self.assertEqual(self.incident.brief_summary, new_brief_summary)

    def test_set_comment(self):
        new_comment = "Updated comment for the incident"
        self.incident.comment = new_comment
        self.assertEqual(self.incident.comment, new_comment)

if __name__ == '__main__':
    unittest.main()