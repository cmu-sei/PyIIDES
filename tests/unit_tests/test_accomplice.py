"""
License:
PyIIDES
Copyright 2024 Carnegie Mellon University.
NO WARRANTY. THIS CARNEGIE MELLON UNIVERSITY AND SOFTWARE ENGINEERING INSTITUTE MATERIAL IS FURNISHED ON AN "AS-IS" BASIS. CARNEGIE MELLON UNIVERSITY MAKES NO WARRANTIES OF ANY KIND, EITHER EXPRESSED OR IMPLIED, AS TO ANY MATTER INCLUDING, BUT NOT LIMITED TO, WARRANTY OF FITNESS FOR PURPOSE OR MERCHANTABILITY, EXCLUSIVITY, OR RESULTS OBTAINED FROM USE OF THE MATERIAL. CARNEGIE MELLON UNIVERSITY DOES NOT MAKE ANY WARRANTY OF ANY KIND WITH RESPECT TO FREEDOM FROM PATENT, TRADEMARK, OR COPYRIGHT INFRINGEMENT.
Licensed under a MIT (SEI)-style license, please see license.txt or contact permission@sei.cmu.edu for full terms.
[DISTRIBUTION STATEMENT A] This material has been approved for public release and unlimited distribution.  Please see Copyright notice for non-US Government use and distribution.
DM24-1597
"""
import unittest, uuid, sys, os
sys.path.append(os.getcwd())
from pyiides import Accomplice, Sponsor, Insider, Job


class TestAccomplice(unittest.TestCase):

    def setUp(self):
        self.accomplice = Accomplice(
            id=str(uuid.uuid4()),  # UUID
            relationship_to_insider="1"  # Acquaintance
        )

    # Initialization test
    def test_initialization(self):
        self.assertTrue(uuid.UUID(self.accomplice.id))  # Validate UUID format
        self.assertEqual(self.accomplice.relationship_to_insider, "1")

    # Test setters
    def test_setters(self):
        new_uuid = str(uuid.uuid4())
        self.accomplice.id = new_uuid
        self.assertEqual(self.accomplice.id, new_uuid)

        self.accomplice.relationship_to_insider = "2"  # Colleague
        self.assertEqual(self.accomplice.relationship_to_insider, "2")

    # Type checking
    def test_type_checking(self):
        with self.assertRaises(TypeError):
            self.accomplice.id = 123

        with self.assertRaises(TypeError):
            self.accomplice.relationship_to_insider = ["1"]

    # Vocab Checking
    def test_vocab_checking_relationship_to_insider(self):
        valid_relationships = ["1", "2", "3", "4", "5", "6", "8", "9"]
        for relationship in valid_relationships:
            accomplice = Accomplice(relationship_to_insider=relationship)
            self.assertEqual(accomplice.relationship_to_insider, relationship)

        with self.assertRaises(ValueError):
            self.accomplice.relationship_to_insider = "unknown"

    # Test delete function
    def test_delete_functions(self):
        del self.accomplice.relationship_to_insider
        self.assertIsNone(self.accomplice.relationship_to_insider)
    
class TestAccompliceRelationships(unittest.TestCase):

    def setUp(self):
        self.accomplice = Accomplice()

    def test_insider_relationship(self):
        insider = Insider(incident_role="1")
        
        # Test setting insider
        self.accomplice.insider = insider
        self.assertEqual(self.accomplice.insider, insider)
        self.assertIn(self.accomplice, insider.accomplices)

        # Test changing insider
        new_insider = Insider(incident_role="1")
        self.accomplice.insider = new_insider
        self.assertEqual(self.accomplice.insider, new_insider)
        self.assertIn(self.accomplice, new_insider.accomplices)
        self.assertNotIn(self.accomplice, insider.accomplices)

        # Test deleting insider
        del self.accomplice.insider
        self.assertIsNone(self.accomplice.insider)
        self.assertNotIn(self.accomplice, new_insider.accomplices)

    def test_jobs_relationship(self):
        job1 = Job()
        job2 = Job()

        # Test setting jobs
        self.accomplice.jobs = [job1, job2]
        self.assertEqual(len(self.accomplice.jobs), 2)
        self.assertIn(job1, self.accomplice.jobs)
        self.assertIn(job2, self.accomplice.jobs)
        self.assertEqual(job1.accomplice, self.accomplice)
        self.assertEqual(job2.accomplice, self.accomplice)

        # Test appending a job
        job3 = Job()
        self.accomplice.append_job(job3)
        self.assertEqual(len(self.accomplice.jobs), 3)
        self.assertIn(job3, self.accomplice.jobs)
        self.assertEqual(job3.accomplice, self.accomplice)

        # Test removing a job
        self.accomplice.remove_job(job2)
        self.assertEqual(len(self.accomplice.jobs), 2)
        self.assertNotIn(job2, self.accomplice.jobs)
        self.assertIsNone(job2.accomplice)

        # Test deleting all jobs
        del self.accomplice.jobs
        self.assertIsNone(self.accomplice.jobs)
        self.assertIsNone(job1.accomplice)
        self.assertIsNone(job3.accomplice)

    def test_sponsor_relationship(self):
        sponsor = Sponsor()

        # Test setting sponsor
        self.accomplice.sponsor = sponsor
        self.assertEqual(self.accomplice.sponsor, sponsor)
        self.assertIn(self.accomplice, sponsor.accomplices)

        # Test changing sponsor
        new_sponsor = Sponsor()
        self.accomplice.sponsor = new_sponsor
        self.assertEqual(self.accomplice.sponsor, new_sponsor)
        self.assertIn(self.accomplice, new_sponsor.accomplices)
        self.assertNotIn(self.accomplice, sponsor.accomplices)

        # Test deleting sponsor
        del self.accomplice.sponsor
        self.assertIsNone(self.accomplice.sponsor)
        self.assertNotIn(self.accomplice, new_sponsor.accomplices)
    
    def test_set_jobs(self):
        job1 = Job()
        job2 = Job()
        job3 = Job()
        job4 = Job()

        self.accomplice.jobs = [job1, job2]
        self.assertEqual(job1.accomplice, self.accomplice)
        self.assertEqual(job2.accomplice, self.accomplice)
        self.assertIn(job1, self.accomplice.jobs)
        self.assertIn(job2, self.accomplice.jobs)

        self.accomplice.jobs = [job3, job4]
        self.assertIsNone(job1.accomplice)
        self.assertIsNone(job2.accomplice)
        self.assertNotIn(job1, self.accomplice.jobs)
        self.assertNotIn(job2, self.accomplice.jobs)
        self.assertEqual(job3.accomplice, self.accomplice)
        self.assertEqual(job4.accomplice, self.accomplice)
        self.assertIn(job3, self.accomplice.jobs)
        self.assertIn(job4, self.accomplice.jobs)