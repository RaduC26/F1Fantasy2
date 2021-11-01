import tkinter as tk

root = tk.Tk()
root.geometry("1140x600")

header = tk.Frame(root, background="#d5e8d4", height=120)
footer = tk.Frame(root, background="#e3e3e3", height=120)
main = tk.PanedWindow(root)

header.pack(side="top", fill="x")
footer.pack(side="bottom", fill="x")
main.pack(side="top", fill="both", expand=True)

left_pane = tk.Frame(main, background="#99fb99", width=100)
right_pane = tk.PanedWindow(main, background="#99fb99", width=200)
main.add(left_pane)
main.add(right_pane)

notebook = tk.Frame(right_pane, background="#99ceff", height=70)
bottom_right = tk.Frame(right_pane, background="#ffe6cd", height=50)
right_pane.add(notebook)
right_pane.add(bottom_right)

root.mainloop()
