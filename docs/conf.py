# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os, sys
#sys.path.insert(0, os.path.abspath('.'))
#sys.path.insert(0, os.path.abspath('_ext'))
import sphinx_rtd_theme
#autodoc_mock_imports = ['_tkinter']
# from docutils.parsers.rst import Directive, directives


#import mock

#MOCK_MODULES = ['numpy', 'scipy', 'matplotlib', 'matplotlib.pyplot']
#for mod_name in MOCK_MODULES:
 #   sys.modules[mod_name] = mock.Mock()



# -- Project information -----------------------------------------------------

project = 'D-Wave Demo Documentation'
copyright = '2021, Rachel Wang'
author = 'Rachel Wang'
version = 'v1.1'

# The full version, including alpha/beta/rc tags
release = '1.0'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx_rtd_theme",
    "sphinx.ext.autodoc", # include documentation from docstrings
    "sphinx.ext.napoleon", # numpy style documentation
    # "sphinx.ext.coverage", # checks coverage
    "sphinx.ext.intersphinx",
    "sphinx.ext.ifconfig",
    "sphinx.ext.autosummary", # generate autodoc summaries
    "sphinx.ext.doctest", # execute code snippets for demo
    "sphinx.ext.extlinks", # shorten external links
    "sphinx.ext.autosectionlabel", # to refer to internal headers
    "sphinx.ext.viewcode", # imports linked modules
   # "sphinxcontrib-pdfembed", # embed PDF files
    "sphinx.ext.githubpages",
   # "edit_on_github",
   # "hoverxref.extension", #must be hosted on readtehdocs
    "numpydoc",
    "sphinx.ext.mathjax",
    "sphinx_togglebutton",
    "sphinx_panels",
  #  "sphinxcontrib-details-directive",
]

autosectionlabel_prefix_document = True
#extensions.append('sphinx_execute_code')
intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}
numfig = True
autodoc_default_flags = ['members']
autosummary_generate = True

napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
#napoleon_use_admonition_for_references = False
autosummary_imported_members = True
numpydoc_show_class_members = False

hoverxref_auto_ref = True
hoverxref_role_types = {
    'ref': 'tooltip',  # for hoverxref_auto_ref config
    'confval': 'tooltip',  # for custom object
    'mod': 'tooltip',  # for Python Sphinx Domain
    'class': 'tooltip',  # for Python Sphinx Domain
}

# The suffix of source filenames
source_suffix = '.rst'

## define the master doc
master_doc = 'index'

## warning suppression
suppress_warnings = [
    "ref.citation",
    "epub.duplicated_toc_entry",
    "autosectionlabel.*",
    "ref.doc",
    "ref.ref",
    "ref.option",
    "ref.footnote",
    "cpp.duplicate_declaration",
    "autoapi",
]


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

## Suffic(es) of source filenames
# source_suffix = ['.rst', '.md']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['**/*scipy.stats.mstats*',]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

#ADDITION: name of Pygments (syntax highlighting) style to use
pygments_style = 'monokai'


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

def setup(app):
    app.add_stylesheet('css/custom.css')
   # app.add_css_file('css/togglebutton.css')

html_js_files = [
    'js/custom.js',
]

# Theme options
html_theme_options = {
    'prev_next_buttons_location': 'bottom',
    'display_version': True,
    # 'style_external_links': True,
    #toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': -1,
}

html_context = {
    'display_github': True,
    'github_user': 'rcywang',
    'github_repo': 'd-wave-demodoc',
    'github_version': 'main/',
}

# configure github extensions
edit_on_github_project = 'rcywang/d-wave-demodoc'
edit_on_github_branch = 'main'

html_last_updated_fmt = '%b %d, %Y'
html_use_smartypants = True


# -- Options for LaTeX output ---------------------------------------------
latex_engine = 'xelatex'
latex_elements = {'preamble':r'\usepackage{physics}, \usepackage{amssymb}, \usepackage{amsfonts}'
}
mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"



# latex_engine = 'pdfLaTeX'
# latex_elements = {
#     'papersize': 'a4paper',
#     'fontpckg': '\\usepackage{amsmath, amssymb}',
#     'figure_align': 'htbp'   
# }
# latex_documents = [
#     (latex_files, 'main.tex', 'CV', 'Rachel Wang', 'article')]
