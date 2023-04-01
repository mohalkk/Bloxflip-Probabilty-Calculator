import tkinter as tk
from tkinter import ttk

def calculate_mines():
    incorrect_squares = max(1, min(24, int(incorrect_entry.get())))
    max_clicked_squares = 25 - incorrect_squares
    clicked_squares = max(0, min(max_clicked_squares, int(clicked_entry.get())))

    if (incorrect_squares != int(incorrect_entry.get())
            or clicked_squares != int(clicked_entry.get())):
        answer_label.config(text="Probability: Error")
        return

    accuracy = (25 - incorrect_squares) / 25 
    probability = accuracy ** clicked_squares * 100
    answer_label.config(text=f"Probability: {probability:.2f}%")

def calculate_towers():
    clicked_rows = max(1, min(8, int(clicked_entry.get())))

    if clicked_rows != int(clicked_entry.get()):
        answer_label.config(text="Probability: Error")
        return
    
    if mode_selector.get() == "Easy":
        chance = 2/3
    elif mode_selector.get() == "Normal":
        chance = 1/2
    elif mode_selector.get() == "Hard":
        chance = 1/3
    
    probability = chance ** clicked_rows * 100
    
    answer_label.config(text=f"Probability: {probability:.2f}%")
    
def switch_calculator():
    selected = calculator_selector.get()
    if selected == "Mines":
        calculate_button.config(command=calculate_mines)
        incorrect_label.config(text="Mines")
        incorrect_entry.grid(row=1, column=1, padx=5, pady=5)
        clicked_label.config(text="Tiles")
        mode_selector.grid_forget()
    elif selected == "Towers":
        calculate_button.config(command=calculate_towers)
        incorrect_label.config(text="Mode")
        incorrect_entry.grid_forget()
        clicked_label.config(text="Tiles")
        mode_selector.grid(row=1, column=1, padx=5, pady=5)
    answer_label.config(text="")

root = tk.Tk()
root.title("Bloxflip Probability Calculator v2.0")
root.geometry("150x155")

calculator_selector = ttk.Combobox(root, values=["Mines", "Towers"], state="readonly")
calculator_selector.current(0)
calculator_selector.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

incorrect_label = ttk.Label(root, text="Mines")
incorrect_label.grid(row=1, column=0, padx=5, pady=5)
incorrect_entry = ttk.Entry(root, width=10)
incorrect_entry.grid(row=1, column=1, padx=5, pady=5)

mode_selector = ttk.Combobox(root, values=["Easy", "Normal", "Hard"], state="readonly", width=7)
mode_selector.current(0)

clicked_label = ttk.Label(root, text="Tiles")
clicked_label.grid(row=2, column=0, padx=5, pady=5)
clicked_entry = ttk.Entry(root, width=10)
clicked_entry.grid(row=2, column=1, padx=5, pady=5)

calculate_button = ttk.Button(root, text="Calculate", command=calculate_mines)
calculate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="sew") # center button

answer_label = ttk.Label(root, text="")
answer_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

calculator_selector.bind("<<ComboboxSelected>>", lambda event: switch_calculator())

root.mainloop()
