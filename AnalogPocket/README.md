createDirStructure is a Python 3 script that will unzip (if prompted), create a folder structure of Alphabetically order and move extracted files into those folders based off the filenames first character.

Usage
=====

createDirStructure.py --path <PATH_TO_FILES> --unzip False
(The above example would create folders 1-9 and A-Z then move all files within that path to inside each folder by first character in the file name. It will not move any files with the extension listed on line 41)

createDirStructure.py --path <PATH_TO_FILES> --unzip True
(Same as above except if a zip file is found, it will extract the contents and move the files that were extracted only, leaving the zip file in the root dir. Use the optional --clean flag to remove the zip files.)
