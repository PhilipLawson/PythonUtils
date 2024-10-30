# A Python 3.6+ script to organize many files into alphabetical folders
# You can provide a path arg via --path "PATH-TO-FOLDER"
# If no --path is provided, script will run in the directory the 
# script is.
# --------------------------------------------------------------------#

import os
import string
import shutil
import argparse
import zipfile

# Get the script's filename
script_name = os.path.basename(__file__)


def unzipFiles(current_directory):
    # Walk through the current directory
    for filename in os.listdir(current_directory):
        # Splits the file name path and extension
        root, extension = os.path.splitext(filename)
        fullPath = os.path.join(current_directory, filename)
        if extension in ['.zip']:
            # Unzip the file
            with zipfile.ZipFile(fullPath, 'r') as zip_ref:
                print(f'Unzipping the following file:- [{fullPath}]')
                zip_ref.extractall(current_directory)


def create_dirs(current_directory):
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
        if os.path.isdir(os.path.join(current_directory, filename)) or filename == script_name or extension in ['.bin', '.zip']:
            continue

        # Get the first letter of the filename
        first_letter = filename[0].upper()

        # Check if the first letter is an alphabet character
        if first_letter in string.ascii_uppercase:
            # Move the file to the corresponding folder
            src_path = os.path.join(current_directory, filename)
            dest_path = os.path.join(current_directory, first_letter, filename)
            # Move the file
            shutil.move(src_path, dest_path)
            print(f"Moving [{filename}] to: {dest_path}")
        elif first_letter.isdigit():
            # Move files starting with a digit to the "0-9" folder
            src_path = os.path.join(current_directory, filename)
            dest_path = os.path.join(current_directory, "0-9", filename)
            # Move the file
            shutil.move(src_path, dest_path)
            print(f"Moving [{filename}] to: {dest_path}")


def main():
    # Parse and command-line arguments
    parser = argparse.ArgumentParser(description="Organize files by first letter.")
    parser.add_argument('--path', type=str, default=os.getcwd(), help='Path to organize (default: current directory)')
    parser.add_argument('--unzip', type=bool, default=False, help='Unzip any zip files first but do not move the zip files themselves.')
    args = parser.parse_args()

    # Get the directory to organize
    current_directory = args.path
    print(f"Organizing files in: {current_directory}")

    # Unzip the files if requested
    if args.unzip == True:
        print(f"Unzip arg set to:- {args.unzip}")
        unzipFiles(current_directory)

    # Create the folders
    if os.path.exists(current_directory):
        create_dirs(current_directory)
        # Print complete message
        print("Folders created and files moved successfully!")
    else:
        print('Path does not exist')


if __name__ == "__main__":
    main()