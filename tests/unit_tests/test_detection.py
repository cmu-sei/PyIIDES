"""
License:
PyIIDES
Copyright 2024 Carnegie Mellon University.
NO WARRANTY. THIS CARNEGIE MELLON UNIVERSITY AND SOFTWARE ENGINEERING INSTITUTE MATERIAL IS FURNISHED ON AN "AS-IS" BASIS. CARNEGIE MELLON UNIVERSITY MAKES NO WARRANTIES OF ANY KIND, EITHER EXPRESSED OR IMPLIED, AS TO ANY MATTER INCLUDING, BUT NOT LIMITED TO, WARRANTY OF FITNESS FOR PURPOSE OR MERCHANTABILITY, EXCLUSIVITY, OR RESULTS OBTAINED FROM USE OF THE MATERIAL. CARNEGIE MELLON UNIVERSITY DOES NOT MAKE ANY WARRANTY OF ANY KIND WITH RESPECT TO FREEDOM FROM PATENT, TRADEMARK, OR COPYRIGHT INFRINGEMENT.
Licensed under a MIT (SEI)-style license, please see license.txt or contact permission@sei.cmu.edu for full terms.
[DISTRIBUTION STATEMENT A] This material has been approved for public release and unlimited distribution.  Please see Copyright notice for non-US Government use and distribution.
DM24-1597
"""
import unittest, uuid, os, sys, datetime
sys.path.append(os.getcwd())
from pyiides import Detection, Incident

class TestDetection(unittest.TestCase):

    def setUp(self):
        self.valid_id = str(uuid.uuid4())
        self.valid_first_detected = datetime.datetime(2020,1,1)
        self.valid_who_detected = ["LE"]
        self.valid_detected_method = ["1"]
        self.valid_logs = ["AC"]
        self.valid_comment = "Test comment"

    def test_initialization(self):
        # Test valid initialization
        detection = Detection(
            id=self.valid_id,
            first_detected=self.valid_first_detected,
            who_detected=self.valid_who_detected,
            detected_method=self.valid_detected_method,
            logs=self.valid_logs,
            comment=self.valid_comment
        )
        self.assertEqual(detection.id, self.valid_id)
        self.assertEqual(detection.first_detected, self.valid_first_detected)
        self.assertEqual(detection.who_detected, self.valid_who_detected)
        self.assertEqual(detection.detected_method, self.valid_detected_method)
        self.assertEqual(detection.logs, self.valid_logs)
        self.assertEqual(detection.comment, self.valid_comment)

        # Test initialization with invalid vocab
        with self.assertRaises(ValueError):
            Detection(who_detected=["INVALID"])
        with self.assertRaises(ValueError):
            Detection(detected_method=["INVALID"])
        with self.assertRaises(ValueError):
            Detection(logs=["INVALID"])

        # Test initialization with invalid types
        with self.assertRaises(TypeError):
            Detection(first_detected="not a datetime")
        with self.assertRaises(TypeError):
            Detection(who_detected="not a list")
        with self.assertRaises(TypeError):
            Detection(detected_method="not a list")
        with self.assertRaises(TypeError):
            Detection(logs="not a list")
        with self.assertRaises(TypeError):
            Detection(comment=123)

    def test_id_property(self):
        detection = Detection()
        new_id = str(uuid.uuid4())
        detection.id = new_id
        self.assertEqual(detection.id, new_id)
        with self.assertRaises(ValueError):
            detection.id = "invalid-uuid"

    def test_first_detected_property(self):
        detection = Detection()
        new_date = datetime.datetime(2023,1,1)
        detection.first_detected = new_date
        self.assertEqual(detection.first_detected, new_date)
        with self.assertRaises(TypeError):
            detection.first_detected = "not a datetime"
        del detection.first_detected
        self.assertIsNone(detection.first_detected)

    def test_who_detected_property(self):
        detection = Detection(who_detected=["LE"])
        detection.who_detected = ["OR", "CU"]
        self.assertEqual(detection.who_detected, ["OR", "CU"])
        with self.assertRaises(ValueError):
            detection.who_detected = ["INVALID"]
        with self.assertRaises(TypeError):
            detection.who_detected = "not a list"
        detection.append_who_detected("AU")
        self.assertEqual(detection.who_detected, ["OR", "CU", "AU"])
        with self.assertRaises(ValueError):
            detection.append_who_detected("INVALID")
        del detection.who_detected
        self.assertIsNone(detection.who_detected)

    def test_detected_method_property(self):
        detection = Detection(detected_method=["1"])
        detection.detected_method = ["2", "3"]
        self.assertEqual(detection.detected_method, ["2", "3"])
        with self.assertRaises(ValueError):
            detection.detected_method = ["INVALID"]
        with self.assertRaises(TypeError):
            detection.detected_method = "not a list"
        detection.append_detected_method("4")
        self.assertEqual(detection.detected_method, ["2", "3", "4"])
        with self.assertRaises(ValueError):
            detection.append_detected_method("INVALID")
        del detection.detected_method
        self.assertIsNone(detection.detected_method)

    def test_logs_property(self):
        detection = Detection(logs=["AC"])
        detection.logs = ["DB", "EM"]
        self.assertEqual(detection.logs, ["DB", "EM"])
        with self.assertRaises(ValueError):
            detection.logs = ["INVALID"]
        with self.assertRaises(TypeError):
            detection.logs = "not a list"
        detection.append_logs("FS")
        self.assertEqual(detection.logs, ["DB", "EM", "FS"])
        with self.assertRaises(ValueError):
            detection.append_logs("INVALID")
        del detection.logs
        self.assertIsNone(detection.logs)

    def test_comment_property(self):
        detection = Detection()
        detection.comment = "New comment"
        self.assertEqual(detection.comment, "New comment")
        with self.assertRaises(TypeError):
            detection.comment = 123
        del detection.comment
        self.assertIsNone(detection.comment)

    def test_incident_bidirectional_relationship(self):    
        # Create a Detection instance
        detection = Detection(
            id=self.valid_id,
            first_detected=self.valid_first_detected,
            who_detected=self.valid_who_detected,
            detected_method=self.valid_detected_method,
            logs=self.valid_logs,
            comment=self.valid_comment
        )
        
        # Create an Incident instance
        incident = Incident()
        
        # Set the relationship from Detection to Incident
        detection.incident = incident
        
        # Check that the relationship is set correctly in both directions
        self.assertEqual(detection.incident, incident)
        self.assertEqual(incident.detection, detection)
        
        # Test removing the relationship
        del detection.incident
        
        # Check that the relationship is removed in both directions
        self.assertIsNone(detection.incident)
        self.assertIsNone(incident.detection)
        
        # Test setting the relationship from the Incident side
        incident.detection = detection
        
        # Check that the relationship is set correctly in both directions
        self.assertEqual(detection.incident, incident)
        self.assertEqual(incident.detection, detection)
        
        # Test removing the relationship from the Incident side
        del incident.detection
        
        # Check that the relationship is removed in both directions
        self.assertIsNone(detection.incident)
        self.assertIsNone(incident.detection)
