import unittest
import sys
sys.path.append("..")

from challenge_2.seq_alignment_a import sequence_align
from challenge_2.seq_alignment_b import sequence_align as sequence_align2

class TestChallenge2(unittest.TestCase):
    ### Public tests
    def test_align_1(self):
        """Public test #1 for alignment"""
        x = "stop"
        y = "tops"
        def c(x,y):
            return 1 if x != y else 0
        delta = 1.
        alignment = sequence_align(x, y, c, delta)
        self.assertEqual(alignment, ([(2,1), (3,2), (4,3)], 2.0))

    def test_align_2(self):
        """Public test #1 for alignment"""
        x = "stop"
        y = "tops"
        def c(x,y):
            return 1 if x != y else 0
        delta = 1.5
        alignment = sequence_align(x, y, c, delta)
        self.assertEqual(alignment, ([(2,1), (3,2), (4,3)], 3.0))

    ### Public tests
    def test_align2_1(self):
        """Public test #1 for alignment"""
        x = "stop"
        y = "tops"
        def c(x,y):
            return 1 if x != y else 0
        delta = 1.
        alignment = sequence_align2(x, y, c, delta)
        self.assertEqual(alignment, ([(2,1), (3,2), (4,3)], 2.0))

    def test_align2_2(self):
        """Public test #1 for alignment"""
        x = "stop"
        y = "tops"
        def c(x,y):
            return 1 if x != y else 0
        delta = 1.5
        alignment = sequence_align2(x, y, c, delta)
        self.assertEqual(alignment, ([(2,1), (3,2), (4,3)], 3.0))

if __name__ == '__main__':
    unittest.main()
