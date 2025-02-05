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
import sys, os
import uuid
sys.path.append(os.getcwd())
from pyiides.pyiides import *
from datetime import date, datetime, timedelta

class TestIncidentRelationships(unittest.TestCase):
    def setUp(self):
        self.incident = Incident()

    def test_add_ttp_to_incident(self):
        ttp1 = TTP(description="this is ttp1")
        ttp2 = TTP(description="this is ttp2")

        self.incident.ttps = [ttp1]
        self.assertIn(ttp1, self.incident.ttps)
        self.assertEqual(ttp1.incident, self.incident)

        self.incident.append_ttp(ttp2)
        self.assertIn(ttp2, self.incident.ttps)
        self.assertEqual(ttp2.incident, self.incident)
    
    def test_remove_ttp_from_incident(self):
        ttp1 = TTP(description="Phishing")
        ttp2 = TTP(description="Malware")
        
        self.incident.ttps = [ttp1, ttp2]
        self.assertIn(ttp1, self.incident.ttps)
        self.assertIn(ttp2, self.incident.ttps)
        
        self.incident.remove_ttp(ttp1)
        self.assertNotIn(ttp1, self.incident.ttps)
        self.assertIsNone(ttp1.incident)

        self.incident.remove_ttp(ttp2)
        self.assertNotIn(ttp2, self.incident.ttps)
        self.assertIsNone(ttp2.incident)
    
    def test_del_ttp(self):
        ttp1 = TTP(description="Phishing")
        
        self.incident.ttps = [ttp1]
        self.assertIn(ttp1, self.incident.ttps)
        
        del self.incident.ttps
        self.assertIsNone(self.incident.ttps)
        self.assertIsNone(ttp1.incident)
    
    def test_add_detection(self):
        d = Detection()
        
        self.incident.detection = d

        self.assertEqual(self.incident.detection, d)
        self.assertEqual(d.incident, self.incident)
    
    def test_delete_detection(self):
        d = Detection()

        self.incident.detection = d

        self.assertEqual(self.incident.detection, d)
        self.assertEqual(d.incident, self.incident)

        del self.incident.detection
        self.assertIsNone(self.incident.detection)
        self.assertIsNone(d.incident)

        self.incident.detection = d
        
        del d.incident
        self.assertIsNone(self.incident.detection)
        self.assertIsNone(d.incident)

if __name__ == '__main__':
    unittest.main()
