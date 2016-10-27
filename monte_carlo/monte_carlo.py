# -*- coding: utf-8 -*-
import networkx as nx 
import numpy as np
import argparse
import unittest
import sys
import math
import argparse
import unittest
from random import *
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
input_file='input_file.txt'#default input file
parser=argparse.ArgumentParser()#parses command line inputs
parser.add_argument('--input_file', nargs="?") #adds a flag for input file
parser.add_argument('monte_carlo/monte_carlo.py', nargs='?')#makes sure that parser doesn't give error when it reads the source code
arguments=parser.parse_args()#arguments given in the command line
r1=1
temp=1
def input_reader1(args):
    '''takes the command line arguments and gives array of vertices
    Variables:
        args=command line
    Returns:
        array of vertices, where each vertex has a floating x and y coordinate arrays
    '''
    input_file1=input_file
    if(args.input_file!=None):
        input_file1=args.input_file
    f=open(input_file1, 'r')#opens the input file
    lines=f.readlines()#reads line by line
    
    vertices=[]#creates an empty array where coordinates of the vertices will be saved
    for line in lines: #iterate through the lines
        line=line.strip() #get rid of the space between x and y coordinates
        line=line.split() #split the x and y coordinates
        line[0],line[1]=(line[0].strip('(')), (line[1].strip(')')) # clean up the string that contain parenthesis
        line[0]=line[0].strip(',')#clean up the string that contain comas
        line[0],line[1]=float(line[0]),float(line[1])# convert the x and y coordinates from strings to floats 
        vertices.append(line)#put the output coordinates to any array
    if(len(vertices)==0):
        raise ValueError
    return vertices#return an array of vertices, each vertex is an array of x and y coordinates
global coordinates;
coordinates=input_reader1(arguments)#saves the matrix of x and y coord
global number_vertices;
number_vertices=len(coordinates)
def  generate_adjacency_matrix(coor):
    ''' takes an array of coordinates and generates nxn adjacency matrix
    Arguments:
         coor=an array of cartesian coordinates
    Returns:
          adj_matrix=adjacency matrix initialized to zero 
          y =an array that keeps the node number and its coordinates
    '''
    y=[]#initializing an array the keeps the vertex number and its cartesian coordinates
    k=len(coor)# the letgth of the coordinates array
    adj_matrix=np.ones((k,k))#adjacency matrix initialized to ones
    for i in range(len(coor)):#iterate through cartesian vertices
        x=[0,0,0]#initialize an array that will keep vertex index, x coordinate and y coordinate
        x[0]=i#index
        x[1]=coor[i][0]#x coordinate
        x[2]=coor[i][1]#y coordinate
        y.append(x)#append them for return 
    return adj_matrix,y
adjacency_matrix,node_info=generate_adjacency_matrix(coordinates) #an adjacency matrix with zeroes and info about nodes
def strongly_con_graph_generator(coor):
    '''takes an array of coordiantes returns a graph and an image
    Arguments:
         coor=any array of x and y coordinates
    Returns:
         G=graph from the given vertices
         image=graph's image
    '''
    G=nx.Graph()#Graph    
    for i in range(len(coor)):
        G.add_node(i)#adding nodes
    for i in range(len(coor)):
        for k in range(len(coor)):
            w=((coor[i][0]-coor[k][0])**2+(coor[i][1]-coor[k][1])**2)**0.5#computing the weight of edges
            G.add_edge(i,k, weight=w)#adding edges between all vertices
    min_span_tree=nx.minimum_spanning_tree(G)#finding minimum spanning tree
    nx.draw(G)#drawing the graph
    image="path.png"#name of the image
    plt.savefig(image)#saving the image
    return G, image
graph, picture=strongly_con_graph_generator(coordinates)#saves an initial graph and it image

def graph_theta(adj_matrix1,r):
    '''takes an adjacency matrix and returns the sum of its weight
    Arguments: 
        adj_matrix1=adjacency matrix
    Returns:
        weight_sum= sum of edges 
        G=weighted undirected graph
    '''

    edge1=[]#will contain edge
    G1=nx.Graph()#generates graph
    for i in range(len(adj_matrix1)):#for number of nodes in adjacency
        G1.add_node(i)#adds nodes
        for k in range(len(adj_matrix1)):
            if (i!=k):
                G1.add_node(k)#adds nodes
            if(adj_matrix1[i][k]!=0):
                edge=[i,k]#adds an edge
                edge1.append(edge)
                weight1=((coordinates[i][0]-coordinates[k][0])**2+(coordinates[i][1]-coordinates[k][1])**2)**0.5
                G1.add_edge(i,k, weight=weight1)
    weight_sums=0
    edges=len(G1.edges())
    nodes=len(coordinates)
    for i in range(edges):
        weight_sums=weight_sums+((coordinates[edge1[i][0]][0]-coordinates[edge1[i][1]][0])**2+(coordinates[edge1[i][0]][1]-coordinates[edge1[i][1]][1])**2)**0.5
    path_length=0
    i=1
    while (i!=0 and i<nodes):
        path_length=path_length+nx.shortest_path_length(G1, 0,i)
        i=i+1
    theta=r*weight_sums+path_length
    return theta, G1




