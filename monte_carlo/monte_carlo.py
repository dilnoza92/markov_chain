# -*- coding: utf-8 -*-
import networkx as nx 
import numpy as np
import argparse
import unittest
import sys
import math
import argparse
import matplotlib.pyplot as plt
input_file='input_file.txt'#default input file
parser=argparse.ArgumentParser()#parses command line inputs
parser.add_argument('--input_file', nargs="?") #adds a flag for input file
parser.add_argument('monte_carlo/monte_carlo.py', nargs='?')#makes sure that parser doesn't give error when it reads the source code
arguments=parser.parse_args()#arguments given in the command line
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
coordinates=input_reader1(arguments)#saves the matrix of x and y coord
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
    adj_matrix=np.zeros((k,k))#adjacency matrix initialized to zeros
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
    nx.draw(min_span_tree)#drawing the minimum spanning tree
    image="path.png"#name of the image
    plt.savefig(image)#saving the image
    return G, image
graph, picture=strongly_con_graph_generator(coordinates)#saves an initial graph and it image
def markov_chain_monte_carlo(graph):
    pass
def graph_prob(adj_matrix1):
    edge1=[]
    G1=nx.Graph()
    for i in range(len(adj_matrix1)):
        G1.add_node(i)
        for k in range(len(adj_matrix1)):
            if (i!=k):
                G1.add_node(k)
            if(adj_matrix1[i][k]!=0):
                edge=[i,k]
                edge1.append(edge)
                weight1=((coor[i][0]-coor[k][0])**2+(coor[i][1]-coor[k][1])**2)**0.5
                G1.add_edge(i,k, weight=weight1)
    weight_sums=0
    edges=len(G1.edges())
    nodes=len(coordinates)
    for i in range(edges):
        weight_sums=weight_sums+((coor[edge1[i][0]][0]-coor[edge1[i][1]][0])**2+(coor[edge1[i][0]][1]-coor[edge1[i][1]][1])**2)**0.5
    while (i!=0 and i<nodes):
        weight_sums=weight_sums
        paths=nx.shortest_path(G1, 0,i)
        for j in paths:
            
    return weighted_sums
print graph_prob(adjacency_matrix)
    
