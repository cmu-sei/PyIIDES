"""
License:
PyIIDES
Copyright 2024 Carnegie Mellon University.
NO WARRANTY. THIS CARNEGIE MELLON UNIVERSITY AND SOFTWARE ENGINEERING INSTITUTE
MATERIAL IS FURNISHED ON AN "AS-IS" BASIS. CARNEGIE MELLON UNIVERSITY MAKES NO
WARRANTIES OF ANY KIND, EITHER EXPRESSED OR IMPLIED, AS TO ANY MATTER
INCLUDING, BUT NOT LIMITED TO, WARRANTY OF FITNESS FOR PURPOSE OR
MERCHANTABILITY, EXCLUSIVITY, OR RESULTS OBTAINED FROM USE OF THE MATERIAL.
CARNEGIE MELLON UNIVERSITY DOES NOT MAKE ANY WARRANTY OF ANY KIND WITH RESPECT
TO FREEDOM FROM PATENT, TRADEMARK, OR COPYRIGHT INFRINGEMENT.
Licensed under a MIT (SEI)-style license, please see license.txt or contact
permission@sei.cmu.edu for full terms.
[DISTRIBUTION STATEMENT A] This material has been approved for public release
and unlimited distribution.  Please see Copyright notice for non-US Government
use and distribution.
DM24-1597
"""
from pyiides.utils.helper_functions import *

