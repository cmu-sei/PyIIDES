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
sys.path.append(os.getcwd())
from pyiides import Organization, Stressor, Job, Incident

class TestOrganization(unittest.TestCase):

    def setUp(self):
        self.organization = Organization(
            id="123e4567-e89b-12d3-a456-426614174000",
            name="Company XYZ, Inc.",
            city="New York",
            state="NY",
            country="US",
            postal_code=10001,
            small_business=True,
            industry_sector="51",
            industry_subsector="51.2",
            business="Software Development",
            parent_company="Parent Company ABC",
            incident_role="V"
        )

    # Initialization test
    def test_initialization(self):
        self.assertEqual(self.organization.id, "123e4567-e89b-12d3-a456-426614174000")
        self.assertEqual(self.organization.name, "Company XYZ, Inc.")
        self.assertEqual(self.organization.city, "New York")
        self.assertEqual(self.organization.state, "NY")
        self.assertEqual(self.organization.country, "US")
        self.assertEqual(self.organization.postal_code, 10001)
        self.assertTrue(self.organization.small_business)
        self.assertEqual(self.organization.industry_sector, "51")
        self.assertEqual(self.organization.industry_subsector, "51.2")
        self.assertEqual(self.organization.business, "Software Development")
        self.assertEqual(self.organization.parent_company, "Parent Company ABC")
        self.assertEqual(self.organization.incident_role, "V")

    # Test setters
    def test_setters(self):
        self.organization.name = "New Company"
        self.assertEqual(self.organization.name, "New Company")

        self.organization.city = "Los Angeles"
        self.assertEqual(self.organization.city, "Los Angeles")

        self.organization.state = "CA"
        self.assertEqual(self.organization.state, "CA")

        self.organization.country = "CA"
        self.assertEqual(self.organization.country, "CA")

        self.organization.postal_code = 90001
        self.assertEqual(self.organization.postal_code, 90001)

        self.organization.small_business = False
        self.assertFalse(self.organization.small_business)

        self.organization.industry_sector = "52"
        self.assertEqual(self.organization.industry_sector, "52")

        self.organization.industry_subsector = "52.1"
        self.assertEqual(self.organization.industry_subsector, "52.1")

        self.organization.business = "Financial Services"
        self.assertEqual(self.organization.business, "Financial Services")

        self.organization.parent_company = "New Parent Company"
        self.assertEqual(self.organization.parent_company, "New Parent Company")

        self.organization.incident_role = "T"
        self.assertEqual(self.organization.incident_role, "T")

    # Type checking
    def test_type_checking(self):
        with self.assertRaises(TypeError):
            self.organization.id = 123

        with self.assertRaises(TypeError):
            self.organization.postal_code = "10001"

        with self.assertRaises(TypeError):
            self.organization.small_business = "True"

    # Vocab Checking
    def test_vocab_checking_industry_sector(self):
        valid_industry_sectors = ["11", "22", "23", "31", "42", "44", "48", "51", "52", "53", "54", "55", "56", "61", "62", "71", "72", "81", "92", "99"]
        for sector in valid_industry_sectors:
            organization = Organization(industry_sector=sector)
            self.assertEqual(organization.industry_sector, sector)

        with self.assertRaises(ValueError):
            self.organization.industry_sector = "invalid"

    def test_vocab_checking_industry_subsector(self):
        valid_industry_subsectors = ["11.1", "11.2", "11.3", "11.4", "11.5", "21.1", "21.2", "21.3", "22.1", "23.6", "23.7", "23.8", "31.1", "31.2", "31.3", "31.4", "31.5", "31.6", "31.21", "31.22", "31.23", "31.24", "31.25", "31.26", "31.27", "31.31", "31.32", "31.33", "31.34", "31.35", "31.36", "31.37", "31.39", "42.3", "42.4", "42.5", "44.1", "44.4", "44.5", "44.9", "44.55", "44.56", "44.57", "44.58", "44.59", "48.1", "48.2", "48.3", "48.4", "48.5", "48.6", "48.7", "48.8", "48.91", "48.92", "48.93", "51.2", "51.3", "51.6", "51.7", "51.8", "51.9", "52.1", "52.2", "52.3", "52.4", "52.5", "53.1", "53.2", "53.3", "54.1", "55.1", "56.1", "56.2", "61.1", "62.1", "62.2", "62.3", "62.4", "71.1", "71.2", "71.3", "72.1", "72.2", "81.1", "81.2", "81.3", "81.4", "92.1", "92.2", "92.3", "92.4", "92.5", "92.6", "92.7", "92.811", "92.812"]
        for subsector in valid_industry_subsectors:
            organization = Organization(industry_sector=subsector[0:subsector.find('.')], industry_subsector=subsector)
            self.assertEqual(organization.industry_subsector, subsector)

        with self.assertRaises(ValueError):
            self.organization.industry_subsector = "invalid"

    def test_vocab_checking_incident_role(self):
        valid_incident_roles = ["B", "V", "S", "T", "O"]
        for role in valid_incident_roles:
            organization = Organization(incident_role=role)
            self.assertEqual(organization.incident_role, role)

        with self.assertRaises(ValueError):
            self.organization.incident_role = "invalid"

    # Test delete function
    def test_delete_functions(self):
        del self.organization.name
        self.assertIsNone(self.organization.name)

        del self.organization.city
        self.assertIsNone(self.organization.city)

        del self.organization.state
        self.assertIsNone(self.organization.state)

        del self.organization.country
        self.assertIsNone(self.organization.country)

        del self.organization.postal_code
        self.assertIsNone(self.organization.postal_code)

        del self.organization.small_business 
        self.assertIsNone(self.organization.small_business)

        del self.organization.industry_sector
        self.assertIsNone(self.organization.industry_sector)

        del self.organization.industry_subsector
        self.assertIsNone(self.organization.industry_subsector)

        del self.organization.business
        self.assertIsNone(self.organization.business)

        del self.organization.parent_company
        self.assertIsNone(self.organization.parent_company)

        del self.organization.incident_role 
        self.assertIsNone(self.organization.incident_role)


    # Test remove function
    def test_remove_functions(self):
        self.organization.name = "Company XYZ, Inc."
        del self.organization.name 
        self.assertIsNone(self.organization.name)

        self.organization.city = "New York"
        del self.organization.city 
        self.assertIsNone(self.organization.city)

        self.organization.state = "NY"
        del self.organization.state
        self.assertIsNone(self.organization.state)

        self.organization.country = "US"
        del self.organization.country
        self.assertIsNone(self.organization.country)

        self.organization.postal_code = 10001
        del self.organization.postal_code 
        self.assertIsNone(self.organization.postal_code)

        self.organization.small_business = True
        del self.organization.small_business
        self.assertIsNone(self.organization.small_business)

        self.organization.industry_subsector = "51.2"
        del self.organization.industry_subsector
        self.assertIsNone(self.organization.industry_subsector)

        self.organization.industry_sector = "51"
        del self.organization.industry_sector 
        self.assertIsNone(self.organization.industry_sector)

        self.organization.business = "Software Development"
        del self.organization.business 
        self.assertIsNone(self.organization.business)

        self.organization.parent_company = "Parent Company ABC"
        del self.organization.parent_company
        self.assertIsNone(self.organization.parent_company)

        self.organization.incident_role = "V"
        del self.organization.incident_role
        self.assertIsNone(self.organization.incident_role)
    
    def test_incident_relationship(self):
        incident = Incident()
        self.organization.incident = incident
        self.assertEqual(self.organization.incident, incident)
        self.assertIn(self.organization, incident.organizations)

        del self.organization.incident
        self.assertIsNone(self.organization.incident)
        self.assertNotIn(self.organization, incident.organizations)

    def test_jobs_relationship(self):
        job1 = Job()
        job2 = Job()
        self.organization.jobs = [job1, job2]
        self.assertEqual(self.organization.jobs, [job1, job2])
        self.assertEqual(job1.organization, self.organization)
        self.assertEqual(job2.organization, self.organization)

        job3 = Job()
        self.organization.append_job(job3)
        self.assertEqual(len(self.organization.jobs), 3)
        self.assertIn(job3, self.organization.jobs)

        job_to_remove = self.organization.jobs[0]
        self.organization.remove_job(job_to_remove)
        self.assertNotIn(job_to_remove, self.organization.jobs)

        del self.organization.jobs
        self.assertIsNone(self.organization.jobs)

    def test_stressors_relationship(self):
        stressor1 = Stressor()
        stressor2 = Stressor()
        self.organization.stressors = [stressor1, stressor2]
        self.assertEqual(self.organization.stressors, [stressor1, stressor2])
        self.assertEqual(stressor1.organization, self.organization)
        self.assertEqual(stressor2.organization, self.organization)

        stressor3 = Stressor()
        self.organization.append_stressor(stressor3)
        self.assertEqual(len(self.organization.stressors), 3)
        self.assertIn(stressor3, self.organization.stressors)

        stressor_to_remove = self.organization.stressors[0]
        self.organization.remove_stressor(stressor_to_remove)
        self.assertNotIn(stressor_to_remove, self.organization.stressors)

        del self.organization.stressors
        self.assertIsNone(self.organization.stressors)