import unittest
import sys
sys.path.append("..")

from problem_3.p3_a import LinkedList
from problem_3.p3_b import SkipList


import random

def to_list(skiplist):
    out = []
    node = skiplist.root
    while node is not None:
        if node.val is not None:
            out.append(node.val)
        node = node.next[0]
    return out

class TestProblem3(unittest.TestCase):

    ### Public tests 3a
    def test_correctness_linkedlist(self):
        """Public base test #1"""
        l = LinkedList()
        l.insert(0)
        l.insert(3)
        l.insert(1)
        self.assertEqual(l.root.val, 0)
        self.assertEqual(l.root.next.val, 1)
        self.assertEqual(l.root.next.next.val, 3)

        self.assertEqual(l.search(0), l.root)
        self.assertEqual(l.search(1), l.root.next)

        l.delete(0)
        self.assertEqual(l.search(0), None)
        self.assertEqual(l.search(1), l.root)

    ### Public tests 3b
    def test_correctness_skiplist(self):
        """Public base test #2"""
        l = SkipList(8, 0.5)
        l.insert(0)
        l.insert(1)
        l.insert(3)

        self.assertEqual(l.root.val, 0)
        self.assertEqual(l.root.next[0].val, 1)
        self.assertEqual(l.root.next[0].next[0].val, 3)

        self.assertEqual(l.search(0), l.root)
        self.assertEqual(l.search(1), l.root.next[0])

        l.delete(0)
        self.assertEqual(l.search(0), None)
        self.assertEqual(l.search(1), l.root)

    def test_correctness_b_n1000(self):
        """Test #1 n = 1000"""
        xs = list(set([random.randint(0,5000) for n in range(1000)]))
        l = SkipList(16, 0.5)
        for x in xs:
            l.insert(x)
        self.assertEqual(sorted(xs), to_list(l))
        for x in xs[:100]:
            l.delete(x)
        for x in xs[-100:]:
            l.delete(x)
        self.assertEqual(sorted(xs[100:-100]), to_list(l))

if __name__ == '__main__':
    unittest.main()
