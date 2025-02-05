## Directory Structure

```
📦docs
 ┣ 📂build
 ┃ ┣ 📂doctrees
 ┃ ┃ ┣ 📜environment.pickle
 ┃ ┃ ┣ 📜index.doctree
 ┃ ┃ ┣ 📜pyiides.doctree
 ┃ ┃ ┗ 📜vocab.doctree
 ┃ ┗ 📂html
 ┃ ┃ ┣ 📂_modules
 ┃ ┃ ┃ ┣ 📂pyiides
 ┃ ┃ ┃ ┃ ┗ 📜pyiides.html
 ┃ ┃ ┃ ┗ 📜index.html
 ┃ ┃ ┣ 📂_sources
 ┃ ┃ ┃ ┣ 📜index.rst.txt
 ┃ ┃ ┃ ┣ 📜pyiides.rst.txt
 ┃ ┃ ┃ ┗ 📜vocab.rst.txt
 ┃ ┃ ┣ 📂_static
 ┃ ┃ ┃ ┣ ...
 ┃ ┃ ┣ 📜.buildinfo
 ┃ ┃ ┣ 📜genindex.html
 ┃ ┃ ┣ 📜index.html
 ┃ ┃ ┣ 📜objects.inv
 ┃ ┃ ┣ 📜pyiides.html
 ┃ ┃ ┣ 📜search.html
 ┃ ┃ ┣ 📜searchindex.js
 ┃ ┃ ┗ 📜vocab.html
 ┣ 📂source
 ┃ ┣ 📂vocab
 ┃ ┃ ┣ 📜access-auth-vocab.rst
 ┃ ┃ ┣ 📜attack-hours-vocab.rst
 ┃ ┃ ┣ ...
 ┃ ┣ 📜conf.py
 ┃ ┣ 📜index.rst
 ┃ ┣ 📜pyiides.rst
 ┃ ┗ 📜vocab.rst
 ┣ 📜make.bat
 ┗ 📜Makefile
```

# Sphinx Documentation Development

- **Installation**:

  - Ensure you have Sphinx installed. You can install it using pip:
    ```sh
    pip install sphinx
    ```
  - Additional Sphinx extensions can be installed if needed, for example:
    ```sh
    pip install sphinx-rtd-theme
    ```

- **Sphinx Directory Structure**:

  - `docs/source/`: Contains the reStructuredText (.rst) files that define the structure and content of your documentation.
  - `docs/source/conf.py`: The configuration file for Sphinx. Customize it to set the project name, version, extensions, and other settings.
  - `docs/build/`: This directory contains the generated documentation files (HTML, PDF, etc.).

- **Generating Documentation**:

  - Navigate to the `docs/` directory and run the following command to generate the HTML documentation:
    ```sh
    make html
    ```
    - Or on windows:
    ```sh
    ./make.bat html
    ```
  - The output will be placed in `docs/build/html/`.

- **Updating Documentation**:

  - Edit the .rst files in the `docs/source/` directory to update the content.
  - Use Sphinx directives and roles to include code snippets, generate API documentation, and create links.
  - Common directives include `.. toctree::`, `.. automodule::`, `.. autoclss::`, etc.

- **Regenerating Vocabulary Documentation**:

  - Use the `gen_vocab_rst.py` script to regenerate the RST files related to the vocabulary.
    ```sh
    python gen_vocab_rst.py
    ```

- **Previewing Documentation**:

  - Open the `index.html` file in `docs/build/html/` to preview the generated documentation in your web browser.

- **Customizing the Theme**:

  - You can customize the appearance of the documentation by modifying the `html_theme` and related settings in `conf.py`.
  - For example, to use the Read the Docs theme:
    ```python
    html_theme = 'sphinx_rtd_theme'
    ```

- **Including Code Documentation**:

  - Use the `autodoc` extension to include docstrings from your Python code:
    ```rst
    .. automodule:: module_name
        :members:
    ```
  - Ensure your Python files have proper docstrings for functions, classes, and methods.

- **Using Extensions**:

  - Sphinx supports various extensions to enhance documentation. Commonly used extensions include `sphinx.ext.autodoc`, `sphinx.ext.napoleon`, `sphinx.ext.viewcode`, etc.
  - Add the desired extensions to the `extensions` list in `conf.py`.

- **Building Other Formats**:

  - Besides HTML, you can build documentation in other formats like PDF, ePub, and LaTeX:
    ```sh
    make latexpdf
    make epub
    ```

- **Hosting Documentation**:

  - Down the line we need to host this documentation on readthedocs or a similar provider.
