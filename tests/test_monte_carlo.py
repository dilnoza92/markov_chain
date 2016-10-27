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
#from click.testing import CliRunner

from monte_carlo import monte_carlo

import networkx as nx
#from monte_carlo.monte_carlo import *

coordinates1=[[5,6],[1,3],[4,5],[6,7],[8,9]]
coordinates2=[[0,0],[0.0],[0,0]]
k=monte_carlo.number_vertices

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
        graph1,picture1=monte_carlo.strongly_con_graph_generator(coordinates1)
        assert os.path.isfile(picture1)==True
        pass
    def test_generate_adjacency_matrix(self):
        adj_matrix=np.zeros((5,5))
        adj_matrix1=monte_carlo.generate_adjacency_matrix(coordinates1)
        print adj_matrix1[0]
        assert len(adj_matrix[0])==len(adj_matrix1[0])
        pass

    def test_proposed_graph(self):
    
        adj_matrix=np.ones((k,k))
        adj_matrix0=np.zeros((k,k))
        adj_matrix1=monte_carlo.proposed_graph(adj_matrix)
        a, G4=monte_carlo.graph_theta(adj_matrix1,1) 
        pass

    def test_metropolis_algorithm(self):
        answer=monte_carlo.metropolis_algorithm(1000,np.ones((k,k)))
        assert answer['{}'.format(np.ones((k,k)))]==monte_carlo.adj_matrices['{}'.format(np.ones((k,k)))]
        pass

