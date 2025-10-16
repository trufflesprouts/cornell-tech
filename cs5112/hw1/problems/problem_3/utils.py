import numpy as np
from scipy.fftpack import dct, idct

def get_luminance_quantization_table(quality):
    # This function remains the same
    base_table = np.array([
        [16, 11, 10, 16, 24, 40, 51, 61], [12, 12, 14, 19, 26, 58, 60, 55],
        [14, 13, 16, 24, 40, 57, 69, 56], [14, 17, 22, 29, 51, 87, 80, 62],
        [18, 22, 37, 56, 68, 109, 103, 77], [24, 35, 55, 64, 81, 104, 113, 92],
        [49, 64, 78, 87, 103, 121, 120, 101], [72, 92, 95, 98, 112, 100, 103, 99]
    ], dtype=np.float32)
    
    if quality < 50:
        scale = 5000 / quality
    else:
        scale = 200 - 2 * quality
        
    scaled_table = (base_table * scale + 50) / 100
    scaled_table[scaled_table < 1] = 1
    return scaled_table

def get_chrominance_quantization_table(quality):
    base_table = np.array([
        [17, 18, 24, 47, 99, 99, 99, 99], [18, 21, 26, 66, 99, 99, 99, 99],
        [24, 26, 56, 99, 99, 99, 99, 99], [47, 66, 99, 99, 99, 99, 99, 99],
        [99, 99, 99, 99, 99, 99, 99, 99], [99, 99, 99, 99, 99, 99, 99, 99],
        [99, 99, 99, 99, 99, 99, 99, 99], [99, 99, 99, 99, 99, 99, 99, 99]
    ], dtype=np.float32)
    
    if quality < 50:
        scale = 5000 / quality
    else:
        scale = 200 - 2 * quality
        
    scaled_table = (base_table * scale + 50) / 100
    scaled_table[scaled_table < 1] = 1
    return scaled_table

def split_into_blocks(matrix, block_size=8):
    h, w = matrix.shape
    blocks = []
    for j in range(0, h, block_size):
        for i in range(0, w, block_size):
            blocks.append(matrix[j:j+block_size, i:i+block_size])
    return blocks

def apply_dct_quantize_zigzag(block, q_table):
    dct_block = dct(dct(block.T, norm='ortho').T, norm='ortho')
    quantized_block = np.round(dct_block / q_table)
    return list(quantized_block.flatten('F'))


def run_length_decode(rle_symbols):
    """Decodes RLE symbols back into a list of 64 coefficients."""
    decoded_list = []
    for symbol in rle_symbols:
        if symbol[0] == 'EOB':
            break
        num_zeros, value = symbol
        decoded_list.extend([0] * num_zeros)
        decoded_list.append(value)
    
    # Pad with zeros to fill the 64-element block
    decoded_list.extend([0] * (64 - len(decoded_list)))
    return decoded_list

def reconstruct_from_rle(all_rle_symbols, shape, q_table, block_size=8):
    h, w = shape
    reconstructed_img = np.zeros(shape)
    num_blocks_h, num_blocks_w = h // block_size, w // block_size
    
    block_rle_lists, current_block = [], []
    for symbol in all_rle_symbols:
        current_block.append(symbol)
        if symbol[0] == 'EOB':
            block_rle_lists.append(current_block)
            current_block = []

    for idx, rle_list in enumerate(block_rle_lists):
        row, col = idx // num_blocks_w, idx % num_blocks_w
        
        flat_list = run_length_decode(rle_list)
        
        if len(flat_list) > 64:
            flat_list = flat_list[:64]
        else:
            flat_list.extend([0] * (64 - len(flat_list)))
        
        quantized_block = np.array(flat_list).reshape((8, 8), order='F')
        dequantized_block = quantized_block * q_table
        reconstructed_block = idct(idct(dequantized_block.T, norm='ortho').T, norm='ortho')
        
        j, i = row * block_size, col * block_size
        reconstructed_img[j:j+block_size, i:i+block_size] = reconstructed_block

    reconstructed_img += 128
    return np.clip(reconstructed_img, 0, 255).astype(np.uint8)

def huffman_decode(encoded_data, huffman_codes):
    if not encoded_data:
        return []
        
    inverse_codes = {code: symbol for symbol, code in huffman_codes.items()}
    
    decoded_symbols = []
    current_code = ""
    for bit in encoded_data:
        current_code += bit
        if current_code in inverse_codes:
            decoded_symbols.append(inverse_codes[current_code])
            current_code = ""
            
    return decoded_symbols