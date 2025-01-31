#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Ethan Zimmerman
# Copyright (c) 2014 Ethan Zimmerman
#
# License: MIT
#

"""This module exports the RamlCop plugin class."""

from SublimeLinter.lint import Linter


class RamlCop(Linter):

    """Provides an interface to raml-cop."""
    defaults = {
        "selector": "source.raml"
    }

    cmd = 'raml-cop --no-color --no-includes'

    regex = (
        r'^\[.+:(?P<line>\d+):(?P<col>\d+)\] '
        r'(?:(?P<error>ERROR)|(?P<warning>WARNING)) '
        r'(?P<message>.+)'
    )

    line_col_base = (0, 0)

    tempfile_suffix = '-'
