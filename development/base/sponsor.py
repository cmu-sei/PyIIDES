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

class Sponsor:
    """
    Initializes a Sponsor instance

    Args:
        id (required) (string) : Unique identifier for the sponsor. Defaults to a new UUIDv4 string if not provided.
        name (string) : The name of the individual or entity sponsoring the insider's actions.
        sponsor_type (string) : The type of sponsor.
            A constant from `sponsor-type-vocab <./vocab/sponsor-type-vocab.html>`_.
    
    Raises:
        TypeError: If any provided attribute is of the incorrect type.
        ValueError: If any provided attribute is of the incorrect vocabulary. 
    
    Example:
        >>> from pyiides.utils.helper_functions import Sponsor
        >>> sponsor = Sponsor(
        ...     id="6eaf8e6c-8c4d-4d9d-8f8e-6c8c4d4d9d8f",
        ...     name="Foreign Government",
        ...     sponsor_type="SS"
        ... )
        >>> print(sponsor.name)
        Foreign Government
        >>> print(sponsor.sponsor_type)
        SS
    """
    
    def __init__(self, id=None, name=None, sponsor_type=None):  
        if id is None:
            id = str(uuid.uuid4())
        check_uuid(id)
        self._id = id

        check_type(name, str)
        self._name = name

        check_type(sponsor_type, str)
        check_vocab(sponsor_type, 'sponsor-type-vocab')
        self._sponsor_type = sponsor_type

        # Relationships
        self._accomplices = None
        self._insiders = None
    
    def __repr__(self):
        return (f"Sponsor(id={self.id}, "
                f"name={self.name}, "
                f"sponsor_type={self.sponsor_type})")

    def to_dict(self):
        class_dict_copy = self.__dict__.copy()

        relationships = {'_accomplices', '_insiders'}

        children_ids = None

        if self.accomplices != None:
            children_ids = ["accomplice--" + x.id for x in self.accomplices]
        
        if self.insiders != None:
            insiders = ["insider--" + x.id for x in self.insiders]
            if children_ids == None: 
                children_ids = insiders
            else:
                children_ids.extend(insiders)

        class_dict_copy["_id"] = f"sponsor--{self.id}"
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
    def sponsor_type(self):
        return self._sponsor_type
    
    @sponsor_type.setter
    def sponsor_type(self, value):
        check_type(value, str)
        check_vocab(value, 'sponsor-type-vocab')
        self._sponsor_type = value
    
    @sponsor_type.deleter
    def sponsor_type(self):
        self._sponsor_type = None

    # - - - - - - - - - - RELATIONSHIPS - - - - - - - - - -

    @property
    def accomplices(self):
        return self._accomplices
    
    @accomplices.setter
    def accomplices(self, value):
        check_type(value, list, allow_none=False)

        # check that all elements are accomplice objects
        for obj in value:
            
            check_type(obj, Accomplice, allow_none=False)
        
        # set to new accomplice list
        # making sure to remove old relationships first
        if self._accomplices != None:
            # use list to create a copy
            for a in list(self._accomplices):
                del a.sponsor
        self._accomplices = value

        # connect those back to this instance of sponsor
        for obj in value: 
            if obj.sponsor != self:
                obj.sponsor = self

    def append_accomplice(self, item):
        
        check_type(item, Accomplice, allow_none=False)
        if self._accomplices == None:
            self._accomplices = [item]
        else:
            self._accomplices.append(item)

        # need to connect this after, or else it adds self twice
        item.sponsor = self
    
    def remove_accomplice(self, item):
        
        check_type(item, Accomplice, allow_none=False)
        if self._accomplices != None:
            del item.sponsor  

    @accomplices.deleter
    def accomplices(self):
        # adding list() creates a copy so that we don't
        # run into any issues with removing elements 
        # from the list we are iterating over
        for obj in list(self._accomplices):
            del obj.sponsor
        self._accomplices = None

    @property
    def insiders(self):
        return self._insiders
    
    @insiders.setter
    def insiders(self, value):
        check_type(value, list, allow_none=False)

        # check that all elements inside are Insider objects
        for obj in value:
            
            check_type(obj, Insider, allow_none=False)

        # set new insider list
        # making sure to remove the old relationships first
        if self._insiders != None:
            # using list() to create a copy
            for i in list(self._insiders):
                del i.sponsor
        self._insiders = value

        # connect those insiders to this sponsor instance
        for obj in value: 
            if obj.sponsor != self:
                obj.sponsor = self

    def append_insider(self, item):
        
        check_type(item, Insider, allow_none=False)
        if self._insiders == None:
            self._insiders = [item]
        else:
            self._insiders.append(item)
        
        # need to set this after, or else it may add self twice
        item.sponsor = self
    
    def remove_insider(self, item):
        
        check_type(item, Insider, allow_none=False)
        if self._insiders != None:
            del item.sponsor  

    @insiders.deleter
    def insiders(self):
        # adding list() creates a copy so that we don't
        # run into any issues with removing elements 
        # from the list we are iterating over
        for obj in list(self._insiders):
            del obj.sponsor
        self._insiders = None
