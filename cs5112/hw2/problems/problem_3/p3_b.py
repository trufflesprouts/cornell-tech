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
        update = [None] * self.max_level
        cur = self.sentinel
        for level in range(self.max_level - 1, -1, -1):
            while cur.next[level] is not None and cur.next[level].val < x:
                cur = cur.next[level]
            update[level] = cur
        next = update[0].next[0]
        if next is not None and next.val == x:
            return
        level = self._random_level()
        new_node = Node(x, level)
        for i in range(level):
            new_node.next[i] = update[i].next[i]
            update[i].next[i] = new_node
        self.root = self.sentinel.next[0]

    def delete(self, x: int) -> None:
        update = [None] * self.max_level
        cur = self.sentinel
        for level in range(self.max_level - 1, -1, -1):
            while cur.next[level] is not None and cur.next[level].val < x:
                cur = cur.next[level]
            update[level] = cur
        target = update[0].next[0]
        if target is None or target.val != x:
            return
        for i in range(target.level):
            if update[i].next[i] is target:
                update[i].next[i] = target.next[i]
        self.root = self.sentinel.next[0]

    def search(self, x: int) -> Node:
        cur = self.sentinel
        for level in range(self.max_level - 1, -1, -1):
            while cur.next[level] is not None and cur.next[level].val < x:
                cur = cur.next[level]
        cur = cur.next[0]
        if cur is not None and cur.val == x:
            return cur
        return None
    
    def _random_level(self) -> int:
        level = 1
        while random.random() < self.p and level < self.max_level:
            level += 1
        return level
