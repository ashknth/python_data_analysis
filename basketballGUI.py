import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt

# Assuming you have a dataset to work with
file_path = "Chapter_11/nba.csv"
data = pd.read_csv(file_path)

# Initialize the main window
root = tk.Tk()
root.title("Basketball Statistics Analyzer")

# Function to display the selected statistic
def display_stat():
    selected_column = selected_stat.get()
    # Clear previous plot
    plt.clf()
    # Plot the selected data column
    data[selected_column].plot(kind='bar', title=f"{selected_column} Data")
    plt.xlabel('Player')
    plt.ylabel(selected_column)
    plt.show()

# Create a label
ttk.Label(root, text="Select a statistic to analyze:").grid(column=0, row=0, padx=10, pady=10)

# Variable to hold the selected option
selected_stat = tk.StringVar()

# Create radio buttons for the different columns
stat_options = ['FG', '3P', 'FT', 'PTS', '3P%']  # Add more columns as needed
for idx, stat in enumerate(stat_options):
    tk.Radiobutton(root, text=stat, variable=selected_stat, value=stat).grid(column=0, row=idx+1, sticky=tk.W)

# Add a button to trigger the display
analyze_button = ttk.Button(root, text="Analyze", command=display_stat)
analyze_button.grid(column=0, row=len(stat_options) + 2, padx=10, pady=10)

# Run the GUI main loop
root.mainloop()
