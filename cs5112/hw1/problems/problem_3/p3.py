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
    symbols = []
    num_zeros = 0
    for value in data_block:
        if value == 0:
            num_zeros += 1
        else:
            symbols.append((num_zeros, value))
            num_zeros = 0

    symbols.append(('EOB',))
    return symbols


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

    frequencies = collections.Counter(all_rle_symbols)

    heap = [Node(symbol, freq) for symbol, freq in frequencies.items()]
    heapq.heapify(heap)

    # build huffman tree
    while len(heap) > 1:
        n1 = heapq.heappop(heap)
        n2 = heapq.heappop(heap)
        merged = Node(None, n1.freq + n2.freq, n1, n2)
        heapq.heappush(heap, merged)

    root = heap[0]

    codes = assign_codes(root)
    stream = "".join(codes[symbol] for symbol in all_rle_symbols)
    return codes, stream

def assign_codes(node, prefix=""):
    codes = {}
    if node.symbol is not None:
        codes[node.symbol] = prefix if prefix else "0"
        return codes
    codes.update(assign_codes(node.left, prefix + "0"))
    codes.update(assign_codes(node.right, prefix + "1"))
    return codes