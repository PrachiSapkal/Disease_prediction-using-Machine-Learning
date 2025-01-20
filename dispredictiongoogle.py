import pandas as pd
import tkinter as tk
from tkinter import ttk

data = pd.read_excel("diseaseRemedies.xlsx")
diseases = data["Disease"].tolist()
remedies = data["Remedies"].tolist()

def search_remedy():
    searched_disease = disease_entry.get().lower()
    if searched_disease in diseases:
        index = diseases.index(searched_disease)
        remedy_label.config(text=remedies[index])
    else:
        remedy_label.config(text="Disease not found.")


root = tk.Tk()
root.title("Disease Remedy Lookup")

# Label and entry for disease search
disease_label = tk.Label(root, text="Enter Disease:")
disease_label.pack()
disease_entry = tk.Entry(root)
disease_entry.pack()

# Result label for displaying remedy
remedy_label = tk.Label(root, text="")
remedy_label.pack()

# Search button
search_button = tk.Button(root, text="Search Remedy", command=search_remedy)
search_button.pack()

root.mainloop()


