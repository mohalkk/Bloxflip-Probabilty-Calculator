import tkinter as tk
from tkinter import ttk

def calculate():
    incorrect_squares = int(incorrect_entry.get())
    safe_squares = 25 - incorrect_squares
    clicked_squares = int(clicked_entry.get())
    
    accuracy = safe_squares / 25 
    accuracy_display = safe_squares / 25 * 100
    probability = accuracy ** clicked_squares * 100
    
    answer_label.config(text=f"Accuracy: {accuracy_display:.2f}%\nProbability: {probability:.2f}%")

root = tk.Tk()
root.title("Mines Probability Calculator v1.0 - Mohalk")
root.geometry("100x150")

# Create the entry widgets
incorrect_label = ttk.Label(root, text="Mines")
incorrect_label.grid(row=0, column=0, padx=5, pady=5)
incorrect_entry = ttk.Entry(root, width=10)
incorrect_entry.grid(row=0, column=1, padx=5, pady=5)

clicked_label = ttk.Label(root, text="Tiles")
clicked_label.grid(row=1, column=0, padx=5, pady=5)
clicked_entry = ttk.Entry(root, width=10)
clicked_entry.grid(row=1, column=1, padx=5, pady=5)

# Create the button
calculate_button = ttk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="sew") # center button

# Create the label to display the result
answer_label = ttk.Label(root, text="")
answer_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
