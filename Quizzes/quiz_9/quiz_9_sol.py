# Randomly generates a binary search tree whose number of nodes
# is determined by user input, with labels ranging between 0 and 999,999,
# displays it, and outputs the maximum difference between consecutive leaves.
#
# Written by Eric Martin for COMP9021

import sys
from random import seed, randrange
from binary_tree_adt import *

def gather_nodes(tree):
    if tree.value == None:
        return []
    nodes = gather_nodes(tree.left_node)
    nodes.extend(gather_nodes(tree.right_node))
    nodes.append(tree)
    return nodes

def max_diff_in_consecutive_leaves(tree):
    leaves = [node for node in gather_nodes(tree)
                      if node.left_node.value is None and node.right_node.value is None
             ]
    if len(leaves) == 1:
        return 0
    return max((leaves[i + 1].value - leaves[i].value for i in range(len(leaves) - 1)))



provided_input = input('Enter two integers, the second one being positive: ')
try:
    arg_for_seed, nb_of_nodes = provided_input.split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, nb_of_nodes = int(arg_for_seed), int(nb_of_nodes)
    if nb_of_nodes < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
tree = BinaryTree()
for _ in range(nb_of_nodes):
    datum = randrange(1000000)
    tree.insert_in_bst(datum)
print('Here is the tree that has been generated:')
tree.print_binary_tree()
print('The maximum difference between consecutive leaves is: ', end = '')
print(max_diff_in_consecutive_leaves(tree))
           
