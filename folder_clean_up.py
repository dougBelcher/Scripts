# a bot to clean up folders
import os
import argparse

parser = argparse.ArgumentParser(
    description="Clean up directory and put files into according folders."
)

parser.add_argument(
    "--path",
    type=str,
    default=".",
    help="Directory path of the to be cleaned directory",
)

# parse the arguments given by the user and extract the path
args = parser.parse_args()
path = args.path

print(f"Cleaning up directory {path}")

# get all files from given directory
dir_content = os.listdir(path)

# create a relative path from the path to the file and the document name
path_dir_content = [os.path.join(path, doc) for doc in dir_content]

# filter our directory content into a documents and folders list
docs = [doc for doc in path_dir_content if os.path.isfile(doc)]
folders = [folder for folder in path_dir_content if os.path.isdir(folder)]

# counter to keep track of amount of moved files
# and list of already created folders to avoid multiple creations
moved = 0
created_folders = []

print(f"Cleaning up {len(docs)} of {len(dir_content)} elements.")

# go through all files and move them into according folders
for doc in docs:
    # separte name from file extension
    full_doc_path, filetype = os.path.splitext(doc)
    doc_path = os.path.dirname(full_doc_path)
    doc_name = os.path.basename(full_doc_path)

    print(filetype)
print(full_doc_path)
print(doc_path)
print(doc_name)

break

# skip this file when it is in the directory
if doc_name == "directory_clean" or doc_name.startswith('.'):
        continue

    # get the subfolder name and create folder if not exist
    subfolder_path = os.path.join(path, filetype[1:].lower())

    if subfolder_path not in folders:
    	# create the folder