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
from datetime import datetime
from pyiides.utils.helper_functions import check_uuid, check_type, check_vocab


class TTP:
    """
    Initialize a TTP instance.

    Args:
        id (str): Unique identifier for the TTP. Defaults to a new UUIDv4 string if not provided.
        date (datetime): The date and time the action happened. If over a range of time, the start time of the action.
        sequence_num (int): The sequence number of this action in the overall timeline of actions. Helpful if the sequence of events is known, but the dates are unknown.
        observed (bool): Whether the action was observed by the victim organization or investigative team at the time it happened.
        number_of_times (int): The number of times this particular action took place. E.g., subject issued "5" fraudulent checks over the course of three weeks.
        ttp_vocab (str): A reference to the TTP framework being used by this TTP. Common options are IIDES, ATT&CK, CAPEC, etc. Default is "IIDES". Required if tactic exists.
        tactic (str): The high-level category or goal of the action. A constant from 
                     `tactic-vocab <./vocab/tactic-vocab.html>`_. Required if technique exists.
        technique (str): The general action taken. If technique exists, tactic should as well. A constant from 
                         `technique-vocab <./vocab/technique-vocab.html>`_.
        location (list): Whether the action was taken on-site or remotely.
        hours (list): Whether the action was taken during work hours.
        device (list): The device where this action either took place or a device that was affected by the action. A device where the action could be detected. One or more constants from 
                       `device-vocab <./vocab/device-vocab.html>`_.
        channel (list): Methods used to transmit information outside, or into, the victim organization. One or more constants from 
                        `channel-vocab <./vocab/channel-vocab.html>`_.
        description (str): Description of the action/procedure.
        **kwargs (dict): Additional attributes for the TTP.

    Raises:
        TypeError: If any provided attribute is of the incorrect type.
        ValueError: If any provided attribute is of the incorrect vocabulary.

    Example:
        >>> ttp = TTP(
        ...     id="123e4567-e89b-12d3-a456-426614174000",
        ...     date=datetime(2023, 1, 1, 0, 0, 0),
        ...     sequence_num=1,
        ...     observed=True,
        ...     number_of_times=5,
        ...     ttp_vocab="IIDES",
        ...     tactic="1",
        ...     technique="1.1",
        ...     location=["1"],
        ...     hours=["1"],
        ...     device=["1"],
        ...     channel=["1"],
        ...     description="Initial description"
        ... )
        >>> print(ttp.id)
        123e4567-e89b-12d3-a456-426614174000
        >>> print(ttp.date)
        2020-01-01 00:00:00
    """
    def __init__(self, id=None, date=None, sequence_num=None, observed=None, number_of_times=None, ttp_vocab=None, tactic=None, technique=None, location=None, hours=None, device=None, channel=None, description=None, **kwargs):
        if id is None:
            id = str(uuid.uuid4())
        check_uuid(id)
        self._id = id

        check_type(date, datetime)
        self._date = date

        check_type(sequence_num, int)
        self._sequence_num = sequence_num

        check_type(observed, bool)
        self._observed = observed

        check_type(number_of_times, int)
        self._number_of_times = number_of_times

        check_type(ttp_vocab, str)
        self._ttp_vocab = ttp_vocab

        check_type(tactic, str)
        check_vocab(tactic, 'tactic-vocab')
        self._tactic = tactic

        check_type(technique, str)
        check_vocab(technique, 'technique-vocab')
        self._technique = technique

        check_type(location, list)
        check_vocab(location, 'attack-location-vocab')
        self._location = location

        check_type(hours, list)
        check_vocab(hours, 'attack-hours-vocab')
        self._hours = hours

        check_type(device, list)
        check_vocab(device, 'device-vocab')
        self._device = device

        check_type(channel, list)
        check_vocab(channel, 'channel-vocab')
        self._channel = channel

        check_type(description, str)
        self._description = description

        # RELATIONSHIPS 
        self._incident = None
    
    def __repr__(self):
        return (f"TTP(id={self.id}, "
                f"date={self.date}, "
                f"sequence_num={self.sequence_num}, "
                f"observed={self.observed}, "
                f"number_of_times={self.number_of_times}, "
                f"ttp_vocab={self.ttp_vocab}, "
                f"tactic={self.tactic}, "
                f"technique={self.technique}, "
                f"location={self.location}, "
                f"hours={self.hours}, "
                f"device={self.device}, "
                f"channel={self.channel}, "
                f"description={self.description})")

    def to_dict(self):
        class_dict_copy = self.__dict__.copy()
        relationships = {'_incident'}

        if self.date != None:
            class_dict_copy["date"] = str(self.date)

        class_dict_copy["_id"] = f"ttp--{self.id}"
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
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        check_type(value, datetime, allow_none=False)
        self._date = value
    
    @date.deleter
    def date(self):
        self._date = None
    
    @property
    def sequence_num(self):
        return self._sequence_num

    @sequence_num.setter
    def sequence_num(self, value):
        check_type(value, int, allow_none=False)
        self._sequence_num = value
    
    @sequence_num.deleter
    def sequence_num(self):
        self._sequence_num = None
    
    @property
    def observed(self):
        return self._observed
    
    @observed.setter
    def observed(self, value):
        check_type(value, bool, allow_none=False)
        self._observed = value
    
    @observed.deleter
    def observed(self):
        self._observed = None
    
    @property
    def number_of_times(self):
        return self._number_of_times
    
    @number_of_times.setter
    def number_of_times(self, value):
        check_type(value, int, allow_none=False)
        self._number_of_times = value
    
    @number_of_times.deleter
    def number_of_times(self):
        self._number_of_times = None
    
    @property
    def ttp_vocab(self):
        return self._ttp_vocab
    
    @ttp_vocab.setter
    def ttp_vocab(self, value):
        check_type(value, str, allow_none=False)
        self._ttp_vocab = value
    
    @ttp_vocab.deleter
    def ttp_vocab(self):
        self._ttp_vocab = None
    
    @property
    def tactic(self):
        return self._tactic
    
    @tactic.setter
    def tactic(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'tactic-vocab')
        self._tactic = value
    
    @tactic.deleter
    def tactic(self):
        self._tactic = None
    
    @property
    def technique(self):
        return self._technique
    
    @technique.setter
    def technique(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'technique-vocab')
        self._technique = value
    
    @technique.deleter
    def technique(self):
        self._technique = None
    
    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, value):
        check_type(value, list, allow_none=False)
        check_vocab(value, 'attack-location-vocab')
        self._location = value
    
    def append_location(self, item):
        check_type(item, str, allow_none=False)
        check_vocab(item, 'attack-location-vocab')
        self._location.append(item)
    
    @location.deleter
    def location(self):
        self._location = None
    
    @property
    def hours(self):
        return self._hours
    
    @hours.setter
    def hours(self, value):
        check_type(value, list, allow_none=False)
        check_vocab(value, 'attack-hours-vocab')
        self._hours = value
    
    def append_hours(self, item):
        check_type(item, str, allow_none=False)
        check_vocab(item, 'attack-hours-vocab')
        self._hours.append(item)

    @hours.deleter
    def hours(self):
        self._hours = None
    
    @property
    def device(self):
        return self._device
    
    @device.setter
    def device(self, value):
        check_type(value, list, allow_none=False)
        check_vocab(value, 'device-vocab')
        self._device = value
    
    def append_device(self, item):
        check_type(item, str, allow_none=False)
        check_vocab(item, 'device-vocab')
        self._device.append(item)

    @device.deleter
    def device(self):
        self._device = None
    
    @property
    def channel(self):
        return self._channel
    
    @channel.setter
    def channel(self, value):
        check_type(value, list, allow_none=False)
        check_vocab(value, 'channel-vocab')
        self._channel = value
    
    def append_channel(self, item):
        check_type(item, str, allow_none=False)
        check_vocab(item, 'channel-vocab')
        self._channel.append(item)

    @channel.deleter
    def channel(self):
        self._channel = None
    
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        check_type(value, str, allow_none=False)
        self._description = value
    
    @description.deleter
    def description(self):
        self._description = None

    # - - - - - - - RELATIONSHIPS - - - - - - 
    @property
    def incident(self):
        return self._incident
    
    @incident.setter
    def incident(self, value):
        check_type(value, Incident, allow_none=False)
        
        # set the incident
        # first remove all old relationships if they exist
        if self._incident != None:
            self._incident.ttps.remove(self)
        self._incident = value

        # add it to the incident's ttp list
        if value.ttps == None:
            value.ttps = [self]
        elif self not in value.ttps:
            value.ttps.append(self)
    
    @incident.deleter
    def incident(self):
        # remove the ttpfrom incident ttp list, as well as 
        # set the incident attribute to none
        if self._incident != None:
            self._incident.ttps.remove(self)
            self._incident = None
