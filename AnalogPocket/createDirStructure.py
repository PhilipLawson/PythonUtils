# A Python 3.6+ script to organize many files into alphabetical folders
# You can provide a path arg via --path "PATH-TO-FOLDER"
# If no --path is provided, script will run in the directory the 
# script is.
# --------------------------------------------------------------------#

import os
import string
import shutil
import argparse

def create_dirs():
    # Make the 0-9 dir
    num_dir = os.path.join(current_directory, "0-9")
    os.makedirs(num_dir, exist_ok=True)

    # Loop through each letter in the alphabet
    for letter in string.ascii_uppercase:
        # Create a folder for each letter
        folder_path = os.path.join(current_directory, letter)
        os.makedirs(folder_path, exist_ok=True)

    # Walk through the current directory
    for filename in os.listdir(current_directory):
        # Splits the file name path and extension
        root, extension = os.path.splitext(filename)
        # Skip existing files, the current script or files with the specified extension(s) 
        if os.path.isdir(os.path.join(current_directory, filename)) or filename == script_name or extension in ['.bin']:
            continue

        # Get the first letter of the filename
        first_letter = filename[0].upper()

        # Check if the first letter is an alphabet character
        if first_letter in string.ascii_uppercase:
            # Move the file to the corresponding folder
            src_path = os.path.join(current_directory, filename)
            dest_path = os.path.join(current_directory, first_letter, filename)
            #shutil.move(src_path, dest_path)
            print(f"Moving [{filename}] to: {dest_path}")
        elif first_letter.isdigit():
            # Move files starting with a digit to the "0-9" folder
            src_path = os.path.join(current_directory, filename)
            dest_path = os.path.join(current_directory, "0-9", filename)
            #shutil.move(src_path, dest_path)
            print(f"Moving [{filename}] to: {dest_path}")

# Parse and command-line arguments
parser = argparse.ArgumentParser(description="Organize files by first letter.")
parser.add_argument('--path', type=str, default=os.getcwd(), help='Path to organize (default: current directory)')
args = parser.parse_args()

# Get the directory to organize
current_directory = args.path
print(f"Organizing files in: {current_directory}")
path_length = len(current_directory)
print(f"The PATH length is currently {path_length} characters.")

# Get the script's filename
script_name = os.path.basename(__file__)

# Create the folders
create_dirs()

# Print complete message
print("Folders created and files moved successfully!")
