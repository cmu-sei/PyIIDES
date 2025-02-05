'''
Generates Sphinx RST files for all IIDES vocabularies

License:
PyIIDES
Copyright 2024 Carnegie Mellon University.
NO WARRANTY. THIS CARNEGIE MELLON UNIVERSITY AND SOFTWARE ENGINEERING INSTITUTE MATERIAL IS FURNISHED ON AN "AS-IS" BASIS. CARNEGIE MELLON UNIVERSITY MAKES NO WARRANTIES OF ANY KIND, EITHER EXPRESSED OR IMPLIED, AS TO ANY MATTER INCLUDING, BUT NOT LIMITED TO, WARRANTY OF FITNESS FOR PURPOSE OR MERCHANTABILITY, EXCLUSIVITY, OR RESULTS OBTAINED FROM USE OF THE MATERIAL. CARNEGIE MELLON UNIVERSITY DOES NOT MAKE ANY WARRANTY OF ANY KIND WITH RESPECT TO FREEDOM FROM PATENT, TRADEMARK, OR COPYRIGHT INFRINGEMENT.
Licensed under a MIT (SEI)-style license, please see license.txt or contact permission@sei.cmu.edu for full terms.
[DISTRIBUTION STATEMENT A] This material has been approved for public release and unlimited distribution.  Please see Copyright notice for non-US Government use and distribution.
DM24-1597
'''
import json
import os


def load_vocab(json_file):
    with open(json_file, 'r') as file:
        vocab_data = json.load(file)
    return vocab_data


def generate_rst(vocab_name, vocab_data):
    rst_content = f"{vocab_name}\n{'=' * len(vocab_name)}\n\n"
    for vocab_obj in vocab_data:
        const = vocab_obj['const']
        title = vocab_obj['title']
        if 'description' in vocab_obj:
            description = vocab_obj['description']
        rst_content += f"**{title}** ({const})\n\n"
        if 'description' in vocab_obj:
            rst_content += f"    {description}\n\n"
    return rst_content


def save_rst(content, output_file):
    with open(output_file, 'w') as file:
        file.write(content)


def generate_index_rst(output_dir, vocab_names):
    index_content = "Vocabulary\n==========\n\n.. toctree::\n   :maxdepth: 2\n\n"
    for vocab_name in vocab_names:
        index_content += f"   {vocab_name}\n"
    save_rst(index_content, os.path.join(output_dir, 'index.rst'))


def main():
    pyiides_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    vocab_file = os.path.join(pyiides_dir, 'pyiides', 'utils', 'vocab.json')
    output_dir = os.path.join(pyiides_dir, 'docs', 'source', 'vocab')
    os.makedirs(output_dir, exist_ok=True)

    vocab_data = load_vocab(vocab_file)

    vocab_names = []
    for vocab_name in vocab_data:
        vocab_names.append(vocab_name)
        rst_content = generate_rst(vocab_name, vocab_data[vocab_name])
        output_file = os.path.join(output_dir, f"{vocab_name}.rst")
        save_rst(rst_content, output_file)

    generate_index_rst(output_dir, vocab_names)
    print(f"Generated reST content saved to {output_dir}")


if __name__ == "__main__":
    main()
