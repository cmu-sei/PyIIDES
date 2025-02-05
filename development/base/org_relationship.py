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

class OrgRelationship:
    """
    Initializes an OrgRelationship instance

    Args:
        id (string) : Unique identifier for the organization relationship. Defaults to a new UUIDv4 string if not provided.
        org1 (required) (Organization) : The first organization involved in the relationship.
        org2 (required) (Organization) : The second organization involved in the relationship.
        relationship (required) (string) : The type of relationship between the two organizations.
            A constant from `org-relationship-vocab <./vocab/org-relationship-vocab.html>`_.
    
    Raises:
        TypeError: If any provided attribute is of the incorrect type.
        ValueError: If any provided attribute is of the incorrect vocabulary. 
    
    Example:
        >>> from pyiides.utils.helper_functions import OrgRelationship
        >>> 
        >>> org1 = Organization(name="Org One")
        >>> org2 = Organization(name="Org Two")
        >>> org_relationship = OrgRelationship(
        ...     org1=org1,
        ...     org2=org2,
        ...     relationship="C",
        ...     id="org-relationship--6eaf8e6c-8c4d-4d9d-8f8e-6c8c4d4d9d8f"
        ... )
        >>> print(org_relationship.org1)
        Org One
        >>> print(org_relationship.relationship)
        C
    """
    def __init__(self, org1, org2, relationship, id=None):
        if id == None:
            id = str(uuid.uuid4())

        check_uuid(id)
        self._id = id
        
        
        check_type(org1, Organization)
        self._org1 = org1 

        check_type(org2, Organization)
        self._org2 = org2 

        check_type(relationship, str)
        check_vocab(relationship, 'org-relationship-vocab')
        self._relationship = relationship

    def __repr__(self):
        return (f"OrgRelationship(id={self.id}, "
                f"org1={self.org1}, "
                f"org2={self.org2}, "
                f"relationship={self.relationship})")

    def to_dict(self):
        class_dict_copy = self.__dict__.copy()
        class_dict_copy["_id"] = f"org-relationship--{self.id}"
        return ({
                    key.lstrip('_'): value for key, value in class_dict_copy.items()
                }, None)

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        check_uuid(value)
        self._id = value
    
    @property
    def org1(self):
        return self.org1

    @org1.setter
    def org1(self, value):
        
        check_type(value, Organization)
        self._org1 = value
    
    @org1.deleter
    def org1(self):
        self._org1 = None
    
    @property
    def org2(self):
        return self.org2

    @org2.setter
    def org2(self, value):
        
        check_type(value, Organization)
        self._org2 = value
    
    @org2.deleter
    def org2(self):
        self._org2 = None
    
    @property
    def relationship(self):
        return self._relationship
    
    @relationship.setter
    def relationship(self, value):
        check_type(value, str)
        check_vocab(value, 'org-relationship-vocab')
        self._relationship = value
    
    @relationship.deleter
    def relationship(self):
        self._relationship = None
