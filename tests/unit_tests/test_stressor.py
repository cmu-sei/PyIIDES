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
from uuid import UUID
from pyiides import Stressor
from pyiides import Organization
from pyiides import Insider

class TestStressor(unittest.TestCase):
    def setUp(self):
        self.stressor = Stressor(
            id="123e4567-e89b-12d3-a456-426614174000",
            date=date(2023, 6, 14),
            category="2",
            subcategory="2.12",
            comment="High-pressure project deadline"
        )

    def test_initialization(self):
        self.assertIsInstance(self.stressor.id, str)
        self.assertIsInstance(self.stressor.date, date)
        self.assertIsInstance(self.stressor.category, str)
        self.assertIsInstance(self.stressor.subcategory, str)
        self.assertIsInstance(self.stressor.comment, str)

    def test_setters_and_getters(self):
        new_id = "456e7890-e12d-3a45-b678-123456789012"
        self.stressor.id = new_id
        self.assertEqual(self.stressor.id, new_id)

        new_date = date(2023, 7, 1)
        self.stressor.date = new_date
        self.assertEqual(self.stressor.date, new_date)

        new_category = "3"
        self.stressor.category = new_category
        self.assertEqual(self.stressor.category, new_category)

        new_subcategory = "3.1"
        self.stressor.subcategory = new_subcategory
        self.assertEqual(self.stressor.subcategory, new_subcategory)

        new_comment = "New comment"
        self.stressor.comment = new_comment
        self.assertEqual(self.stressor.comment, new_comment)

    def test_deleters(self):
        del self.stressor.date
        self.assertIsNone(self.stressor.date)

        del self.stressor.subcategory
        self.assertIsNone(self.stressor.subcategory)

        del self.stressor.category
        self.assertIsNone(self.stressor.category)

        del self.stressor.comment
        self.assertIsNone(self.stressor.comment)

    def test_type_checks(self):
        with self.assertRaises(TypeError):
            self.stressor.id = 123

        with self.assertRaises(TypeError):
            self.stressor.date = "2023-06-14"
        
        with self.assertRaises(TypeError):
            self.stressor.category = 2
        
        with self.assertRaises(TypeError):
            self.stressor.subcategory = 2.12
        
        with self.assertRaises(TypeError):
            self.stressor.comment = 123

    def test_vocab_checks(self):
        with self.assertRaises(ValueError):
            self.stressor.category = "invalid_category"
            self.stressor.subcategory = "invalid_subcategory"

    def test_relationship(self):
        organization = Organization()
        self.stressor.organization = organization
        self.assertEqual(self.stressor.organization, organization)
        self.assertIn(self.stressor, organization.stressors)

        del self.stressor.organization
        self.assertIsNone(self.stressor.organization)
        self.assertNotIn(self.stressor, organization.stressors)

        insider = Insider(incident_role="1")
        self.stressor.insider = insider
        self.assertEqual(self.stressor.insider, insider)
        self.assertIn(self.stressor, insider.stressors)

        del self.stressor.insider
        self.assertIsNone(self.stressor.insider)
        self.assertNotIn(self.stressor, insider.stressors)

    def test_category_subcategory_validation(self):
        with self.assertRaises(ReferenceError):
            self.stressor.subcategory = "2.12"
            del self.stressor.category
