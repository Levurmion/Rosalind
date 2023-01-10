# Completing a Tree

'''
Trees are graphs without cycles (paths that would allow nodes to get revisited through a different edge). Phylogenetics is the study of the evolutionary relationships between different organisms. These relationships are often visualised using phylogenetic trees.

Phylogenetic trees are binary trees whereby each node is not allowed to have degrees > 3 as new species can only evolve from common ancestors over time typically due to extended periods of environmental isolation. In a phylogenetic tree, taxa are repressented by leaf nodes (nodes with degree = 1).

In this example, given A positive integer n and an adjacency list corresponding to a graph on n nodes that contains no cycles, return the minimum number of edges that can be added to the graph to form a tree.

SIMPLE SOLUTION: Trees with n nodes are always guaranteed to have n-1 edges (no cycles). So with the m edges provided, the difference in number of edges required to merge all n nodes into a tree is (n-1)-m.
'''

import numpy as np

def bfs(node,path=[]):

    global EDGES
    
    adj_nodes = []
    path.append(node)

    for edge in EDGES:

        if node in edge:
            this_edge = list.copy(edge)
            this_edge.remove(node)

            if this_edge[0] not in path:
                adj_nodes.append(this_edge[0])
            
            else:
                pass
        
        else:
            pass
    
    if adj_nodes != []:
        for next_node in adj_nodes:
            QUEUE.insert(0,next_node)
    
    elif adj_nodes == []:
        pass

    if QUEUE != []:
        to_visit = QUEUE.pop(-1)
        bfs(to_visit,path)
    
    elif QUEUE == []:
        GRAPHS.append(path)
        return


global EDGES, NODES, QUEUE, GRAPHS
EDGES = []
QUEUE = []
GRAPHS = []

with open('rosalind_tree.txt','r') as file:
    
    content = file.readlines()

    NODES = np.arange(1,int(content[0])+1)
    NODES = [str(node) for node in NODES]

    for line in content[1:]:

        stripped_line = line.rstrip('\n')   # remove newline character
        edge = stripped_line.split(' ')

        EDGES.append(edge)

for node in NODES:

    if GRAPHS == []:
        bfs(node, path=[])
    
    elif any(node in graph for graph in GRAPHS) == False:
        bfs(node, path=[])

    else:
        pass

print('disconnected graphs: ', GRAPHS, '\n')

min_edges_to_add = len(GRAPHS) - 1
print('edges to add: ', min_edges_to_add)

        
        

