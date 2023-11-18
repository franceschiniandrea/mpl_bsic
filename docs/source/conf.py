# Configuration file for the Sphinx documentation builder.

import os
import sys
import re

package_path = os.path.abspath("../../")
sys.path.insert(0, package_path)


def get_property(prop, project):
    print(os.getcwd())
    result = re.search(
        r'{}\s*=\s*[\'"]([^\'"]*)[\'"]'.format(prop),
        open("../../" + project + "/__init__.py").read(),
    )
    return result.group(1)


#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "mpl_bsic"
copyright = "2023, Andrea Franceschini"
author = "Andrea Franceschini"
release = get_property("__version__", "mpl_bsic")

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "numpydoc",
    "sphinx.ext.ifconfig",
    "sphinx.ext.viewcode",
    "sphinx.ext.imgmath",
    "nbsphinx",
    "sphinx_simplepdf",
    "matplotlib.sphinxext.plot_directive",
]

templates_path = ["_templates"]
exclude_patterns = []

autosummary_generate = True

# -- Options for NumpyDocs  ---------------------------------------------
numpydoc_xref_param_type = True
numpydoc_xref_ignore = {"optional", "type_without_description", "BadException"}
numpydoc_class_members_toctree = True
numpydoc_validation_checks = {"all", "GL01", "GL02", "SA04", "RT03"}
pygments_style = "sphinx"

# -- Options for matplotlib plots -----------------------------------------
plot_include_source = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
html_logo = "_static/bsic_logo_3x.png"
html_theme_options = {"header_links_before_dropdown": 2}


# -- Intersphinx setup ----------------------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "numpy": ("https://numpy.org/devdocs/", None),
    "sklearn": ("https://scikit-learn.org/stable/", None),
    "matplotlib": ("https://matplotlib.org/stable/", None),
    "pandas": ("https://pandas.pydata.org/docs/", None),
}
