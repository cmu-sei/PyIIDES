"""
License:
PyIIDES
Copyright 2024 Carnegie Mellon University.
NO WARRANTY. THIS CARNEGIE MELLON UNIVERSITY AND SOFTWARE ENGINEERING INSTITUTE MATERIAL IS FURNISHED ON AN "AS-IS" BASIS. CARNEGIE MELLON UNIVERSITY MAKES NO WARRANTIES OF ANY KIND, EITHER EXPRESSED OR IMPLIED, AS TO ANY MATTER INCLUDING, BUT NOT LIMITED TO, WARRANTY OF FITNESS FOR PURPOSE OR MERCHANTABILITY, EXCLUSIVITY, OR RESULTS OBTAINED FROM USE OF THE MATERIAL. CARNEGIE MELLON UNIVERSITY DOES NOT MAKE ANY WARRANTY OF ANY KIND WITH RESPECT TO FREEDOM FROM PATENT, TRADEMARK, OR COPYRIGHT INFRINGEMENT.
Licensed under a MIT (SEI)-style license, please see license.txt or contact permission@sei.cmu.edu for full terms.
[DISTRIBUTION STATEMENT A] This material has been approved for public release and unlimited distribution.  Please see Copyright notice for non-US Government use and distribution.
DM24-1597
"""
import unittest, os, sys
from uuid import UUID
sys.path.append(os.getcwd())
from pyiides import Sponsor
from pyiides import Accomplice
from pyiides import Insider

class TestSponsor(unittest.TestCase):
    def setUp(self):
        self.sponsor = Sponsor(
            id="123e4567-e89b-12d3-a456-426614174000",
            name="John Doe",
            sponsor_type="OC"
        )

    def test_initialization(self):
        self.assertIsInstance(self.sponsor.id, str)
        self.assertIsInstance(self.sponsor.name, str)
        self.assertIsInstance(self.sponsor.sponsor_type, str)

    def test_setters_and_getters(self):
        new_id = "456e7890-e12d-3a45-b678-123456789012"
        self.sponsor.id = new_id
        self.assertEqual(self.sponsor.id, new_id)

        new_name = "Jane Smith"
        self.sponsor.name = new_name
        self.assertEqual(self.sponsor.name, new_name)

        new_sponsor_type = "SS"
        self.sponsor.sponsor_type = new_sponsor_type
        self.assertEqual(self.sponsor.sponsor_type, new_sponsor_type)

    def test_deleters(self):
        del self.sponsor.name
        self.assertIsNone(self.sponsor.name)

        del self.sponsor.sponsor_type
        self.assertIsNone(self.sponsor.sponsor_type)

    def test_type_checks(self):
        with self.assertRaises(TypeError):
            self.sponsor.id = 123

        with self.assertRaises(TypeError):
            self.sponsor.name = 123

        with self.assertRaises(TypeError):
            self.sponsor.sponsor_type = 1

    def test_vocab_checks(self):
        with self.assertRaises(ValueError):
            self.sponsor.sponsor_type = "invalid_sponsor_type"

    def test_accomplices_relationship(self):
        accomplice1 = Accomplice()
        accomplice2 = Accomplice()
        self.sponsor.accomplices = [accomplice1, accomplice2]
        self.assertListEqual(self.sponsor.accomplices, [accomplice1, accomplice2])
        self.assertEqual(accomplice1.sponsor, self.sponsor)
        self.assertEqual(accomplice2.sponsor, self.sponsor)

        self.sponsor.append_accomplice(Accomplice())
        self.assertEqual(len(self.sponsor.accomplices), 3)
        self.assertEqual(self.sponsor.accomplices[-1].sponsor, self.sponsor)

        self.sponsor.remove_accomplice(accomplice1)
        self.assertListEqual(self.sponsor.accomplices, [accomplice2, self.sponsor.accomplices[-1]])
        self.assertIsNone(accomplice1.sponsor)

        del self.sponsor.accomplices
        self.assertIsNone(self.sponsor.accomplices)
        self.assertIsNone(accomplice2.sponsor)

    def test_insiders_relationship(self):
        insider1 = Insider(incident_role="1")
        insider2 = Insider(incident_role="1")
        self.sponsor.insiders = [insider1, insider2]
        self.assertListEqual(self.sponsor.insiders, [insider1, insider2])
        self.assertEqual(insider1.sponsor, self.sponsor)
        self.assertEqual(insider2.sponsor, self.sponsor)

        self.sponsor.append_insider(Insider(incident_role="1"))
        self.assertEqual(len(self.sponsor.insiders), 3)
        self.assertEqual(self.sponsor.insiders[-1].sponsor, self.sponsor)

        self.sponsor.remove_insider(insider1)
        self.assertListEqual(self.sponsor.insiders, [insider2, self.sponsor.insiders[-1]])
        self.assertIsNone(insider1.sponsor)

        del self.sponsor.insiders
        self.assertIsNone(self.sponsor.insiders)
        self.assertIsNone(insider2.sponsor)