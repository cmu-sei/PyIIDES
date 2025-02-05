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


class Stressor:
    """
    Initialize a Stressor instance

    Args:
        id (required) (string) : Unique identifier for the stressor. Defaults to a new UUIDv4 string if not provided.
        date (date) : The date the stressor first occurred.
        category (string) : The category to which the stressor belongs. 
            A constant from `stressor-category-vocab <./vocab/stressor-category-vocab.html>`_.
            Required if subcategory exists.
        subcategory (string) : The subcategory to which the stressor belongs. When subcategory is specified, category MUST also be specified. The subcategory constant MUST map to the specified category constant.
            A constant from `stressor-subcategory-vocab <./vocab/stressor-subcategory-vocab.html>`_.
        comment (string) : Clarifying comments about the stressor.

    Raises:
        TypeError: If any provided attribute is of the incorrect type.
        ValueError: If any provided attribute is of the incorrect vocabulary. 
    
    Example:
        >>> from pyiides import Stressor
        >>> stressor = Stressor(date=datetime.date(2023, 6, 14), category="2", subcategory="2.12", comment="High-pressure project deadline")
        >>> print(stressor.id)
        ac386e51-2f66-40fe-bfb7-c791019b2b97
        >>> print(stressor.date)
        2023-06-14
        >>> print(stressor.category)
        2
        >>> print(stressor.subcategory)
        2.12
        >>> print(stressor.comment)
        High-pressure project deadline
    """
    def __init__(self, id=None, date=None, category=None, subcategory=None, comment=None):
        if id == None:
            id = str(uuid.uuid4())

        check_uuid(id)
        self._id = id

        check_type(date, dt)
        self._date = date

        check_type(subcategory, str)
        check_vocab(subcategory, 'stressor-subcategory-vocab')
        self._subcategory = subcategory

        check_type(category, str)
        check_vocab(category, 'stressor-category-vocab')
        if self._subcategory != None and category == None:
            raise ReferenceError("The attribute category is required if subcategory exists")
        self._category = category

        check_type(comment, str)
        self._comment = comment

        # relationships 
        self._organization = None
        self._insider = None
    
    def __repr__(self):
        return (f"Stressor(id={self.id}, "
                f"date={self.date}, "
                f"category={self.category}, "
                f"subcategory={self.subcategory}, "
                f"comment={self.comment})")

    def to_dict(self):
        class_dict_copy = self.__dict__.copy()
        relationships = {'_organization', '_insider'}

        if self.date != None:
            class_dict_copy["date"] = str(self.date)

        class_dict_copy["_id"] = f"stressor--{self.id}"
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
        check_type(value, dt, allow_none=False)
        self._date = value
    
    @date.deleter
    def date(self):
        self._date = None
    
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'stressor-category-vocab')
        self._category = value

    @category.deleter
    def category(self):
        if self.subcategory != None:
            raise ReferenceError("The attribute category is required if subcategory exists")
        self._category = None

    @property
    def subcategory(self):
        return self._subcategory

    @subcategory.setter
    def subcategory(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'stressor-subcategory-vocab')
        self._subcategory = value

    @subcategory.deleter
    def subcategory(self):
        self._subcategory = None

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
        # first remove all old relationships 
        if self._organization != None:
            self._organization.stressors.remove(self)
        self._organization = value

        # add it to the organization's stressor list
        if value.stressors == None:
            value.stressors = [self]
        elif self not in value.stressors:
            value.stressors.append(self)

    @organization.deleter
    def organization(self):
        if self._organization != None:
            self._organization.stressors.remove(self)
            self._organization = None
    
    @property
    def insider(self):
        return self._insider
    
    @insider.setter
    def insider(self, value):
        
        check_type(value, Insider, allow_none=False)
        
        # set the insider 
        # first remove old relationships if they exist
        if self._insider != None:
            self._insider.stressors.remove(self)
        self._insider = value 

        # add it to the insider's stressor list 
        if value.stressors == None:
            value.stressors = [self]
        elif self not in value.stressors: 
            value.stressors.append(self)
    
    @insider.deleter
    def insider(self):
        if self._insider != None:
            self._insider.stressors.remove(self)
            self._insider = None
