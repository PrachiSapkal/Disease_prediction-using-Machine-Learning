# from tkinter import *
# from tkinter import messagebox
# from tkinter import Tk
# import numpy as np
# import pandas as pd
# #changes
# from tkinter import Tk

# def search_remedy():
#     disease = prectictedDisease.strip().title()

#     # Use str.contains for a case-insensitive search
#     mask = gf['Disease'].str.contains(f'\\b{disease}\\b', case=False, regex=True)
    
#     if mask.any():
#         remedy = gf.loc[mask, 'Remedies'].values[0]
#         result_label.config(text=f"Remedies for {disease} are : {remedy}",font=("Elephant", 20))
#     else:
#         result_label.config(text=f"Consult With Doctor for {disease}")
        



# root = Tk()
# # Set background image
# background_image = PhotoImage(file="diseaseprediction.png")  # Replace with your image path
# background_label = Label(root, image=background_image)
# background_label.place(relwidth=1, relheight=1)

# root.title(" Disease Prediction and Remedies From Symptoms")
# root.configure()

# Symptom1 = StringVar()
# Symptom1.set(None)
# Symptom2 = StringVar()
# Symptom2.set(None)
# Symptom3 = StringVar()
# Symptom3.set(None)
# Symptom4 = StringVar()
# Symptom4.set(None)
# Symptom5 = StringVar()
# Symptom5.set(None)

# # w2 = Label(root, justify=LEFT, text=" Disease Prediction From Symptoms ")
# # w2.config(font=("Elephant", 30))
# # w2.grid(row=1, column=0, columnspan=2, padx=100)

# # Change color schemes
# root.config(bg="lightblue")  # Set the background color of the root window
# w2 = Label(root, justify=LEFT, text=" Disease Prediction and Remedies From Symptoms ", bg="lightblue")  # Set background color
# w2.config(font=("Monospace", 30))
# w2.grid(row=1, column=0, columnspan=2, padx=100)

# NameLb1 = Label(root, text="Enter Your Symptoms : ")
# NameLb1.config(font=("Elephant", 20))
# NameLb1.grid(row=5, column=1, pady=0,  sticky=W)

# S1Lb = Label(root,  text="Symptom 1")
# S1Lb.config(font=("Elephant", 15))
# S1Lb.grid(row=7, column=1, pady=10 , sticky=W)
# S1Lb.config(background="lightyellow") #add color to the background

# S2Lb = Label(root,  text="Symptom 2")
# S2Lb.config(font=("Elephant", 15),background="lightyellow")
# S2Lb.grid(row=8, column=1, pady=10, sticky=W)

# S3Lb = Label(root,  text="Symptom 3")
# S3Lb.config(font=("Elephant", 15),background="lightyellow")
# S3Lb.grid(row=9, column=1, pady=10, sticky=W)

# S4Lb = Label(root,  text="Symptom 4")
# S4Lb.config(font=("Elephant", 15),background="lightyellow")
# S4Lb.grid(row=10, column=1, pady=10, sticky=W)

# S5Lb = Label(root,  text="Symptom 5")
# S5Lb.config(font=("Elephant", 15),background="lightyellow")
# S5Lb.grid(row=11, column=1, pady=10, sticky=W)

# lr = Button(root, text="Predict",height=2, width=20, command=Message)
# lr.config(font=("Elephant", 15),background="green")
# lr.grid(row=13, column=1,pady=20)



# OPTIONS = sorted(lr)
# # Create combobox widgets
# # S1En = ttk.Combobox(root, textvariable=Symptom1)
# # S1En.grid(row=7, column=2)
# # S1En['values'] = OPTIONS
# # S1En.bind("<Button-1>", lambda event: update_combobox(Symptom1, event))

# S1En = ttk.Combobox(root, textvariable=Symptom1)
# S1En.grid(row=7, column=2)
# S1En['values'] = OPTIONS
# S1En.bind("<Button-1>", lambda event: update_combobox(Symptom1, event))
# S1En.config(background="lightblue")  # Set background color



# S2En = ttk.Combobox(root, textvariable=Symptom2)
# S2En.grid(row=8, column=2)
# S2En['values'] = OPTIONS
# S2En.bind("<Button-1>", lambda event: update_combobox(Symptom2, event))

# S3En = ttk.Combobox(root, textvariable=Symptom3)
# S3En.grid(row=9, column=2)
# S3En['values'] = OPTIONS
# S3En.bind("<Button-1>", lambda event: update_combobox(Symptom3, event))

# S4En = ttk.Combobox(root, textvariable=Symptom4)
# S4En.grid(row=10, column=2)
# S4En['values'] = OPTIONS
# S4En.bind("<Button-1>", lambda event: update_combobox(Symptom4, event))

# S5En = ttk.Combobox(root, textvariable=Symptom5)
# S5En.grid(row=11, column=2)
# S5En['values'] = OPTIONS
# S5En.bind("<Button-1>", lambda event: update_combobox(Symptom5, event))

# # Function to update the list of symptoms for the combobox
# def update_combobox(symptom_var, event):
#     symptom_var.set('')
#     symptom_var.set(OPTIONS)

