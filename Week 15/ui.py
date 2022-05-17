#! /usr/bin/env python3

import tkinter as tk
from tkinter import ttk
import locale

from business import Investment


class FutureValueFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.parent = parent
        self.investment = Investment()

        # Set locale
        result = locale.setlocale(locale.LC_ALL, "")
        if result[0] == "C":
            locale.setlocale(locale.LC_ALL, "en_US")

        # Define string variables for text entry fields
        self.monthly_investment = tk.StringVar()
        self.yearly_interest_rate = tk.StringVar()
        self.years = tk.StringVar()
        self.futureValue = tk.StringVar()

        self.init_components()

    def init_components(self):
        self.pack()

        # Display the grid of labels and text entry fields
        ttk.Label(self, text="Monthly Investment:").grid(column=0, row=0, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.monthly_investment).grid(
            column=1, row=0
        )

        ttk.Label(self, text="Yearly Interest Rate:").grid(column=0, row=1, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.yearly_interest_rate).grid(
            column=1, row=1
        )

        ttk.Label(self, text="Years:").grid(column=0, row=2, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.years).grid(column=1, row=2)

        ttk.Label(self, text="Future Value:").grid(column=0, row=3, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.futureValue, state="readonly").grid(
            column=1, row=3
        )

        self.make_buttons()

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)

    def make_buttons(self):
        # Create a frame to store the two buttons
        button_frame = ttk.Frame(self)

        # Add the button frame to the bottom row of the main grid
        button_frame.grid(column=0, row=4, columnspan=2, sticky=tk.E)

        # Add two buttons to the button frame
        ttk.Button(button_frame, text="Calculate", command=self.calculate).grid(
            column=0, row=0, padx=5
        )
        ttk.Button(button_frame, text="Exit", command=self.parent.destroy).grid(
            column=1, row=0
        )

    def calculate(self):
        self.investment.monthly_investment = float(self.monthly_investment.get())
        self.investment.yearly_interest_rate = float(self.yearly_interest_rate.get())
        self.investment.years = int(self.years.get())

        self.futureValue.set(
            locale.currency(self.investment.calculate_future_value(), grouping=True)
        )


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Future Value Calculator")
    FutureValueFrame(root)
    root.mainloop()