def proposed_graph(adj_matrix1):
    ''' takes an adjacency matrix and generates a new adjacency matrix with a porposal distribution
    Arguments:
         adj_matrix1= an adjacency matrix
    Returns:
         adj_matrix1= an new mutated adjacency matrix


    '''
    extra,G2=graph_theta(adj_matrix1,r1)#graph and its coordinates
    node1=randint(0, len(adj_matrix1[0])-1)#random node 1
    node2=randint(0, len(adj_matrix1[0])-1)#random node 2
    G2_min_span_edges=nx.minimum_spanning_edges(G2)#edge of minimum spanning tree
    bridges=len(list(G2_min_span_edges))#number of edges in the spanning tree
    element=(node1, node2)#tuple of two nodes for an edge
    M=len(adj_matrix1[0])#number of vertices
    q_i_j=2.0/(M*(M-1.0))#i state probability
    q_j_i=2.0/(M*(M-1.0)-bridges)#j state probability
    ratio=float(q_j_i)/float(q_i_j)#calculates the ratio
    if (node1!=node2 and adj_matrix1[node1][node2]==0):# makes sure the two nodes are not identical and that there is no edge between them
        adj_matrix1[node1][node1]=1#add an edge
    elif(node1!=node2 and adj_matrix1[node1][node2]!=0):#
        if element in G2_min_span_edges:
            adj_matrix1[node1][node2]=1#if the edge is in MST don't remove
        else:
            adj_matrix1[node1][node2]=0#if it is not remove the edge
            extra1,G3=graph_theta(adj_matrix1,r1)
            if (nx.is_connected(G3)==False):#makes sure that the graph is connected
                adj_matrix1[node1][node2]=1
    return adj_matrix1

def relativity_ratio(adj_matrix_1,adj_matrix_2):
    ''' gives a relative ratio of two graphs
    Argumets:
       adj_matrix_1=adjacency matrix for graph 1
       adj_matrix_2=adjacency matrix for graph 2
    Returns:
       relative probability value of two graphs
    '''
    theta_1,graph_1=graph_theta(adj_matrix_1,r1)
    theta_2,graph_2=graph_theta(adj_matrix_2,r1)
    return math.exp((theta_1-theta_2)/temp)
##below i generated new graph for 100 times
def metropolis_algorithm(number_iterations, adjacency_matrix_1):
    i=0
    adjacency_matrices={'{}'.format(adjacency_matrix_1):1}
    while(i<number_iterations):
        
        adjacency_matrix_2=proposed_graph(adjacency_matrix_1)
        acceptance_ratio=relativity_ratio(adjacency_matrix_1, adjacency_matrix_2)
        if (acceptance_ratio>=1):
            adjacency_matrix_1=adjacency_matrix_2
            if ('{}'.format(adjacency_matrix_1)  in adjacency_matrices.keys()):
                adjacency_matrices['{}'.format(adjacency_matrix_2)]=adjacency_matrices['{}'.format(adjacency_matrix_2)]+1
            else:
                adjacency_matrices['{}'.format(adjacency_matrix_1)]=1
        else:
            if ('{}'.format(adjacency_matrix_2) in adjacency_matrices.keys):
                a=np.random.binomial(1, acceptance_ratio,1000)
                if (a==0):
                    adjacency_matrices['{}'.format(adjacency_matrix_2)]=adjacency_matrices['{}'.format(adjacency_matrix_2)]+a
                    adjacency_matrix_1=adjacency_matrix_1
                elif(a==1):
                    adjacency_matrices['{}'.format(adjacency_matrix_1)]=adjacency_matrices['{}'.format(adjacency_matrix_2)]+a
                    adjacency_matrix_1=adjacency_matrix_2
            else:
                a=np.random.binomial(1, acceptance_ratio,1000)
                if (a==0):
                    adjacency_matrices['{}'.format(adjacency_matrix_2)]=a
                    adjacency_matrix_1=adjacency_matrix_1
                elif(a==1):
                    adjacency_matrices['{}'.format(adjacency_matrix_1)]=a
                    adjacency_matrix_1=adjacency_matrix_2   
        i=i+1
    return adjacency_matrices
global adj_matrices;
adj_matrices=metropolis_algorithm(10,adjacency_matrix)

#nx.draw(G_proposed)#drawing the graph                           
#image1="proposed_graph.png"#name of the image                           
#plt.savefig(image1)#saving the image   
