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

class CourtCase:
    """
    Initializes a CourtCase instance

    Args:
        id (required) (string) : Unique identifier for the court case. Defaults to a new UUIDv4 string if not provided.
        case_number (string) : A case number assigned by the court system in which the case is being tried.
        case_title (string) : Title provided by the court system (e.g., 'USA v. LastName' or 'USA v. LastName, et al.').
        court_country (string) : Country where the case was tried.
            A constant from `country-vocab <./vocab/country-vocab.html>`_.
        court_state (string) : State or region where the case was tried.
            A constant from `state-vocab-us <./vocab/state-vocab-us.html>`_.
        court_district (string) : District where the case was tried, if applicable (e.g., "CA Central District Court").
        court_type (string) : Type or level of the court where the case is tried.
            A constant from `court-type-vocab <./vocab/court-type-vocab.html>`_.
        case_type (string) : Type of case.
            A constant from `case-type-vocab <./vocab/case-type-vocab.html>`_.
        defendant (array) : The names of all the defendants (or respondents, or appellees) in the case.
            One or more string values.
        plaintiff (array) : The names of all the plaintiffs (or petitioners, or appellants) in the case.
            One or more string values.
        comment (string) : Clarifying comments about any of the court case details, or its associated charges and sentences, 
                          such as which sentences run concurrently, the structure of a plea deal, or the status of the case.
    
    Raises:
        TypeError: If any provided attribute is of the incorrect type.
        ValueError: If any provided attribute is of the incorrect vocabulary. 

    Example:
        >>> from pyiides.utils.helper_functions import CourtCase
        >>> court_case = CourtCase(
        ...     case_number="1:22-cr-00123-JMF",
        ...     case_title="USA v. Smith",
        ...     court_country="US",
        ...     court_state="NY",
        ...     court_district="Southern District of New York",
        ...     court_type="Federal",
        ...     case_type="Criminal",
        ...     defendant=["John Smith"],
        ...     plaintiff=["United States of America"],
        ...     comment="This case involved multiple charges including espionage and unauthorized disclosure of classified information."
        ... )
        >>> print(court_case.case_title)
        USA v. Smith
        >>> print(court_case.court_country)
        US
    """
    def __init__(self, id=None, case_number=None, case_title=None, court_country=None, court_state=None, court_district=None, court_type=None, case_type=None, defendant=None, plaintiff=None, comment=None):
        if id == None:
            id = str(uuid.uuid4())

        check_uuid(id)
        self._id = id

        check_type(case_number, str)
        self._case_number = case_number

        check_type(case_title, str)
        self._case_title = case_title

        check_type(court_country, str)
        check_vocab(court_country, 'country-vocab')
        self._court_country = court_country

        check_type(court_state, str)
        check_vocab(court_state, 'state-vocab-us')
        self._court_state = court_state

        check_type(court_district, str)
        self._court_district = court_district

        check_type(court_type, str)
        check_vocab(court_type, 'court-type-vocab')
        self._court_type = court_type

        check_type(case_type, str)
        check_vocab(case_type, 'case-type-vocab')
        self._case_type = case_type

        check_type(defendant, list)
        if defendant != None:
            for s in defendant:
                check_type(s, str)
        self._defendant = defendant

        check_type(plaintiff, list)
        if plaintiff != None:
            for s in plaintiff:
                check_type(s, str)
        self._plaintiff = plaintiff

        check_type(comment, str)
        self._comment = comment

        # Relationships:
        self._legal_response = None
        self._sentences = None
        self._charges = None

    def __repr__(self):
        return (f"CourtCase(id={self.id}, "
                f"case_number={self.case_number}, "
                f"case_title={self.case_title}, "
                f"court_country={self.court_country}, "
                f"court_state={self.court_state}, "
                f"court_district={self.court_district}, "
                f"court_type={self.court_type}, "
                f"case_type={self.case_type}, "
                f"defendant={self.defendant}, "
                f"plaintiff={self.plaintiff}, "
                f"comment={self.comment}) ")
    
    def to_dict(self):
        class_dict_copy = self.__dict__.copy()

        relationships = {'_legal_response', '_sentences', '_charges'}

        children_ids = None 

        if self.charges != None:
            children_ids = ["charge--" + x.id for x in self.charges]

        if self.sentences != None:
            sentences = ["sentence--" + x.id for x in self.sentences]
            if children_ids == None: 
                children_ids = sentences
            else:
                children_ids.extend(sentences)
        
        class_dict_copy["_id"] = f"court-case--{self.id}"
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
    def case_number(self):
        return self._case_number
    
    @case_number.setter
    def case_number(self, value):
        check_type(value, str, allow_none=False)
        self._case_number = value
    
    @case_number.deleter
    def case_number(self):
        self._case_number = None

    @property
    def case_title(self):
        return self._case_title

    @case_title.setter
    def case_title(self, value):
        check_type(value, str, allow_none=False)
        self._case_title = value

    @case_title.deleter
    def case_title(self):
        self._case_title = None

    @property
    def court_country(self):
        return self._court_country
    
    @court_country.setter
    def court_country(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'country-vocab')
        self._court_country = value
    
    @court_country.deleter
    def court_country(self):
        self._court_country = None

    @property
    def court_state(self):
        return self._court_state
    
    @court_state.setter
    def court_state(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'state-vocab-us')
        self._court_state = value
    
    @court_state.deleter
    def court_state(self):
        self._court_state = None

    @property
    def court_district(self):
        return self._court_district
    
    @court_district.setter
    def court_district(self, value):
        check_type(value, str, allow_none=False)
        self._court_district = value
    
    @court_district.deleter
    def court_district(self):
        self._court_district = None

    @property
    def court_type(self):
        return self._court_type
    
    @court_type.setter
    def court_type(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'court-type-vocab')
        self._court_type = value
    
    @court_type.deleter
    def court_type(self):
        self._court_type = None

    @property
    def case_type(self):
        return self._case_type
    
    @case_type.setter
    def case_type(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'case-type-vocab')
        self._case_type = value
    
    @case_type.deleter
    def case_type(self):
        self._case_type = None

    @property
    def defendant(self):
        return self._defendant
    
    @defendant.setter
    def defendant(self, value):
        check_type(value, list, allow_none=False)
        if value is not None:
            for s in value:
                check_type(s, str, allow_none=False)
        self._defendant = value
    
    def append_defendant(self, item):
        check_type(item, str, allow_none=False)
        self._defendant.append(item)
    
    @defendant.deleter
    def defendant(self):
        self._defendant = None

    @property
    def plaintiff(self):
        return self._plaintiff
    
    @plaintiff.setter
    def plaintiff(self, value):
        check_type(value, list, allow_none=False)
        if value is not None:
            for s in value:
                check_type(s, str, allow_none=False)
        self._plaintiff = value
    
    def append_plaintiff(self, item):
        check_type(item, str, allow_none=False)
        self._plaintiff.append(item)

    @plaintiff.deleter
    def plaintiff(self):
        self._plaintiff = None

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
    def legal_response(self):
        return self._legal_response
    
    @legal_response.setter
    def legal_response(self, value):
        
        check_type(value, LegalResponse, allow_none=False)
        
        # if the legal response was already set, we have to remove
        # its current relationships before setting the new one
        if self._legal_response != None:
            self._legal_response.court_cases.remove(self)
        self._legal_response = value

        # add court case to legal response's court case list
        if value.court_cases == None:
            value.court_cases = [self]
        elif self not in value.court_cases:
            value.court_cases.append(self)
    
    @legal_response.deleter
    def legal_response(self):
        if self._legal_response != None:
            self._legal_response.court_cases.remove(self)
            self._legal_response = None

    @property
    def sentences(self):
        return self._sentences
    
    @sentences.setter
    def sentences(self, value):
        check_type(value, list, allow_none=False)

        # check that all elements are sentence objects
        for obj in value:
            
            check_type(obj, Sentence, allow_none=False)
        
        # set the new sentences list:
        # if it is not None, we need to remove 
        # the old relationships first
        if self._sentences != None:
            for s in self._sentences:
                del s.court_case
        self._sentences = value

        # connect those sentences back to this 
        # instance of court case
        for obj in value: 
            if obj.court_case != self:
                obj.court_case = self
    
    def append_sentence(self, item):
        
        check_type(item, Sentence, allow_none=False)
        
        if self._sentences == None:
            self._sentences = [item]
        else:
            self._sentences.append(item)
        
        item.court_case = self    
    
    def remove_sentence(self, item):
        
        check_type(item, Sentence, allow_none=False)
        if self._sentences != None:
            del item.court_case 
    
    @sentences.deleter
    def sentences(self):
        # adding list() creates a copy so that we don't
        # run into any issues with removing elements 
        # from the list we are iterating over
        for obj in list(self._sentences):
            del obj.court_case
        self._sentences = None
    
    @property
    def charges(self):
        return self._charges
    
    @charges.setter
    def charges(self, value):
        check_type(value, list, allow_none=False)

        # check that all elements within the list
        # are Charge objects 
        for obj in value:
            
            check_type(obj, Charge, allow_none=False)

        # set the charges list
        # if it is not None, we need to remove 
        # the old relationships first
        if self._charges != None:
            # use list() to create a copy
            for c in list(self._charges):
                del c.court_case
        self._charges = value

        # connect each charge back to this court case
        # instance
        for obj in value: 
            if obj.court_case != self:
                obj.court_case = self
    
    def append_charge(self, item):
        
        check_type(item, Charge, allow_none=False)
          
        if self._charges == None:
            self._charges = [item]
        else:
            self._charges.append(item)
        
        item.court_case = self 
    
    def remove_charge(self, item):
        
        check_type(item, Charge, allow_none=False)
        if self._charges != None:
            del item.court_case 
 
    @charges.deleter
    def charges(self):
        # adding list() creates a copy so that we don't
        # run into any issues with removing elements 
        # from the list we are iterating over
        for obj in list(self._charges):
            del obj.court_case
        self._charges = None
