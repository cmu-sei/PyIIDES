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


class Impact:
    """
    Initialize an Impact instance

    Args:
        id (required) (string) : Unique identifier for the impact. Defaults to
            a new UUIDv4 string if not provided.
        high (required) (number) : The quantity of the impact being measured.
            If a range, the high end of the range.
        low (number) : If a range, the low estimate of the range.
        metric (required) (string) : The type of impact being quantified.
            A constant from `impact-metric-vocab <./vocab/impact-metric-vocab.html>`_.
        estimated (required) (boolean) : True if the impact low and/or high is
            an estimated number or range.
        comment (string) : Clarifying comments.

    Raises:
        TypeError: If any provided attribute is of the incorrect type.
        ValueError: If any provided attribute is of the incorrect vocabulary.

    Example:
        >>> from pyiides import Impact
        >>> impact = Impact(high=5000, metric="dollars", estimated=True)
        >>> print(impact.high)
        5000
        >>> print(impact.metric)
        dollars
        >>> print(impact.estimated)
        True
    """
    def __init__(self, high, metric, estimated, id=None, low=None, comment=None):
        if id == None:
            id = str(uuid.uuid4())

        check_uuid(id)
        self._id = id

        check_type(high, float)
        self._high = high

        check_type(low, float)
        self._low = low

        check_type(metric, str)
        check_vocab(metric, 'impact-metric-vocab')
        self._metric = metric

        check_type(estimated, bool)
        self._estimated = estimated

        check_type(comment, str)
        self._comment = comment 

        # RELATIONSHIP

        self._incident = None

    def __repr__(self):
        return (f"Impact(id={self.id}, "
                f"high={self.high}, "
                f"low={self.low}, "
                f"metric={self.metric}, "
                f"estimated={self.estimated}, "
                f"comment={self.comment})")

    def to_dict(self):
        class_dict_copy = self.__dict__.copy()
        relationships = {'_incident'}
        class_dict_copy["_id"] = f"impact--{self.id}"
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
    def high(self):
        return self._high

    @high.setter
    def high(self, value):
        check_type(value, float, allow_none=False)
        self._high = value

    @high.deleter
    def high(self):
        self._high = None

    @property
    def low(self):
        return self._low

    @low.setter
    def low(self, value):
        check_type(value, float, allow_none=False)
        self._low = value

    @low.deleter
    def low(self):
        self._low = None

    @property
    def metric(self):
        return self._metric

    @metric.setter
    def metric(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'impact-metric-vocab')
        self._metric = value

    @metric.deleter
    def metric(self):
        self._metric = None

    @property
    def estimated(self):
        return self._estimated

    @estimated.setter
    def estimated(self, value):
        check_type(value, bool, allow_none=False)
        self._estimated = value

    @estimated.deleter
    def estimated(self):
        self._estimated = None

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

        # set the incident:
        # if there is already an incident set, we want to
        # remove this impact instance from that incident
        # before setting the new one
        if self._incident != None:
            self._incident.impacts.remove(self)
        self._incident = value

        # add this impact instance to the incident's
        # impacts list
        if value.impacts == None:
            value.impacts = [self]
        elif self not in value.impacts:
            value.impacts.append(self)

    @incident.deleter
    def incident(self):
        if self._incident != None:
            self._incident.impacts.remove(self)
            self._incident = None
