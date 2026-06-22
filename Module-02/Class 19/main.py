# Python OS Module
# --> Bridge between the python program and the operating system
# Create Folders, Delete Folders, Navigate Directories, Execute terminal commands,
# Get The System Information.

# Deployment Script --> Can be kept at a particular location and can be executed.

import os

from fontTools.feaLib.ast import ScriptStatement
from tensorflow.python.distribute.multi_process_runner import Resources

info = os.uname()
print(info)

# posix.uname_result(sysname='Darwin', nodename='Ashrafs-Mac-mini.local', release='25.5.0', version='Darwin Kernel Version 25.5.0: Mon Apr 27 20:41:26 PDT 2026; root:xnu-12377.121.6~2/RELEASE_ARM64_T8132', machine='arm64')

print(os.name)
# posix --> Linux / Unix / macOS
# nt --> Windows
# java --> Jython

# Application --> backup.
# if(os.name == "posix"):
#     # execute macOS Commands
# elif(os.name == "nt"):
#     # execute windowd Command for backup

# try:
#     os.mkdir("/Users/ashraf/Math Code Academy/Eshan/NestedFolder1/NestedFolder2")
# except FileExistsError:
#     print("Folder already exists")

try:
    os.makedirs("/Users/ashraf/Math Code Academy/Eshan/NestedFolder2/NestedFolder2")
except FileExistsError:
    print("Folder already exists")

# src
#   -> Resources
#   -> Scripts
# test
#    -> Resources
#    -> Test Scripts

# List Directory Contents.


# os.mkdir("hello")
print(os.listdir())

# Current Working Directory --> Tells in which folder we are currently in.
# pwd -> Present working directory --> Used in terminal

print(os.getcwd())
# os.chdir("hello")
print(os.getcwd())

# Remove Directories --> IT SHOULD BE EMPTY !!
# os.rmdir("hello")
# os.rmdir("My_new_folder")

os.system("git add .")
os.system("git commit -m 'Class 19'")
os.system("git push origin main")
