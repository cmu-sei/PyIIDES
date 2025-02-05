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
from uuid import UUID
from pyiides import Target, Incident

class TestTarget(unittest.TestCase):
    def setUp(self):
        self.target = Target(
            id="123e4567-e89b-12d3-a456-426614174000",
            asset_type="4",
            category="4.1",
            subcategory="4.1.1",
            format="1",
            owner="O",
            sensitivity=["25"],
            description="Client list for manifold sales"
        )

    def test_initialization(self):
        self.assertIsInstance(self.target.id, str)
        self.assertIsInstance(self.target.asset_type, str)
        self.assertIsInstance(self.target.category, str)
        self.assertIsInstance(self.target.subcategory, str)
        self.assertIsInstance(self.target.format, str)
        self.assertIsInstance(self.target.owner, str)
        self.assertIsInstance(self.target.sensitivity, list)
        self.assertIsInstance(self.target.description, str)

    def test_setters_and_getters(self):
        new_id = "456e7890-e12d-3a45-b678-123456789012"
        self.target.id = new_id
        self.assertEqual(self.target.id, new_id)

        new_asset_type = "5"
        self.target.asset_type = new_asset_type
        self.assertEqual(self.target.asset_type, new_asset_type)

        new_category = "5.1"
        self.target.category = new_category
        self.assertEqual(self.target.category, new_category)

        new_subcategory = "5.1.1"
        self.target.subcategory = new_subcategory
        self.assertEqual(self.target.subcategory, new_subcategory)

        new_format = "2"
        self.target.format = new_format
        self.assertEqual(self.target.format, new_format)

        new_owner = "C"
        self.target.owner = new_owner
        self.assertEqual(self.target.owner, new_owner)

        new_sensitivity = ["26"]
        self.target.sensitivity = new_sensitivity
        self.assertEqual(self.target.sensitivity, new_sensitivity)

        new_description = "New description"
        self.target.description = new_description
        self.assertEqual(self.target.description, new_description)

    def test_deleters(self):
        del self.target.id
        self.assertIsNone(self.target.id)

        del self.target.asset_type
        self.assertIsNone(self.target.asset_type)

        del self.target.category
        self.assertIsNone(self.target.category)

        del self.target.subcategory
        self.assertIsNone(self.target.subcategory)

        del self.target.format
        self.assertIsNone(self.target.format)

        del self.target.owner
        self.assertIsNone(self.target.owner)

        del self.target.sensitivity
        self.assertIsNone(self.target.sensitivity)

        del self.target.description
        self.assertIsNone(self.target.description)

    def test_type_checks(self):
        with self.assertRaises(TypeError):
            self.target.id = 123

        with self.assertRaises(TypeError):
            self.target.asset_type = 4

        with self.assertRaises(TypeError):
            self.target.category = 4.1

        with self.assertRaises(TypeError):
            self.target.subcategory = 4.1

        with self.assertRaises(TypeError):
            self.target.format = 1

        with self.assertRaises(TypeError):
            self.target.owner = 1

        with self.assertRaises(TypeError):
            self.target.sensitivity = "25"

        with self.assertRaises(TypeError):
            self.target.description = 123

    def test_vocab_checks(self):
        with self.assertRaises(ValueError):
            self.target.asset_type = "invalid_asset_type"

        with self.assertRaises(ValueError):
            self.target.category = "invalid_category"

        with self.assertRaises(ValueError):
            self.target.subcategory = "invalid_subcategory"

        with self.assertRaises(ValueError):
            self.target.format = "invalid_format"

        with self.assertRaises(ValueError):
            self.target.owner = "invalid_owner"

        with self.assertRaises(ValueError):
            self.target.sensitivity = ["invalid_sensitivity"]

    def test_relationship(self):
        i = Incident()
        self.target.incident = i
        self.assertEqual(self.target.incident, i)
        self.assertIn(self.target, i.targets)

        del self.target.incident
        self.assertIsNone(self.target.incident)
        self.assertNotIn(self.target, i.targets)