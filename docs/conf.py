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
import hashlib
sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.join(os.path.abspath('..'),'src'))
from src.enum_extend import __version__
from src.enum_extend import AutoEnum
from typing import Any, Optional
from docutils.statemachine import StringList
from sphinx.ext.autodoc import ClassDocumenter, bool_option

# region Project information -----------------------------------------------------

project = 'enum-extend'
copyright = '2021, :Barry-Thomas-Paul: Moss'
author = ':Barry-Thomas-Paul: Moss'
# endregion Project information

# The full version, including alpha/beta/rc tags
release = __version__

# region General configuration ---------------------------------------------------

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

# endregion General configuration

# region AutoEnumDocumenter

class AutoEnumDocumenter(ClassDocumenter):
    # https://www.sphinx-doc.org/en/master/development/tutorials/autodoc_ext.html
    objtype = '_autoenum'
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
        super().add_content(more_content)

        source_name = self.get_sourcename()
        enum_object: AutoEnum = self.object
        use_hex = self.options.hex
        self.add_line('', source_name)
        # capture the class doc string for comparsion.
        # when no docstring is assigned to enum then enum
        # objects default to the class docstring when calling the __doc__ method.
        # for this reason a comparsion is done to ensure that
        # the enum is using class docstring
        class_doc_hash = hashlib.md5(
            enum_object.__doc__.encode("utf-8")).hexdigest()
        indent_str = '    '
        for enum_value in enum_object:
            the_value_name = enum_value.name
            the_value_value = enum_value.value
            the_docstring: str = enum_value.__doc__
            valid_docstring = False
            if use_hex:
                the_value_value = hex(the_value_value)

            self.add_line(
                f"**{the_value_name}**\= {the_value_value}", source_name)
            # self.add_line('', source_name)
            if the_docstring.strip():  # not a blank line
                # capture hash of current docstring
                enum_doc_hash = hashlib.md5(
                    the_docstring.encode("utf-8")).hexdigest()
                # make sure this is not the same docstring of the class
                if class_doc_hash != enum_doc_hash:
                    indent = self.indent
                    self.indent = indent + indent_str
                    docstrings = the_docstring.splitlines()
                    for i, line in enumerate(self.process_doc([docstrings])):
                        self.add_line(line, source_name, i)
                    self.add_line('', source_name)
                    self.indent = indent
                    valid_docstring = True

            if not valid_docstring:
                # this is a bit of hack
                # when there is no enum doc string provided
                # this section will inject a no printing character
                # with an indent. This will result in the Name, Value having special formating applied
                # as the cas when there is a doc string provided
                indent = self.indent
                self.indent = indent + indent_str
                self.add_line(u"\u007f", source_name)
                self.indent = indent

# endregion AutoEnumDocumenter

def setup(app):
    app.setup_extension('sphinx.ext.autodoc')  # Require autodoc extension
    app.add_autodocumenter(AutoEnumDocumenter)
