"""
File: helper_functions.py

Summary:

This file contains helper functions used by the classes in 'base'

License:
PyIIDES
Copyright 2024 Carnegie Mellon University.
NO WARRANTY. THIS CARNEGIE MELLON UNIVERSITY AND SOFTWARE ENGINEERING INSTITUTE MATERIAL IS FURNISHED ON AN "AS-IS" BASIS. CARNEGIE MELLON UNIVERSITY MAKES NO WARRANTIES OF ANY KIND, EITHER EXPRESSED OR IMPLIED, AS TO ANY MATTER INCLUDING, BUT NOT LIMITED TO, WARRANTY OF FITNESS FOR PURPOSE OR MERCHANTABILITY, EXCLUSIVITY, OR RESULTS OBTAINED FROM USE OF THE MATERIAL. CARNEGIE MELLON UNIVERSITY DOES NOT MAKE ANY WARRANTY OF ANY KIND WITH RESPECT TO FREEDOM FROM PATENT, TRADEMARK, OR COPYRIGHT INFRINGEMENT.
Licensed under a MIT (SEI)-style license, please see license.txt or contact permission@sei.cmu.edu for full terms.
[DISTRIBUTION STATEMENT A] This material has been approved for public release and unlimited distribution.  Please see Copyright notice for non-US Government use and distribution.
DM24-1597
"""

from string import Formatter
import uuid
from os import path
from json import load
from datetime import *

"""
- - - - - - - - - - - - - - - - - - - - - 

        Date Helper Functions

- - - - - - - - - - - - - - - - - - - - -
"""


# found at: https://stackoverflow.com/questions/538666/format-timedelta-to-string
# Author: MarredCheese, https://stackoverflow.com/users/5405967/marredcheese
def strfdelta(tdelta, fmt='{D:02}d {H:02}h {M:02}m {S:02}s', inputtype='timedelta'):
    """
    Convert a datetime.timedelta object or a regular number to a custom-formatted string.

    This function allows custom formatting of timedelta objects similar to the strftime() method for datetime objects.

    Args:
        tdelta (timedelta or number): The timedelta object or a regular number to format.
        fmt (str): The format string. Fields can include seconds, minutes, hours, days, and weeks. Each field is optional.
            Examples:
                '{D:02}d {H:02}h {M:02}m {S:02}s' --> '05d 08h 04m 02s' (default)
                '{W}w {D}d {H}:{M:02}:{S:02}'     --> '4w 5d 8:04:02'
                '{D:2}d {H:2}:{M:02}:{S:02}'      --> ' 5d  8:04:02'
                '{H}h {S}s'                       --> '72h 800s'
        inputtype (str): The type of the input `tdelta`. Valid strings:
            's', 'seconds'
            'm', 'minutes'
            'h', 'hours'
            'd', 'days'
            'w', 'weeks'

    Returns:
        str: The formatted string representation of the timedelta or number.
    """
    # Convert tdelta to integer seconds.
    if inputtype == 'timedelta':
        remainder = int(tdelta.total_seconds())
    elif inputtype in ['s', 'seconds']:
        remainder = int(tdelta)
    elif inputtype in ['m', 'minutes']:
        remainder = int(tdelta)*60
    elif inputtype in ['h', 'hours']:
        remainder = int(tdelta)*3600
    elif inputtype in ['d', 'days']:
        remainder = int(tdelta)*86400
    elif inputtype in ['w', 'weeks']:
        remainder = int(tdelta)*604800

    f = Formatter()
    desired_fields = [field_tuple[1] for field_tuple in f.parse(fmt)]
    possible_fields = ('W', 'D', 'H', 'M', 'S')
    constants = {'W': 604800, 'D': 86400, 'H': 3600, 'M': 60, 'S': 1}
    values = {}
    for field in possible_fields:
        if field in desired_fields and field in constants:
            values[field], remainder = divmod(remainder, constants[field])
    return f.format(fmt, **values)

def check_tenure(hire_date, departure_date, tenure):
    if hire_date != None and departure_date != None:
        # Calculate the tenure
        calculated_tenure = departure_date - hire_date
        if calculated_tenure != tenure:
            raise ValueError("The tenure must be (departure date - hire date)")
        return None
    else:
        return None

"""
- - - - - - - - - - - - - - - - - - - - - 

        Subtype Helper Functions

- - - - - - - - - - - - - - - - - - - - -
"""

def check_subtype(t, st):
    """
    Determines if st is a subtype of t

    Example:
      1. "3.1.1" is a subtype of "3.1" 
    
    Non-Example:
      1. "F.1" is not a subtype of "S"
    """
    if t == None and st == None: 
        return 
    elif t == None and st != None: 
        raise ReferenceError("The parent type must exist to have a subtype")
    elif st == None:
        return 

    i = st.rfind(".")
    if t != st[:i]:
        raise ValueError(f"{st} is not a subtype of {t}") 
    return 

