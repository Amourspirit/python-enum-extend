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
import os
import sys
sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.join(os.path.abspath('..'),'src'))
from src.enum_extend import __version__
from src.enum_extend import AutoEnum

from enum import IntEnum
from typing import Any, Optional
from docutils.statemachine import StringList
from sphinx.application import Sphinx
from sphinx.ext.autodoc import ClassDocumenter, bool_option

# -- Project information -----------------------------------------------------

project = 'python-enum-extend'
copyright = '2021, :Barry-Thomas-Paul: Moss'
author = ':Barry-Thomas-Paul: Moss'

# The full version, including alpha/beta/rc tags
release = __version__


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# region Custom Documenter


class AutoEnumDocumenter(ClassDocumenter):
    # https://www.sphinx-doc.org/en/master/development/tutorials/autodoc_ext.html
    objtype = 'autoenum'
    directivetype = 'class'
    priority = 10 + ClassDocumenter.priority
    option_spec = dict(ClassDocumenter.option_spec)
    option_spec['hex'] = bool_option

    @classmethod
    def can_document_member(cls,
                            member: Any, membername: str,
                            isattr: bool, parent: Any) -> bool:
        return isinstance(member, AutoEnum)

    def add_directive_header(self, sig: str) -> None:
        super().add_directive_header(sig)
        self.add_line('   :final:', self.get_sourcename())

    def add_content(self,
                    more_content: Optional[StringList],
                    no_docstring: bool = False
                    ) -> None:
        print('add_content()')
        super().add_content(more_content, no_docstring)

        source_name = self.get_sourcename()
        print('source_name', source_name)
        enum_object: AutoEnum = self.object
        use_hex = self.options.hex
        self.add_line('', source_name)

        for enum_value in enum_object:
            the_value_name = enum_value.name
            the_value_value = enum_value.value
            if use_hex:
                the_value_value = hex(the_value_value)

            self.add_line(
                f"**{the_value_name}**: {the_value_value}", source_name)
            self.add_line('\nhello world', source_name)
            self.add_line('', source_name)
            
# endregion

def skip(app, what, name, obj, would_skip, options):
    # print('skip', what)
    print("skip", name, would_skip)
    if name == 'EX_ONE':
        # print(obj)
        return False
    if name == "__init__":
        return False
    return would_skip

def autodoc_process_docstring(app, what, name, obj, options, lines):
    print('ds-what', what)
    print("ds-name", name)
    # print('ds-lines', lines)


def autodoc_process_signature(app, what, name, obj, options, signature, return_annotation):
    print('signature', what)
    print('signature', name)
    if name == 'ex.ExAutoEnum.EX_ONE':
        print("obj", obj)
        print("signature", signature)
        print("return_annotation", return_annotation)
        return ("yes","Hello W")

def setup(app):
    app.setup_extension('sphinx.ext.autodoc')  # Require autodoc extension
    # app.connect("autodoc-skip-member", skip)
    # app.connect("autodoc-process-docstring", autodoc_process_docstring)
    # app.connect("autodoc-process-signature", autodoc_process_signature)
    app.add_autodocumenter(AutoEnumDocumenter)