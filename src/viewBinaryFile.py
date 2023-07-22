import ipfshttpclient
import base64

# Connect to the IPFS node
client = ipfshttpclient.connect()


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


# Example Usage:
ipfs_hash = 'your_binary_file_ipfs_hash_here'
view_binary_file(ipfs_hash)
