# CoVar Readers Digest Sphinx-docs Repo

This repo provides a functional sphinx-docs based template for auto-generating
HTML sphinx-docs that are served up on Gitlab pages via CI/CD. This can also
be optionally used to generate PDF outputs using `sphinx-build`.

## Setup

Clone this repo or copy its contents into your target repo. If your repo is
purely a documentation repo, then the contents can be copied into the root of
your repo. If this is meant for the documentation of a code-repo, then the
contents of this repo will need to be placed within a sub-directory at the 
top-level of the target repo (typically in a folder called `docs`). In this case,
the `tox.ini` and `gitlab-ci.yml` will need to be merged in with that of the
existing code-repo and some paths within them may need to be updated to point
appropriately to the nested structure under which the sphinx-docs reside.

## Generating the HTML Docs Locally

You can generate Sphinx-Docs locally either via `tox` (easier) or manually
using `sphinx-build` which enables more control and also enables generating PDFs,
etc. In either case, you will need to create a local venv with appropriate
developer dependencies installed.

### Creating a local venv

Simply create a local Python venv. For example, use the following command to
create a venv called `sphinx_docs` in the `~/.venvs` folder on a machine:

`python -m venv ~/.venvs/sphinx_docs`

Activate the venv using `source ~/.venvs/bin/activate` .

Finally, install the developer dependencies:

`pip install -r requirements.txt`

### Using tox to Generate HTML Docs

Once you have activated your venv, simply launch the command `tox` to generate
the HTML docs. These will be generated locally in a sub-folder called `/public`
and the entry-point is `index.html`

### Using sphinx-build to Generate HTML Docs

In the activated venv, run the following command:

```
sphinx-build -b html ./docs ./public
```

If new updates are not showing up in your local copy at `./public/index.html`
then you may need to use the following command instead:

```
rm -rf ./public && sphinx-build -b html ./docs ./public
```

This forces clearing out any cached entities in the `./public` folder and
re-generates all the HTML from scratch.

## Important Notes

### Difference between local HTML and Served HTML

The sidebar in the local HTML copy will not work correctly as it requires active
javascript which isn't correctly linked/served by the local copy but should work
for the gitlab pages served via CI/CD.

### ReStructured Text (RST) Primer

Refer to this primer for some basics: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html

### Heading Levels

RST does not have any opinion about how different level headings are formatted.
Sphinx will introspect the documents and determine what headings should go under
what level. However, the convention should be documented across a project for
consistency. Here is the recommended level formatting as is demonstrated in the
example `01-Overview.rst` file:

```
Level 1 Heading
===============

Level 2 Heading
---------------

Level 3 Heading
~~~~~~~~~~~~~~~

Level 4 Heading
^^^^^^^^^^^^^^^

Level 5 Heading
"""""""""""""""
```
