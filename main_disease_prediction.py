from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import numpy as np
import pandas as pd
#changes
from tkinter import ttk
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
import json
user_email = None
user_token = None  # JWT Token for authenticated requests
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "pradyumnacharate1@gmail.com",
EMAIL_PASSWORD = "gaohijayvruqnccn"
l1=['itching','skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering','chills','joint_pain',
    'stomach_pain','acidity','ulcers_on_tongue','muscle_wasting','vomiting','burning_micturition','spotting_ urination','fatigue',
    'weight_gain','anxiety','cold_hands_and_feets','mood_swings','weight_loss','restlessness','lethargy','patches_in_throat',
    'irregular_sugar_level','cough','high_fever','sunken_eyes','breathlessness','sweating','dehydration','indigestion',
    'headache','yellowish_skin','dark_urine','nausea','loss_of_appetite','pain_behind_the_eyes','back_pain','constipation',
    'abdominal_pain','diarrhoea','mild_fever','yellow_urine','yellowing_of_eyes','acute_liver_failure','fluid_overload',
    'swelling_of_stomach','swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
    'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs','fast_heart_rate',
    'pain_during_bowel_movements','pain_in_anal_region','bloody_stool','irritation_in_anus','neck_pain','dizziness','cramps',
    'bruising','obesity','swollen_legs','swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
    'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips','slurred_speech','knee_pain','hip_joint_pain',
    'muscle_weakness','stiff_neck','swelling_joints','movement_stiffness','spinning_movements','loss_of_balance','unsteadiness','weakness_of_one_body_side',
    'loss_of_smell','bladder_discomfort','foul_smell_of urine','continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
    'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain','abnormal_menstruation','dischromic _patches',
    'watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum','rusty_sputum','lack_of_concentration','visual_disturbances',
    'receiving_blood_transfusion','receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen','history_of_alcohol_consumption',
    'fluid_overload','blood_in_sputum','prominent_veins_on_calf','palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
    'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose','yellow_crust_ooze']

disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
        'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
        ' Migraine','Cervical spondylosis',
        'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
'Impetigo']

l2=[]
for x in range(0,len(l1)):
    l2.append(0)

# Load the data from the Excel file
excel_file = 'diseaseRemedies.xlsx'  # Change this to the path of your Excel file
gf = pd.read_excel(excel_file)

# TESTING DATA
tr=pd.read_csv("Testing.csv")
tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

X_test= tr[l1]
y_test = tr[["prognosis"]]
np.ravel(y_test)
prectictedDisease=""
# TRAINING DATA
df=pd.read_csv("Training.csv")

df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

X= df[l1]

y = df[["prognosis"]]
np.ravel(y)
def send_email(subject, body):
    try:
        # Set up the server
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        sender_email = 'pradyumnacharate1@gmail.com'
        sender_password = ''
        
        # Create the message
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = "pradyumnacharate1@gmail.com"
        msg['To'] = user_email

        # Send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure connection
            server.login(sender_email, sender_password)  # Login
            server.sendmail(sender_email, sender_email, msg.as_string())  # Send email

       
    except Exception as e:
        print(f"Failed to send email: {e}")

# Login/Register API interactions
def login():
    global user_email, user_token
    email = email_entry.get()
    password = password_entry.get()
    response = requests.post("http://localhost:7000/api/farmer-login", json={"email": email, "password": password})
    if response.status_code == 200:
        data = response.json()
        print(data)
        user_email = str(data['user']['email'])
        user_token = data['token']
        messagebox.showinfo("Login Successful", "Welcome back!")
        show_prediction_screen()
    else:
        messagebox.showerror("Error", "Invalid credentials.")

def register():
    email = email_entry.get()
    password = password_entry.get()
    response = requests.post("http://localhost:7000/api/farmer-register", json={"email": email, "password": password})
    if response.status_code == 200:
        messagebox.showinfo("Success", "Registration completed.")
    else:
        messagebox.showerror("Error", "Registration failed.")

        



root = Tk()
def show_login_screen():
    # Clear all widgets and reset to login screen
    for widget in root.winfo_children():
        widget.destroy()

    # Set background image
    background_image = tk.PhotoImage(file="ssnewbackground.png")
    background_label = tk.Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)
    
    # Add login screen components
    tk.Label(root, text="Email:", font=("Elephant", 20), bg="lightblue").grid(row=0, column=0, padx=10, pady=10)
    tk.Label(root, text="Password:", font=("Elephant", 20), bg="lightblue").grid(row=1, column=0, padx=10, pady=10)

    global email_entry, password_entry
    email_entry = tk.Entry(root, font=("Elephant", 20), width=30)
    password_entry = tk.Entry(root, font=("Elephant", 20), show="*", width=30)
    email_entry.grid(row=0, column=1, padx=10, pady=10)
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    # Add login and register buttons
    tk.Button(root, text="Login", font=("Elephant", 20), bg="green", command=login).grid(row=2, column=0, padx=10, pady=20)
    tk.Button(root, text="Register", font=("Elephant", 20), bg="blue", command=register).grid(row=2, column=1, padx=10, pady=20)

    root.mainloop()

