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
from pyiides.utils.helper_functions import check_uuid


class Bundle:
    """
    A class used to represent a Bundle of IIDES objects.

    Attributes:
        id (str): A unique identifier for the Bundle instance. If not provided,
            a new UUID is generated.
        objects (list): A list of objects contained within the bundle.
    """

    def __init__(self, id=None, objects=None):
        if id is None:
            id = str(uuid.uuid4())

        check_uuid(id)
        self._id = id

        # Add a type checking that the objects are IIDES objects or atleast follow the format
        check_iides(objects)
        self._objects = objects

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        check_uuid(value)
        self._id = value

    @property
    def objects(self):
        return self._objects

    @objects.setter
    def objects(self, value):
        check_iides(value)
        self._objects = value

    @objects.deleter
    def objects(self):
        self._objects = None
