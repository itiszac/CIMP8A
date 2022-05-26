#! /usr/bin/env python3

# Formatting with field widths
print("{:15} {:>5} {:>10}".format("Description", "Qty", "Price"))
print("{:15} {:>5d} {:>10.2f}".format("Hammer", 3, 9.99))
print("{:15} {:>5d} {:>10.2f}".format("Nails", 10, 14.5))