class Organization:
    """
    Initialize an Organization instance.
    
    Args:
        id (str): Unique identifier for the Organization. Defaults to a new UUIDv4 string if not provided.
        name (str): The name of the organization. E.g., "Company XYZ, Inc."
        city (str): The city where the organization is located. Use the address of the headquarters if the whole
                    organization was affected or use the address of the local branch if only that local branch was affected.
        state (str): The state where the organization is located. Use the address of the headquarters if the whole
                     organization was affected or use the address of the local branch if only that local branch was affected.
        country (str): The country where the organization is located. Use the address of the headquarters if the whole
                       organization was affected or use the address of the local branch if only that local branch was affected.
                       Public implementations should use the standard codes provided by ISO 3166-1 alpha-2.
        postal_code (int): The postal code of the organization. Use the address of the headquarters if the whole
                           organization was affected or use the address of the local branch if only that local branch was affected.
        small_business (bool): TRUE if the organization is a privately owned business with 500 or fewer employees.
        industry_sector (str): Top-level category for the economic sector the organization belongs to. Note, sectors
                               are derived from the North American Industry Classification System (NAICS) version 2022
                               published by the United States Office of Management and Budget. A constant from 
                               `industry-sector-vocab <./vocab/industry-sector-vocab.html>`_. Required if industry_subsector exists.
        industry_subsector (str): Second-level category for the economic sector the organization belongs to. This value
                                  MUST map back to industry_sector. E.g., if sector is "9", subsector must be "9.x". A constant
                                  from `industry-subsector-vocab <./vocab/industry-subsector-vocab.html>`_.
        business (str): Description of the organization's business.
        parent_company (str): Name of the organization's parent company, if applicable.
        incident_role (str): The organization's role in the incident. A constant from 
                             `org-role-vocab <./vocab/org-role-vocab.html>`_.
        **kwargs (dict): Additional attributes for the Organization.

    Raises:
        TypeError: If any provided attribute is of the incorrect type.
        ValueError: If any provided attribute is of the incorrect vocabulary. 
    
    Example:
        >>> organization = Organization(
        ...     id="123e4567-e89b-12d3-a456-426614174000",
        ...     name="Company XYZ, Inc.",
        ...     city="New York",
        ...     state="NY",
        ...     country="US",
        ...     postal_code=10001,
        ...     small_business=True,
        ...     industry_sector="51",
        ...     industry_subsector="51.2",
        ...     business="Software Development",
        ...     parent_company="Parent Company ABC",
        ...     incident_role="V"
        ... )
        >>> print(organization.id)
        123e4567-e89b-12d3-a456-426614174000
        >>> print(organization.name)
        Company XYZ, Inc.
    """
    def __init__(self, id=None, name=None, city=None, state=None, country=None, postal_code=None, small_business=None, industry_sector=None, industry_subsector=None, business=None, parent_company=None, incident_role=None, **kwargs):
        if id is None:
            id = str(uuid.uuid4())
        check_uuid(id)
        self._id = id

        check_type(name, str)
        self._name = name

        check_type(city, str)
        self._city = city

        check_type(state, str)
        check_vocab(state, 'state-vocab-us')
        self._state = state

        check_type(country, str)
        check_vocab(country, 'country-vocab')
        self._country = country

        check_type(postal_code, int)
        self._postal_code = postal_code

        check_type(small_business, bool)
        self._small_business = small_business

        check_type(industry_sector, str)
        check_vocab(industry_sector, 'industry-sector-vocab')
        self._industry_sector = industry_sector

        check_type(industry_subsector, str)
        check_vocab(industry_subsector, 'industry-subsector-vocab')
        check_subtype(industry_sector, industry_subsector)
        self._industry_subsector = industry_subsector

        check_type(business, str)
        self._business = business

        check_type(parent_company, str)
        self._parent_company = parent_company

        check_type(incident_role, str)
        check_vocab(kwargs.get("incident_role"), 'org-role-vocab')
        self._incident_role = incident_role

        # Relationships
        self._incident = None
        self._jobs = None
        self._stressors = None
    
    def __repr__(self):
        return (f"Organization(id={self.id}, "
                f"name={self.name}, "
                f"city={self.city}, "
                f"state={self.state}, "
                f"country={self.country}, "
                f"postal_code={self.postal_code}, "
                f"small_business={self.small_business}, "
                f"industry_sector={self.industry_sector}, "
                f"industry_subsector={self.industry_subsector}, "
                f"business={self.business}, "
                f"parent_company={self.parent_company}, "
                f"incident_role={self.incident_role})")

    def to_dict(self):
        class_dict_copy = self.__dict__.copy()

        relationships = {'_incident', '_jobs', '_stressors'}

        children_ids = None 

        if self.jobs != None:
            children_ids = ["job--" + x.id for x in self.jobs]
        
        if self.stressors != None:
            stressors = ["stressor--" + x.id for x in self.stressors]
            if children_ids == None:
                children_ids = stressors 
            else:
                children_ids.extend(stressors)
        
        class_dict_copy["_id"] = f"organization--{self.id}"
        return ({
                    key.lstrip('_'): value 
                    for key, value in class_dict_copy.items()
                    if key not in relationships
                }, children_ids)

    @property
    def id(self):
        return self._id  

    @id.setter
    def id(self, value):
        check_uuid(value)
        self._id = value
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        check_type(value, str, allow_none=False)
        self._name = value
    
    @name.deleter
    def name(self):
        self._name = None
    
    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, value):
        check_type(value, str, allow_none=False)
        self._city = value
    
    @city.deleter
    def city(self):
        self._city = None
    
    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'state-vocab-us')
        self._state = value
    
    @state.deleter
    def state(self):
        self._state = None
    
    @property
    def country(self):
        return self._country
    
    @country.setter
    def country(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'country-vocab')
        self._country = value
    
    @country.deleter
    def country(self):
        self._country = None
    
    @property
    def postal_code(self):
        return self._postal_code
    
    @postal_code.setter
    def postal_code(self, value):
        check_type(value, int, allow_none=False)
        self._postal_code = value
    
    @postal_code.deleter
    def postal_code(self):
        self._postal_code = None
    
    @property
    def small_business(self):
        return self._small_business
    
    @small_business.setter
    def small_business(self, value):
        check_type(value, bool, allow_none=False)
        self._small_business = value
    
    @small_business.deleter
    def small_business(self):
        self._small_business = None
    
    @property
    def industry_sector(self):
        return self._industry_sector
    
    @industry_sector.setter
    def industry_sector(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'industry-sector-vocab')
        self._industry_sector = value
    
    @industry_sector.deleter
    def industry_sector(self):
        self._industry_sector = None
    
    @property
    def industry_subsector(self):
        return self._industry_subsector
    
    @industry_subsector.setter
    def industry_subsector(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'industry-subsector-vocab')
        check_subtype(self._industry_sector, value)
        self._industry_subsector = value
    
    @industry_subsector.deleter
    def industry_subsector(self):
        self._industry_subsector = None
    
    @property
    def business(self):
        return self._business
    
    @business.setter
    def business(self, value):
        check_type(value, str, allow_none=False)
        self._business = value
    
    @business.deleter
    def business(self):
        self._business = None
    
    @property
    def parent_company(self):
        return self._parent_company
    
    @parent_company.setter
    def parent_company(self, value):
        check_type(value, str, allow_none=False)
        self._parent_company = value
    
    @parent_company.deleter
    def parent_company(self):
        self._parent_company = None
    
    @property
    def incident_role(self):
        return self._incident_role
    
    @incident_role.setter
    def incident_role(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'org-role-vocab')
        self._incident_role = value
    
    @incident_role.deleter
    def incident_role(self):
        self._incident_role = None

    # - - - - - - - RELATIONSHIPS - - - - - - 
    @property
    def incident(self):
        return self._incident
    
    @incident.setter
    def incident(self, value):
        
        check_type(value, Incident, allow_none=False)
        
        # set the incident
        # making sure to remove any old relationships first
        if self._incident != None:
            self._incident.organizations.remove(self)
        self._incident = value

        # add it to the incident's organization list
        if value.organizations == None:
            value.organizations = [self]
        elif self not in value.organizations:
            value.organizations.append(self)
    
    @incident.deleter
    def incident(self):
        if self._incident != None:
            self._incident.organizations.remove(self)
            self._incident = None

    @property
    def jobs(self):
        return self._jobs
    
    @jobs.setter
    def jobs(self, value):
        check_type(value, list, allow_none=False)

        # check all elements of the list are Job 
        # objects
        for obj in value:
            
            check_type(obj, Job, allow_none=False)
        
        # set new job list
        # making sure to remove any old relationships first
        if self._jobs != None:
            # use list() to create a copy
            for j in list(self._jobs):
                del j.organization
        self._jobs = value

        # connect those back to this
        # organization instance
        for obj in value: 
            if obj.organization != self:
                obj.organization = self

    def append_job(self, item):
        
        check_type(item, Job)
        
        if self._jobs == None:
            self._jobs = [item]
        else:
            self._jobs.append(item)
        
        item.organization = self
    
    def remove_job(self, item):
        
        check_type(item, Job, allow_none=False)
        if self._jobs != None:
            del item.organization    

    @jobs.deleter
    def jobs(self):
        # adding list() creates a copy so that we don't
        # run into any issues with removing elements 
        # from the list we are iterating over
        for obj in list(self._jobs):
            del obj.organization
        self._jobs = None
    
    @property
    def stressors(self):
        return self._stressors
    
    @stressors.setter
    def stressors(self, value):
        check_type(value, list, allow_none=False)

        # check that all elements are stressor object
        for obj in value:
            
            check_type(obj, Stressor, allow_none=False)
        
        # set the new stressor value 
        # making sure to delete any old relationships first
        if self._stressors != None:
            # use list() to create a copy
            for s in list(self._stressors):
                del s.organization
        self._stressors = value

        # connect those back to this organization instance
        for obj in value: 
            if obj.organization != self:
                obj.organization = self

    def append_stressor(self, item):
        
        check_type(item, Stressor)
        
        if self._stressors == None:
            self._stressors = [item]
        else:
            self._stressors.append(item)
        
        item.organization = self
    
    def remove_stressor(self, item):
        
        check_type(item, Stressor, allow_none=False)
        if self._stressors != None:
            del item.organization    

    @stressors.deleter
    def stressors(self):
        # adding list() creates a copy so that we don't
        # run into any issues with removing elements 
        # from the list we are iterating over
        for obj in list(self._stressors):
            del obj.organization
        self._stressors = None
