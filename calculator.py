import tkinter as tk
from tkinter import ttk

def calculate_mines():
    # Get the input values and restrict them to the desired range
    incorrect_squares = max(1, min(24, int(incorrect_entry.get())))
    max_clicked_squares = 25 - incorrect_squares
    clicked_squares = max(0, min(max_clicked_squares, int(clicked_entry.get())))

    # Check if the input values are within the desired range
    if (incorrect_squares != int(incorrect_entry.get())
            or clicked_squares != int(clicked_entry.get())):
        answer_label.config(text="Probability: Error")
        return

    # Calculate the probability and update the label
    accuracy = (25 - incorrect_squares) / 25 
    probability = accuracy ** clicked_squares * 100
    answer_label.config(text=f"Probability: {probability:.2f}%")

def calculate_towers():
    # Get the input value and restrict it to the desired range
    clicked_rows = max(1, min(8, int(clicked_entry.get())))

    # Check if the input value is within the desired range
    if clicked_rows != int(clicked_entry.get()):
        answer_label.config(text="Probability: Error")
        return

    # Calculate the probability based on the selected mode and update the label
    if mode_selector.get() == "Easy":
        chance = 2/3
    elif mode_selector.get() == "Normal":
        chance = 1/2
    elif mode_selector.get() == "Hard":
        chance = 1/3
    
    probability = chance ** clicked_rows
    
    answer_label.config(text=f"Probability: {probability*100:.2f}%")
    
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

# Create the dropdown
calculator_selector = ttk.Combobox(root, values=["Mines", "Towers"], state="readonly")
calculator_selector.current(0) # Set the default option to Minesweeper
calculator_selector.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

# Create the entry widgets
incorrect_label = ttk.Label(root, text="Mines")
incorrect_label.grid(row=1, column=0, padx=5, pady=5)
incorrect_entry = ttk.Entry(root, width=10)
incorrect_entry.grid(row=1, column=1, padx=5, pady=5)

mode_selector = ttk.Combobox(root, values=["Easy", "Normal", "Hard"], state="readonly", width=7)
mode_selector.current(0) # Set the default option to Easy

clicked_label = ttk.Label(root, text="Tiles")
clicked_label.grid(row=2, column=0, padx=5, pady=5)
clicked_entry = ttk.Entry(root, width=10)
clicked_entry.grid(row=2, column=1, padx=5, pady=5)

# Create the button
calculate_button = ttk.Button(root, text="Calculate", command=calculate_mines)
calculate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="sew") # center button

# Create the label to display the result
answer_label = ttk.Label(root, text="")
answer_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Create the function to switch between the Minesweeper and Towers calculators
calculator_selector.bind("<<ComboboxSelected>>", lambda event: switch_calculator())

root.mainloop()
