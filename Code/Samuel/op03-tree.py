# PDX Code Guild Fullstack Course
# Optional Lab 3 Tree
# Samuel Purdy
# 4/22/2020

import random

names = ['virginia', 'christine', 'carl', 'lillian']


def generate_tree(depth):
    n_children = int(random.random()*10/depth)
    if n_children == 0:
        return {'type': 'leaf', 'name': random.choice(names)}
    branch = {'type': 'branch', 'children': []}
    for i in range(n_children):
        child = generate_tree(depth+1)
        branch['children'].append(child)
    return branch


def print_node(node, indentation):
    if node['type'] == 'leaf':
        print(indentation + node['name'])
    else:
        print(indentation + '-')
        for i in range(len(node['children'])):
            print_node(node['children'][i], indentation + '\t')


# count all trees and branches
def count_nodes(node):
    if node['type'] == 'leaf':
        return 1
    r = 1
    for i in range(len(node['children'])):
        r += count_nodes(node['children'][i])
    return r

# Renames the leaves based on what is given with what it will replace.
# It uses recursion in order to get each branch to be checked carefully,
# since the size of the tree is close to random.
# Node = tree/branch/leaf that is given.
# to_find = name that is being replaced.
# to_replace = name that is replacing.
def rename_leaves(node, to_find, to_replace):
    # If the node is a list, it will loop through each element of the 
    # list and generate a new branch/leaf and replaces it.
    if type(node) == list:
        for i in range(len(node)):
            node[i] = rename_leaves(node[i], to_find, to_replace)
    # If the "type" of the node is "leaf" and the "name" is what is being 
    # searched for, it will re-write the node to be equal to a new leaf 
    # with a new name.
    elif node["type"] == "leaf":
        if node["name"] == to_find:
            node = {'type': 'leaf', 'name': to_replace}
    # If the "type" of the node is "branch", it will make node equal to 
    # a new branch with new children.
    elif node["type"] == "branch":
        node = {'type': 'branch', 'children': rename_leaves(node["children"], to_find, to_replace)}
    # Returns the node.
    return node


root = generate_tree(1)
print(root)
print_node(root, '')
print(count_nodes(root))
root = rename_leaves(root, "carl", "bob")
print(root)
print(count_nodes(root))