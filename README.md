# PyIIDES

PyIIDES is a Python implementation of the [IIDES (Insider Incident Data Exchange Standard)](https://github.com/cmu-sei/iides) schema. This package provides tools for the coding, storage, and sharing of data related specifically to insider incidents of all kinds.

## Introduction

PyIIDES leverages the [IIDES](https://github.com/cmu-sei/iides) framework to help organizations and researchers efficiently handle insider threat data. By implementing IIDES in Python, PyIIDES facilitates the creation, management, and sharing of insider incident data using a standardized schema.

## Benefits

PyIIDES provides a range of benefits for users in both research and operational environments:

- **Efficient Data Sharing**: Supports the consistent sharing of incident data among practitioners, organizations, and researchers.
- **Standardized Vocabulary**: Provides a foundational vocabulary for incident data, aiding in the development of consistent reporting mechanisms.
- **Ease of Integration**: Simplifies the integration of IIDES into existing data collection and case management systems.

## Features

- **Dynamic Dating**: Insider tenure is automatically calculated via Python date objects, ensuring accurate and consistent date management.

  ```python
  from pyiides import Job
  from datetime import datetime

  job = Job(
      id="123e4567-e89b-12d3-a456-426614174000",
      job_function="15",
      occupation="15.1",
      title="Software Developer",
      position_technical=True,
      access_authorization="3",
      employment_type="FLT",
      hire_date=datetime(2020, 1, 1),
      departure_date=datetime(2022, 1, 1),
      comment="This is a test job."
  )
  print(job.tenure)  # Outputs timedelta(days=731)
  ```

- **Responsive Relationships**: Deleting one side of a relationship will terminate that relationship in both objects, as well as creating a new relationship.

  ```python
  from pyiides import LegalResponse, CourtCase

  legal_response = LegalResponse(id="123e4567-e89b-12d3-a456-426614174000")
  court_case = CourtCase(id="456e7890-b12d-34f5-g678-901hijklm234")

  legal_response.add_court_case(court_case)
  print(legal_response.court_cases)  # Includes court_case
  print(court_case.legal_response)  # Points to legal_response

  legal_response.remove_court_case(court_case)
  print(legal_response.court_cases)  # Does not include court_case
  print(court_case.legal_response)  # Is None
  ```

- **Expandability**: Pass in any additional fields into any object using new parameters.

  ```python
  from pyiides import CourtCase
  from datetime import datetime

  court_case = CourtCase(
      id="456e7890-b12d-34f5-g678-901hijklm234",
      additional_date=datetime(2023, 5, 1)  # Custom field
  )
  print(court_case.additional_date)  # Outputs datetime(2023, 5, 1)
  ```

- **Data Integrity**: Ensures data integrity through strict type and value checking, raising errors when needed.

## IIDES Architecture in PyIIDES

PyIIDES implements the core components, subcomponents, relationships, and vocabularies defined by IIDES.

### Core Components

The core components implemented in PyIIDES are:

- **Incident**: Represents an insider incident.
- **Insider**: Represents individuals involved in the incident.
- **Organization**: Represents organizations involved in the incident.
- **Job**: Represents employment details related to the insider.
- **Detection**: Describes how, when, and by whom the incident was detected.
- **Response**: Describes the organization's response to the incident.
- **TTP**: Details specific actions taken by the insider during the incident.

### Subcomponents

- **Target**: The system, data, person, or property targeted by the insider.
- **Impact**: Quantitative measurement of the impact of the incident.
- **Note**: Details unrelated to the incident, such as case management notes or research references.
- **Source**: Documents and files related to the incident or its investigation.
- **Legal Response**: Specific details about incidents that go through the legal system, including court cases, charges, and sentences.

### Relationships

PyIIDES connects components through relationships defined by IIDES. Some of the primary relationships include:

- **Incident to Insider**: An incident can be associated with one or more insiders.
- **Incident to Organization**: Organizations involved in the incident.
- **Job to Insider**: Employment details related to the insider.
- **Incident to Detection**: How the incident was detected.
- **Incident to Response**: The organization's response to the incident, including legal responses.
- **Incident to TTP**: Actions taken by the insider during the incident.

## Installation

Download directly from PyPI:

`pip install pyiides`

OR

Local install after downloading the GitHub repository:

1. Clone the repository or download the project files to your local machine.
2. Navigate to the project directory.
3. Install the package using pip in editable mode:

   ```sh
   pip install -e .
   ```

## Usage

Below is an example of how to use PyIIDES to create a legal response:

```python
from pyiides import LegalResponse
from datetime import datetime

legal_response = LegalResponse(
    id="123e4567-e89b-12d3-a456-426614174000",
    law_enforcement_contacted=datetime(2020, 1, 1),
    insider_arrested=datetime(2020, 1, 2),
    insider_charged=datetime(2020, 1, 3),
    insider_pleads=datetime(2020, 1, 4),
    insider_judgment=datetime(2020, 1, 5),
    insider_sentenced=datetime(2020, 1, 6),
    insider_charges_dropped=datetime(2020, 1, 7),
    insider_charges_dismissed=datetime(2020, 1, 8),
    insider_settled=datetime(2020, 1, 9),
    comment="This is a test legal response."
)

print(legal_response)
```

If working with larger datasets you can use IIDES conformant data and import it as bundles into PyIIDES. Below is an example of importing the first example json file from the Examples folder as a bundle, making some changes, and then exporting it to a new file:

```python
import pyiides
import json
from datetime import datetime

# Create a new bundle from json file
with open("example1.json") as f:
    data = json.load(f)

new_bundle = pyiides.json_to_Bundle(data)
# Errors will be thrown if the json file is not formatted correctly

# Print some information about the bundle
print("Bundle object: ", new_bundle)
print("Bundle ID: ", new_bundle.id)
print("First Bundle Charge: ", new_bundle.objects['charge'][0])
print("First Bundle Source: ", new_bundle.objects['source'][0])

# Update a charge object
target_charge = new_bundle.objects['charge'][0]
target_charge.plea_bargain = True

# Create a new source object
new_source = pyiides.Source(title="New Source", source_type="New Type", file_type="New File Type", date=datetime.fromisoformat("2023-01-01 00:00:00"), public=True, document="http://example.com")
new_bundle.objects['source'].append(new_source)

# Print the updated bundle
print("Updated Bundle object: ", new_bundle)
print("Updated Bundle ID: ", new_bundle.id)
print("Updated Bundle Charge: ", new_bundle.objects['charge'][0])

# Printing the new source via iterating through the source list and finding the matching source title
print("Updated Bundle Source: ", next((source for source in new_bundle.objects['source'] if source.title == 'New Source'), None))


# Save the updated bundle back to a JSON file
try:
    with open("example1_updated.json", "w") as f:
        f.write(pyiides.Bundle_to_json(new_bundle))
    print("Updated bundle saved to 'example1_updated.json'.")
except IOError as e:
    print(f"Error saving the updated bundle: {e}")
```

The corresponding output should be:
![Import-Change-Export-Example](images/import-change-export-example.png)
with the respective changes in a new file named **example1_updated.json**

## Contributing

We welcome contributions to PyIIDES. Please submit issues, discussions, or pull requests via the PyIIDES GitHub page.

## License

PyIIDES

Copyright 2024 Carnegie Mellon University.

NO WARRANTY. THIS CARNEGIE MELLON UNIVERSITY AND SOFTWARE ENGINEERING INSTITUTE MATERIAL IS FURNISHED ON AN "AS-IS" BASIS. CARNEGIE MELLON UNIVERSITY MAKES NO WARRANTIES OF ANY KIND, EITHER EXPRESSED OR IMPLIED, AS TO ANY MATTER INCLUDING, BUT NOT LIMITED TO, WARRANTY OF FITNESS FOR PURPOSE OR MERCHANTABILITY, EXCLUSIVITY, OR RESULTS OBTAINED FROM USE OF THE MATERIAL. CARNEGIE MELLON UNIVERSITY DOES NOT MAKE ANY WARRANTY OF ANY KIND WITH RESPECT TO FREEDOM FROM PATENT, TRADEMARK, OR COPYRIGHT INFRINGEMENT.

Licensed under a MIT (SEI)-style license, please see license.txt or contact permission@sei.cmu.edu for full terms.

[DISTRIBUTION STATEMENT A] This material has been approved for public release and unlimited distribution.  Please see Copyright notice for non-US Government use and distribution.

DM24-1597
