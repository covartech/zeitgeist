# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import sphinx.domains.std
from docutils import nodes
import sphinx_rtd_theme

from recommonmark.transform import AutoStructify

source_suffix = ['.rst', '.md']

# -- Project information -----------------------------------------------------

project = 'CoVar Readers Digest'
copyright = '2024, CoVar, LLC'
author = 'team@covar.com'

# The full version, including alpha/beta/rc tags
release = '1.0.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'recommonmark',            # Support for Markdown files
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",  # Generate summary listings for methods/items
    'sphinx.ext.intersphinx',  # Reference external Sphinx doc sources
    'sphinx.ext.mathjax',      # Math support via .. math:: directive
    "sphinx.ext.napoleon",  # Support for Numpy and Google docstring format
    "sphinx.ext.todo",  # Support .. todo::, ... todolist:: directives
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

intersphinx_mapping = {
    'pytorch': ('http://pytorch.org/docs/stable/', None),
    'python': ('https://docs.python.org/3.6', None),
    'matplotlib': ('https://matplotlib.org/stable/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
}

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# From `numsec`:
#   https://github.com/jterrace/sphinxtr/blob/master/extensions/numsec.py
# to enable referencing sections by section numbers
class CustomStandardDomain(sphinx.domains.std.StandardDomain):

    def __init__(self, env):
        env.settings['footnote_references'] = 'superscript'
        sphinx.domains.std.StandardDomain.__init__(self, env)

    def resolve_xref(self, env, fromdocname, builder,
                     typ, target, node, contnode):
        res = super(CustomStandardDomain, self).resolve_xref(
            env, fromdocname, builder, typ, target, node, contnode)

        if res is None:
            return res

        if typ == 'ref' and not node['refexplicit']:
            docname, labelid, sectname = self.data['labels'].get(target, ('','',''))
            res['refdocname'] = docname

        return res


def doctree_resolved(app, doctree, docname):
    secnums = app.builder.env.toc_secnumbers
    for node in doctree.traverse(nodes.reference):
        if 'refdocname' in node:
            refdocname = node['refdocname']
            if refdocname in secnums:
                secnum = secnums[refdocname]
                toclist = app.builder.env.tocs[refdocname]
                for child in node.traverse():
                    if isinstance(child, nodes.Text):
                        text = child.astext()
                        anchorname = None
                        for refnode in toclist.traverse(nodes.reference):
                            if refnode.astext() == text:
                                anchorname = refnode['anchorname']
                        if anchorname is None:
                            continue
                        linktext = '.'.join(map(str, secnum[anchorname]))
                        child.parent.replace(child, nodes.Text(linktext))

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Note: Defaults here have the CoVar logo displayed at the top of the sidebar
# in the sphinx-generated HTML. If you wish to remove the logo and simply have
# a text hyperlink with the ``project`` name as defined above, then comment out
# the `html_logo` variable below, and set `'logo_only': False,` in the
# `html_theme_options` dictionary below.
html_logo = "_static/covar_logo_white.png"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'collapse_navigation': False,
    'display_version': True,
    'logo_only': True,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# app setup hook
def setup(app):
    # app.add_config_value('recommonmark_config', {
    #     #'url_resolver': lambda url: github_doc_root + url,
    #     'auto_toc_tree_section': 'Contents',
    #     'enable_math': False,
    #     'enable_inline_math': False,
    #     'enable_eval_rst': True,
    # }, True)
    app.add_transform(AutoStructify)
    app.add_css_file('https://fonts.googleapis.com/css?family=Lato')
    app.add_css_file('pytorch_theme.css')
    app.add_css_file('custom.css')

    # Register `numsec` extension stuff to enable cross-referencing sections
    # by number instead of default which is section-name
    app.add_domain(CustomStandardDomain, override=True)
    app.connect('doctree-resolved', doctree_resolved)
