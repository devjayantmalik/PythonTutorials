# ==================================================
# ==================================================
#           Working with Directories
# ==================================================
# ==================================================


# ==============================================
# Use all 6 six methods of pathlib module to print current path.

import pathlib

path1 = pathlib.Path()
path2 = pathlib.PurePath()
path3 = pathlib.PosixPath()
path4 = pathlib.PurePosixPath()

# Can't use them on mac or linux
# path5 = pathlib.WindowsPath()
# path6 = pathlib.PureWindowsPath()

print("Path:", path1)
print("PurePath:", path2)
print("PosixPath:", path3)
print("PurePosixPath:", path4)


# ===============================================
# Use pathlib module to set a working path and
# use os module to:
#   1. Create a directory
#   2. Check if the directory exists if not create it
#   3. Remove a directory
#   4. Create a file
#   5. Check if file exists if not create it
#   6. Remove a file

# Import pathlib module
import pathlib

# Set path as temp, as temp does not exist
path = pathlib.Path('../temp')

# Check if path exists
if path.exists() == False:
    path.mkdir()

# Use path object to remove a direcory
# path.rmdir()

# Using pathlib module to check if a file exists
path = pathlib.Path("../temp/data.txt")


path2 = pathlib.Path('../temp')

# Creating path2
if path2.exists() == False:
    path2.mkdir()

# Changing path of file
path2 = pathlib.Path('../temp/data.txt')

# Creating a file
path2.touch()


# ======================================
# List all directories and files in a path using pathlib

# Import the module
import pathlib

# Set a path
path = pathlib.Path('../')

# Get all files and path
for item in path.glob('*'):
    print(item)





