#! /usr/bin/env python3

import pickle

OS = [["Mac OS", "10.6"],
      ["Windows", "10"],
      ["Android", "7"]]

# Open a binary file for write (overwrite)
with open("os.txt", "wb") as file:
    pickle.dump(OS, file)

# Open a binary file for read
with open("os.txt", "rb") as file:
    os = pickle.load(file)
    print(os)
