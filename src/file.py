import ipfshttpclient

# Connect to the IPFS node
client = ipfshttpclient.connect()

def upload_file(file_path):
    res = client.add(file_path)
    return res['Hash']

def download_file(ipfs_hash, output_path):
    client.get(ipfs_hash, output=output_path)

# Example Usage:
file_path = 'C:/Users/ambe/OneDrive - Software AG/Desktop/CDrive/personal/project/NIQYUK/projects/ipfs/testFile.txt'
uploaded_hash = upload_file(file_path)
print("File uploaded to IPFS with hash:", uploaded_hash)

downloaded_output_path = 'path/to/save/downloaded_file.txt'
download_file(uploaded_hash, downloaded_output_path)
print("File downloaded from IPFS and saved to:", downloaded_output_path)

