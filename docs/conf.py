# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Extended Matrix'
copyright = '2024, Emanuel Demetrescu'
author = 'Emanuel Demetrescu'

release = '1.5'
version = '1.5.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Il marchio, vendorizzato da `stratigraph-brand` con il suo
# `docs-theme/sync-brand-docs.sh`, come lo vendorizzano le applicazioni. Chiaro
# e scuro seguono l'impostazione di sistema di chi legge.
# EPUB non conosce il tipo di un .woff2: la sua lamentela è silenziata per nome.
suppress_warnings = ['epub.unknown_project_files']
html_css_files = [
    'brand/stratigraph-theme.css',
    'brand/skins.css',
    'brand/sphinx-rtd-bridge.css',
]

# -- Options for EPUB output
epub_show_urls = 'footnote'

# Enable numref
numfig = True




