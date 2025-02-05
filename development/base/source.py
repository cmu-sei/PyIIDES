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
from datetime import datetime 


class Source:
    """
    Initializes a Source instance

    Args:
        id (string) : Unique identifier for the source. Defaults to a new UUIDv4 string if not provided.
        title (required) (string) : The title of the source.
        source_type (string) : The type of the source.
        file_type (string) : The type of file (e.g., pdf, html).
        date (datetime) : The date the source was created or last modified.
        public (bool) : Indicates if the source is public.
        document (string) : The document or URL associated with the source.

    Raises:
        TypeError: If any provided attribute is of the incorrect type.
        ValueError: If any provided attribute is of the incorrect vocabulary.
    
    Example:
        >>> from datetime import datetime
        >>> source = Source(
        ...     title="Sample Title",
        ...     id="source--123e4567-e89b-12d3-a456-426614174000",
        ...     source_type="Type A",
        ...     file_type="pdf",
        ...     date=datetime(2023, 1, 1),
        ...     public=True,
        ...     document="http://example.com"
        ... )
        >>> print(source.title)
        Sample Title
        >>> print(source.date)
        2023-01-01 00:00:00
    """
    def __init__(self, title, id=None, source_type=None, file_type=None, date=None, public=None, document=None):
        if id is None:
            id = str(uuid.uuid4())
        check_uuid(id)
        self._id = id

        check_type(title, str)
        self._title = title 

        check_type(source_type, str)
        self._source_type = source_type

        check_type(file_type, str)
        self._file_type = file_type

        check_type(date, datetime)
        self._date = date

        check_type(public, bool)
        self._public = public

        check_type(document, str)
        self._document = document 

        # relationships 
        self._incident = None 
    
    def __repr__(self):
        return (f"Source(id={self.id}, "
                f"title={self.title}, "
                f"source_type={self.source_type}, "
                f"file_type={self.file_type}, "
                f"date={self.date}, "
                f"public={self.public}, "
                f"document={self.document})")

    def to_dict(self):
        class_dict_copy = self.__dict__.copy()
        relationships = {'_incident'}

        if self.date != None:
            class_dict_copy["_date"] = str(self.date)

        class_dict_copy["_id"] = f"source--{self.id}"
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
        check_type(value, str)
        self._title = value 

    @title.deleter
    def title(self):
        self._title = None 

    @property
    def source_type(self):
        return self._source_type

    @source_type.setter
    def source_type(self, value):
        check_type(value, str)
        self._source_type = value

    @source_type.deleter
    def source_type(self):
        self._source_type = None

    @property
    def file_type(self):
        return self._file_type

    @file_type.setter
    def file_type(self, value):
        check_type(value, str)
        self._file_type = value

    @file_type.deleter
    def file_type(self):
        self._file_type = None

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        check_type(value, datetime)
        self._date = value

    @date.deleter
    def date(self):
        self._date = None

    @property
    def public(self):
        return self._public

    @public.setter
    def public(self, value):
        check_type(value, bool)
        self._public = value

    @public.deleter
    def public(self):
        self._public = None

    @property
    def document(self):
        return self._document

    @document.setter
    def document(self, value):
        check_type(value, str)
        self._document = value

    @document.deleter
    def document(self):
        self._document = None
    
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
            self._incident.sources.remove(self)
        self._incident = value

        # add this note instance to the incident's
        # sources list
        if value.sources == None:
            value.sources = [self]
        elif self not in value.sources:
            value.sources.append(self)
    
    @incident.deleter
    def incident(self):
        if self._incident != None:
            self._incident.sources.remove(self)
            self._incident = None
