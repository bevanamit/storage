import ipfshttpclient
import os

# Connect to the IPFS node
client = ipfshttpclient.connect()

def upload_folder(folder_path):
    res = client.add(folder_path, recursive=True)
    return res['Hash']

def download_folder(ipfs_hash, output_path):
    client.get(ipfs_hash, output=output_path)

# Example Usage:
folder_path = 'path/to/your/folder'
uploaded_hash = upload_folder(folder_path)
print("Folder uploaded to IPFS with hash:", uploaded_hash)

downloaded_output_path = 'path/to/save/downloaded_folder'
download_folder(uploaded_hash, downloaded_output_path)
print("Folder downloaded from IPFS and saved to:", downloaded_output_path)
