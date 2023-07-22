import ipfshttpclient

# Connect to the IPFS node
client = ipfshttpclient.connect()


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
folder_hash = 'your_folder_ipfs_hash_here'
view_folder(folder_hash)
