## Tests Documentation

### Directory Structure

```plaintext
📦tests
┣ 📂unit_tests
┃ ┣ 📜test_accomplice.py
┃ ┣ 📜test_charge.py
┃ ┣ 📜test_court_case.py
┃ ┣ 📜test_detection.py
┃ ┣ 📜test_impact.py
┃ ┣ 📜test_incident.py
┃ ┣ 📜test_insider.py
┃ ┣ 📜test_job.py
┃ ┣ 📜test_legal_response.py
┃ ┣ 📜test_organization.py
┃ ┣ 📜test_person.py
┃ ┣ 📜test_response.py
┃ ┣ 📜test_sentence.py
┃ ┣ 📜test_sponsor.py
┃ ┣ 📜test_stressor.py
┃ ┣ 📜test_target.py
┃ ┣ 📜test_ttp.py
┃ ┗ 📜__init__.py
┣ 📜base_tests.py
┣ 📜extensive_core_tests.py
┣ 📜import_export_tests.py
┣ 📜relationship_tests.py
┗ 📜validate_examples.py
```

### Discovering and Running Unit Tests

To discover and run all the unit tests in the `unit_tests` directory, you can use the following command:

```sh
python -m unittest discover -s tests/unit_tests -p "test_*.py"
```

Other tests can just be run with python:

```sh
python -m import_export_tests.py
```

## License

PyIIDES

Copyright 2024 Carnegie Mellon University.

NO WARRANTY. THIS CARNEGIE MELLON UNIVERSITY AND SOFTWARE ENGINEERING INSTITUTE MATERIAL IS FURNISHED ON AN "AS-IS" BASIS. CARNEGIE MELLON UNIVERSITY MAKES NO WARRANTIES OF ANY KIND, EITHER EXPRESSED OR IMPLIED, AS TO ANY MATTER INCLUDING, BUT NOT LIMITED TO, WARRANTY OF FITNESS FOR PURPOSE OR MERCHANTABILITY, EXCLUSIVITY, OR RESULTS OBTAINED FROM USE OF THE MATERIAL. CARNEGIE MELLON UNIVERSITY DOES NOT MAKE ANY WARRANTY OF ANY KIND WITH RESPECT TO FREEDOM FROM PATENT, TRADEMARK, OR COPYRIGHT INFRINGEMENT.

Licensed under a MIT (SEI)-style license, please see license.txt or contact permission@sei.cmu.edu for full terms.

[DISTRIBUTION STATEMENT A] This material has been approved for public release and unlimited distribution.  Please see Copyright notice for non-US Government use and distribution.

DM24-1597