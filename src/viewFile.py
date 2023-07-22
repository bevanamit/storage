import ipfshttpclient

# Connect to the IPFS node
client = ipfshttpclient.connect()


def view_file(ipfs_hash):
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


# Example Usage:
ipfs_hash = 'your_file_ipfs_hash_here'
view_file(ipfs_hash)

