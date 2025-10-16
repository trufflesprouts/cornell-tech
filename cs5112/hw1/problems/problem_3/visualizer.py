import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Import all necessary functions
from utils import (
    get_luminance_quantization_table,
    get_chrominance_quantization_table,
    split_into_blocks,
    apply_dct_quantize_zigzag,
    reconstruct_from_rle,
    huffman_decode
)
from p3 import run_length_encode, huffman_compress

def main():
    image_path = 'image.jpeg'
    quality = 50

    print(f"Reading '{image_path}' and converting to YCbCr...")
    img = Image.open(image_path)
    ycbcr_img = img.convert('YCbCr')
    
    y_channel, cb_channel, cr_channel = ycbcr_img.split()
    
    channels_data = {
        'Y': np.array(y_channel, dtype=np.float32),
        'Cb': np.array(cb_channel, dtype=np.float32),
        'Cr': np.array(cr_channel, dtype=np.float32)
    }
    
    q_tables = {
        'Y': get_luminance_quantization_table(quality),
        'Cb': get_chrominance_quantization_table(quality),
        'Cr': get_chrominance_quantization_table(quality)
    }

    compressed_data_streams = {}
    reconstructed_channels = {}
    total_compressed_bits = 0

    for name, data in channels_data.items():
        print(f"\n--- Processing {name} Channel ---")
        
        original_shape = data.shape
        h, w = data.shape
        pad_h = (8 - h % 8) % 8
        pad_w = (8 - w % 8) % 8
        if pad_h != 0 or pad_w != 0:
            data = np.pad(data, ((0, pad_h), (0, pad_w)), mode='edge')
        
        data -= 128
        blocks = split_into_blocks(data)
        
        processed_blocks = [apply_dct_quantize_zigzag(block, q_tables[name]) for block in blocks]
        
        all_rle_symbols = []
        for block in processed_blocks:
            all_rle_symbols.extend(run_length_encode(block))
        
        huffman_codes, encoded_data = huffman_compress(all_rle_symbols)
        
        print("Verifying Huffman implementation by decoding the bitstream...")
        decoded_rle_symbols = huffman_decode(encoded_data, huffman_codes)

        if all_rle_symbols != decoded_rle_symbols or not decoded_rle_symbols:
            print("\n*** VERIFICATION FAILED! ***")
            print("The decoded RLE symbols do not match the original RLE symbols.")
            print("Please check your huffman_compress implementation.")
            return

        print("Verification successful.")
        total_compressed_bits += len(encoded_data)
        
        reconstructed_channel_data = reconstruct_from_rle(decoded_rle_symbols, data.shape, q_tables[name])
        reconstructed_channels[name] = reconstructed_channel_data[:original_shape[0], :original_shape[1]]

        reconstructed_channel_data = reconstruct_from_rle(all_rle_symbols, data.shape, q_tables[name])
        reconstructed_channels[name] = reconstructed_channel_data[:original_shape[0], :original_shape[1]]

    print("\nMerging channels and converting back to RGB...")
    reconstructed_y = Image.fromarray(reconstructed_channels['Y'])
    reconstructed_cb = Image.fromarray(reconstructed_channels['Cb'])
    reconstructed_cr = Image.fromarray(reconstructed_channels['Cr'])
    
    reconstructed_image = Image.merge('YCbCr', (reconstructed_y, reconstructed_cb, reconstructed_cr))
    reconstructed_image_rgb = reconstructed_image.convert('RGB')
    
    original_bits = img.size[0] * img.size[1] * 3 * 8
    ratio = original_bits / total_compressed_bits
    
    print("\n--- Final Compression Analysis ---")
    print(f"Original Image Size       : {original_bits / 8 / 1024:.2f} KB")
    print(f"Total Compressed Size     : {total_compressed_bits / 8 / 1024:.2f} KB")
    print(f"Overall Compression Ratio : {ratio:.2f} : 1")

    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    axes[0].imshow(img)
    axes[0].set_title('Original Image')
    axes[0].axis('off')

    axes[1].imshow(reconstructed_image_rgb)
    axes[1].set_title(f'Reconstructed Image (Q={quality})')
    axes[1].axis('off')
    
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()