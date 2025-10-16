'''
Problem 3a
'''

class Node:
    def __init__(self, val:int, next):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.root = None

    def insert(self, x):
        if self.root is None:
            self.root = Node(x, None)
            return
        
        curr = self.root
        while curr.next is not None and curr.next.val < x:
            curr = curr.next
        new_node = Node(x, curr.next)
        curr.next = new_node

    def search(self, x):
        curr = self.root
        while curr is not None:
            if curr.val == x:
                return curr
            curr = curr.next
        return None

    def delete(self, x):
        prev = None
        curr = self.root
        while curr is not None:
            if curr.val == x:
                if prev is None:
                    self.root = curr.next
                else:
                    prev.next = curr.next
                return
            prev = curr
            curr = curr.next
