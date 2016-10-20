#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_monte_carlo
----------------------------------

Tests for `monte_carlo` module.
"""


import sys
import unittest
from contextlib import contextmanager
from click.testing import CliRunner

from monte_carlo import monte_carlo
from monte_carlo import cli



class TestMonte_carlo(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_something(self):
        pass

    def test_command_line_interface(self):
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'monte_carlo.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output