
# read() --> Text File, Binary File

file = open('story.txt','r')

# Reading a particular no. of characters.

# contents = file.read(10)
# line = file.readline()
#
# print(line)


# print(file.readline())
# print(file.readline())

# lines = file.readlines()
#
# print(lines)
#
# file.close()


# Readinto() --> Used with binary files.

# data = bytearray(1024)
#
# file = open('img.png','rb')
#
# file.readinto(data)
#
# file.close()
# print(data)


# write() --> method to write.

# file = open('story.txt','w')
#
# file.write("Python is awesome")
# file.close()


for line in open('story.txt','rt'):
    print(line,end="")

