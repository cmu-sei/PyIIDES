"""
License:
PyIIDES
Copyright 2024 Carnegie Mellon University.
NO WARRANTY. THIS CARNEGIE MELLON UNIVERSITY AND SOFTWARE ENGINEERING INSTITUTE MATERIAL IS FURNISHED ON AN "AS-IS" BASIS. CARNEGIE MELLON UNIVERSITY MAKES NO WARRANTIES OF ANY KIND, EITHER EXPRESSED OR IMPLIED, AS TO ANY MATTER INCLUDING, BUT NOT LIMITED TO, WARRANTY OF FITNESS FOR PURPOSE OR MERCHANTABILITY, EXCLUSIVITY, OR RESULTS OBTAINED FROM USE OF THE MATERIAL. CARNEGIE MELLON UNIVERSITY DOES NOT MAKE ANY WARRANTY OF ANY KIND WITH RESPECT TO FREEDOM FROM PATENT, TRADEMARK, OR COPYRIGHT INFRINGEMENT.
Licensed under a MIT (SEI)-style license, please see license.txt or contact permission@sei.cmu.edu for full terms.
[DISTRIBUTION STATEMENT A] This material has been approved for public release and unlimited distribution.  Please see Copyright notice for non-US Government use and distribution.
DM24-1597
"""
import sys
import os
import json

# Add the current working directory to the system path
sys.path.append(os.getcwd())

# Import the Bundle class from the pyiides.bundle module
from development.base import Bundle
from pyiides.utils import bundle_util

# Open and load the example JSON file
"""
Validating each example before instantiation
"""
json_examples = []
bundles = []
for i in range(1,5):
    with open('Examples/example' + str(i) + '.json') as f:
        data = json.load(f)
    json_examples.append(data)
    

    # Create a Bundle instance with the objects from the JSON data
    bundle = bundle_util.json_to_Bundle(data)
    bundles.append(bundle)

    # Print the initial objects in the bundle
    print("Initial objects in the bundle:")
    print(bundle.objects)


    print("testing export")
    j = bundle_util.Bundle_to_json(bundle)

    print("\n\n\n\n")
    print(j)