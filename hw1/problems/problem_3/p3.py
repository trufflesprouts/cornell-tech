import heapq
import collections

# A Node class is useful for building the Huffman tree.
class Node:
    def __init__(self, symbol, freq, left=None, right=None):
        """Initializes a Node for the Huffman tree."""
        self.symbol = symbol
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        """Overloads the less-than operator to allow Node objects to be compared in a min-heap."""
        return self.freq < other.freq

def run_length_encode(data_block):
    """
    Performs Run-Length Encoding on a single block of quantized DCT coefficients.

    Args:
        data_block (list[int]): A list of 64 integers representing one block that has been
                                quantized and zig-zag scanned.

    Returns:
        list[tuple]: A list of RLE symbols. Each symbol is either ('EOB',)
                     or (num_zeros, value).
    """
    # <<< YOUR IMPLEMENTATION HERE >>>
    #
    # Example: [52, -7, 0, 0, 3, 0, -2, 0, ..., 0] -> [(0, 52), (0, -7), (2, 3), (1, -2), ('EOB',)]
    #
    # Hint: Iterate through the block. If you see a zero, increment a counter.
    # If you see a non-zero value, create a symbol with the current zero count
    # and the value, then reset the counter. Don't forget the EOB symbol
    # when you reach the end of the non-zero coefficients.
    
    return []


def huffman_compress(all_rle_symbols):
    """
    Generates Huffman codes and encodes a stream of RLE symbols.

    Args:
        all_rle_symbols (list[tuple]): A list of all RLE symbols from an entire image.

    Returns:
        tuple[dict, str]: A tuple containing:
            - A dictionary mapping each unique RLE symbol to its Huffman code (binary string).
            - The fully encoded data as a single binary string.
    """
    if not all_rle_symbols:
        return {}, ""

    # <<< YOUR IMPLEMENTATION HERE >>>
    #
    # 1. Calculate frequency of each RLE symbol. `collections.Counter` is useful.
    # 2. Build the Huffman tree using a priority queue. `heapq` is recommended.
    #    - Create a leaf Node for each symbol and add it to the heap.
    #    - While the heap has more than one node, pop the two lowest frequency nodes,
    #      merge them into a new internal node, and push it back onto the heap.
    # 3. Traverse the tree to generate Huffman codes. A recursive helper function is a good approach.
    # 4. Encode the `all_rle_symbols` list into a single bitstring using your generated codes.
    
    huffman_codes = {}
    encoded_data = ""
    
    return huffman_codes, encoded_data