import json
import base64
import gzip
import os

def decode_and_decompress_chunks(json_file_path, output_file_path):
    # Read chunks from the JSON file
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        chunks = data.get('chunks', [])

    # Concatenate the base64 chunks
    concatenated_base64 = ''.join(chunks)
    print(f"Total size of concatenated base64 data: {len(concatenated_base64)}")

    # Decode the base64 data to bytes
    decoded_data = base64.urlsafe_b64decode(concatenated_base64.encode("utf-8"))

    # Decompress the data using GZIP
    try:
        decompressed_data = gzip.decompress(decoded_data)
        with open(output_file_path, 'wb') as out_file:
            out_file.write(decompressed_data)
        print(f"Data has been decompressed and saved to {output_file_path}")
    except Exception as e:
        print(f"Exception occurred during decompression: {e}")

# Path to the JSON file containing the base64 chunks
json_file_path = 'builder/chunks/data_chunks.json'

# Path to the output file where the decompressed data will be saved
output_file_path = 'builder/decoded/all_conversations.txt'

decode_and_decompress_chunks(json_file_path, output_file_path)
