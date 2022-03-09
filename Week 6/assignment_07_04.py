#! /usr/bin/env python3

import csv

OS = [["Mac OS", "10.6"],
      ["Windows", "10"],
      ["Android", "7"]]

with open("os.txt", "w", newline="") as file:
    writer = csv.writer(file, delimiter="|")
    writer.writerows(OS)

with open("os.txt", newline="") as file:
    reader = csv.reader(file, delimiter="|")
    for row in reader:
        print(row[0], row[1])