# Set background image
def show_prediction_screen():
    def message():
        if (Symptom1.get() == "None" and  Symptom2.get() == "None" and Symptom3.get() == "None" and Symptom4.get() == "None" and Symptom5.get() == "None"):
            messagebox.showinfo("OOPS!!", "ENTER  SYMPTOMS PLEASE")
        else :
            RF_classifier()

    def RF_classifier():
        from sklearn.ensemble import RandomForestClassifier
        clf = RandomForestClassifier(n_estimators=250, random_state=42)
        clf.fit(X, np.ravel(y))
        from sklearn.metrics import accuracy_score
        y_pred = clf.predict(X_test)
        print(accuracy_score(y_test, y_pred))
        #print(accuracy_score(y_test, y_pred, normalize=False))
        print("Accuracy : ",accuracy_score(y_test, y_pred)*100)
        #print("Accuracy Score : ",accuracy_score(y_test, y_pred, normalize=False))

        psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

        for k in range(0,len(l1)):
            for z in psymptoms:
                if(z==l1[k]):
                    l2[k]=1

        inputtest = [l2]
        predict = clf.predict(inputtest)
        predicted=predict[0]

        h='no'
        for a in range(0,len(disease)):
            if(disease[predicted] == disease[a]):
                h='yes'
                break

        if (h=='yes'):
            t3.delete("1.0", END)
            t3.insert(END, disease[a])
            global prectictedDisease
            prectictedDisease=disease[a]
            search_remedy()
        else:
            t3.delete("1.0", END)
            t3.insert(END, "No Disease")

    def NaiveBayes():
        from sklearn.naive_bayes import MultinomialNB
        gnb = MultinomialNB()
        gnb=gnb.fit(X,np.ravel(y))
        y_pred = gnb.predict(X_test)
        from sklearn.metrics import accuracy_score
        print(accuracy_score(y_test, y_pred))
        #print(accuracy_score(y_test, y_pred, normalize=False))
        print("Accuracy : ",accuracy_score(y_test, y_pred)*100)
        #print("Accuracy Score : ",accuracy_score(y_test, y_pred, normalize=False))

        psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

        for k in range(0,len(l1)):
            for z in psymptoms:
                if(z==l1[k]):
                    l2[k]=1

        inputtest = [l2]
        predict = gnb.predict(inputtest)
        predicted=predict[0]

        h='no'
        for a in range(0,len(disease)):
            if(disease[predicted] == disease[a]):
                h='yes'
                break

        if (h=='yes'):
            t3.delete("1.0", END)
            t3.insert(END, disease[a])
            global prectictedDisease
            prectictedDisease=disease[a]
            search_remedy()
        else:
            t3.delete("1.0", END)
            t3.insert(END, "No Disease")

    # search remedies function
    def search_remedy():
        disease = prectictedDisease.strip().title()

        # Use str.contains for a case-insensitive search
        mask = gf['Disease'].str.contains(f'\\b{disease}\\b', case=False, regex=True)
        
        if mask.any():
            remedy = gf.loc[mask, 'Remedies'].values[0]
            result_label.config(text=f"Remedies for {disease} are : {remedy}",font=("Elephant", 20))
            body = f"""
Hello,

You have been diagnosed with the disease: {disease}.
Here are the symptoms you are experiencing:
- {Symptom1.get()}
- {Symptom2.get()}

To help manage your condition, you can try the following remedies:
- {remedy}

Please consult with a healthcare professional for further advice.

Best regards,
Your Health Assistant
"""
            send_email("Your Prediction Results are ready",body)
        else:
            result_label.config(text=f"Consult With Doctor for {disease}")
            body = f"""
Hello,

You have been diagnosed with the disease: {disease}.
Here are the symptoms you are experiencing:
- {Symptom1.get()}
- {Symptom2.get()}

Please consult with a healthcare professional for further advice.

Best regards,
Your Health Assistant
"""
            send_email("Your Prediction Results are ready",body)
    # Clear the window (for switching screens)
    for widget in root.winfo_children():
        widget.destroy()
    background_image = tk.PhotoImage(file="ssnewbackground.png")
    background_label = tk.Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)
 
 

    root.title(" Disease Prediction and Remedies From Symptoms")
    root.configure()
 

    Symptom1 = StringVar()
    Symptom1.set(None)
    Symptom2 = StringVar()
    Symptom2.set(None)
    Symptom3 = StringVar()
    Symptom3.set(None)
    Symptom4 = StringVar()
    Symptom4.set(None)
    Symptom5 = StringVar()
    Symptom5.set(None)

    # w2 = Label(root, justify=LEFT, text=" Disease Prediction From Symptoms ")
    # w2.config(font=("Elephant", 30))
    # w2.grid(row=1, column=0, columnspan=2, padx=100)

    # Change color schemes
    root.config(bg="lightblue")  # Set the background color of the root window
    w2 = Label(root, justify=LEFT, text=" Disease Prediction and Remedies From Symptoms ", bg="lightblue")  # Set background color
    w2.config(font=("Monospace", 30))
    w2.grid(row=1, column=0, columnspan=2, padx=100)

    NameLb1 = Label(root, text="Enter Your Symptoms : ")
    NameLb1.config(font=("Elephant", 20))
    NameLb1.grid(row=5, column=1, pady=0,  sticky=W)

    S1Lb = Label(root,  text="Symptom 1")
    S1Lb.config(font=("Elephant", 15))
    S1Lb.grid(row=7, column=1, pady=10 , sticky=W)
    S1Lb.config(background="lightyellow") #add color to the background

    S2Lb = Label(root,  text="Symptom 2")
    S2Lb.config(font=("Elephant", 15),background="lightyellow")
    S2Lb.grid(row=8, column=1, pady=10, sticky=W)

    S3Lb = Label(root,  text="Symptom 3")
    S3Lb.config(font=("Elephant", 15),background="lightyellow")
    S3Lb.grid(row=9, column=1, pady=10, sticky=W)

    S4Lb = Label(root,  text="Symptom 4")
    S4Lb.config(font=("Elephant", 15),background="lightyellow")
    S4Lb.grid(row=10, column=1, pady=10, sticky=W)

    S5Lb = Label(root,  text="Symptom 5")
    S5Lb.config(font=("Elephant", 15),background="lightyellow")
    S5Lb.grid(row=11, column=1, pady=10, sticky=W)

    lr = Button(root, text="Predict",height=2, width=20, command=message)
    lr.config(font=("Elephant", 15),background="green")
    lr.grid(row=13, column=1,pady=20)



    OPTIONS = sorted(l1)
    # Create combobox widgets
    # S1En = ttk.Combobox(root, textvariable=Symptom1)
    # S1En.grid(row=7, column=2)
    # S1En['values'] = OPTIONS
    # S1En.bind("<Button-1>", lambda event: update_combobox(Symptom1, event))

    S1En = ttk.Combobox(root, textvariable=Symptom1)
    S1En.grid(row=7, column=2)
    S1En['values'] = OPTIONS
    S1En.bind("<Button-1>", lambda event: update_combobox(Symptom1, event))
    S1En.config(background="lightblue")  # Set background color



    S2En = ttk.Combobox(root, textvariable=Symptom2)
    S2En.grid(row=8, column=2)
    S2En['values'] = OPTIONS
    S2En.bind("<Button-1>", lambda event: update_combobox(Symptom2, event))

    S3En = ttk.Combobox(root, textvariable=Symptom3)
    S3En.grid(row=9, column=2)
    S3En['values'] = OPTIONS
    S3En.bind("<Button-1>", lambda event: update_combobox(Symptom3, event))

    S4En = ttk.Combobox(root, textvariable=Symptom4)
    S4En.grid(row=10, column=2)
    S4En['values'] = OPTIONS
    S4En.bind("<Button-1>", lambda event: update_combobox(Symptom4, event))

    S5En = ttk.Combobox(root, textvariable=Symptom5)
    S5En.grid(row=11, column=2)
    S5En['values'] = OPTIONS
    S5En.bind("<Button-1>", lambda event: update_combobox(Symptom5, event))

    # Function to update the list of symptoms for the combobox
    def update_combobox(symptom_var, event):
        symptom_var.set('')
        symptom_var.set(OPTIONS)

    # S1En = OptionMenu(root, Symptom1,*OPTIONS)
    # S1En.grid(row=7, column=2)

    # S2En = OptionMenu(root, Symptom2,*OPTIONS)
    # S2En.grid(row=8, column=2)

    # S3En = OptionMenu(root, Symptom3,*OPTIONS)
    # S3En.grid(row=9, column=2)

    # S4En = OptionMenu(root, Symptom4,*OPTIONS)
    # S4En.grid(row=10, column=2)

    # S5En = OptionMenu(root, Symptom5,*OPTIONS)
    # S5En.grid(row=11, column=2)
        
    #empty hidden
    NameLb = Label(root, text="press here >>> ")
    NameLb.config(font=("Elephant", 20))
    NameLb.grid(row=13, column=1, pady=10,  sticky=W)

    NameLb = Label(root, text="Remedies : ")
    NameLb.config(font=("Elephant", 15))
    NameLb.grid(row=18, column=1, pady=10,  sticky=W)

    t3 = Text(root, height=2, width=30)
    t3.config(font=("Elephant", 20))
    t3.grid(row=17, column=1 , padx=10)

    result_label = ttk.Label(root, text="")
    result_label.grid(row=20, column=0, pady=0)
    result_label.config(font=("Elephant", 15),background="lightblue")
# Call the login screen when the application starts
show_login_screen()
