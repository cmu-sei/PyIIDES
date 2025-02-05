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
from pyiides import TTP, Incident
from datetime import datetime

class TestTTP(unittest.TestCase):
    def setUp(self):
        self.ttp = TTP(
            id="123e4567-e89b-12d3-a456-426614174000",
            date=datetime(2023, 1, 1, 0, 0, 0),
            sequence_num=1,
            observed=True,
            number_of_times=5,
            ttp_vocab="IIDES",
            tactic="1",
            technique="1.1",
            location=["1"],
            hours=["1"],
            device=["1"],
            channel=["1"],
            description="Initial description"
        )

    def test_initialization(self):
        self.assertIsInstance(self.ttp.id, str)
        self.assertIsInstance(self.ttp.date, datetime)
        self.assertIsInstance(self.ttp.sequence_num, int)
        self.assertIsInstance(self.ttp.observed, bool)
        self.assertIsInstance(self.ttp.number_of_times, int)
        self.assertIsInstance(self.ttp.ttp_vocab, str)
        self.assertIsInstance(self.ttp.tactic, str)
        self.assertIsInstance(self.ttp.technique, str)
        self.assertIsInstance(self.ttp.location, list)
        self.assertIsInstance(self.ttp.hours, list)
        self.assertIsInstance(self.ttp.device, list)
        self.assertIsInstance(self.ttp.channel, list)
        self.assertIsInstance(self.ttp.description, str)

    def test_setters_and_getters(self):
        new_id = "456e7890-e12d-3a45-b678-123456789012"
        self.ttp.id = new_id
        self.assertEqual(self.ttp.id, new_id)

        new_date = datetime(2023, 2, 1, 0, 0, 0)
        self.ttp.date = new_date
        self.assertEqual(self.ttp.date, new_date)

        new_sequence_num = 2
        self.ttp.sequence_num = new_sequence_num
        self.assertEqual(self.ttp.sequence_num, new_sequence_num)

        new_observed = False
        self.ttp.observed = new_observed
        self.assertEqual(self.ttp.observed, new_observed)

        new_number_of_times = 10
        self.ttp.number_of_times = new_number_of_times
        self.assertEqual(self.ttp.number_of_times, new_number_of_times)

        new_ttp_vocab = "ATT&CK"
        self.ttp.ttp_vocab = new_ttp_vocab
        self.assertEqual(self.ttp.ttp_vocab, new_ttp_vocab)

        new_tactic = "2"
        self.ttp.tactic = new_tactic
        self.assertEqual(self.ttp.tactic, new_tactic)

        new_technique = "2.1"
        self.ttp.technique = new_technique
        self.assertEqual(self.ttp.technique, new_technique)

        new_location = ["2"]
        self.ttp.location = new_location
        self.assertEqual(self.ttp.location, new_location)

        new_hours = ["2"]
        self.ttp.hours = new_hours
        self.assertEqual(self.ttp.hours, new_hours)

        new_device = ["2"]
        self.ttp.device = new_device
        self.assertEqual(self.ttp.device, new_device)

        new_channel = ["2"]
        self.ttp.channel = new_channel
        self.assertEqual(self.ttp.channel, new_channel)

        new_description = "New description"
        self.ttp.description = new_description
        self.assertEqual(self.ttp.description, new_description)

    def test_deleters(self):
        del self.ttp.date
        self.assertIsNone(self.ttp.date)

        del self.ttp.sequence_num
        self.assertIsNone(self.ttp.sequence_num)

        del self.ttp.observed
        self.assertIsNone(self.ttp.observed)

        del self.ttp.number_of_times
        self.assertIsNone(self.ttp.number_of_times)

        del self.ttp.ttp_vocab
        self.assertIsNone(self.ttp.ttp_vocab)

        del self.ttp.tactic
        self.assertIsNone(self.ttp.tactic)

        del self.ttp.technique
        self.assertIsNone(self.ttp.technique)

        del self.ttp.location
        self.assertIsNone(self.ttp.location)

        del self.ttp.hours
        self.assertIsNone(self.ttp.hours)

        del self.ttp.device
        self.assertIsNone(self.ttp.device)

        del self.ttp.channel
        self.assertIsNone(self.ttp.channel)

        del self.ttp.description
        self.assertIsNone(self.ttp.description)

    def test_append_methods(self):
        self.ttp.append_location("2")
        self.assertListEqual(self.ttp.location, ["1", "2"])

        self.ttp.append_hours("2")
        self.assertListEqual(self.ttp.hours, ["1", "2"])

        self.ttp.append_device("2")
        self.assertListEqual(self.ttp.device, ["1", "2"])

        self.ttp.append_channel("2")
        self.assertListEqual(self.ttp.channel, ["1", "2"])

    def test_type_checks(self):
        with self.assertRaises(TypeError):
            self.ttp.id = 123

        with self.assertRaises(TypeError):
            self.ttp.date = "2023-01-01"

        with self.assertRaises(TypeError):
            self.ttp.sequence_num = "1"

        with self.assertRaises(TypeError):
            self.ttp.observed = 1

        with self.assertRaises(TypeError):
            self.ttp.number_of_times = "5"

        with self.assertRaises(TypeError):
            self.ttp.ttp_vocab = 123

        with self.assertRaises(TypeError):
            self.ttp.tactic = 1

        with self.assertRaises(TypeError):
            self.ttp.technique = 1

        with self.assertRaises(TypeError):
            self.ttp.location = "1"

        with self.assertRaises(TypeError):
            self.ttp.hours = "1"

        with self.assertRaises(TypeError):
            self.ttp.device = "1"

        with self.assertRaises(TypeError):
            self.ttp.channel = "1"

        with self.assertRaises(TypeError):
            self.ttp.description = 123

    def test_vocab_checks(self):
        with self.assertRaises(ValueError):
            self.ttp.tactic = "invalid_tactic"

        with self.assertRaises(ValueError):
            self.ttp.technique = "invalid_technique"

        with self.assertRaises(ValueError):
            self.ttp.location = ["invalid_location"]

        with self.assertRaises(ValueError):
            self.ttp.hours = ["invalid_hours"]

        with self.assertRaises(ValueError):
            self.ttp.device = ["invalid_device"]

        with self.assertRaises(ValueError):
            self.ttp.channel = ["invalid_channel"]

    def test_relationship(self):
        i = Incident()
        self.ttp.incident = i
        self.assertEqual(self.ttp.incident, i)
        self.assertIn(self.ttp, i.ttps)

        del self.ttp.incident
        self.assertIsNone(self.ttp.incident)
        self.assertNotIn(self.ttp, i.ttps)