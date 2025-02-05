The PyIIDES structure, classes, attributes, and vocabularly are based on [IIDES](https://github.com/sei-cmu/IIDES). The following are instructions for updating PyIIDES when IIDES changes or when making changes to PyIIDES for local implementations. If adding or changing attributes or vocabulary, consider submitting a request for a change to IIDES instead.

**Table of Contents**
1. [Understanding the PyIIDES Development Directory](#understanding-the-pyiides-development-directory)
2. [Development Scripts](#development-scripts)
3. [Changing Vocabulary](#changing-vocabulary)
4. [Example Base Python File](#example-base-python-file-accomplicepy)
5. [Contributing to PyIIDES](#contributing-to-pyiides)
6. [Testing Your Changes](#testing-your-changes)
7. [Updating Documentation](#updating-documentation)

# Understanding the PyIIDES Development Directory

For ease of development, PyIIDES splits the IIDES components and subcomponents into separate files. When changes need to be made to components, subcomponents, or their attributes, make the change in the component's dedicated python file.

```📦 development
┣ 📂 base
┃ ┣ 📜 accomplice.py
┃ ┣ 📜 bundle.py
┃ ┣ 📜 charge.py
┃ ┣ ...
┃ ┗ 📜 __init__.py
┣ 📜 gen_vocab.py
┣ 📜 gen_vocab_rst.py
┣ 📜 host_schema.py
┣ 📜 join_classes.py
┗ 📜 README.md
```

## Development Scripts

After you have made changes to PyIIDES you will need to use one or more of the following scripts to ensure the pyiides package itself will incorporate those changes.

- **join_classes.py**: Used after making changes to any of the files inside of the `base/` directory. This script compiles all classes into one file, `pyiides.py` which will contain all of the code present in the `base/` folder.
- **gen_vocab.py**: Used after making changes to any of the vocabulary in the IIDES schema. The `gen_vocab.py` script will read the current schema in `pyiides/utils/json` and compile a large vocabulary dictionary, `vocab.json`, that is used by the `check_vocab` function in `pyiides/utils/helper_functions.py`.
- **host_schema.py**: This script will host the schema for the JSON schema references to work (this is a workaround for not having the schema available online yet).
- **gen_vocab_rst.py**: Used after making changes to any of the vocabulary in the IIDES schema. This script regenerates the documentation RST files used by Sphinx for the PyIIDES html documentation.

## Changing Vocabulary

To incorporate changes made to any of the vocabularies used by PyIIDES,

1. Run the gen_vocab script to compile the full vocabularly dictionary used by pyiides. Note, this will pull from the IIDES repository on GitHub. If you want to make custom changes make them directly to the vocab.json file in the pyiides/utils folder.

```sh
# From the pyiides root
python development/gen_vocab.py
```

3. Run the gen_vocab_rst script to regenerate RST documentation files for the vocabulary.

```sh
# From the root folder
python development/gen_vocab_rst.py
```

4. Update the rest of the documentation and repackage PyIIDES (see [Updating Documentation](#updating-documentation) below)

## Example Base Python File: accomplice.py

The Accomplice class is a subclass of the Person class and includes additional attributes and methods specific to an accomplice in the context of the module.

### Initialization Method

The **init** method initializes an instance of the Accomplice class, setting up default values and performing type and vocabulary checks.

```python
def __init__(self, id=None, relationship_to_insider=None, **kwargs):
super().**init**(**kwargs) # Inherit from Person

    if id is None:
        id = str(uuid.uuid4())  # Generate a new UUID if not provided

    check_uuid(id)  # Validate UUID
    self._id = id

    check_type(relationship_to_insider, str)
    check_vocab(relationship_to_insider, 'insider-relationship-vocab')
    self._relationship_to_insider = relationship_to_insider

    self._insider = None
    self._jobs = None
    self._sponsor = None
```

### Getter, Setter, and Deleter Methods

These methods are used to control access to the attributes of the class, ensuring proper validation and encapsulation.

#### Getter Method

The getter method retrieves the value of an attribute.

```python
@property
def id(self):
    return self._id # Return the ID of the accomplice
```

#### Setter Method

The setter method sets the value of an attribute, with validation to ensure it meets specific criteria.

```python
@id.setter
def id(self, value):
    check_uuid(value) # Validate UUID
    self._id = value # Set the ID of the accomplice
```

#### Deleter Method

The deleter method removes the value of an attribute, typically resetting it to None.

```python
@insider.deleter
def insider(self):
    if self._insider != None:
        self._insider.accomplices.remove(self)
        self._insider = None
```

#### Relationships

The Accomplice class includes relationships with other entities such as insiders, jobs, and sponsors. These methods ensure that relationships are correctly established and maintained.

##### Example: Managing insider Relationship

```python
@property
def insider(self):
return self._insider

@insider.setter
def insider(self, value):
from development.base.insider import Insider
check_type(value, Insider, allow_none=False)

    if self._insider != None:
        self._insider.accomplices.remove(self)
    self._insider = value

    if value.accomplices == None:
        value.accomplices = [self]
    elif self not in value.accomplices:
        value.accomplices.append(self)

@insider.deleter
def insider(self):
if self._insider != None:
self._insider.accomplices.remove(self)
self._insider = None
```

As you can see the relationship set and delete effect both involved classes. When initializing the insider relationship to the accomplice, we add the insider to the accomplice object as well as add the accomplice to the insider object.

## Contributing to `pyiides`

### Adding a Class, Attribute, or Field

If you need to add a new class, attribute, or field to the module, follow these steps to ensure consistency and maintain the integrity of the project:

### Adding a New Class

1. **Create the Class File**:

   - Navigate to the `development/base/` directory.
   - Create a new Python file named after your class (e.g., `new_class.py`).

2. **Define the Class**:

   - Ensure your class inherits from the appropriate base class, if applicable (e.g., `Person`).

3. **Implement Initialization**:

   - Include an `__init__` method to initialize the class attributes.

4. **Add Validation**:

   - Use helper functions (`check_uuid`, `check_type`, `check_vocab`) to validate the attributes.
     - To create a new vocab list just ammend it to the vocab dictionary in the pyiides folder.

5. **Manage Relationships**:

   - If your class has relationships with other entities, include getter, setter, and deleter methods to manage these relationships.

6. **Example**:

```python
from .person import Person
from pyiides.utils.helper_functions import *

class NewClass(Person): # new class inheriting from Person
    def __init__(self, id=None, new_attribute=None, **kwargs):
        super().__init__(**kwargs)

        if id is None:
            id = str(uuid.uuid4())
        check_uuid(id)
        self._id = id

        check_type(new_attribute, str)
        self._new_attribute = new_attribute

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        check_uuid(value)
        self._id = value

    @property
    def new_attribute(self):
        return self._new_attribute

    @new_attribute.setter
    def new_attribute(self, value):
        check_type(value, str)
        check_vocab(value, 'value-vocab')
        self._new_attribute = value

    @new_attribute.deleter
    def new_attribute(self):
        self._new_attribute = None
```

### Adding an Attribute or Field to an Existing Class

1. **Update the Class File**:

   - Navigate to the file containing the class (e.g., `accomplice.py`).

2. **Modify the `__init__` Method**:

   - Add the new attribute to the `__init__` method, including default values and validation.

3. **Create Getter, Setter, and Deleter Methods**:

   - Add these methods to manage the new attribute.

4. **Example**:

Adding `new_field` to `Accomplice` class in `accomplice.py`:

```python
class Accomplice(Person):
    def __init__(self, id=None, relationship_to_insider=None, new_field=None, **kwargs):
        super().__init__(**kwargs)

        if id is None:
            id = str(uuid.uuid4())
        check_uuid(id)
        self._id = id

        check_type(relationship_to_insider, str)
        check_vocab(relationship_to_insider, 'insider-relationship-vocab')
        self._relationship_to_insider = relationship_to_insider

        check_type(new_field, str)
        self._new_field = new_field

    @property
    def new_field(self):
        return self._new_field

    @new_field.setter
    def new_field(self, value):
        check_type(value, str)
        self._new_field = value

    @new_field.deleter
    def new_field(self):
        self._new_field = None
```

## Testing Your Changes

1. **Add Unit Tests**:

   - Navigate to the `tests/unit_tests` directory.
   - Create a new test file or update an existing one to include tests for your new class, attribute, or field.

2. **Run Tests**:
   - Issue the following command respective to the new test.

```sh
python -m unittest discover -s tests/unit_tests -p "test_*.py"
```

## Updating Documentation

**Update examples**

1. Ensure examples and usage instructions are include in the docstrings for any new or modified classes or functions
2. Update the examples in `Examples` to include examples of the new or modified component, attribute, or vocabulary
3. Import and export the updated examples to ensure these functions work properly.

**Update Sphinx source**

1. Ensure that any new classes are included in the `pyiides.rst` file in `docs/source`
2. If vocabulary has changed run the `gen_vocab.py` and `gen_vocab_rst.py` scripts in `docs/source`
3. Build the html documentation (from docs directory)

```sh
make html
```

**Update setup.py and build the package**

1. Increase the version number in the setup.py file
2. Build the package

```sh
python -m build
```

## License

PyIIDES

Copyright 2024 Carnegie Mellon University.

NO WARRANTY. THIS CARNEGIE MELLON UNIVERSITY AND SOFTWARE ENGINEERING INSTITUTE MATERIAL IS FURNISHED ON AN "AS-IS" BASIS. CARNEGIE MELLON UNIVERSITY MAKES NO WARRANTIES OF ANY KIND, EITHER EXPRESSED OR IMPLIED, AS TO ANY MATTER INCLUDING, BUT NOT LIMITED TO, WARRANTY OF FITNESS FOR PURPOSE OR MERCHANTABILITY, EXCLUSIVITY, OR RESULTS OBTAINED FROM USE OF THE MATERIAL. CARNEGIE MELLON UNIVERSITY DOES NOT MAKE ANY WARRANTY OF ANY KIND WITH RESPECT TO FREEDOM FROM PATENT, TRADEMARK, OR COPYRIGHT INFRINGEMENT.

Licensed under a MIT (SEI)-style license, please see license.txt or contact permission@sei.cmu.edu for full terms.

[DISTRIBUTION STATEMENT A] This material has been approved for public release and unlimited distribution.  Please see Copyright notice for non-US Government use and distribution.

DM24-1597
