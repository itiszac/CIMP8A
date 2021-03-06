#! /usr/bin/env python3

import tkinter as tk
from tkinter import ttk


class MPGFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.pack()

        # Define string variables for text entry fields
        self.milesDriven = tk.StringVar()
        self.gallonsUsed = tk.StringVar()
        self.milesPerGallon = tk.StringVar()

        # Display the components
        ttk.Label(self, text="Miles Driven:").grid(column=0, row=0, sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=self.milesDriven).grid(column=1, row=0)

        ttk.Label(self, text="Gallons of Gas Used:").grid(column=0, row=1, sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=self.gallonsUsed).grid(column=1, row=1)

        ttk.Label(self, text="Miles Per Gallon:").grid(column=0, row=2, sticky=tk.E)
        ttk.Entry(
            self, width=30, textvariable=self.milesPerGallon, state="readonly"
        ).grid(column=1, row=2)

        ttk.Button(self, text="Calculate", command=self.calculate).grid(
            column=1, row=3, sticky=tk.E
        )

        # Add padding to all components
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)

    def calculate(self):
        # Get numbers from the first two text entry fields
        milesDriven = float(self.milesDriven.get())
        gallonsUsed = float(self.gallonsUsed.get())

        # Calc the miles per gallon (mpg)
        mpg = milesDriven / gallonsUsed
        mpg = round(mpg, 2)

        # Display the mpg in the third text field
        self.milesPerGallon.set(mpg)


if __name__ == "__main__":
    # Create the root window
    root = tk.Tk()

    # Add a title to the root
    root.title("Miles Per Gallon Calculator")

    MPGFrame(root)

    # Display the root Window
    root.mainloop()
