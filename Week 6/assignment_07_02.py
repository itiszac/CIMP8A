#! /usr/bin/env python3
import os

# open a file in write mode (overwrite)
file = open(os.path.expandvars("$HOME/Desktop/hello.txt"), "w")

# write to the file
file.write("Hello World\n")
file.write("From Zach")

# close the file
file.close()

# Read and print the entire file
print("This will read and print the entire file")
with open(os.path.expandvars("$HOME/Desktop/hello.txt")) as file:
    text = file.read()
    print(text)

print()

# Read the entire file and print 1 line at a time
print("This will read the entire file "
      "and then print 1 line at a time")
with open(os.path.expandvars("$HOME/Desktop/hello.txt")) as file:
    for line in file:
        print(line, end="")

print("\n")

# Read the entire file as a list
print("This will read file as a list "
      "and then print 1 list item at a time")
with open(os.path.expandvars("$HOME/Desktop/hello.txt")) as file:
    listItems = file.readlines()
    for item in listItems:
        print(item, end="")

print("\n")

# Read and print the file 1 line at a time
print("This will read and print the file "
      "1 line at a time")
with open(os.path.expandvars("$HOME/Desktop/hello.txt")) as file:
    line = file.readline()
    print(line, end="")
    line = file.readline()
    print(line)
