# Diffferent Files Structures --> Text, CSV, PNG, PDF, JPG, mp3, mp4
# Text, CSV, PDF --> Text Files
# PNG, JPG, mp3, mp4 --> Binary Files
from os.path import exists

from IPython.lib.deepreload import found_now

# Read / Write / Store information permanently / Process the text

# Python does not have a direct access.
# It creates "Stream" --> A simple abstract connection between the Program and File.

# Step 1 : Opening a file:

# stream = open(file_name, mode)

stream = open("notes.txt" , "r")
print(stream.read())
stream.close()


# Last Step should be stream.close()
# Save changes, Release the resources.

# Different Modes "r", "w", "r+"

stream = open("notes.txt" , "w")
stream.write("Python Programming.")
stream.close()

# If the file already exists, then "w" mode will erase all of its previous content.

# For all the Binary Files, The modes will have "rb" ,"wb" and "ab"

# Is a python project.
# Eshan Project --> Takes a few input --> It processes Something --> Send you the email about
# the reports.

# Text encoding: UTF-8, ASCII, UTF-16
stream = open("notes.txt" , "w", encoding="utf-8")
stream.write("Python Programming.")
stream.close()

# WhatsApp --> Person A --> Message --> {Encoded Message}--> Whatsapp
# --> {Encoded Message} --> Decoder --> Message --> Person B

# Predefined Streams:

#1. Input Stream. input("enter your input")
# sys.stdin
import sys
data = sys.stdin.readline()

#2. Output Stream.
import sys
sys.stdout.write("Hello")

#3. Error Stream

import sys
sys.stderr.write("Error Occured")

# Failing File operations --> IOError is raised.

try :
    file=open("notes.txt","r")
except IOError:
    print("Error on File opening")

# errno --> Stores the error code
import errno

try:
    file = open("abc.txt")

except IOError as error:
    print(error.errno)

# errno.ENONET --> File not found_
# errno.EACCES --> Permission Denied
# errno.EEXIST --> File already exists


