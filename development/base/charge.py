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


class Charge:
    """
    Initializes a Charge instance

    Args:
        id (required) (string) : Unique identifier for the charge. Defaults to a new UUIDv4 string if not provided.
        title (required) (string) : Broad subject matter area of the legal code. For U.S. cases, these are often title '18 U.S.C.'.
        section (string) : Section (and subsection) of the law the subject is accused of violating. For U.S. cases for example, Wire Fraud is section 1343 of Title 18.
        nature_of_offense (string) : Description of the title and section of the law being violated.
        count (integer) : Number of times the subject is accused of violating the law associated with this charge. Note that multiple violations of a law are often listed as a range of counts (e.g. 'Count 2-6' would have count=5 for this property).
        plea (string) : Plea entered by the defendant for this charge.
            A constant from `charge-plea-vocab <./vocab/charge-plea-vocab.html>`_.
        plea_bargain (boolean) : Whether the charge indicated here is a lesser charge based on a previous plea agreement.
        disposition (string) : The decision in the case or the final result.
            A constant from `charge-disposition-vocab <./vocab/charge-disposition-vocab.html>`_.
    
    Raises:
        TypeError: If any provided attribute is of the incorrect type.
        ValueError: If any provided attribute is of the incorrect vocabulary. 

    Example:
        >>> from pyiides.utils.helper_functions import Charge
        >>> charge = Charge(
        ...     title="18 U.S.C.",
        ...     id="6eaf8e6c-8c4d-4d9d-8f8e-6c8c4d4d9d8f",
        ...     section="1343",
        ...     nature_of_offense="Wire Fraud",
        ...     count=5,
        ...     plea="1",
        ...     plea_bargain=False,
        ...     disposition="2"
        ... )
        >>> print(charge.title)
        18 U.S.C.
        >>> print(charge.section)
        1343
    """
    def __init__(self, title, id=None, section=None, nature_of_offense=None, count=None, plea=None, plea_bargain=None, disposition=None):
        if id == None:
            id = str(uuid.uuid4())

        check_uuid(id)
        self._id = id

        check_type(title, str)
        self._title = title

        check_type(section, str)
        self._section = section

        check_type(nature_of_offense, str)
        self._nature_of_offense = nature_of_offense

        check_type(count, int)
        self._count = count

        check_type(plea, str)
        check_vocab(plea, 'charge-plea-vocab')
        self._plea = plea

        check_type(plea_bargain, bool)
        self._plea_bargain = plea_bargain

        check_type(disposition, str)
        check_vocab(disposition, 'charge-disposition-vocab')
        self._disposition = disposition

        # relationships
        self._court_case = None
    
    def __repr__(self):
        return (f"Charge(id={self.id}, "
                f"title={self.title}, "
                f"section={self.section}, "
                f"nature_of_offense={self.nature_of_offense}, "
                f"count={self.count}, plea={self.plea}, "
                f"plea_bargain={self.plea_bargain}, "
                f"disposition={self.disposition})")

    def to_dict(self):
        class_dict_copy = self.__dict__.copy()
        relationships = {'_court_case'}
        class_dict_copy["_id"] = f"charge--{self.id}"
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
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        check_type(value, str, allow_none=False)
        self._title = value

    @title.deleter
    def title(self):
        self._title = None
    
    @property
    def section(self):
        return self._section

    @section.setter
    def section(self, value):
        check_type(value, str, allow_none=False)
        self._section = value

    @section.deleter
    def section(self):
        self._section = None

    @property
    def nature_of_offense(self):
        return self._nature_of_offense

    @nature_of_offense.setter
    def nature_of_offense(self, value):
        check_type(value, str, allow_none=False)
        self._nature_of_offense = value

    @nature_of_offense.deleter
    def nature_of_offense(self):
        self._nature_of_offense = None

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        check_type(value, int, allow_none=False)
        self._count = value

    @count.deleter
    def count(self):
        self._count = None

    @property
    def plea(self):
        return self._plea

    @plea.setter
    def plea(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'charge-plea-vocab')
        self._plea = value

    @plea.deleter
    def plea(self):
        self._plea = None

    @property
    def plea_bargain(self):
        return self._plea_bargain

    @plea_bargain.setter
    def plea_bargain(self, value):
        check_type(value, bool, allow_none=False)
        self._plea_bargain = value

    @plea_bargain.deleter
    def plea_bargain(self):
        self._plea_bargain = None

    @property
    def disposition(self):
        return self._disposition

    @disposition.setter
    def disposition(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'charge-disposition-vocab')
        self._disposition = value

    @disposition.deleter
    def disposition(self):
        self._disposition = None
    
    # - - - - - - - RELATIONSHIPS - - - - - - 
    @property
    def court_case(self):
        return self._court_case
    
    @court_case.setter
    def court_case(self, value):
        
        check_type(value, CourtCase, allow_none=False)
        
        # if the court case was already set, we have to remove
        # its current relationships before setting the new one
        if self._court_case != None:
            self._court_case.charges.remove(self)
        self._court_case = value
        
        # then add this charge instance to the court 
        # case's charge list 
        if value.charges == None:
            value.charges = [self]
        elif self not in value.charges:
            value.charges.append(self)
    
    @court_case.deleter
    def court_case(self):
        if self._court_case != None:
            self._court_case.charges.remove(self)
            self._court_case = None
