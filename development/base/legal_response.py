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

class LegalResponse:
    """
    Initializes a LegalResponse instance

    Args:
        id (required) (string) : Unique identifier for the legal response. Defaults to a new UUIDv4 string if not provided.
        law_enforcement_contacted (date) : Organization contacts law enforcement to aid in the investigation of the incident. E.g., Police are called to respond to the Insider's violent behavior in the workplace).
        insider_arrested (date) : Insider is taken into custody. E.g., Police arrest insider in their home.
        insider_charged (date) : Insider is formally charged. Charges must relate to the incident. This category also covers a waiver of indictment and subsequent filing of information. E.g., Insider was indicted on computer fraud charges.
        insider_pleads (date) : Insider puts forth a plea to the court, including guilty, not guilty, nolo contendere (no contest). E.g., Insider pleads guilty to computer intrusion.
        insider_judgment (date) : Insider is found guilty, not guilty, or liable or not liable in a court of law. E.g., Insider is found guilty in a jury trial.
        insider_sentenced (date) : Insider is given a legally mandated punishment. E.g., Insider sentenced to 5 months in jail, then supervised release, community service, and restitution.
        insider_charges_dropped (date) : The plaintiff drops their case against the insider. E.g., The organization in a civil suit decides to drop the suit.
        insider_charges_dismissed (date) : The plaintiff dismiss their case against the insider. E.g., Upon discovery of further evidence, the judge decided to drop the charges against the insider.
        insider_settled (date) : The case against the insider is settled outside of the courtroom. E.g., The victim organization reached an agreement with the insider to not file formal charges in return for financial compensation.
        comment (string) : Comments clarifying the details or dates of the legal response.
    
    Raises:
        TypeError: If any provided attribute is of the incorrect type.
        ValueError: If any provided attribute is of the incorrect vocabulary. 
    
    Example:
        >>> from pyiides.utils.helper_functions import LegalResponse
        >>> legal_response = LegalResponse(
        ...     id="6eaf8e6c-8c4d-4d9d-8f8e-6c8c4d4d9d8f",
        ...     law_enforcement_contacted=datetime.date(2023, 1, 1),
        ...     insider_arrested=datetime.date(2023, 1, 2),
        ...     insider_charged=datetime.date(2023, 1, 3),
        ...     insider_pleads=datetime.date(2023, 1, 4),
        ...     insider_judgment=datetime.date(2023, 1, 5),
        ...     insider_sentenced=datetime.date(2023, 1, 6),
        ...     insider_charges_dropped=datetime.date(2023, 1, 7),
        ...     insider_charges_dismissed=datetime.date(2023, 1, 8),
        ...     insider_settled=datetime.date(2023, 1, 9),
        ...     comment="This is a sample comment."
        ... )
        >>> print(legal_response.id)
        6eaf8e6c-8c4d-4d9d-8f8e-6c8c4d4d9d8f
        >>> print(legal_response.comment)
        This is a sample comment.
    """
    def __init__(self, id=None, law_enforcement_contacted=None, insider_arrested=None, insider_charged=None, insider_pleads=None, insider_judgment=None, insider_sentenced=None, insider_charges_dropped=None, insider_charges_dismissed=None, insider_settled=None, comment=None):
        if id is None:
            id = str(uuid.uuid4())
        check_uuid(id)
        self._id = id

        check_type(law_enforcement_contacted, dt)
        self._law_enforcement_contacted = law_enforcement_contacted

        check_type(insider_arrested, dt)
        self._insider_arrested = insider_arrested

        check_type(insider_charged, dt)
        self._insider_charged = insider_charged

        check_type(insider_pleads, dt)
        self._insider_pleads = insider_pleads

        check_type(insider_judgment, dt)
        self._insider_judgment = insider_judgment

        check_type(insider_sentenced, dt)
        self._insider_sentenced = insider_sentenced

        check_type(insider_charges_dropped, dt)
        self._insider_charges_dropped = insider_charges_dropped

        check_type(insider_charges_dismissed, dt)
        self._insider_charges_dismissed = insider_charges_dismissed

        check_type(insider_settled, dt)
        self._insider_settled = insider_settled

        check_type(comment, str)
        self._comment = comment

        # Relationship
        self._response = None
        self._court_cases = None

    def __repr__(self):
        return (f"LegalResponse(id={self.id}, "
                f"law_enforcement_contacted={self.law_enforcement_contacted}, "
                f"insider_arrested={self.insider_arrested}, "
                f"insider_charged={self.insider_charged}, "
                f"insider_pleads={self.insider_pleads}, "
                f"insider_judgment={self.insider_judgment}, "
                f"insider_sentenced={self.insider_sentenced}, "
                f"insider_charges_dropped={self.insider_charges_dropped}, "
                f"insider_charges_dismissed={self.insider_charges_dismissed}, "
                f"insider_settled={self.insider_settled}, "
                f"comment={self.comment})")

    def to_dict(self):
        class_dict_copy = self.__dict__.copy()
        relationships = {'_response', '_court_cases'}

        if self.law_enforcement_contacted != None:
            class_dict_copy["_law_enforcement_contacted"] = str(self.law_enforcement_contacted)

        if self.insider_arrested != None:
            class_dict_copy["_insider_arrested"] = str(self.insider_arrested)

        if self.insider_charged != None:
            class_dict_copy["_insider_charged"] = str(self.insider_charged)

        if self.insider_pleads != None:
            class_dict_copy["_insider_pleads"] = str(self.insider_pleads)

        if self.insider_judgment != None:
            class_dict_copy["_insider_judgment"] = str(self.insider_judgment)

        if self.insider_sentenced != None:
            class_dict_copy["_insider_sentenced"] = str(self.insider_sentenced)

        if self.insider_charges_dropped != None:
            class_dict_copy["_insider_charges_dropped"] = str(self.insider_charges_dropped)

        if self.insider_charges_dismissed != None:
            class_dict_copy["_insider_charges_dismissed"] = str(self.insider_charges_dismissed)

        if self.insider_settled != None:
            class_dict_copy["_insider_settled"] = str(self.insider_settled)

        class_dict_copy["_id"] = f"legal-response--{self.id}"
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
    def law_enforcement_contacted(self):
        return self._law_enforcement_contacted
    
    @law_enforcement_contacted.setter
    def law_enforcement_contacted(self, value):
        check_type(value, dt, allow_none=False)
        self._law_enforcement_contacted = value
    
    @law_enforcement_contacted.deleter
    def law_enforcement_contacted(self):
        self._law_enforcement_contacted = None
    
    @property
    def insider_arrested(self):
        return self._insider_arrested

    @insider_arrested.setter
    def insider_arrested(self, value):
        check_type(value, dt, allow_none=False)
        self._insider_arrested = value

    @insider_arrested.deleter
    def insider_arrested(self):
        self._insider_arrested = None

    @property
    def insider_charged(self):
        return self._insider_charged

    @insider_charged.setter
    def insider_charged(self, value):
        check_type(value, dt, allow_none=False)
        self._insider_charged = value

    @insider_charged.deleter
    def insider_charged(self):
        self._insider_charged = None

    @property
    def insider_pleads(self):
        return self._insider_pleads

    @insider_pleads.setter
    def insider_pleads(self, value):
        check_type(value, dt, allow_none=False)
        self._insider_pleads = value

    @insider_pleads.deleter
    def insider_pleads(self):
        self._insider_pleads = None

    @property
    def insider_judgment(self):
        return self._insider_judgment

    @insider_judgment.setter
    def insider_judgment(self, value):
        check_type(value, dt, allow_none=False)
        self._insider_judgment = value

    @insider_judgment.deleter
    def insider_judgment(self):
        self._insider_judgment = None

    @property
    def insider_sentenced(self):
        return self._insider_sentenced

    @insider_sentenced.setter
    def insider_sentenced(self, value):
        check_type(value, dt, allow_none=False)
        self._insider_sentenced = value

    @insider_sentenced.deleter
    def insider_sentenced(self):
        self._insider_sentenced = None

    @property
    def insider_charges_dropped(self):
        return self._insider_charges_dropped

    @insider_charges_dropped.setter
    def insider_charges_dropped(self, value):
        check_type(value, dt, allow_none=False)
        self._insider_charges_dropped = value

    @insider_charges_dropped.deleter
    def insider_charges_dropped(self):
        self._insider_charges_dropped = None

    @property
    def insider_charges_dismissed(self):
        return self._insider_charges_dismissed

    @insider_charges_dismissed.setter
    def insider_charges_dismissed(self, value):
        check_type(value, dt, allow_none=False)
        self._insider_charges_dismissed = value

    @insider_charges_dismissed.deleter
    def insider_charges_dismissed(self):
        self._insider_charges_dismissed = None

    @property
    def insider_settled(self):
        return self._insider_settled

    @insider_settled.setter
    def insider_settled(self, value):
        check_type(value, dt, allow_none=False)
        self._insider_settled = value

    @insider_settled.deleter
    def insider_settled(self):
        self._insider_settled = None

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

    # relationships 
    @property
    def response(self):
        return self._response
    
    @response.setter
    def response(self, value):
        
        check_type(value, Response)
        self._response = value
        if value.legal_response != self:
            value.legal_response = self

    @response.deleter
    def response(self):
        temp = self._response
        self._response = None
        if temp != None:
            del temp.legal_response

    @property
    def court_cases(self):
        return self._court_cases

    @court_cases.setter
    def court_cases(self, value):
        check_type(value, list, allow_none=False)

        # check that all elements are court case objects
        for obj in value:
            
            check_type(obj, CourtCase, allow_none=False)

        # set new court case list
        # making sure to remove older relationships before
        # setting the new ones 
        if self._court_cases != None:
            # use list() to create a copy
            for cc in list(self._court_cases):
                del cc.legal_response
        self._court_cases = value

        # connect them back to this instance of legal response
        for obj in value: 
            if obj.legal_response != self:
                obj.legal_response = self
    
    def append_court_case(self, item):
        
        check_type(item, CourtCase, allow_none=False)

        if self._court_cases == None:
            self._court_cases = [item]
        else:
            self._court_cases.append(item)

        item.legal_response = self

    def remove_court_case(self, item):
        
        check_type(item, CourtCase, allow_none=False)
        if self._court_cases != None:
            del item.legal_response

    @court_cases.deleter
    def court_cases(self):
        # adding list() creates a copy so that we don't
        # run into any issues with removing elements
        # from the list we are iterating over
        for obj in list(self._court_cases):
            del obj.legal_response
        self._court_cases = None
