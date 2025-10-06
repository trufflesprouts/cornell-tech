'''
Problem 3b
'''

import random

class Node: 
    def __init__(self, val, level):
        self.val = val
        self.next = [None] * level
        self.level = level

class SkipList:
    def __init__(self, max_level, p):
        self.max_level = max_level
        self.p = p
        self.sentinel = Node(None, self.max_level)
        self.root = None

    def insert(self, x: int) -> None:
        pass

    def delete(self, x: int) -> None:
        pass

    def search(self, x: int) -> Node:
        pass
