# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys

sys.path.insert(0, os.path.abspath('../..'))

project = 'Fitness Shopping REST API'
copyright = '2025, Avigael'
author = 'Avigael'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinxcontrib.httpdomain',
    'sphinx.ext.autosectionlabel'
        ]

templates_path = ['_templates']
exclude_patterns = []
autodoc_default_options = {
    'members': True,
    'undoc-members': True,  # Show even undocumented members
    'inherited-members': True,  # Show inherited methods
    'show-inheritance': True
}


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = 'furo'
html_static_path = ['_static']
