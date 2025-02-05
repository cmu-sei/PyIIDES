## `pyiides` Module Documentation

The `pyiides` module is designed to handle various aspects of incident detection, insider threat management, and related processes. It includes utilities for managing JSON schemas, vocabulary, and other helper functions. Below is a detailed overview of the module's structure and its components.

### Directory Structure

```plaintext
📦pyiides
 ┣ 📂utils
 ┃ ┣ 📂json
 ┃ ┃ ┣ 📂common
 ┃ ┃ ┃ ┣ 📜country-vocab.json
 ┃ ┃ ┃ ┣ 📜insider-relationship-vocab.json
 ┃ ┃ ┃ ┗ 📜state-vocab.json
 ┃ ┃ ┣ 📂objects
 ┃ ┃ ┃ ┣ 📜accomplice.json
 ┃ ┃ ┃ ┣ 📜bundle.json
 ┃ ┃ ┃ ┣ 📜charge.json
 ┃ ┃ ┃ ┣ 📜court-case.json
 ┃ ┃ ┃ ┣ 📜detection.json
 ┃ ┃ ┃ ┣ 📜impact.json
 ┃ ┃ ┃ ┣ 📜incident.json
 ┃ ┃ ┃ ┣ 📜insider.json
 ┃ ┃ ┃ ┣ 📜job.json
 ┃ ┃ ┃ ┣ 📜legal-response.json
 ┃ ┃ ┃ ┣ 📜note.json
 ┃ ┃ ┃ ┣ 📜organization.json
 ┃ ┃ ┃ ┣ 📜person.json
 ┃ ┃ ┃ ┣ 📜response.json
 ┃ ┃ ┃ ┣ 📜sentence.json
 ┃ ┃ ┃ ┣ 📜source.json
 ┃ ┃ ┃ ┣ 📜sponsor.json
 ┃ ┃ ┃ ┣ 📜stressor.json
 ┃ ┃ ┃ ┣ 📜target.json
 ┃ ┃ ┃ ┗ 📜ttp.json
 ┃ ┃ ┗ 📂structs
 ┃ ┃ ┃ ┣ 📜collusion.json
 ┃ ┃ ┃ ┣ 📜org-owner.json
 ┃ ┃ ┃ ┣ 📜org-relationship.json
 ┃ ┃ ┃ ┗ 📜relationship.json
 ┃ ┃
 ┃ ┣ 📜bundle_util.py
 ┃ ┣ 📜helper_functions.py
 ┃ ┗ 📜vocab.json
 ┣ 📂__pycache__
 ┃ ┣ 📜pyiides.cpython-312.pyc
 ┃ ┗ 📜__init__.cpython-312.pyc
 ┣ 📜pyiides.py
 ┣ 📜README.md
 ┗ 📜__init__.py
```

## Description of Components

- **pyiides/**:

  - **pyiides**.py: The main module file which contains all of the base python files compiled into one file.

  - **init**.py: Initializes the pyiides package. The **all** list explicitly declares the public API of the module. When someone uses from pyiides import \*, only the names listed in **all** will be imported. Including items in the init will ensure the "from pyiides import ..." works.

    - **utils/**:
      - bundle_util.py: Contains utility functions related to bundling operations like import/export.
      - helper_functions.py: Contains various helper functions used across the module including validators like check_vocab and check_type.
      - vocab.json: Stores the compiled vocabulary dictionary used for various checks and validations. Compiled by ../development/gen_vocab.py
    - **json/**: The IIDES json schema is included in the python package until the schema is accessible online.
