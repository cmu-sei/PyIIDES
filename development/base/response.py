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

class Response:
    """
    Initialize a Response instance.

    Args:
        id (str): Unique identifier for the response. Defaults to a new UUIDv4 string if not provided.
        technical_controls (list): Controls put in place to limit or monitor the insider's access to devices, data,
                                   or the network, or to limit/monitor network/device access for the user population more generally. One or more list values.
        behavioral_controls (list): Controls put in place to limit, monitor, or correct the insider's behavior
                                    within the organization. One or more list values.
        investigated_by (list): The organization(s) or entity(s) that investigated the incident.
                                One or more constants from 
                                `investigator-vocab <./vocab/investigator-vocab.html>`_.
        investigation_events (list): Specific events that happened during the course of the investigation into the incident.
                                     One or more array values.
        comment (str): Clarifying comments or additional details about the organization's response.
        **kwargs (dict): Additional attributes for the response.

    Raises:
        TypeError: If any provided attribute is of the incorrect type.
        ValueError: If any provided attribute is of the incorrect vocabulary. 
    
    Example:
        >>> response = Response(
        ...     id="123e4567-e89b-12d3-a456-426614174000",
        ...     technical_controls=[("1", date(2023, 1, 1))],
        ...     behavioral_controls=[("4", date(2023, 1, 2))],
        ...     investigated_by=["1", "2"],
        ...     investigation_events=[("2", date(2023, 1, 3))],
        ...     comment="Initial comment"
        ... )
        >>> print(response.id)
        123e4567-e89b-12d3-a456-426614174000
        >>> print(response.technical_controls)
        [("1", "2023-01-01")]
    """
    def __init__(self, id=None, technical_controls=None, behavioral_controls=None, investigated_by=None, investigation_events=None, comment=None, **kwargs):
        if id == None:
            id = str(uuid.uuid4())

        check_uuid(id)
        self._id = id

        check_type(technical_controls, list)
        check_vocab(technical_controls, 'technical-control-vocab')
        self._technical_controls = technical_controls

        check_type(behavioral_controls, list)
        check_vocab(behavioral_controls, 'behavioral-control-vocab')
        self._behavioral_controls = behavioral_controls

        check_type(investigated_by, list)
        check_vocab(investigated_by, 'investigator-vocab')
        self._investigated_by = investigated_by

        check_type(investigation_events, list)
        check_vocab(investigation_events, 'investigation-vocab')
        self._investigation_events = investigation_events

        check_type(comment, str)
        self._comment = comment

        # RELATIONSHIPS
        self._incident = None    # belongs to incident
        self._legal_response = None

    def __repr__(self):
        return (f"Response(id={self.id}, "
                f"technical_controls={self.technical_controls}, "
                f"behavioral_controls={self.behavioral_controls}, "
                f"investigated_by={self.investigated_by}, "
                f"investigation_events={self.investigation_events}, "
                f"comment={self.comment})")

    def to_dict(self):
        class_dict_copy = self.__dict__.copy()
        relationships = {'_incident', '_legal_response'}

        if self.technical_controls != None:
            for (_, date) in class_dict_copy["_technical_controls"]:
                date = str(date)
                
        if self.behavioral_controls != None:
            for (_, date) in class_dict_copy["_behavioral_controls"]:
                date = str(date)
        
        if self.investigation_events != None:
            for (_, date) in class_dict_copy["_investigation_events"]:
                date = str(date)

        class_dict_copy["_id"] = f"response--{self.id}"
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
    def technical_controls(self):
        return self._technical_controls
    
    @technical_controls.setter
    def technical_controls(self, value):
        check_type(value, list, allow_none=False)
        check_vocab(value, 'technical-control-vocab')
        self._technical_controls = value
    
    def append_technical_controls(self, item):
        check_type(item, tuple, allow_none=False)
        check_vocab(item, 'technical-control-vocab')
        self._technical_controls.append(item)
    
    @technical_controls.deleter
    def technical_controls(self):
        self._technical_controls = None
    
    @property
    def behavioral_controls(self):
        return self._behavioral_controls
    
    @behavioral_controls.setter
    def behavioral_controls(self, value):
        check_type(value, list, allow_none=False)
        check_vocab(value, 'behavioral-control-vocab')
        self._behavioral_controls = value
    
    def append_behavioral_controls(self, item):
        check_type(item, tuple, allow_none=False)
        check_vocab(item, 'behavioral-control-vocab')
        self._behavioral_controls.append(item)
    
    @behavioral_controls.deleter
    def behavioral_controls(self):
        self._behavioral_controls = None

    @property
    def investigated_by(self):
        return self._investigated_by
    
    @investigated_by.setter
    def investigated_by(self, value):
        check_type(value, list, allow_none=False)
        check_vocab(value, 'investigator-vocab')
        self._investigated_by = value
    
    def append_investigated_by(self, item):
        check_type(item, str, allow_none=False)
        check_vocab(item, 'investigator-vocab')
        self._investigated_by.append(item)

    @investigated_by.deleter
    def investigated_by(self):
        self._investigated_by = None
    
    @property
    def investigation_events(self):
        return self._investigation_events
    
    @investigation_events.setter
    def investigation_events(self, value):
        check_type(value, list, allow_none=False)
        check_vocab(value, 'investigation-vocab')
        self._investigation_events = value
    
    def append_investigation_events(self, item):
        check_type(item, tuple, allow_none=False)
        check_vocab(item, 'investigation-vocab')
        self._investigation_events.append(item)

    @investigation_events.deleter
    def investigation_events(self):
        self._investigation_events = None

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
    def incident(self):
        return self._incident
    
    @incident.setter
    def incident(self, value):
        
        check_type(value, Incident, allow_none=False)
        self._incident = value
        if value.response != self:
            value.response = self
    
    @incident.deleter
    def incident(self):
        temp = self._incident
        self._incident = None
        if temp != None:
            del temp.response
    
    @property
    def legal_response(self):
        return self._legal_response
    
    @legal_response.setter
    def legal_response(self, value):
        
        check_type(value, LegalResponse)
        self._legal_response = value
        if value.response != self:
            value.response = self

    @legal_response.deleter
    def legal_response(self):
        temp = self._legal_response
        self._legal_response = None
        if temp != None:
            del temp.response
