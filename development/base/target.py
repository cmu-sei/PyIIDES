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

class Target:
    """
    Initializes a Target instance 

    Args:
        id (required) (string) : Unique identifier for the target. Defaults to a new UUIDv4 string if not provided.
        asset_type (required) (string) : The type of target.
            A constant from `target-asset-vocab <./vocab/target-asset-vocab.html>`_.
            Required if category exists.
        category (required) (string) : The classification group a target belongs to.
            A constant from `target-category-vocab <./vocab/target-category-vocab.html>`_.
            Required if subcategory exists.
        subcategory (required) (string) : The lower-level classification group a target belongs to.
            A constant from `target-subcategory-vocab <./vocab/target-subcategory-vocab.html>`_.
        format (required) (string) : The data type of the target.
            A constant from `target-format-vocab <./vocab/target-format-vocab.html>`_.
        owner (required) (string) : Who the data is about. For assets, the owner of the asset. In cases where the owner and subject of the data/asset is unclear, pick the person/group most responsible for safeguarding the data/asset.
            A constant from `target-owner-vocab <./vocab/target-owner-vocab.html>`_.
        sensitivity (required) (array) : The level of sensitivity and controls applied to a target.
            One or more constants from `target-sensitivity-vocab <./vocab/target-sensitivity-vocab.html>`_.
        description (string) : Brief description of the target.
    
    Raises:
        TypeError: If any provided attribute is of the incorrect type.
        ValueError: If any provided attribute is of the incorrect vocabulary. 
    
    Example:
        >>> target = Target(
        ...     id="12345678-1234-1234-1234-123456789abc",
        ...     asset_type="4",
        ...     category="4.1",
        ...     subcategory="4.1.1",
        ...     format="1",
        ...     owner="O",
        ...     sensitivity=["25"],
        ...     description="Client list for manifold sales"
        ... )
        >>> print(target.id)
        12345678-1234-1234-1234-123456789abc
        >>> print(target.asset_type)
        4
        >>> print(target.category)
        4.1
        >>> print(target.subcategory)
        4.1.1
        >>> print(target.format)
        1
    """
    def __init__(self, asset_type, category, subcategory, format, owner, sensitivity, id=None, description=None):
        if id is None:
            id = str(uuid.uuid4())

        check_uuid(id)
        self._id = id

        check_type(asset_type, str)
        check_vocab(asset_type, 'target-asset-vocab')
        self._asset_type = asset_type

        check_type(category, str)
        check_vocab(category, 'target-category-vocab')
        self._category = category

        check_type(subcategory, str)
        check_vocab(subcategory, 'target-subcategory-vocab')
        self._subcategory = subcategory

        check_type(format, str)
        check_vocab(format, 'target-format-vocab')
        self._format = format

        check_type(owner, str)
        check_vocab(owner, 'target-owner-vocab')
        self._owner = owner

        check_type(sensitivity, list)
        check_vocab(sensitivity, 'target-sensitivity-vocab')
        self._sensitivity = sensitivity

        check_type(description, str)
        self._description = description

        # relationships
        self._incident = None
    
    def __repr__(self):
        return (f"Target(id={self.id}, "
                f"assert_type={self.asset_type}, "
                f"category={self.category}, "
                f"subcategory={self.subcategory}, "
                f"format={self.format}, "
                f"owner={self.owner}, "
                f"sensitivity={self.sensitivity}, "
                f"description={self.description})")
    
    def to_dict(self):
        class_dict_copy = self.__dict__.copy()
        relationships = {'_incident'}
        class_dict_copy["_id"] = f"target--{self.id}"
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
    
    @id.deleter
    def id(self):
        self._id = None

    @property
    def asset_type(self):
        return self._asset_type
    
    @asset_type.setter
    def asset_type(self, value):
        check_type(value, str)
        check_vocab(value, 'target-asset-vocab')
        self._asset_type = value
    
    @asset_type.deleter
    def asset_type(self):
        self._asset_type = None

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        check_type(value, str)
        check_vocab(value, 'target-category-vocab')
        self._category = value
    
    @category.deleter
    def category(self):
        self._category = None

    @property
    def subcategory(self):
        return self._subcategory
    
    @subcategory.setter
    def subcategory(self, value):
        check_type(value, str)
        check_vocab(value, 'target-subcategory-vocab')
        self._subcategory = value
    
    @subcategory.deleter
    def subcategory(self):
        self._subcategory = None

    @property
    def format(self):
        return self._format
    
    @format.setter
    def format(self, value):
        check_type(value, str)
        check_vocab(value, 'target-format-vocab')
        self._format = value
    
    @format.deleter
    def format(self):
        self._format = None

    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, value):
        check_type(value, str)
        check_vocab(value, 'target-owner-vocab')
        self._owner = value
    
    @owner.deleter
    def owner(self):
        self._owner = None

    @property
    def sensitivity(self):
        return self._sensitivity
    
    @sensitivity.setter
    def sensitivity(self, value):
        check_type(value, list)
        check_vocab(value, 'target-sensitivity-vocab')
        self._sensitivity = value
    
    @sensitivity.deleter
    def sensitivity(self):
        self._sensitivity = None

    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        check_type(value, str)
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
        # making sure to remove old relationships first
        if self._incident != None:
            self._incident.targets.remove(self)
        self._incident = value 

        # add this to the incident's target list 
        if value.targets == None:
            value.targets = [self]
        elif self not in value.targets: 
            value.targets.append(self)
    
    @incident.deleter
    def incident(self):
        if self._incident != None:
            self._incident.targets.remove(self)
            self._incident = None
