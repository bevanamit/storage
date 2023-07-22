import ipfshttpclient
import base64

# Replace 'http://your_remote_ipfs_api_endpoint/' with the actual API endpoint URL.
# Example of a public IPFS gateway: 'https://ipfs.io/api/'
remote_endpoint = 'http://your_remote_ipfs_api_endpoint/'

# Connect to the remote IPFS node
client = ipfshttpclient.connect(endpoint=remote_endpoint)


# Uploading all types of files
def upload_file(file_path):
    res = client.add(file_path)
    return res['Hash']


# Uploading a folder
def upload_folder(folder_path):
    res = client.add(folder_path, recursive=True)
    return res['Hash']


# Downloading files
def download_file(ipfs_hash, output_path):
    client.get(ipfs_hash, output=output_path)


# Downloading a folder
def download_folder(ipfs_hash, output_path):
    client.get(ipfs_hash, output=output_path)


# Viewing the content of text-based files
def view_text_file(ipfs_hash):
    try:
        # Download the file from IPFS
        res = client.cat(ipfs_hash)

        # Decode the bytes to UTF-8 (assuming it's a text file)
        content = res.decode('utf-8')

        # Display the content
        print("Content of the file:")
        print(content)

    except ipfshttpclient.exceptions.ErrorResponse as e:
        print("Error:", e)


# Viewing binary files as base64-encoded strings
def view_binary_file(ipfs_hash):
    try:
        # Download the file from IPFS
        res = client.cat(ipfs_hash)

        # Display the content as base64 encoded string
        content_base64 = base64.b64encode(res).decode('utf-8')
        print("Base64-encoded content of the binary file:")
        print(content_base64)

        # If you want to save the binary content to a file, you can do so like this:
        # with open('output_file.bin', 'wb') as output_file:
        #     output_file.write(res)

    except ipfshttpclient.exceptions.ErrorResponse as e:
        print("Error:", e)


# Viewing the content of a folder
def view_folder(ipfs_hash, indent=0):
    try:
        # Get the directory listing from IPFS
        res = client.ls(ipfs_hash)

        for item in res:
            # If it's a file, display the file name
            if item['Type'] == 'file':
                print(" " * indent + "- " + item['Name'])
            # If it's a directory, display the folder name and recursively view its contents
            elif item['Type'] == 'directory':
                print(" " * indent + "- " + item['Name'] + " (folder)")
                view_folder(item['Hash'], indent + 2)

    except ipfshttpclient.exceptions.ErrorResponse as e:
        print("Error:", e)


# Example Usage:

# Uploading files
file_path = 'path/to/your/file.txt'
uploaded_hash = upload_file(file_path)
print("File uploaded to IPFS with hash:", uploaded_hash)

# Downloading files
downloaded_output_path = 'path/to/save/downloaded_file.txt'
download_file(uploaded_hash, downloaded_output_path)
print("File downloaded from IPFS and saved to:", downloaded_output_path)

# Viewing text files
view_text_file(uploaded_hash)

# Uploading folders
folder_path = 'path/to/your/folder'
uploaded_hash = upload_folder(folder_path)
print("Folder uploaded to IPFS with hash:", uploaded_hash)

# Downloading folders
downloaded_output_path = 'path/to/save/downloaded_folder'
download_folder(uploaded_hash, downloaded_output_path)
print("Folder downloaded from IPFS and saved to:", downloaded_output_path)

# Viewing the content of a folder
view_folder(uploaded_hash)
