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


class Collusion:
    """
    Initializes a Collusion instance

    Args:
        id (string) : Unique identifier for the collusion. Defaults to a new UUIDv4 string if not provided.
        insider1 (required) (Insider) : The first insider involved in the collusion.
        insider2 (required) (Insider) : The second insider involved in the collusion.
        relationship (required) (string) : The relationship between the two insiders.
            A constant from `insider-relationship-vocab <./vocab/insider-relationship-vocab.html>`_.
        recruitment (required) (string) : The recruitment method or relationship between the insiders.
            A constant from `insider-recruitment-vocab <./vocab/insider-recruitment-vocab.html>`_.
    
    Raises:
        TypeError: If any provided attribute is of the incorrect type.
        ValueError: If any provided attribute is of the incorrect vocabulary.

    Example:
        >>> from pyiides.utils.helper_functions import Collusion
        >>> 
        >>> insider1 = Insider(first_name="John", last_name="Doe")
        >>> insider2 = Insider(first_name="Jane", last_name="Smith")
        >>> collusion = Collusion(
        ...     insider1=insider1,
        ...     insider2=insider2,
        ...     relationship="1",
        ...     recruitment="2"
        ... )
        >>> print(collusion.relationship)
        1
        >>> print(collusion.recruitment)
        2
    """
    def __init__(self, insider1, insider2, relationship, recruitment, id=None):
        if id == None:
            id = str(uuid.uuid4())

        check_uuid(id)
        self._id = id
        
        
        check_type(insider1, Insider)
        self._insider1 = insider1

        check_type(insider2, Insider)
        self._insider2 = insider2 

        check_type(relationship, str)
        check_vocab(relationship, 'insider-relationship-vocab')
        self._relationship = relationship

        check_type(recruitment, str)
        check_vocab(recruitment, 'insider-recruitment-vocab')
        self._recruitment = recruitment 
    
    def __repr__(self):
        return (f"Collusion(id={self.id}, "
                f"insider1={self.insider1!r}, "
                f"insider2={self.insider2!r}, "
                f"relationship={self.relationship}, "
                f"recruitment={self.recruitment})")

    def to_dict(self):
        class_dict_copy = self.__dict__.copy()
        class_dict_copy["_id"] = f"collusion--{self.id}"
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
    def insider1(self):
        return self._insider1

    @insider1.setter
    def insider1(self, value):
        
        check_type(value, Insider)
        self._insider1 = value

    @insider1.deleter
    def insider1(self):
        self._insider1 = None
    
    @property 
    def insider2(self):
        return self._insider2

    @insider2.setter
    def insider2(self, value):
        
        check_type(value, Insider)
        self._insider2 = value

    @insider2.deleter
    def insider2(self):
        self._insider2 = None
    
    @property
    def relationship(self):
        return self._relationship
    
    @relationship.setter
    def relationship(self, value):
        check_type(value, str)
        check_vocab(value, 'insider-relationship-vocab')
        self._relationship = value
    
    @relationship.deleter
    def relationship(self):
        self._relationship = None
    
    @property 
    def recruitment(self):
        return self._recruitment

    @recruitment.setter
    def recruitment(self, value):
        check_type(value, str)
        check_vocab(value, 'insider-recruitment-vocab')
        self._recruitment = value

    @recruitment.deleter
    def recruitment(self):
        self._recruitment = None
