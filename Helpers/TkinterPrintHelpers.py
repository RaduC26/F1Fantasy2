import tkinter.ttk
import tkinter as tk
from tkinter import VERTICAL


def printPanelText(root, number):
    if number % 2 == 0:
        team_no = "Team #%s" % int((number + 2) / 2)
        label = tk.Label(root, text=team_no, width=20, height=3, font=('Courier', 10, 'bold'))
        label.grid(column=number, row=0)
        label = tk.Label(root, text="Total team price", width=20, height=3, font=('Courier', 10, 'bold'))
        label.grid(column=number, row=7)
        label = tk.Label(root, text="Total team score", width=20, height=3, font=('Courier', 10, 'bold'))
        label.grid(column=number, row=8)
    else:
        label = tk.Label(root, text="Price", width=8, height=3, font=('Courier', 10, 'bold'))
        label.grid(column=number, row=0)


def printVerticalSeparator(root, i):
    tkinter.ttk.Separator(root, orient=VERTICAL).grid(column=i, row=0, rowspan=9, sticky='nsw')