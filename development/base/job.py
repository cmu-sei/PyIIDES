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
from datetime import date as dt
from datetime import timedelta

class Job:
    """
    Initialize a Job instance.

    Args:
        id (str): Unique identifier for the Job. Defaults to a new UUIDv4 string if not provided.
        job_function (str): Functional category of the individual's job. Based on the 2018 Standard Occupational Classification system published by the Bureau of Labor Statistics. A constant from 
                            `job-function-vocab <./vocab/job-function-vocab.html>`_. Required if occupation exists.
        occupation (str): The subcategory of the individual's job. Must match the constant for job_function. A constant from 
                          `occupation-vocab <./vocab/occupation-vocab.html>`_. Required if title exists.
        title (str): The individual's job title. If title is specified, occupation should be as well.
        position_technical (bool): The individual had access to technical areas of the organization as part of their job role. E.g. IT admin, network engineer, help desk associate, etc.
        access_authorization (str): The level of access control given by this job role. A constant from 
                                    `access-auth-vocab <./vocab/access-auth-vocab.html>`_.
        employment_type (str): The individual's employment arrangement at the time of the incident. A constant from 
                               `employment-type-vocab <./vocab/employment-type-vocab.html>`_.
        hire_date (date): Date the individual is hired into this position.
        departure_date (date): Date the individual departed from this position.
        tenure (timedelta): The amount of time the individual spent in this particular job role.
        comment (str): Clarifying comments or details about the job or the individual's employment with the organization.
        **kwargs (dict): Additional attributes for the Job.

    Raises:
        TypeError: If any provided attribute is of the incorrect type.
        ValueError: If any provided attribute is of the incorrect vocabulary. 
    
    Example:
        >>> job = Job(
        ...     id="123e4567-e89b-12d3-a456-426614174000",
        ...     job_function="15",
        ...     occupation="15.1",
        ...     title="Software Developer",
        ...     position_technical=True,
        ...     access_authorization="2",
        ...     employment_type="FLT",
        ...     hire_date=date(2020, 1, 1),
        ...     departure_date=date(2023, 1, 1),
        ...     tenure=timedelta(days=1096),
        ...     comment="This is a comment"
        ... )
        >>> print(job.id)
        123e4567-e89b-12d3-a456-426614174000
        >>> print(job.title)
        Software Developer
        >>> print(access_authorization)
        2
    """
    def __init__(self, id=None, job_function=None, occupation=None, title=None, position_technical=None, access_authorization=None, employment_type=None, hire_date=None, departure_date=None, tenure=None, comment=None, **kwargs):
        if id is None:
            id = str(uuid.uuid4())
        check_uuid(id)
        self._id = id

        check_type(job_function, str)
        check_vocab(job_function, 'job-function-vocab')
        self._job_function = job_function

        check_type(occupation, str)
        check_vocab(occupation, 'occupation-vocab')
        check_subtype(self._job_function, occupation)
        self._occupation = occupation

        check_type(title, str)
        self._title = title

        check_type(position_technical, bool)
        self._position_technical = position_technical

        check_type(access_authorization, str)
        check_vocab(access_authorization, 'access-auth-vocab')
        self._access_authorization = access_authorization

        check_type(employment_type, str)
        check_vocab(employment_type, 'employment-type-vocab')
        self._employment_type = employment_type

        check_type(hire_date, dt)
        self._hire_date = hire_date
        
        check_type(departure_date, dt)
        self._departure_date = departure_date

        check_type(tenure, timedelta)
        check_tenure(self._hire_date, self._departure_date, tenure)
        self._tenure = tenure
        
        check_type(comment, str)
        self._comment = comment

        # Relationships 
        self._organization = None
        self._insider = None
        self._accomplice = None
    
    def __repr__(self):
        return (f"Job(id={self.id}, "
                f"job_function={self.job_function}, "
                f"occupation={self.occupation}, "
                f"title={self.title}, "
                f"position_technical={self.position_technical}, "
                f"access_authorization={self.access_authorization}, "
                f"employment_type={self.employment_type}, "
                f"hire_date={self.hire_date}, "
                f"departure_date={self.departure_date}, "
                f"tenure={self.tenure}, "
                f"comment={self.comment})")

    def to_dict(self):
        class_dict_copy = self.__dict__.copy()
        relationships = {'_organization', '_insider', '_accomplice'}
        self.__dict__["id"] = f"job--{self.id}"

        if self.hire_date != None:
            class_dict_copy["_hire_date"] = str(self.hire_date)
        
        if self.departure_date != None:
            class_dict_copy["_departure_date"] = str(self.departure_date)

        if self.tenure != None:
            class_dict_copy["_tenure"] = str(self.tenure)

        return ({
                    key.lstrip('_'): value 
                    for key, value in class_dict_copy.items()
                    if key not in relationships
                }, None)

    @property
    def id(self):
        return self._id  

    @id.setter
    def id(self, value):
        check_uuid(value)
        self._id = value

    @property
    def job_function(self):
        return self._job_function

    @job_function.setter
    def job_function(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'job-function-vocab')
        self._job_function = value
    
    @job_function.deleter
    def job_function(self):
        self._job_function = None

    @property
    def occupation(self):
        return self._occupation

    @occupation.setter
    def occupation(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'occupation-vocab')
        self._occupation = value
    
    @occupation.deleter
    def occupation(self):
        self._occupation = None

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        check_type(value, str, allow_none=False)
        self._title = value

    @title.deleter
    def title(self):
        self._title = None

    @property
    def position_technical(self):
        return self._position_technical

    @position_technical.setter
    def position_technical(self, value):
        check_type(value, bool, allow_none=False)
        self._position_technical = value
    
    @position_technical.deleter
    def position_technical(self):
        self._position_technical = None

    @property
    def access_authorization(self):
        return self._access_authorization

    @access_authorization.setter
    def access_authorization(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'access-auth-vocab')
        self._access_authorization = value
    
    @access_authorization.deleter
    def access_authorization(self):
        self._access_authorization = None

    @property
    def employment_type(self):
        return self._employment_type

    @employment_type.setter
    def employment_type(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'employment-type-vocab')
        self._employment_type = value
    
    @employment_type.deleter
    def employment_type(self):
        self._employment_type = None
    
    @property 
    def hire_date(self):
        return self._hire_date

    @hire_date.setter
    def hire_date(self, value):   
        check_type(value, dt, allow_none=False)
        self._hire_date = value
        if (self._hire_date != None and self._departure_date != None):
            self._tenure = self._departure_date - self._hire_date
    
    @hire_date.deleter
    def hire_date(self):
        self._hire_date = None

    @property
    def departure_date(self):
        return self._departure_date

    @departure_date.setter
    def departure_date(self, value):
        check_type(value, dt, allow_none=False)
        self._departure_date = value
        if (self._hire_date != None and self._departure_date != None):
            self._tenure = self._departure_date - self._hire_date
    
    @departure_date.deleter
    def departure_date(self):
        self._departure_date = None
    
    @property
    def tenure(self):
        return self._tenure

    @tenure.setter
    def tenure(self, value):
        check_type(value, timedelta, allow_none=False)
        if (self._hire_date == None or self._departure_date == None):
            raise ReferenceError("You must set the hire date and departure date in order to set the tenure")
        td = self._departure_date - self._hire_date
        if (td != value):
            raise ValueError("Incorrect value for the given hire date and departure date")
        self._tenure = value
    
    @tenure.deleter
    def tenure(self):
        self._tenure = None
    
    @property
    def comment(self):
        return self._comment
    
    @comment.setter
    def comment(self, value):
        check_type(value, str, allow_none=False)
        self._comment = value

    @comment.deleter
    def comment(self):
        self._comment = None

    # - - - - - - - RELATIONSHIPS - - - - - - 
    @property
    def organization(self):
        return self._organization
    
    @organization.setter
    def organization(self, value):
        
        check_type(value, Organization, allow_none=False)
        
        # set the organization 
        # making sure to remove any old relationships first
        if self._organization != None:
            self._organization.jobs.remove(self)
        self._organization = value

        # add it to the organization's job list
        if value.jobs == None:
            value.jobs = [self]
        elif self not in value.jobs: 
            value.jobs.append(self)
    
    @organization.deleter
    def organization(self):
        if self._organization != None:
            self._organization.jobs.remove(self)
            self._organization = None
    
    @property
    def insider(self):
        return self._insider
    
    @insider.setter
    def insider(self, value):
        
        check_type(value, Insider, allow_none=False)
        
        # set the insider 
        # making sure to remove any old relationships first
        if self._insider != None:
            self._insider.jobs.remove(self)
        self._insider = value

        # add it to the insiders's job list
        if value.jobs == None:
            value.jobs = [self]
        elif self not in value.jobs: 
            value.jobs.append(self)
    
    @insider.deleter
    def insider(self):
        if self._insider != None:
            self._insider.jobs.remove(self)
            self._insider = None

    @property
    def accomplice(self):
        return self._accomplice
    
    @accomplice.setter
    def accomplice(self, value):
        
        check_type(value, Accomplice, allow_none=False)
        
        # set the accomplice
        # making sure to remove old relationships first
        if self._accomplice != None:
            self._accomplice.jobs.remove(self)
        self._accomplice = value

        # add it to the insiders's job list
        if value.jobs == None:
            value.jobs = [self]
        elif self not in value.jobs: 
            value.jobs.append(self)
    
    @accomplice.deleter
    def accomplice(self):
        if self._accomplice != None:
            self._accomplice.jobs.remove(self)
            self._accomplice = None
