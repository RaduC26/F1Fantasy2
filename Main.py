import tkinter as tk
import tkinter.ttk
from tkinter import VERTICAL

from CalculationClient import calculateBestTeams
from Data.TeamExport import TeamExport
from Helpers.TkinterPrintHelpers import printPanelText, printVerticalSeparator

root = tk.Tk()
root.iconbitmap('Resources/assets/F1-icon.ico')
root.title('F1 Fantasy Calculator')
root.geometry("708x632")

header = tk.Frame(root, background="#d5e8d4", height=100)
footer = tk.Frame(root, background="#e3e3e3", height=100)
main = tk.Frame(root, background="#99fb99", height=486)

# root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
header.grid(row=0, column=0, sticky="ew")
main.grid(row=1, column=0, sticky="nsew")
footer.grid(row=2, column=0, sticky="ew")

# Header design
header.grid_columnconfigure(0, weight=1)
header.grid_columnconfigure(1, weight=1)

# Welcome message
welcome_message = tk.Label(header, text="Welcome to F1 Fantasy Calculator!", background="#d5e8d4", width=30, height=6)
welcome_message.grid(column=0, row=0)
instructions = tk.Label(header, text='Enter your budget below and click the button to generate your '
                                     'top 3 teams', background="#d5e8d4", width=30, height=6, wraplength=220)
instructions.grid(column=1, row=0)


def print_teams():
    best_teams = calculateBestTeams(float(budget_input.get()), 3)
    for i in range(6):
        panel = tk.Frame(main, background="red", width=100, height=450)
        panel.grid(row=0, column=i)
        printPanelText(panel, i)
        if i % 2 == 0:
            printVerticalSeparator(main, i)
            team: TeamExport = best_teams[int(i / 2)]
            for j in range(6):
                driver = tk.Label(panel, width=20, height=3, text=team.getNames()[j], font=('Courier', 10))
                driver.grid(row=j + 1, column=i)
        else:
            team: TeamExport = best_teams[int((i - 1) / 2)]
            for j in range(6):
                price = tk.Label(panel, width=8, height=3, text=team.getPrices()[j], font=('Courier', 10))
                price.grid(row=j + 1, column=i)
            totalPriceLabel = tk.Label(panel, width=8, height=3, text=team.getTotalPrice(), font=('Courier', 10))
            totalPriceLabel.grid(column=i, row=j + 2)
            totalScoreLabel = tk.Label(panel, width=8, height=3, text=team.getTotalScore(), font=('Courier', 10))
            totalScoreLabel.grid(column=i, row=j + 3)


# Footer design
footer.grid_columnconfigure(0, weight=1)
footer.grid_columnconfigure(1, weight=1)
footer.grid_columnconfigure(2, weight=1)

# generate budget input
budget_label = tk.Label(footer, text="Budget: ", background="#e3e3e3")
budget_label.grid(column=0, row=0)
budget_input = tk.Entry(footer)
budget_input.grid(column=1, row=0)

# generate button
generate_teams_button = tk.Button(footer, text="Generate teams", height=2, width=20, bg='#7765E3',
                                  command=lambda: print_teams())
generate_teams_button.grid(column=2, row=0, pady=5)

root.mainloop()
