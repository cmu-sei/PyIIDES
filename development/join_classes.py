'''
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
'''

import os

LICENSE = (
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
)
IMPORTS = [
    "import uuid",
    "from datetime import datetime, timedelta",
    "from datetime import date as dt",
    "from pyiides.utils.helper_functions import (\n    check_tenure, check_subtype, check_subtype_list, check_uuid, check_type, check_vocab, check_iides, check_tuple_list)",
]


def skip_license(lines):
    '''Returns the index of the first line with code'''
    for index, line in enumerate(lines):
        if line.startswith("class "):
            return index


def merge_python_files(src_dir, output_dir, output_file, priority_file):
    if not os.path.isdir(src_dir):
        raise ValueError(f"Source directory {src_dir} does not exist.")

    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    output_path = os.path.join(output_dir, output_file)
    other_code = []
    priority_code = []

    # Function to process a file and collect imports and other code
    def process_file(file_path, code_list):
        with open(file_path, 'r') as infile:
            lines = infile.readlines()
            for line in lines[skip_license(lines):]:
                code_list.append(line)
            code_list.append("\n\n")

    # Process the priority file first
    priority_file_path = os.path.join(src_dir, priority_file)
    if os.path.isfile(priority_file_path):
        process_file(priority_file_path, priority_code)
    else:
        raise ValueError(
            f"Priority file {priority_file} does not exist in {src_dir}.")

    # Process all other files
    for filename in os.listdir(src_dir):
        if filename.endswith('.py') and filename != '__init__.py' and filename != priority_file:
            file_path = os.path.join(src_dir, filename)
            process_file(file_path, other_code)

    with open(output_path, 'w') as outfile:
        outfile.write('"""')
        outfile.write(LICENSE)
        outfile.write('"""\n')
        outfile.write('\n'.join(IMPORTS))

        # Write the priority code first
        outfile.write('\n\n\n# --- Priority Content ---\n')
        for line in priority_code:
            outfile.write(line)
        outfile.write('\n')

        # Write all other code
        outfile.write('# --- Merged Content ---\n')
        for line in other_code:
            outfile.write(line)


if __name__ == "__main__":

    pyiides_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

    src_directory = os.path.join(pyiides_dir, 'development', 'base')  # Source directory containing class Python files
    output_directory = os.path.join(pyiides_dir, 'pyiides')  # Output directory for the merged file
    output_filename = 'pyiides.py'  # Output file name
    priority_filename = 'person.py'  # Priority file containing the Person class

    merge_python_files(
        src_directory, output_directory, output_filename, priority_filename)
    print(
        f"Merged all Python files from {src_directory} into {os.path.join(output_directory, output_filename)}, with {priority_filename} content first.")
