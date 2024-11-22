# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Fedlex-JOLux'
copyright = 'Federal Chancellery'
author = 'Jean-Louis Morard, Benedikt Hitz-Gamper'
release = '0.1'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser',
              'sphinxcontrib.mermaid']

templates_path = ['_templates']

exclude_patterns = ['_build', 
                    'Thumbs.db', 
                    '.DS_Store']

myst_enable_extensions = ["deflist", 
                          "attrs_block",
                          "colon_fence",
                          "linkify"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'

html_theme_options = {
    "repository_url": "https://github.com/swiss/fedlex-jolux",
    "path_to_docs": "doc",
    "use_repository_button": True,
    "use_source_button": True,
    "use_edit_page_button": True,
    "use_issues_button": True,
    "logo": {
        "text": "JOLux Ontology",
        "image_light": "img/logo-ch.svg",
        "image_dark": "img/logo-ch.svg",
        "link": "https://swiss.github.io/fedlex-jolux"
    },
    "navigation_depth": 2
}

html_static_path = ['_static']

rinoh_documents = [dict(doc='index',
                        target='jolux')]


# add custom js for sparql link generation
def setup(app):
    app.add_js_file('sparql_link.js')
    app.add_css_file('custom.css')