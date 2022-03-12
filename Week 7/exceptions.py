#! /usr/bin/env python3

import sys
import os

# Prompt for the filename
filename = input("Enter the OS filename: ")

OS = []

try:
    # Try to open the file
    with open(filename) as file:
        try:
            if os.stat(filename).st_size == 0:
                raise ValueError("The file is empty")
            for line in file:
                # Add the OS to the list
                line = line.replace("\n", "")
                OS.append(line)
        except Exception as e:
            # display a generic error message
            print(type(e), e)
            sys.exit()
        finally:
            file.close()
except FileNotFoundError as e:
    # Display a file not found error
    print("FileNotFoundError:", e)
    sys.exit()
except OSError as e:
    # Display an error reading file message
    print("OSError:", e)
    sys.exit()
except Exception as e:
    # Display a generic error message
    print(type(e), e)
    sys.exit()
