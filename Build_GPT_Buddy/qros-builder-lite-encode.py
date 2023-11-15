import gzip
import base64
import os
import json

# Create directories to store chunks and decoded files
os.makedirs('builder', exist_ok=True)
os.makedirs('builder/chunks', exist_ok=True)
os.makedirs('builder/decoded', exist_ok=True)

def compress_and_generate_base64_chunks(file_path, chunk_size=1500):
    # Read the file in binary mode
    with open(file_path, 'rb') as f:
        data = f.read()

    # Compress the data using GZIP
    compressed_data = gzip.compress(data)

    # Encode the compressed data to base64
    encoded_data_base64 = base64.urlsafe_b64encode(compressed_data).decode("utf-8")

    print(f"Total size of base64 data before splitting: {len(encoded_data_base64)}")

    # Split the base64 data into chunks
    chunks = [encoded_data_base64[i:i+chunk_size] for i in range(0, len(encoded_data_base64), chunk_size)]

    # Write chunks to a JSON file
    json_file_path = os.path.join('builder', 'chunks', 'data_chunks.json')
    with open(json_file_path, 'w') as json_file:
        json.dump({"chunks": chunks}, json_file)  # Save the chunks as an array within a JSON object

    print(f"Chunks have been saved to {json_file_path}")

# File to be processed
file_path = 'all_conversations.txt'
compress_and_generate_base64_chunks(file_path)
