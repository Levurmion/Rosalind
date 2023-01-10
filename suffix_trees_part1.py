# PATTERN MATCHING WITH SUFFIX TREES (1)

'''
A trie (suffix tree) is a rooted tree that represents paths through subsequent symbols of a collection of strings.
- Each symbol is represented by a path through an edge connecting two nodes
- Nodes are arbitrary connections between edges

The combination of edges traversed through a unique path from the root node towards a leaf represents a unique word in the collection. As long as no strings in the collection is a prefix of another, all paths will terminate at a leaf node. Otherwise, the path representing the prefix word is going to end at an internal node.

Given a collection of strings where none of the strings are
'''
from collections import defaultdict


# program start
filename = 'rosalind_trie.txt'

with open(filename,'r') as file:

    READS = file.readlines()
    READS = [read.strip() for read in READS]


def make_trie(STRINGS):

    # make a dictionary of node connections (edge_list) and the symbols representing each node
    edge_list = defaultdict(list)           
    edge_list[1].append(1)                  # start with root node (1)
    edge_symbols = {'1-1':'$'}              # take note of the root with $ sign
    output_list = []

    # root node starts at 1
    unique_nodes = 1

    for string in STRINGS:

        thisNode = 1
        prefix_exists = True

        idx = 0
        while prefix_exists == True:

            adjList = edge_list[thisNode]
            sym_found = False

            for adjNode in adjList:
                
                edgeSym = edge_symbols[str(thisNode)+'-'+str(adjNode)]

                if edgeSym == string[idx]:
                    thisNode = adjNode
                    idx += 1
                    sym_found = True
                    break
                else:
                    pass
            
            if sym_found == False:
                prefix_exists = False
        
        parent_node = thisNode
        string = string[idx:]

        for symbol in string:

            unique_nodes += 1

            edge_list[parent_node].append(unique_nodes)
            edge_symbols[str(parent_node)+'-'+str(unique_nodes)] = symbol
            output_list.append((parent_node,unique_nodes,symbol))
            parent_node = unique_nodes

    return output_list


trie = make_trie(READS)

with open('rosalind_trie_output.txt','w') as outfile:

    for edge in trie:
        outfile.write(str(edge[0])+' '+str(edge[1])+' '+edge[2]+'\n')
            


