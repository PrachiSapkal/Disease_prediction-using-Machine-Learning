
import pandas as pd
import tkinter as tk
from tkinter import ttk

# Load the data from the Excel file
excel_file = 'diseaseRemedies.xlsx'  # Change this to the path of your Excel file
gf = pd.read_excel(excel_file)

def search_remedy():
    disease = entry_disease.get().strip().title()

    # Use str.contains for a case-insensitive search
    mask = gf['Disease'].str.contains(f'\\b{disease}\\b', case=False, regex=True)
    
    if mask.any():
        remedy = gf.loc[mask, 'Remedies'].values[0]
        result_label.config(text=f"Remedies for {disease}: {remedy}")
    else:
        result_label.config(text=f"No information found for {disease}")

# Create the main window
window = tk.Tk()
window.title("Disease Remedies Search")

# Create and place widgets
label_disease = tk.Label(window, text="Enter Disease:")
label_disease.grid(row=0, column=0, padx=10, pady=10, sticky='e')

entry_disease = tk.Entry(window)
entry_disease.grid(row=0, column=1, padx=10, pady=10)

search_button = tk.Button(window, text="Search", command=search_remedy)
search_button.grid(row=0, column=2, padx=10, pady=10)

result_label = tk.Label(window, text="")
result_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Start the GUI event loop
window.mainloop()