def check_subtype_list(tL, stL):
    """
    Determines if all of the subtypes in the subtype list are
    subtypes of those types in the type list
    """
    if tL == None or stL == None: return
    type_set = set(tL)
    if isinstance(stL, list):
        for sub_type in stL:
            i = sub_type.rfind(".")
            s = sub_type[:i]
            if s not in type_set:
                raise ValueError(f"Sub type has no parent type in the type list")
    elif isinstance(stL, str):
        i = stL.rfind(".")
        s = stL[:i]
        if s not in type_set:
            raise ValueError(f"Sub type has no parent type in the type list")
    else: 
        raise TypeError("Incorrect types passed into check_subtype_list, must be list or str")


"""
- - - - - - - - - - - - - - - - - - - - - 

        Vocab Helper Functions

- - - - - - - - - - - - - - - - - - - - -
"""

def extract_constants(vocab_name):
    """
    Extracts the 'const' values from a list of dictionaries.

    Args:
        vocab_list (list): A list of dictionaries, each containing a 'const' key.

    Returns:
        list: A list of 'const' values.
    """
    vocab_file_path = path.join(path.dirname(__file__), 'vocab.json')
    with open(vocab_file_path, 'r') as f:
        vocab = load(f)
    if vocab_name not in vocab:
        raise NameError(f"Vocabulary '{vocab_name}' not found in VOCAB.")
    return [item['const'] for item in vocab[vocab_name]]

def check_vocab(const, vocab_name):
    """
    const: str, list
     -> the constant or list that we wish to validate corresponds to the vocab_name
    vocab_name: str 
     -> the vocab we want to check the values to
    """
    if const is None:
        return True
    
    vocab_set = set(extract_constants(vocab_name))

    if isinstance(const, list):
        if vocab_name in ['technical-control-vocab', 'investigation-vocab', 'behavioral-control-vocab']:
            for item in const:
                if item[0] is None:
                    raise ValueError(f"{const} is not in the vocab")
                check_vocab(item[0], vocab_name)
            return
        if set(const) > vocab_set:
            raise ValueError(f"{const} is not in the vocab for {vocab_set}")
        for elem in const:
            if elem not in vocab_set:
                raise ValueError(f"{const} is not in the vocab for {vocab_set}")
    elif isinstance(const, str):
        if set([const]) > vocab_set or const not in vocab_set:
            raise ValueError(f"{const} is not in the vocab for {vocab_set}")
    return 

def check_uuid(uuid_str) -> None:
    """
    Returns True if uuid_str is a valid uuid, False otherwise
    """
    if not isinstance(uuid_str, str):
        raise TypeError("id must be a str")
    try:
        uuid.UUID(uuid_str, version=4)
    except:
        raise ValueError("id must correspond to a UUIDv4")
    return 

def check_type(x, type, allow_none=True) -> None:
    """
    Checks that the type of x is type "type"

    If it is not, it raises a TypeError, if it is, it returns None

    allow_none -> flag that determines whether or not we raise TypeError
                  on x == None
    """
    if x == None and not allow_none:
        raise TypeError("Cannot use NoneType here")

    if x == None or isinstance(x, type):
        return 
    else:
        raise TypeError(f"{x} should be of type {type}")

def check_tuple_list(L, vocab0, vocab1):
    """
    if L is a list: 
    Loops through a list of tuples and ensures that elem0 and elem1 are the
    correct vocabulary, and also ensures that elem1 is a subtype of elem0

    if L is a single tuple:
    checks if that tuple is valid (used for the append functionality)
    """
    if L == None: return
    if isinstance(L, tuple):
        check_vocab(L[0], vocab0)
        check_vocab(L[1], vocab1)
        check_subtype(L[0], L[1])
    elif isinstance(L, list):
        for elem in L:
            check_type(elem, tuple)
            check_vocab(elem[0], vocab0)
            check_vocab(elem[1], vocab1)
            check_subtype(elem[0], elem[1])
    else:
        raise TypeError("Input to this function must be a tuple or a list of tuples")
    
def check_iides(objects):
    """
    Checks if all objects in the given list are instances of a class with an 'id' attribute, confirming to IDES.

    Args:
        objects (list): List of objects to check.

    Returns:
        bool: True if all objects have an 'id' attribute, False otherwise.
    """
    for obj in objects:
        if not hasattr(obj, 'id'):
            raise TypeError("One or more objects failed to parse: Missing ID")
    return