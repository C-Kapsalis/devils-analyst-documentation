# Configuration file for the Sphinx documentation builder.
#
# Deliberately minimal: two extensions, the Read the Docs theme, nothing
# else. No autodoc, no napoleon, no custom directives, every page in this
# project is hand-written reStructuredText.

project = "Devil's Analyst"
copyright = '2026, Christoforos Kapsalis'
author = 'Christoforos Kapsalis'
release = '0.1.0'

extensions = [
    'sphinx.ext.intersphinx',
    'sphinxcontrib.spelling',
]

# One entry per sibling project, so any of the sites can link to an exact
# page on another with a build-time-checked reference instead of a
# hand-typed URL. Uncomment a line once that project is live on Read the
# Docs, and confirm the slug matches its actual RTD project name.
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'diataxis': ('https://diataxis.fr', None),
    # 'second-read': ('https://second-read-documentation.readthedocs.io/en/latest/', None),
    # 'tmdl-preflight': ('https://tmdl-preflight-documentation.readthedocs.io/en/latest/', None),
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

spelling_lang = 'en_US'

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
