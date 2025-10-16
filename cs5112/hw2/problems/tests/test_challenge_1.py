import unittest
import sys
import random
sys.path.append("..")

from challenge_1.partition import brute_force, greedy, dp

def compute_sum(S, mask):                          
    return (                                       
        sum([x for x,m in zip(S, mask) if m == 0]),
        sum([x for x,m in zip(S, mask) if m == 1]),
    )                                              
class TestChallenge1(unittest.TestCase):

    ### Public tests
    def test_correctness_public_brute_force(self):
        S = [1,2,3]
        s = compute_sum(S, brute_force(S))
        self.assertEqual((3,3), s)

    def test_correctness_public_greedy(self):
        N = 20
        S = list(set([random.randint(0, 100) for _ in range(N)]))

        ref = compute_sum(S, brute_force(S))

        s1, s2 = compute_sum(S, greedy(S))
        m = min(s1, s2)
        M = max(s1, s2)

        self.assertGreaterEqual(m, 0.75 * min(ref))
        self.assertLessEqual(M, 4 / 3 * max(ref))

    def test_correctness_public_dp(self):
        N = 20
        S = list(set([random.randint(0, 100) for _ in range(N)]))

        ref = compute_sum(S, brute_force(S))

        s = compute_sum(S, dp(S))

        self.assertEqual(min(ref), min(s))
        self.assertEqual(max(ref), max(s))


if __name__ == '__main__':
    unittest.main()
