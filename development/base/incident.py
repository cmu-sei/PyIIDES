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
import json

class Incident:
    """
    Initialize an Incident instance.

    Args:
        id (str): Unique identifier for the incident. Defaults to a new UUIDv4 string if not provided.
        cia_effect (list): CIA triad components which were affected. One or more constants from 
                           `cia-vocab <./vocab/cia-vocab.html>`_.
        incident_type (list): Categorization of the incident. One or more constants from 
                              `incident-type-vocabulary <./vocab/incident-type-vocab.html>`_. 
                              Required if incident_subtype exists.
        incident_subtype (list): The subtype that the incident fits. MUST match the specified incident_type.
                                 One or more constants from 
                                 `incident-subtype-vocabulary <./vocab/incident-subtype-vocab.html>`_.
        outcome (list): Consequences suffered by the victim organization as a result of the insider's attack.
                        This is NOT the outcome or consequences imposed on the insider.
                        One or more constants from 
                        `outcome-type-vocabulary <./vocab/outcome-type-vocab.html>`_.
        status (str): The current status of the incident. A constant from 
                      `incident-status-vocabulary <./vocab/incident-status-vocab.html>`_.
        summary (str): A brief prose explanation of the incident. This summary should serve as a stand-alone 
                       explanation of the incident and should include the following information as a general rule: 
                       who, what, when, where, why, and how.
        brief_summary (str): A shortened version of the summary (2-4 sentences, max 500 characters) with 
                             anonymized data.
        comment (str): Clarifying details about the incident or any of the above properties.
        **kwargs (dict): Additional attributes for the incident.

    Raises:
        TypeError: If any provided attribute is of the incorrect type.
        ValueError: If any provided attribute is of the incorrect vocabulary. 
    
    Examples:
        >>> incident = Incident(
        ...     cia_effect=["C", "I"],
        ...     incident_type=["F"],
        ...     incident_subtype=["F.1"],
        ...     outcome=["BR"],
        ...     status="P",
        ...     summary="An insider incident involving data theft.",
        ...     brief_summary="Insider data theft.",
        ...     comment="Additional details about the incident."
        ... )
        >>> print(incident.id)
        123e4567-e89b-12d3-a456-426614174000
        >>> print(incident.incident_type)
        ['F']
    """
    def __init__(self, id=None, cia_effect=None, incident_type=None, incident_subtype=None, outcome=None, status=None, summary=None, brief_summary=None, comment=None, **kwargs):
        if id == None:
            id = str(uuid.uuid4())

        check_uuid(id)
        self._id = id
        
        check_type(cia_effect, list)
        check_vocab(cia_effect, 'cia-vocab')
        self._cia_effect = cia_effect

        check_type(incident_type, list)
        check_vocab(incident_type, 'incident-type-vocab')
        self._incident_type = incident_type

        check_type(incident_subtype, list)
        check_vocab(incident_subtype, 'incident-subtype-vocab')
        check_subtype_list(self._incident_type, incident_subtype)
        self._incident_subtype = incident_subtype

        check_type(outcome, list)
        check_vocab(outcome, 'outcome-type-vocab')
        self._outcome = outcome

        check_type(status, str)
        check_vocab(status, 'incident-status-vocab')
        self._status = status

        check_type(summary, str)
        self._summary = summary

        check_type(brief_summary, str)
        self._brief_summary = brief_summary

        check_type(comment, str)
        self._comment = comment

        # - - - - - - RELATIONSHIPS - - - - - - - # 
        self._detection = None
        self._response = None 
        self._ttps = None
        self._organizations = None
        self._insiders = None
        self._impacts = None
        self._targets = None
        self._notes = None
        self._sources = None

    def __repr__(self):
        return (f"Incident(id={self.id}, "
                f"cia_effect={self.cia_effect}, "
                f"incident_type={self.incident_type}, "
                f"incident_subtype={self.incident_subtype}, "
                f"outcome={self.outcome}, "
                f"status={self.status}, "
                f"summary={self.summary}, "
                f"brief_summary={self.brief_summary}, "
                f"comment={self.comment})")

    def to_dict(self):
        class_dict_copy = self.__dict__.copy()
        relationships = {'_detection', '_response', '_ttps', '_organizations', '_insiders', '_impacts', '_targets', '_notes', '_sources'}
        class_dict_copy["_id"] = f"incident--{self.id}"
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
    def cia_effect(self):
        return self._cia_effect
    
    @cia_effect.setter
    def cia_effect(self, value):
        check_type(value, list, allow_none=False)
        check_vocab(value, 'cia-vocab')
        self._cia_effect = value
    
    def append_cia(self, item):
        check_type(item, str, allow_none=False)
        check_vocab(item, 'cia-vocab')
        self._cia_effect.append(item)

    @cia_effect.deleter
    def cia_effect(self):
        self._cia_effect = None
    
    @property
    def incident_type(self):
        return self._incident_type
    
    @incident_type.setter
    def incident_type(self, value):
        check_type(value, list, allow_none=False)
        check_vocab(value, 'incident-type-vocab')
        self._incident_type = value
    
    def append_type(self, item):
        check_type(item, str, allow_none=False)
        check_vocab(item, 'incident-type-vocab')        
        self._incident_type.append(item)

    @incident_type.deleter
    def incident_type(self):
        self._incident_type = None

    @property
    def incident_subtype(self):
        return self._incident_subtype
    
    @incident_subtype.setter
    def incident_subtype(self, value):
        check_type(value, list, allow_none=False)
        check_vocab(value, 'incident-subtype-vocab')
        check_subtype_list(self._incident_type, value)
        self._incident_subtype = value
    
    def append_subtype(self, item):
        check_type(item, str, allow_none=False)
        check_vocab(item, 'incident-subtype-vocab')
        check_subtype_list(self._incident_type, item)
        self._incident_subtype.append(item)

    @incident_subtype.deleter
    def incident_subtype(self):
        self._incident_subtype = None
    
    @property 
    def outcome(self):
        return self._outcome
    
    @outcome.setter
    def outcome(self, value):
        check_type(value, list, allow_none=False)
        check_vocab(value, 'outcome-type-vocab')
        self._outcome = value
    
    def append_outcome(self, item):
        check_type(item, str, allow_none=False)
        check_vocab(item, 'outcome-type-vocab')
        self._outcome.append(item)

    @outcome.deleter
    def outcome(self):
        self._outcome = None
    
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'incident-status-vocab')
        self._status = value
    
    @status.deleter 
    def status(self):
        self._status = None
    
    @property
    def summary(self):
        return self._summary

    @summary.setter
    def summary(self, value):
        check_type(value, str, allow_none=False)
        self._summary = value
    
    @summary.deleter 
    def summary(self):
        self._summary = None
    
    @property
    def brief_summary(self):
        return self._brief_summary

    @brief_summary.setter
    def brief_summary(self, value):
        check_type(value, str, allow_none=False)
        self._brief_summary = value
    
    @brief_summary.deleter 
    def brief_summary(self):
        self._brief_summary = None
    
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

    # - - - - - - - RELATIONSHIPS - - - - - - - -

    @property
    def detection(self):
        return self._detection
    
    @detection.setter
    def detection(self, value):
        
        check_type(value, Detection, allow_none=False)
        self._detection = value
        if value.incident != self:
            value.incident = self
    
    @detection.deleter
    def detection(self):
        temp = self._detection
        self._detection = None
        if temp != None:
            del temp.incident
    
    @property
    def response(self):
        return self._response
    
    @response.setter
    def response(self, value):
        
        check_type(value, Response, allow_none=False)
        self._response = value
        if value.incident != self:
            value.incident = self 
    
    @response.deleter
    def response(self):
        temp = self._response
        self._response = None
        if temp != None:
            del temp.incident
    
    @property
    def ttps(self):
        return self._ttps
    
    @ttps.setter
    def ttps(self, value):
        check_type(value, list, allow_none=False)

        # check that all elements inside the list are
        # a TTP object
        for obj in value:
            check_type(obj, TTP, allow_none=False)
        
        # set the ttps attribute to the new list
        # if it isn't None, we want to remove all old 
        # relationships before setting the new ones
        if self._ttps != None:
            # using list() creates a copy
            for t in list(self._ttps):
                del t.incident
        self._ttps = value

        # set each incident attribute of the TTP list
        # to this instance of Incident 
        for obj in value: 
            if obj.incident != self:
                obj.incident = self

    def append_ttp(self, item):
        
        check_type(item, TTP, allow_none=False)
         
        if self._ttps == None:
            self._ttps = [item]
        else:
            self._ttps.append(item)

        item.incident = self   
    
    def remove_ttp(self, item):
        
        check_type(item, TTP, allow_none=False)
        if self._ttps != None:
            del item.incident 

    @ttps.deleter
    def ttps(self):
        # adding list() creates a copy so that we don't
        # run into any issues with removing elements 
        # from the list we are iterating over
        for obj in list(self._ttps):
            del obj.incident
        self._ttps = None
    
    @property
    def organizations(self):
        return self._organizations
    
    @organizations.setter
    def organizations(self, value):
        check_type(value, list, allow_none=False)

        # check that all elements of list are Organization objects
        for obj in value:
            
            check_type(obj, Organization, allow_none=False)
        
        # set the organizations list
        # if it is not None, then we want to remove all the old 
        # relationships
        if self._organizations != None:
            # using list() creates a copy
            for o in list(self._organizations):
                del o.incident
        self._organizations = value

        # set the rest of the relationships for the newly set
        # organizations
        for obj in value: 
            if obj.incident != self:
                obj.incident = self
    
    def append_organization(self, item):
        
        check_type(item, Organization)
        if self._organizations == None:
            self._organizations = [item]
        else:
            self._organizations.append(item)

        item.incident = self
    
    def remove_organization(self, item):
        
        check_type(item, Organization, allow_none=False)
        if self._organizations != None:
            del item.incident  

    @organizations.deleter
    def organizations(self):
        # adding list() creates a copy so that we don't
        # run into any issues with removing elements 
        # from the list we are iterating over
        for obj in list(self._organizations):
            del obj.incident
        self._organizations = None
    
    @property
    def insiders(self):
        return self._insiders
    
    @insiders.setter
    def insiders(self, value):
        check_type(value, list, allow_none=False)

        # check that all elements in this list are 
        # Insider objects 
        for obj in value:
            
            check_type(obj, Insider, allow_none=False)
        
        # set the new insider list:
        # if a insiders list already exists, we want
        # to remove the relationships before setting  
        # a new one
        if self._insiders != None:
            # using list() creates a copy
            for i in list(self._insiders):
                del i.incident
        self._insiders = value

        # connect each insider object to this instance
        # of the incident
        for obj in value: 
            if obj.incident != self:
                obj.incident = self

    def append_insider(self, item):
        
        check_type(item, Insider, allow_none=False)
        if self._insiders == None:
            self._insiders = [item]
        else:
            self._insiders.append(item)
        
        item.incident = self
    
    def remove_insider(self, item):
        
        check_type(item, Insider, allow_none=False)
        if self._insiders != None:
            del item.incident  

    @insiders.deleter
    def insiders(self):
        # adding list() creates a copy so that we don't
        # run into any issues with removing elements 
        # from the list we are iterating over
        for obj in list(self._insiders):
            del obj.incident
        self._insiders = None
    
    @property
    def impacts(self):
        return self._impacts
    
    @impacts.setter
    def impacts(self, value):
        check_type(value, list, allow_none=False)

        # check that all elements in the list are
        # Impact objects
        for obj in value:
            
            check_type(obj, Impact, allow_none=False)
        
        # set the new impact list:
        # making sure to remove all old relationships first
        if self._impacts != None:
            # using list() creates a copy
            for i in list(self._impacts):
                del i.incident
        self._impacts = value

        # connect each impact to this incident instance
        for obj in value: 
            if obj.incident != self:
                obj.incident = self

    def append_impact(self, item):
        
        check_type(item, Impact, allow_none=False)
        if self._impacts == None:
            self._impacts = [item]
        else:
            self._impacts.append(item)
        
        item.incident = self
    
    def remove_impact(self, item):
        
        check_type(item, Impact, allow_none=False)
        if self._impacts != None:
            del item.incident  

    @impacts.deleter
    def impacts(self):
        # adding list() creates a copy so that we don't
        # run into any issues with removing elements 
        # from the list we are iterating over
        for obj in list(self._impacts):
            del obj.incident
        self._impacts = None

    @property
    def targets(self):
        return self._targets
    
    @targets.setter
    def targets(self, value):
        check_type(value, list, allow_none=False)

        # check that all elements are target objects 
        for obj in value:
            
            check_type(obj, Target, allow_none=False)
        
        # set the new targets list:
        # making sure to remove old relationships first
        if self._targets != None:
            # using list() creates a copy
            for t in list(self._targets):
                del t.incident
        self._targets = value

        # connect those back to this instance of incident
        for obj in value: 
            if obj.incident != self:
                obj.incident = self

    def append_target(self, item):
        
        check_type(item, Target, allow_none=False)
        if self._targets == None:
            self._targets = [item]
        else:
            self._targets.append(item)
        
        item.incident = self
    
    def remove_target(self, item):
        
        check_type(item, Target, allow_none=False)
        if self._targets != None:
            del item.incident  

    @targets.deleter
    def targets(self):
        # adding list() creates a copy so that we don't
        # run into any issues with removing elements 
        # from the list we are iterating over
        for obj in list(self._targets):
            del obj.incident
        self._targets = None

    
    # - - - - - - -
    @property
    def notes(self):
        return self._notes
    
    @notes.setter
    def notes(self, value):
        check_type(value, list, allow_none=False)

        # check that all elements are target objects 
        for obj in value:
            
            check_type(obj, Note, allow_none=False)
        
        # set the new notes list:
        # making sure to remove old relationships first
        if self._notes != None:
            # using list() creates a copy
            for t in list(self._notes):
                del t.incident
        self._notes = value

        # connect those back to this instance of incident
        for obj in value: 
            if obj.incident != self:
                obj.incident = self

    def append_note(self, item):
        
        check_type(item, Note, allow_none=False)
        if self._notes == None:
            self._notes = [item]
        else:
            self._notes.append(item)
        
        item.incident = self
    
    def remove_note(self, item):
        
        check_type(item, Note, allow_none=False)
        if self._notes != None:
            del item.incident  

    @notes.deleter
    def notes(self):
        # adding list() creates a copy so that we don't
        # run into any issues with removing elements 
        # from the list we are iterating over
        for obj in list(self._notes):
            del obj.incident
        self._notes = None
    
    # - - - - - - -
    @property
    def sources(self):
        return self._sources
    
    @sources.setter
    def sources(self, value):
        check_type(value, list, allow_none=False)

        # check that all elements are target objects 
        for obj in value:
            
            check_type(obj, Source, allow_none=False)
        
        # set the new sources list:
        # making sure to remove old relationships first
        if self._sources != None:
            # using list() creates a copy
            for t in list(self._sources):
                del t.incident
        self._sources = value

        # connect those back to this instance of incident
        for obj in value: 
            if obj.incident != self:
                obj.incident = self

    def append_source(self, item):
        
        check_type(item, Source, allow_none=False)
        if self._sources == None:
            self._sources = [item]
        else:
            self._sources.append(item)
        
        item.incident = self
    
    def remove_source(self, item):
        
        check_type(item, Source, allow_none=False)
        if self._sources != None:
            del item.incident  

    @sources.deleter
    def sources(self):
        # adding list() creates a copy so that we don't
        # run into any issues with removing elements 
        # from the list we are iterating over
        for obj in list(self._sources):
            del obj.incident
        self._sources = None
