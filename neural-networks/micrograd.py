import math
import numpy as np
import matplotlib.pyplot as plt



class Node:
    def __init__(self, name):
        self.name = name
        self._prev = []

    def __repr__(self):
        return f"Node({self.name})"


# """
#   A
#  / \/
# B   C
#  \ /
#   D
# """


A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')


A._prev = [B, C] # A ma dzieci B oraz C
B._prev = [D] # B ma dziecko D
C._prev = [D] # C ma dziecko D



def trace(root):
    nodes, edges = set(), set()

    def build(v):
        if v not in nodes:
            nodes.add(v)
        for child in v._prev:
            edges.add((child, v))
            build(child)

    build(root)
    return nodes, edges


nodes, edges = trace(A)

for node in nodes:
    print(node)

print("\nEdges:")
for edge in edges:
    print(f"{edge[0]}--> {edge[1]}")



