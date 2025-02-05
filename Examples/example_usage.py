'''
Test IIDES bundle creation and updating with example files.

License:
PyIIDES
Copyright 2024 Carnegie Mellon University.
NO WARRANTY. THIS CARNEGIE MELLON UNIVERSITY AND SOFTWARE ENGINEERING INSTITUTE MATERIAL IS FURNISHED ON AN "AS-IS" BASIS. CARNEGIE MELLON UNIVERSITY MAKES NO WARRANTIES OF ANY KIND, EITHER EXPRESSED OR IMPLIED, AS TO ANY MATTER INCLUDING, BUT NOT LIMITED TO, WARRANTY OF FITNESS FOR PURPOSE OR MERCHANTABILITY, EXCLUSIVITY, OR RESULTS OBTAINED FROM USE OF THE MATERIAL. CARNEGIE MELLON UNIVERSITY DOES NOT MAKE ANY WARRANTY OF ANY KIND WITH RESPECT TO FREEDOM FROM PATENT, TRADEMARK, OR COPYRIGHT INFRINGEMENT.
Licensed under a MIT (SEI)-style license, please see license.txt or contact permission@sei.cmu.edu for full terms.
[DISTRIBUTION STATEMENT A] This material has been approved for public release and unlimited distribution.  Please see Copyright notice for non-US Government use and distribution.
DM24-1597
'''

from datetime import datetime
import json
import pyiides

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
new_source = pyiides.Source(
    title="New Source",
    source_type="New Type",
    file_type="New File Type",
    date=datetime.fromisoformat("2023-01-01 00:00:00"),
    public=True,
    document="http://example.com")
new_bundle.objects['source'].append(new_source)

# Print the updated bundle
print("Updated Bundle object: ", new_bundle)
print("Updated Bundle ID: ", new_bundle.id)
print("Updated Bundle Charge: ", new_bundle.objects['charge'][0])
print("Updated Bundle Source: ", next((source for source in new_bundle.objects['source'] if source.title == 'New Source'), None))


# Save the updated bundle back to a JSON file
try:
    with open("example1_updated.json", "w") as f:
        f.write(pyiides.Bundle_to_json(new_bundle))
    print("Updated bundle saved to 'example1_updated.json'.")
except IOError as e:
    print(f"Error saving the updated bundle: {e}")
