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
from .person import Person
from pyiides.utils.helper_functions import *

class Insider(Person):
    """
    Initialize an Insider instance.

    Args:
        id (str): Unique identifier for the Job. Defaults to a new UUIDv4 string if not provided.
        incident_role (str): The insider's role in the incident. Whether the insider was the primary actor or had a different role in the incident. A constant from 
                             `incident-role-vocab <./vocab/incident-role-vocab.html>`_.
        motive (list): The insider's motive(s) for the incident. One or more constants from 
                       `motive-vocab <./vocab/motive-vocab.html>`_.
        substance_use_during_incident (bool): Indicates if the insider was using or abusing substances at the time they took one or more actions related to the incident.
        psychological_issues (list): Psychological issue(s) the insider experienced during or before the incident. One or more constants from 
                                     `psych-issues-vocab <./vocab/psych-issues-vocab.html>`_.
        predispositions (list): The insider's tendency toward certain actions or qualities. One or more array values.
        concerning_behaviors (list): The insider's history of past behavior that could indicate future issues. One or more array values.
        **kwargs (dict): Additional attributes for the Job.

    Raises:
        TypeError: If any provided attribute is of the incorrect type.
        ValueError: If any provided attribute is of the incorrect vocabulary. 
    
    Example:
        >>> from pyiides.pyiides.insider import Insider
        >>> insider = Insider(
        ...     id="123e4567-e89b-12d3-a456-426614174000",
        ...     incident_role="1",
        ...     motive=["1"],
        ...     substance_use_during_incident=True,
        ...     psychological_issues=["1"],
        ...     predispositions=[("1", "1.1")],
        ...     concerning_behaviors=[("3.1", "3.1.1")]
        ... )
        >>> print(insider.id)
        123e4567-e89b-12d3-a456-426614174000
        >>> print(insider.incident_role)
        1
    """
    def __init__(self, incident_role, id=None, motive=None, substance_use_during_incident=None, psychological_issues=None, predispositions=None, concerning_behaviors=None, **kwargs):
        # inherit everything from Person
        super().__init__(**kwargs)

        if id is None:
            id = str(uuid.uuid4())
        check_uuid(id)
        self._id = id

        check_type(incident_role, str)
        check_vocab(incident_role, 'incident-role-vocab')
        self._incident_role = incident_role

        check_type(motive, list)
        check_vocab(motive, 'motive-vocab')
        self._motive = motive

        check_type(substance_use_during_incident, bool)
        self._substance_use_during_incident = substance_use_during_incident

        check_type(psychological_issues, list)
        check_vocab(psychological_issues, 'psych-issues-vocab')
        self._psychological_issues = psychological_issues

        check_type(predispositions, list)
        check_tuple_list(predispositions, 'predisposition-type-vocab', 'predisposition-subtype-vocab')
        self._predispositions = predispositions

        check_type(concerning_behaviors, list)
        check_tuple_list(concerning_behaviors, 'concerning-behavior-vocab', 'cb-subtype-vocab')
        self._concerning_behaviors = concerning_behaviors

        # relationships
        self._incident = None
        self._sponsor = None
        self._jobs = None
        self._stressors = None
        self._accomplices = None

    def __repr__(self):
        return (f"Insider(id={self.id}, "
                f"incident_role={self.incident_role}, "
                f"motive={self.motive}, "
                f"substance_use_during_incident={self.substance_use_during_incident}, "
                f"psychological_issues={self.psychological_issues}, "
                f"predispositions={self.predispositions}, "
                f"concerning_behaviors={self.concerning_behaviors}) ")

    def to_dict(self):
        class_dict_copy = self.__dict__.copy()

        relationships = {'_incident', '_sponsor', '_jobs', '_stressors', '_accomplices'}

        children_ids = None 

        if self.jobs != None:
            children_ids = ["job--" + x.id for x in self.jobs]
        
        if self.stressors != None:
            stressors = ["stressor--" + x.id for x in self.stressors]
            if children_ids == None:
                children_ids = stressors 
            else:
                children_ids.extend(stressors)
        
        if self.accomplices != None:
            accomplices = ["accomplice--" + x.id for x in self.accomplices]
            if children_ids == None:
                children_ids = accomplices 
            else:
                children_ids.extend(accomplices)

        class_dict_copy["_id"] = f"insider--{self.id}"
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
    def incident_role(self):
        return self._incident_role
    
    @incident_role.setter
    def incident_role(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'incident-role-vocab')
        self._incident_role = value
    
    @incident_role.deleter
    def incident_role(self):
        self._incident_role = None

    @property
    def motive(self):
        return self._motive

    @motive.setter
    def motive(self, value):
        check_type(value, list, allow_none=False)
        check_vocab(value, 'motive-vocab')
        self._motive = value

    def append_motive(self, item):
        check_type(item, str, allow_none=False)
        check_vocab(item, 'motive-vocab')
        self._motive.append(item)

    @motive.deleter
    def motive(self):
        self._motive = None

    @property
    def substance_use_during_incident(self):
        return self._substance_use_during_incident

    @substance_use_during_incident.setter
    def substance_use_during_incident(self, value):
        check_type(value, bool, allow_none=False)
        self._substance_use_during_incident = value

    @substance_use_during_incident.deleter
    def substance_use_during_incident(self):
        self._substance_use_during_incident = None

    @property
    def psychological_issues(self):
        return self._psychological_issues

    @psychological_issues.setter
    def psychological_issues(self, value):
        check_type(value, list, allow_none=False)
        check_vocab(value, 'psych-issues-vocab')
        self._psychological_issues = value
    
    def append_psychological_issues(self, item):
        check_type(item, str, allow_none=False)
        check_vocab(item, 'psych-issues-vocab')
        self._psychological_issues.append(item)

    @psychological_issues.deleter
    def psychological_issues(self):
        self._psychological_issues = None

    @property
    def predispositions(self):
        return self._predispositions

    @predispositions.setter
    def predispositions(self, value):
        check_type(value, list, allow_none=False)
        check_tuple_list(value, 'predisposition-type-vocab', 'predisposition-subtype-vocab')
        self._predispositions = value
    
    def append_predispositions(self, elem):
        check_tuple_list(elem, 'predisposition-type-vocab', 'predisposition-subtype-vocab')
        self._predispositions.append(elem)

    @predispositions.deleter
    def predispositions(self):
        self._predispositions = None

    @property
    def concerning_behaviors(self):
        return self._concerning_behaviors

    @concerning_behaviors.setter
    def concerning_behaviors(self, value):
        check_type(value, list, allow_none=False)
        check_tuple_list(value, 'concerning-behavior-vocab', 'cb-subtype-vocab')
        self._concerning_behaviors = value

    def append_concerning_behaviors(self, elem):
        check_tuple_list(elem, 'concerning-behavior-vocab', 'cb-subtype-vocab')
        self._concerning_behaviors.append(elem) 

    @concerning_behaviors.deleter
    def concerning_behaviors(self):
        self._concerning_behaviors = None

    # - - - - - - - - - - RELATIONSHIPS - - - - - - - - - -
    @property
    def incident(self):
        return self._incident
    
    @incident.setter
    def incident(self, value):
        
        check_type(value, Incident, allow_none=False)
        
        # set incident 
        # first though, we need to remove old 
        # relationships if there exist any
        if self._incident != None:
            self._incident.insiders.remove(self)
        self._incident = value

        # add the insider to the incident's insider list
        if value.insiders == None:
            value.insiders = [self]
        elif self not in value.insiders:
            value.insiders.append(self)

    @incident.deleter
    def incident(self):
        if self._incident != None:
            self._incident.insiders.remove(self)
            self._incident = None
    
    @property
    def sponsor(self):
        return self._sponsor
    
    @sponsor.setter
    def sponsor(self, value):
        
        check_type(value, Sponsor, allow_none=False)
        
        # set the sponsor 
        # first though, we must remove any old relationships
        if self._sponsor != None:
            self._sponsor.insiders.remove(self)
        self._sponsor = value

        # add this insider instance to the sponsor's 
        # insiders list
        if value.insiders == None:
            value.insiders = [self]
        elif self not in value.insiders:
            value.insiders.append(self)
    
    @sponsor.deleter
    def sponsor(self):
        if self._sponsor != None:
            self._sponsor.insiders.remove(self)
            self._sponsor = None

    @property
    def jobs(self):
        return self._jobs
    
    @jobs.setter
    def jobs(self, value):
        check_type(value, list, allow_none=False)

        # check that all elements are a Job object
        for obj in value:
            
            check_type(obj, Job, allow_none=False)
        
        # set the new job list 
        # making sure to remove old relationships first
        if self._jobs != None:
            # use list() to create a copy 
            for j in list(self._jobs):
                del j.insider
        self._jobs = value

        # connect each job back to this instance 
        # of insider
        for obj in value: 
            if obj.insider != self:
                obj.insider = self
    
    def append_job(self, item):
        
        check_type(item, Job, allow_none=False)
         
        if self._jobs == None:
            self._jobs = [item]
        else:
            self._jobs.append(item)
        
        item.insider = self   
    
    def remove_job(self, item):
        
        check_type(item, Job, allow_none=False)
        if self._jobs != None:
            del item.insider    

    @jobs.deleter
    def jobs(self):
        # adding list() creates a copy so that we don't
        # run into any issues with removing elements 
        # from the list we are iterating over
        for obj in list(self._jobs):
            del obj.insider
        self._jobs = None
    
    @property
    def stressors(self):
        return self._stressors
    
    @stressors.setter
    def stressors(self, value):
        check_type(value, list, allow_none=False)

        # check that all elements are stressor objects
        for obj in value:
            
            check_type(obj, Stressor, allow_none=False)
        
        # set the new stressor list 
        # making sure to remove old relationships first
        if self._stressors != None:
            # using list() to create a copy
            for s in list(self._stressors):
                del s.insider
        self._stressors = value

        # connect those back to this instance of insider
        for obj in value: 
            if obj.insider != self:
                obj.insider = self

    def append_stressor(self, item):
        
        check_type(item, Stressor, allow_none=False)
          
        if self._stressors == None:
            self._stressors = [item]
        else:
            self._stressors.append(item)

        item.insider = self
    
    def remove_stressor(self, item):
        
        check_type(item, Stressor, allow_none=False)
        if self._stressors != None:
            del item.insider    

    @stressors.deleter
    def stressors(self):
        # adding list() creates a copy so that we don't
        # run into any issues with removing elements 
        # from the list we are iterating over
        for obj in list(self._stressors):
            del obj.insider
        self._stressors = None
    
    @property
    def accomplices(self):
        return self._accomplices
    
    @accomplices.setter
    def accomplices(self, value):
        check_type(value, list, allow_none=False)

        # check that all elements in the list are Accomplice
        # objects
        for obj in value:
            
            check_type(obj, Accomplice, allow_none=False)

        # set the accomplices list
        # making sure to remove any old relationships first
        if self._accomplices != None:
            for a in list(self._accomplices):
                del a.insider
        self._accomplices = value

        # connect each accomplice back to this insider instance
        for obj in value: 
            if obj.insider != self:
                obj.insider = self

    def append_accomplice(self, item):
        
        check_type(item, Accomplice, allow_none=False)
        
        if self._accomplices == None:
            self._accomplices = [item]
        else:
            self._accomplices.append(item)
        
        item.insider = self
    
    def remove_accomplice(self, item):
        
        check_type(item, Accomplice, allow_none=False)
        if self._accomplices != None:
            del item.insider  

    @accomplices.deleter
    def accomplices(self):
        # adding list() creates a copy so that we don't
        # run into any issues with removing elements 
        # from the list we are iterating over
        for obj in list(self._accomplices):
            del obj.insider
        self._accomplices = None
