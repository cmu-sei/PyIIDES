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
from pyiides import Sentence
from pyiides import CourtCase

class TestSentence(unittest.TestCase):
    def setUp(self):
        self.sentence = Sentence(
            id="123e4567-e89b-12d3-a456-426614174000",
            sentence_type="1",
            quantity=5,
            metric="2",
            concurrency=True
        )

    def test_initialization(self):
        self.assertIsInstance(self.sentence.id, str)
        self.assertIsInstance(self.sentence.sentence_type, str)
        self.assertIsInstance(self.sentence.quantity, int)
        self.assertIsInstance(self.sentence.metric, str)
        self.assertIsInstance(self.sentence.concurrency, bool)

    def test_setters_and_getters(self):
        new_id = "456e7890-e12d-3a45-b678-123456789012"
        self.sentence.id = new_id
        self.assertEqual(self.sentence.id, new_id)

        new_sentence_type = "2"
        self.sentence.sentence_type = new_sentence_type
        self.assertEqual(self.sentence.sentence_type, new_sentence_type)

        new_quantity = 10
        self.sentence.quantity = new_quantity
        self.assertEqual(self.sentence.quantity, new_quantity)

        new_metric = "3"
        self.sentence.metric = new_metric
        self.assertEqual(self.sentence.metric, new_metric)

        self.sentence.concurrency = False
        self.assertFalse(self.sentence.concurrency)

    def test_deleters(self):
        del self.sentence.sentence_type
        self.assertIsNone(self.sentence.sentence_type)

        del self.sentence.quantity
        self.assertIsNone(self.sentence.quantity)

        del self.sentence.metric
        self.assertIsNone(self.sentence.metric)

        del self.sentence.concurrency
        self.assertIsNone(self.sentence.concurrency)

    def test_type_checks(self):
        with self.assertRaises(TypeError):
            self.sentence.id = 123

        with self.assertRaises(TypeError):
            self.sentence.sentence_type = 1

        with self.assertRaises(TypeError):
            self.sentence.quantity = "10"

        with self.assertRaises(TypeError):
            self.sentence.metric = 3

        with self.assertRaises(TypeError):
            self.sentence.concurrency = "True"

    def test_vocab_checks(self):
        with self.assertRaises(ValueError):
            self.sentence.sentence_type = "invalid_sentence_type"

        with self.assertRaises(ValueError):
            self.sentence.metric = "invalid_metric"

    def test_quantity_deletion(self):
        self.assertIsNotNone(self.sentence.quantity)
        self.assertIsNotNone(self.sentence.metric)

        del self.sentence.quantity
        self.assertIsNone(self.sentence.quantity)
        self.assertIsNone(self.sentence.metric)

    def test_metric_deletion(self):
        self.assertIsNotNone(self.sentence.quantity)
        self.assertIsNotNone(self.sentence.metric)

        del self.sentence.metric
        self.assertIsNone(self.sentence.quantity)
        self.assertIsNone(self.sentence.metric)
    
    def test_quantity_metric_input(self):
        del self.sentence.quantity

        self.sentence.quantity = 5  
        # will prompt for input on metric if both are none

        self.assertIsNotNone(self.sentence.quantity)
        self.assertIsNotNone(self.sentence.metric)


    def test_relationship(self):
        court_case = CourtCase()
        self.sentence.court_case = court_case
        self.assertEqual(self.sentence.court_case, court_case)
        self.assertIn(self.sentence, court_case.sentences)

        del self.sentence.court_case
        self.assertIsNone(self.sentence.court_case)
        self.assertNotIn(self.sentence, court_case.sentences)
