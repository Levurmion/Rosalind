# COUNTING PHYLOGENETIC ANCESTORS

'''
Phylogenetic trees are always constructed as binary trees whereby each node is only allowed to have a maximum degree of 3. This means from each parent node, there could only ever be two child nodes emanating from it.

A rooted tree is where one node serves as the pinnacle of the tree (i.e., the root). The root node is the only node that has a degree = 2. In an unrooted tree, this "root node" has a virtual edge that leads to an "unknown" ancestor thus allowing all internal nodes to have a degree = 3.

In this example, given a positive integer n, calculate the number of internal nodes for an unrooted binary tree with n leaf nodes (excluding the virtual root node).
'''

n = 5248
k = n-2

print(k)

'''
EXPLANATION

For any graph (including trees of course), it's an elementary result that the sum of the node degrees is double the number of edges (since each edge is counted twice, because it has two nodes). Also, any tree with N nodes has N-1 edges (as stated in the hint for this problem).

If k is the number of internal nodes (all of which have vertex degree 3 since the tree is an unrooted binary tree) and n is the number of leaves (a leaf has vertex degree 1), then the two results above imply:

3k + n = 2((k + n) - 1)

solving for k we get k = n - 2
'''