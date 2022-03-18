# Configuration file for the Sphinx documentation builder.

import os
import sys
sys.path.insert(0, os.path.abspath('../..'))


def read(rel_path: str) -> str:
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, rel_path)) as fp:
        return fp.read()


def get_version(rel_path: str) -> str:
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")


# -- Project information

project = 'decoupler'
copyright = """2022, Badia-i-Mompel P., Vélez Santiago J., Braunger J., Geiss C., Dimitrov D., Müller-Dott S., Taus P., Dugourd A.,
Holland C.H., Ramirez Flores R.O. and Saez-Rodriguez J."""
author = 'Pau Badia i Mompel'
release = get_version("../../decoupler/__init__.py")
version = get_version("../../decoupler/__init__.py")

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
    'numpydoc',
    'nbsphinx'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output
master_doc = 'index'

html_theme = 'sphinx_rtd_theme'
html_static_path = ["_static"]
html_theme_options = dict(
    logo_only=True,
    display_version=True,
)
html_context = dict(
    display_github=True,  # Integrate GitHub
    github_user='saezlab',  # Username
    github_repo='decoupler-py',  # Repo name
    github_version='master',  # Version
    conf_py_path='/docs/source/',  # Path in the checkout to the docs root
)
html_show_sphinx = False
html_logo = 'logo.png'
html_favicon = 'logo.png'
html_css_files = [
    'css/custom.css',
]

# -- Options for EPUB output
epub_show_urls = 'footnote'