# # S1En = OptionMenu(root, Symptom1,*OPTIONS)
# # S1En.grid(row=7, column=2)

# # S2En = OptionMenu(root, Symptom2,*OPTIONS)
# # S2En.grid(row=8, column=2)

# # S3En = OptionMenu(root, Symptom3,*OPTIONS)
# # S3En.grid(row=9, column=2)

# # S4En = OptionMenu(root, Symptom4,*OPTIONS)
# # S4En.grid(row=10, column=2)

# # S5En = OptionMenu(root, Symptom5,*OPTIONS)
# # S5En.grid(row=11, column=2)
    
# #empty hidden
# NameLb = Label(root, text="press here >>> ")
# NameLb.config(font=("Elephant", 20))
# NameLb.grid(row=13, column=1, pady=10,  sticky=W)

# NameLb = Label(root, text="Remedies : ")
# NameLb.config(font=("Elephant", 15))
# NameLb.grid(row=18, column=1, pady=10,  sticky=W)

# t3 = Text(root, height=2, width=30)
# t3.config(font=("Elephant", 20))
# t3.grid(row=17, column=1 , padx=10)

# result_label = ttk.Label(root, text="")
# result_label.grid(row=20, column=0, pady=0)
# result_label.config(font=("Elephant", 15),background="lightblue")
# # t4 = Text(root, height=0, width=0)
# # t4.config(font=("Elephant", 20))
# # t4.grid(row=1, column=1 , padx=10)
# root.mainloop()



from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk  # For image handling

# Sample remedies dataset
import pandas as pd
gf = pd.DataFrame({
    'Disease': ['Cold', 'Fever', 'Diabetes'],
    'Remedies': ['Drink warm liquids, rest', 'Stay hydrated, take antipyretics', 'Maintain blood sugar levels, consult a doctor']
})

def search_remedy():
    disease = disease_entry.get().strip().title()
    mask = gf['Disease'].str.contains(f'\\b{disease}\\b', case=False, regex=True)
    if mask.any():
        remedy = gf.loc[mask, 'Remedies'].values[0]
        result_label.config(text=f"Remedies for {disease}: {remedy}")
    else:
        result_label.config(text=f"No remedy found. Consult a doctor for {disease}.")
        
def clear_inputs():
    symptom1.set("")
    symptom2.set("")
    symptom3.set("")
    disease_entry.delete(0, END)
    result_label.config(text="")

root = Tk()
root.title("Disease Prediction and Remedies")
root.geometry("800x600")

# Set background image
bg_image = Image.open("background.png")  # Replace with your image file
bg_photo = ImageTk.PhotoImage(bg_image.resize((800, 600)))
bg_label = Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# Frames
main_frame = Frame(root, bg="#f5f5f5", relief=RIDGE, bd=5)
main_frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=700, height=500)

# Title Label
title_label = Label(main_frame, text="Disease Prediction and Remedies", font=("Arial", 24, "bold"), bg="#f5f5f5", fg="blue")
title_label.pack(pady=20)

# Entry for Symptoms and Disease
symptom1 = StringVar()
symptom2 = StringVar()
symptom3 = StringVar()

Label(main_frame, text="Symptom 1:", font=("Arial", 14), bg="#f5f5f5").pack(anchor=W, padx=50)
symptom1_entry = ttk.Entry(main_frame, textvariable=symptom1, font=("Arial", 12))
symptom1_entry.pack(pady=5, padx=50, anchor=W, fill=X)

Label(main_frame, text="Symptom 2:", font=("Arial", 14), bg="#f5f5f5").pack(anchor=W, padx=50)
symptom2_entry = ttk.Entry(main_frame, textvariable=symptom2, font=("Arial", 12))
symptom2_entry.pack(pady=5, padx=50, anchor=W, fill=X)

Label(main_frame, text="Symptom 3:", font=("Arial", 14), bg="#f5f5f5").pack(anchor=W, padx=50)
symptom3_entry = ttk.Entry(main_frame, textvariable=symptom3, font=("Arial", 12))
symptom3_entry.pack(pady=5, padx=50, anchor=W, fill=X)

Label(main_frame, text="Disease Name:", font=("Arial", 14), bg="#f5f5f5").pack(anchor=W, padx=50)
disease_entry = ttk.Entry(main_frame, font=("Arial", 12))
disease_entry.pack(pady=5, padx=50, anchor=W, fill=X)

# Buttons
button_frame = Frame(main_frame, bg="#f5f5f5")
button_frame.pack(pady=20)

predict_button = Button(button_frame, text="Search Remedy", command=search_remedy, bg="green", fg="white", font=("Arial", 12), width=15)
predict_button.grid(row=0, column=0, padx=10)

clear_button = Button(button_frame, text="Clear", command=clear_inputs, bg="red", fg="white", font=("Arial", 12), width=15)
clear_button.grid(row=0, column=1, padx=10)

# Result Label
result_label = Label(main_frame, text="", font=("Arial", 14), bg="#f5f5f5", wraplength=600, fg="darkgreen")
result_label.pack(pady=20)

root.mainloop()
