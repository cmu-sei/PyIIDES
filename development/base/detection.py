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
from datetime import datetime


class Detection:
    """
    Initialize a Detection instance.

    Args:
        id (str): Unique identifier for the detection. Defaults to a new UUIDv4 string if not provided.
        first_detected (datetime): The date and time the victim organization first became aware of the incident.
        who_detected (list): The individual entities or teams that first detected the incident. One or more constants from 
                             `detection-team-vocab <./vocab/detection-team-vocab.html>`_.
        detected_method (list): The system or process that led to the first detection of the incident. One or more constants from 
                                `detection-method-vocab <./vocab/detection-method-vocab.html>`_.
        logs (list): The type(s) of logs used by the detection team and/or method to first detect the incident. One or more constants from 
                     `detection-log-vocab <./vocab/detection-log-vocab.html>`_.
        comment (str): Clarifying comments about who, what, when, or how the incident was detected.
        **kwargs (dict): Additional attributes for the detection.
    
    Raises:
        TypeError: If any provided attribute is of the incorrect type.
        ValueError: If any provided attribute is of the incorrect vocabulary. 
    
    Examples:
        >>> from datetime import datetime
        >>> from pyiides.pyiides.detection import Detection
        >>> detection = detection = Detection(
        ...     first_detected= datetime(2023, 1, 1, 0, 0, 0),
        ...     who_detected=["LE"],
        ...     detected_method=["1"],
        ...     logs=["AC"],
        ...     comment="Additional details about the detection."
        ... )
        >>> print(detection.first_detected)
        2023-01-1 00:00:00
    """
    def __init__(self, id=None, first_detected=None, who_detected=None, detected_method=None, logs=None, comment=None, **kwargs):
        if id == None:
            id = str(uuid.uuid4())

        check_uuid(id)
        self._id = id

        check_type(first_detected, datetime)
        self._first_detected = first_detected

        check_type(who_detected, list)
        check_vocab(who_detected, 'detection-team-vocab')
        self._who_detected = who_detected

        check_type(detected_method, list)
        check_vocab(detected_method, 'detection-method-vocab')
        self._detected_method = detected_method

        check_type(logs, list)
        check_vocab(logs, 'detection-log-vocab')
        self._logs = logs

        check_type(comment, str)
        self._comment = comment

        # RELATIONSHIPS
        self._incident = None  # belongs to incident

    def __repr__(self):
        return (f"Detection(id={self.id}, "
                f"first_detected={self.first_detected}, "
                f"who_detected={self.who_detected}, "
                f"detected_method={self.detected_method}, "
                f"logs={self.logs}, "
                f"comment={self.comment})")

    def to_dict(self):
        class_dict_copy = self.__dict__.copy()

        relationships = {'_incident'}

        class_dict_copy["_id"] = f"detection--{self.id}"
        if self.first_detected != None:
            class_dict_copy["_first_detected"] = str(self.first_detected)
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
    def first_detected(self):
        return self._first_detected

    @first_detected.setter
    def first_detected(self, value):   
        check_type(value, datetime, allow_none=False)
        self._first_detected = value
    
    @first_detected.deleter
    def first_detected(self):
        self._first_detected = None
    
    @property
    def who_detected(self):
        return self._who_detected
    
    @who_detected.setter
    def who_detected(self, value):
        check_type(value, list, allow_none=False)
        check_vocab(value, 'detection-team-vocab')
        self._who_detected = value
    
    def append_who_detected(self, item):
        check_type(item, str, allow_none=False)
        check_vocab(item, 'detection-team-vocab')
        self._who_detected.append(item)
    
    @who_detected.deleter
    def who_detected(self):
        self._who_detected = None
    
    @property
    def detected_method(self):
        return self._detected_method
    
    @detected_method.setter
    def detected_method(self, value):
        check_type(value, list, allow_none=False)
        check_vocab(value, 'detection-method-vocab')
        self._detected_method = value
    
    def append_detected_method(self, item):
        check_type(item, str, allow_none=False)
        check_vocab(item, 'detection-method-vocab')
        self._detected_method.append(item)
    
    @detected_method.deleter
    def detected_method(self):
        self._detected_method = None

    @property
    def logs(self):
        return self._logs
    
    @logs.setter
    def logs(self, value):
        check_type(value, list, allow_none=False)
        check_vocab(value, 'detection-log-vocab')
        self._logs = value
    
    def append_logs(self, item):
        check_type(item, str, allow_none=False)
        check_vocab(item, 'detection-log-vocab')
        self._logs.append(item)
    
    @logs.deleter
    def logs(self):
        self._logs = None
    
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
        if value.detection != self:
            value.detection = self
    
    @incident.deleter
    def incident(self):
        temp = self._incident
        self._incident = None
        if temp != None:
            del temp.detection
