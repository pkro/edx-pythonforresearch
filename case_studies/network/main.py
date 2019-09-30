# -*- coding: utf-8 -*-

import random

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import networkx as nx
from scipy.stats import bernoulli

'''
vertex / node: Eckpunkt
edge: connection (line) of verteces
path: sequence of unique connected verteces
length of pass: number of edges in path
graph is connected, if all verteces can be reached by all verteces
disconnected if not
components: disconnected graphs
Size of component: number of connected vertices
Largest connected component: Component with most connected verteces
Degree of x: number of directly connected nodes of x
Adjacency matrix: matrix with nodes * nodes, 1 if edge exists, 0 if not

Network / Graph with 2 components:
(1)--b--(2)
|
a
|
|
(3)--c--(4)

(5)----(6)

1-4: vertices /nodes
a,b,c: edges
(1,3,4): path between vertex 1 and 4
length of path: 2 (2 lines / edges)
degree of (1): 2
Adjacency matrix:
  1 2 3 4 5 6
1 0 1 1 0 0 0
2 1 0 0 0 0 0  
3 1 0 0 1 0 0
4 0 0 1 0 0 0  
5 0 0 0 0 0 1
6 0 0 0 0 1 0


Homophily: occurs when nodes that are neighbors in a network also share a characteristic more often than nodes that are not network neighbors.
Homophily is the proportion of edges in the network whose constituent nodes share that characteristic. 
If characteristics are distributed completely randomly, the probability that two nodes  𝑥  and  𝑦  share characteristic  𝑎  is the probability both nodes have characteristic  𝑎 , which is the frequency of  𝑎  squared. The total probability that nodes  𝑥  and  𝑦  share their characteristic is therefore the sum of the frequency of each characteristic in the network.
'''

# G = nx.karate_club_graph()
# nx.draw(G, with_labels=True, node_color="lightblue", edge_coloe="gray")


def er_graph(N,p):
    ''' creates a network with N nodes, each node is connected to each other
    node with a probability of p'''
    G = nx.Graph()
    G.add_nodes_from(range(N))
    for node in G.nodes():
        for connected_node in G.nodes():
            if node < connected_node and bernoulli.rvs(p=p):
                if not G.has_edge(node, connected_node):
                    G.add_edge(node, connected_node)
        
    return G




# G = er_graph(5, 0.2)
# nx.draw(G)

def plot_degree_distribution(G):
    plt.hist([degree for _, degree in G.degree()], histtype="step")
    plt.xlabel("Degree $k$")
    plt.ylabel("$P(k)$")
    plt.title("Degree Distribution")
    

def basic_netstats(G):
    print("Nodes: %d" % G.number_of_nodes())
    print("Edges: %d" % G.number_of_edges())
    print("Average degree: %2f" % np.mean([d for _, d in G.degree()]))
    G_LCC = max(nx.connected_component_subgraphs(G), key=len).number_of_nodes()
    print("Nodes in largest connected component %d" % G_LCC)
    print("%% of nodes in largest connected component %f" % (G_LCC/G.number_of_nodes()))
    

A1 = np.loadtxt("adj_allVillageRelationships_vilno_1.csv", delimiter=",")
A2 = np.loadtxt("adj_allVillageRelationships_vilno_2.csv", delimiter=",")

G1 = nx.to_networkx_graph(A1)
G2 = nx.to_networkx_graph(A2)

basic_netstats(G1)
basic_netstats(G2)

# plot_degree_distribution(G1)
# plot_degree_distribution(G2)

G1_LCC = max(nx.connected_component_subgraphs(G1), key=len)
G2_LCC = max(nx.connected_component_subgraphs(G2), key=len)
 
plt.figure()
nx.draw(G1_LCC, edge_color="gray", node_size=20, node_color="red")

plt.figure()
nx.draw(G2_LCC, edge_color="gray", node_size=20, node_color="green")



















