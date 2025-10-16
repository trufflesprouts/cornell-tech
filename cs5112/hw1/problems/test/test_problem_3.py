import unittest
import sys
sys.path.append("..")
from problem_3.p3 import run_length_encode, huffman_compress
import unittest
from collections import Counter


class TestProblem3(unittest.TestCase):
    def setUp(self):
        pass

    def _is_prefix_code(self, codes):
        sorted_codes = sorted(codes.values())
        for i in range(len(sorted_codes) - 1):
            if sorted_codes[i+1].startswith(sorted_codes[i]):
                return False
        return True

    def test_rle_basic(self):
        block = [52, -7, 0, 0, 3, 0, -2] + [0] * 57
        expected = [(0, 52), (0, -7), (2, 3), (1, -2), ('EOB',)]
        self.assertEqual(run_length_encode(block), expected, "Failed on a basic RLE case.")


    def test_rle_edge_cases(self):
        test_cases = {
            "All Zeros": ([0] * 64, [('EOB',)]),
            "No Zeros": ([i for i in range(1, 65)], [(0, i) for i in range(1, 65)] + [('EOB',)]),
            "Ends with Non-Zero": ([5, 0, 0, -10], [(0, 5), (2, -10), ('EOB',)]),
            "Starts with Zeros": ([0, 0, 0, 25] + [0] * 60, [(3, 25), ('EOB',)]),
            "Empty block": ([], [('EOB',)])
        }
        for name, (block, expected) in test_cases.items():
            if len(block) < 64:
                block.extend([0] * (64 - len(block)))
            self.assertEqual(run_length_encode(block), expected, f"RLE failed on edge case: {name}")



    def test_huffman_basic(self):
        symbols = ['A', 'A', 'B', 'C', 'A', 'A', 'B'] # Freq: A=4, B=2, C=1
        codes, stream = huffman_compress(symbols)
        
        self.assertEqual(set(codes.keys()), set(symbols), "Not all symbols were encoded.")
        
        self.assertTrue(self._is_prefix_code(codes), "Generated codes are not prefix codes.")
        
        freq = Counter(symbols)
        self.assertTrue(len(codes['A']) <= len(codes['B']))
        self.assertTrue(len(codes['B']) <= len(codes['C']))

        expected_stream = "".join([codes[s] for s in symbols])
        self.assertEqual(stream, expected_stream, "Encoded bitstream is incorrect.")


    def test_huffman_with_rle(self):
        rle_symbols = [(0, 10), (2, -5), (0, 10), ('EOB',), (0, 10), (2, -5)]
        codes, stream = huffman_compress(rle_symbols)
        
        self.assertEqual(set(codes.keys()), set(rle_symbols), "Not all RLE symbols were encoded.")
        self.assertTrue(self._is_prefix_code(codes), "Generated codes for RLE symbols are not prefix codes.")
        
        freq = Counter(rle_symbols)
        self.assertTrue(len(codes[(0, 10)]) <= len(codes[(2, -5)]))
        self.assertTrue(len(codes[(2, -5)]) == len(codes[('EOB',)])) # Same frequency -> same length

        expected_stream = "".join([codes[s] for s in rle_symbols])
        self.assertEqual(stream, expected_stream, "Encoded bitstream for RLE symbols is incorrect.")


    def test_huffman_edge_cases(self):
        symbols_single = ['X', 'X', 'X', 'X']
        codes, stream = huffman_compress(symbols_single)
        self.assertEqual(len(codes), 1, "Should only be one code for a single unique symbol.")
        self.assertIn(codes['X'], ['0', '1'], "Code for a single symbol should be '0' or '1'.")
        self.assertEqual(stream, codes['X'] * 4, "Stream for single symbol is incorrect.")
        
        symbols_uniform = ['A', 'B', 'C', 'D']
        codes, stream = huffman_compress(symbols_uniform)
        self.assertTrue(self._is_prefix_code(codes), "Prefix property failed for uniform distribution.")
        code_lengths = {len(c) for c in codes.values()}
        self.assertEqual(len(code_lengths), 1, "All codes should have the same length for uniform frequencies.")
        self.assertEqual(list(code_lengths)[0], 2, "Code length should be 2 for 4 unique symbols with uniform frequency.")

if __name__=='__main__':
    unittest.main()
