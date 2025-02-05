"""
File: vocab.py

Summary:

This file will generate the vocab.json by collecting all the vocab
from the json schema and parsing it to one file.

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
import json
import requests
import certifi


SCHEMA_URL = 'https://raw.githubusercontent.com/cmu-sei/iides/refs/heads/main/json/'
SCHEMA_FILES = [
    'common/country-vocab.json',
    'common/insider-relationship-vocab.json',
    'common/state-vocab.json',
    'objects/accomplice.json',
    'objects/bundle.json',
    'objects/charge.json',
    'objects/court-case.json',
    'objects/detection.json',
    'objects/impact.json',
    'objects/incident.json',
    'objects/insider.json',
    'objects/job.json',
    'objects/legal-response.json',
    'objects/note.json',
    'objects/organization.json',
    'objects/person.json',
    'objects/response.json',
    'objects/sentence.json',
    'objects/source.json',
    'objects/sponsor.json',
    'objects/stressor.json',
    'objects/target.json',
    'objects/ttp.json',
    'structs/collusion.json',
    'structs/org-owner.json',
    'structs/org-relationship.json',
    'structs/relationship.json'
]


if __name__ == "__main__":
    # Define the directory containing JSON files (replace with your path)
    vocab_json = "pyiides/utils/vocab.json"

    # Create an empty dictionary to store vocabulary data
    vocabulary = {}

    for filename in SCHEMA_FILES:
        response = requests.get(SCHEMA_URL+filename, verify=certifi.where())
        schema = json.loads(response.content.decode('utf-8'))
        if '$defs' in schema:
            for vocab_bundle in schema['$defs']:
                const_list = []
                if 'oneOf' in schema['$defs'][vocab_bundle]:
                    for oneof_obj in schema['$defs'][vocab_bundle]['oneOf']:
                        const_list.append(oneof_obj)
                if 'anyOf' in schema['$defs'][vocab_bundle]:
                    for anyof_obj in schema['$defs'][vocab_bundle]['anyOf']:
                        const_list.append(anyof_obj)
                if 'enum' in schema['$defs'][vocab_bundle]:
                    for enum_obj in schema['$defs'][vocab_bundle]['enum']:
                        const_list.append(enum_obj)
                vocabulary[vocab_bundle] = const_list

    f = open(f"{vocab_json}", "w")
    f.write(json.dumps(vocabulary, indent=4))
    f.close()
    print("Successfuly made vocab.")
