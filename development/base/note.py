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


class Note:
    """
    Initialize a Note instance

    Args:
        id (required) (string) : A unique string that begins with "note--" and
            is appended with a UUIDv4.
        author (required) (string) : Individual, group, or organization that
            authored the note.
        date (required) (date-time) : Date and time the note was authored or
            most recently modified.
        comment (required) (string) : Notes, comments, details as needed.

    Raises:
        TypeError: If any provided attribute is of the incorrect type.
        ValueError: If any provided attribute is of the incorrect vocabulary.

    Example:
        >>> from pyiides.utils.helper_functions import Note
        >>> from datetime import date
        >>> note = Note(
        ...     author="John Doe",
        ...     date=date(2023, 1, 1),
        ...     comment="This is a sample comment.",
        ...     id="note--6eaf8e6c-8c4d-4d9d-8f8e-6c8c4d4d9d8f"
        ... )
        >>> print(note.author)
        John Doe
        >>> print(note.date)
        2023-01-01
    """
    def __init__(self, author, date, comment, id=None):
        if id == None:
            id = str(uuid.uuid4())

        check_uuid(id)
        self._id = id

        check_type(author, str)
        self._author = author

        check_type(date, dt)
        # There is a naming conflict between the date attribute and date type
        self._date = date

        check_type(comment, str)
        self._comment = comment

        # Relationships
        self._incident = None

    def __repr__(self):
        return (f"Note(id={self.id}, "
                f"author={self.author}, "
                f"date={self.date}, "
                f"comment={self.comment})")

    def to_dict(self):
        class_dict_copy = self.__dict__.copy()
        relationships = {'_incident'}

        if self.date != None:
            class_dict_copy["_date"] = str(self.date)

        class_dict_copy["_id"] = f"note--{self.id}"
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
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        check_type(value, str, allow_none=False)
        self._author = value

    @author.deleter
    def author(self):
        self._author = None

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        check_type(value, dt)
        self._date = value

    @date.deleter
    def date(self):
        self._date = None

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

    # - - - - - - - - RELATIONSHIPS - - - - - - - -
    @property
    def incident(self):
        return self._incident

    @incident.setter
    def incident(self, value):
        
        check_type(value, Incident, allow_none=False)

        # set the incident: 
        # if there is already an incident set, we want to 
        # remove this note instance from that incident 
        # before setting the new one
        if self._incident != None:
            self._incident.notes.remove(self)
        self._incident = value

        # add this note instance to the incident's
        # notes list
        if value.notes == None:
            value.notes = [self]
        elif self not in value.notes:
            value.notes.append(self)
    
    @incident.deleter
    def incident(self):
        if self._incident != None:
            self._incident.notes.remove(self)
            self._incident = None
