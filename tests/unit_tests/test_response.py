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
from datetime import date
import uuid
from pyiides import Response
from pyiides import Incident
from pyiides import LegalResponse

class TestResponse(unittest.TestCase):
    def setUp(self):
        self.response = Response(
            id="123e4567-e89b-12d3-a456-426614174000",
            technical_controls=[("1", date(2023, 1, 1))],
            behavioral_controls=[("4", date(2023, 1, 2))],
            investigated_by=["1", "2"],
            investigation_events=[("2", date(2023, 1, 3))],
            comment="Initial comment"
        )

    def test_initialization(self):
        self.assertIsInstance(self.response.id, str)
        self.assertIsInstance(self.response.technical_controls, list)
        self.assertIsInstance(self.response.behavioral_controls, list)
        self.assertIsInstance(self.response.investigated_by, list)
        self.assertIsInstance(self.response.investigation_events, list)
        self.assertIsInstance(self.response.comment, str)

    def test_setters_and_getters(self):
        new_id = str(uuid.uuid4())
        self.response.id = new_id
        self.assertEqual(self.response.id, new_id)

        new_technical_controls = [("2", date(2023, 2, 1))]
        self.response.technical_controls = new_technical_controls
        self.assertEqual(self.response.technical_controls, new_technical_controls)

        new_behavioral_controls = [("5", date(2023, 2, 2))]
        self.response.behavioral_controls = new_behavioral_controls
        self.assertEqual(self.response.behavioral_controls, new_behavioral_controls)

        new_investigated_by = ["3", "4"]
        self.response.investigated_by = new_investigated_by
        self.assertEqual(self.response.investigated_by, new_investigated_by)

        new_investigation_events = [("3", date(2023, 2, 3))]
        self.response.investigation_events = new_investigation_events
        self.assertEqual(self.response.investigation_events, new_investigation_events)

        new_comment = "New comment"
        self.response.comment = new_comment
        self.assertEqual(self.response.comment, new_comment)

    def test_deleters(self):
        del self.response.technical_controls
        self.assertIsNone(self.response.technical_controls)

        del self.response.behavioral_controls
        self.assertIsNone(self.response.behavioral_controls)

        del self.response.investigated_by
        self.assertIsNone(self.response.investigated_by)

        del self.response.investigation_events
        self.assertIsNone(self.response.investigation_events)

        del self.response.comment
        self.assertIsNone(self.response.comment)

    def test_append_methods(self):
        self.response.append_technical_controls(("3", date(2023, 3, 1)))
        self.assertEqual(len(self.response.technical_controls), 2)

        self.response.append_behavioral_controls(("6", date(2023, 3, 2)))
        self.assertEqual(len(self.response.behavioral_controls), 2)

        self.response.append_investigated_by("5")
        self.assertEqual(len(self.response.investigated_by), 3)

        self.response.append_investigation_events(("4", date(2023, 3, 3)))
        self.assertEqual(len(self.response.investigation_events), 2)

    def test_type_checks(self):
        with self.assertRaises(TypeError):
            self.response.id = 123

        with self.assertRaises(TypeError):
            self.response.technical_controls = "1"

        with self.assertRaises(TypeError):
            self.response.behavioral_controls = "4"

        with self.assertRaises(TypeError):
            self.response.investigated_by = "1"

        with self.assertRaises(TypeError):
            self.response.investigation_events = "2"

        with self.assertRaises(TypeError):
            self.response.comment = 123

    def test_vocab_checks(self):
        with self.assertRaises(ValueError):
            self.response.technical_controls = [("invalid", date(2023, 4, 1))]

        with self.assertRaises(ValueError):
            self.response.behavioral_controls = [("invalid", date(2023, 4, 2))]

        with self.assertRaises(ValueError):
            self.response.investigated_by = ["invalid"]

        with self.assertRaises(ValueError):
            self.response.investigation_events = [("invalid", date(2023, 4, 3))]

    def test_incident_relationship(self):
        incident = Incident()
        self.response.incident = incident
        self.assertEqual(self.response.incident, incident)
        self.assertEqual(incident.response, self.response)

        del self.response.incident
        self.assertIsNone(self.response.incident)
        self.assertIsNone(incident.response)

    def test_legal_response_relationship(self):
        legal_response = LegalResponse()
        self.response.legal_response = legal_response
        self.assertEqual(self.response.legal_response, legal_response)
        self.assertEqual(legal_response.response, self.response)

        del self.response.legal_response
        self.assertIsNone(self.response.legal_response)
        self.assertIsNone(legal_response.response)

if __name__ == '__main__':
    unittest.main()