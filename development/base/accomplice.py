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
import uuid
from pyiides.utils.helper_functions import check_uuid, check_type, check_vocab
from .person import Person


class Accomplice(Person):
    """
    Initialize an Accomplice instance, inheriting from Person.

    Args:
        id (str): Unique identifier for the accomplice. Defaults to a new
            UUIDv4 string if not provided.
        relationship_to_insider (str): The relationship of the accomplice to
            the insider. Must be a valid constant from
            `insider-relationship-vocab <./vocab/insider-relationship-vocab.html>`_.
        **kwargs (dict): Additional attributes inherited from the Person class.

    Raises:
        TypeError: If any provided attribute is of the incorrect type.
        ValueError: If any provided attribute is of the incorrect vocabulary.

    Examples:
        >>> from pyiides.pyiides.accomplice import Accomplice
        >>> accomplice = Accomplice(
        ...     first_name="John",
        ...     last_name="Doe",
        ...     relationship_to_insider="1"
        ... )
        >>> print(accomplice.id)
        e6d8b622-8d6a-4f5b-8b9a-d7c93c6ee6b6
        >>> print(accomplice.relationship_to_insider)
        1
    """
    def __init__(self, id=None, relationship_to_insider=None, **kwargs):
        # inherit everything from Person
        super().__init__(**kwargs)

        if id is None:
            id = str(uuid.uuid4())

        check_uuid(id)
        self._id = id

        check_type(relationship_to_insider, str)
        check_vocab(relationship_to_insider, 'insider-relationship-vocab')
        self._relationship_to_insider = relationship_to_insider

        # Relationships:
        self._insider = None
        self._jobs = None
        self._sponsor = None

    def __repr__(self):
        return (f"Accomplice(id={self.id}, "
                f"relationship_to_insider={self.relationship_to_insider})")

    def to_dict(self):
        """
        returns tuple: (dict of class itself, list containing child id's to connect)
        """
        class_dict_copy = self.__dict__.copy()

        relationships = {'_insider', '_jobs', '_sponsor'}

        children_ids = None
        if self.jobs != None:
            children_ids = ["jobs--" + x.id for x in self.jobs]

        class_dict_copy["_id"] = f"accomplice--{self.id}"
        return ({
                    key.lstrip('_'): value
                    for key, value in class_dict_copy.items()
                    if key not in relationships
                },
                children_ids
                )

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        check_uuid(value)
        self._id = value

    @property
    def relationship_to_insider(self):
        return self._relationship_to_insider

    @relationship_to_insider.setter
    def relationship_to_insider(self, value):
        check_type(value, str, allow_none=False)
        check_vocab(value, 'insider-relationship-vocab')
        self._relationship_to_insider = value

    @relationship_to_insider.deleter
    def relationship_to_insider(self):
        self._relationship_to_insider = None

    # - - - - - - - - - - RELATIONSHIPS - - - - - - - - - -
    @property
    def insider(self):
        return self._insider

    @insider.setter
    def insider(self, value):
        
        check_type(value, Insider, allow_none=False)

        # set the insider
        # making sure to remove all old relationships first if they exist
        if self._insider != None:
            self._insider.accomplices.remove(self)
        self._insider = value

        # add this accomplice to the insider's accomplice list
        if value.accomplices == None:
            value.accomplices = [self]
        elif self not in value.accomplices:
            value.accomplices.append(self)

    @insider.deleter
    def insider(self):
        if self._insider != None:
            self._insider.accomplices.remove(self)
            self._insider = None

    @property
    def jobs(self):
        return self._jobs

    @jobs.setter
    def jobs(self, value):
        # to the future dev: im sorry i didnt modularize these setters/getters,
        # they could be made into one cute little helper function
        # you got it :)
        check_type(value, list)

        # check that all elements are Job objects
        for obj in value:
            
            check_type(obj, Job, allow_none=False)

        # set the new job list
        # making sure to remove old relationships first if they exist
        if self._jobs != None:
            for j in list(self._jobs):
                del j.accomplice
        self._jobs = value

        # connect those jobs back to this instance of accomplice
        for obj in value:
            if obj.accomplice != self:
                obj.accomplice = self

    def append_job(self, item):
        
        check_type(item, Job, allow_none=False)

        if self._jobs == None:
            self._jobs = [item]
        else:
            self._jobs.append(item)

        item.accomplice = self

    def remove_job(self, item):
        
        check_type(item, Job, allow_none=False)
        if self._jobs != None:
            del item.accomplice

    @jobs.deleter
    def jobs(self):
        # need to create a copy using list() since we
        # are removing from the list we are also
        # iterating over
        for obj in list(self._jobs):
            del obj.accomplice
        self._jobs = None

    @property
    def sponsor(self):
        return self._sponsor

    @sponsor.setter
    def sponsor(self, value):
        
        check_type(value, Sponsor, allow_none=False)

        # set the sponsor
        # making sure to remove old relationships first
        if self._sponsor != None:
            self._sponsor.accomplices.remove(self)
        self._sponsor = value

        # add it to the sponsor's accomplice list
        if value.accomplices == None:
            value.accomplices = [self]
        elif self not in value.accomplices:
            value.accomplices.append(self)

    @sponsor.deleter
    def sponsor(self):
        if self._sponsor != None:
            self._sponsor.accomplices.remove(self)
            self._sponsor = None
