#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_monte_carlo
----------------------------------

Tests for `monte_carlo` module.
"""

import argparse
import sys
import os.path
import unittest
import numpy as np
from contextlib import contextmanager
from click.testing import CliRunner

from monte_carlo import monte_carlo
from monte_carlo import cli
import networkx as nx
#from monte_carlo import *

coordinates=[[5,6],[1,3],[4,5],[6,7],[8,9]]
   

class TestMonte_carlo(unittest.TestCase):

    def test_input_reader(self):
        parser1=argparse.ArgumentParser()
        parser1.add_argument('--input_file', nargs='?')
        parser1.add_argument('monte_carlo/monte_carlo.py')
        test_args=parser1.parse_args()
        test_args.input_file="input_file.txt"
#        self.assertRaises(ValueError, monte_carlo.input_reader1, test_args)
 
        f2=open('input2.txt', 'w')
        f2.write('')
        f2.close()
        test_args.input_file='input2.txt'
        self.assertRaises(ValueError, monte_carlo.input_reader1, test_args)
 
        pass
    def test_strongly_con_graph_generator(self):
        graph1,picture1=monte_carlo.strongly_con_graph_generator(coordinates)
        assert os.path.isfile(picture1)==True
        pass
    def test_generate_adjacency_matrix(self):
        adj_matrix=np.zeros((5,5))
        adj_matrix1=monte_carlo.generate_adjacency_matrix(coordinates)
        print adj_matrix1[0]
        assert len(adj_matrix[0])==len(adj_matrix1[0])
        pass

    def test_proposed_graph(self):
        adj_matrix=np.ones((20,20))
        adj_matrix1=monte_carlo.proposed_graph(adj_matrix)
        a, G4=monte_carlo.graph_prob(adj_matrix1)
        assert nx.is_connected(G4)==True
        pass

    '''
    def test_command_line_interface(self):
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'monte_carlo.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
'''
