import unittest
import sys
sys.path.append("..")

from problem_1.p1_b import stable_matching_1b
from problem_1.p1_c import stable_matching_1c

'''
Passing all tests in class:TestProblem1 will not garentee that you will pass all the tests on autograder,
we released all private/public tests used in autograder in the input folder 
so you can write more unit test to test on them.
'''

class TestProblem1(unittest.TestCase):
    ### Public tests for 1b
    def test_correctness_public_b_n2(self):
        """Public test for n = 2"""
        pair = stable_matching_1b("input/test_p1_public_n2.txt")
        self.assertEqual(pair, {1:1, 0:0})

    def test_correctness_public_b_n3_1(self):
        """Public test #1 for n = 3"""
        pair = stable_matching_1b("input/test_p1_public_n3_1.txt")
        self.assertEqual(pair, {1:1, 0:0, 2:2})

    def test_correctness_public_b_n3_2(self):
        """Public test #2 for n = 3"""
        pair = stable_matching_1b("input/test_p1_public_n3_2.txt")
        self.assertEqual(pair, {0:0, 1:2, 2:1})

    ### Public tests for 1c
    def test_correctness_public_c_n2(self):
        """Public test for n = 2"""
        pair = stable_matching_1c("input/test_p1_public_n2.txt")
        self.assertEqual(pair, {1:1, 0:0})

    def test_correctness_public_c_n3_1(self):
        """Public test #1 for n = 3"""
        pair = stable_matching_1c("input/test_p1_public_n3_1.txt")
        self.assertEqual(pair, {1:1, 0:0, 2:2})

    def test_correctness_public_c_n3_2(self):
        """Public test #2 for n = 3"""
        pair = stable_matching_1c("input/test_p1_public_n3_2.txt")
        self.assertEqual(pair, {0:0, 1:2, 2:1})

if __name__ == '__main__':
    unittest.main()


