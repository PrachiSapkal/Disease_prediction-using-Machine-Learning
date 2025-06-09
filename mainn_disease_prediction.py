from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import numpy as np
import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
#changes
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
from PIL import Image, ImageTk
import json
user_email = None
user_token = None  # JWT Token for authenticated requests
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "medicareai.analytics@gmail.com"
EMAIL_PASSWORD = "eafw uuxr mfis rujl"
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
excel_file = 'diseaseRemedies.xlsx'  # path of Excel file
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
tr = tr.infer_objects(copy=False)

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
df = df.infer_objects(copy=False)

X= df[l1]
y = df[["prognosis"]]
np.ravel(y)

def send_email(subject, body):
    try:
        # Set up the server
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        sender_email = 'medicareai.analytics@gmail.com'
        sender_password = 'eafw uuxr mfis rujl'
        global user_email
        # Create the message
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = "medicareai.analytics@gmail.com"
        msg['To'] = user_email

        # Send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure connection
            server.login(sender_email, sender_password)  # Login
            server.sendmail(sender_email, user_email, msg.as_string())  # Send email

       
    except Exception as e:
        print(f"Failed to send email: {e}")


# Login/Register API interactions
root = tk.Tk()
root.title("Disease Prediction System")
root.geometry("1024x768")

background_image = tk.PhotoImage(file="image.png")

def set_background():
    bg_label = tk.Label(root, image=background_image)
    bg_label.image = background_image
    bg_label.place(relwidth=1, relheight=1)


def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()
    set_background()

def show_logo():
    logo_image = Image.open("loggo.png")
    logo_image = logo_image.resize((160, 160), Image.Resampling.LANCZOS)
    logo_photo = ImageTk.PhotoImage(logo_image)
    logo_label = tk.Label(root, image=logo_photo, bg="#FEE7E0", borderwidth=0)
    logo_label.image = logo_photo  # Keep reference to prevent garbage collection
    logo_label.place(x=1384, y=10)

def login():
    global user_email, user_token
    email = email_entry.get()
    password = password_entry.get()
    response = requests.post("http://localhost:7000/api/farmer-login", json={"email": email, "password": password})
    if response.status_code == 200:
        data = response.json()
        user_email = data['user']['email']
        user_token = data['token']
        messagebox.showinfo("Login Successful", "Welcome to MediCareAi!")
        show_prediction_screen()
    else:
        messagebox.showerror("Error", "Invalid credentials.")

def register():
    email = email_entry.get()
    password = password_entry.get()
    phone = phone_entry.get()
    name = name_entry.get()
    response = requests.post("http://localhost:7000/api/farmer-register", json={"email": email, "password": password, "phone": phone, "name": name})
    if response.status_code == 200:
        messagebox.showinfo("Success", "Registration completed.")
    else:
        messagebox.showerror("Error", "Email already exists.")

    
def show_login_screen():
    clear_screen()
    show_logo()

    # Main container for left (login) and right (intro)
    main_frame = tk.Frame(root, bg="#EDBBAF", bd=2, relief="solid")
    main_frame.pack(expand=True, pady=100)

    #Left Frame: Login Form 
    login_frame = tk.Frame(main_frame, bg="#EDBBAF")
    login_frame.pack(side="left", padx=50)

    tk.Label(login_frame, text="Email:", font=("Elephant", 18), bg="#EDBBAF").grid(row=0, column=0, sticky='e', padx=10, pady=10)
    tk.Label(login_frame, text="Password:", font=("Elephant", 18), bg="#EDBBAF").grid(row=1, column=0, sticky='e', padx=10, pady=10)

    global email_entry, password_entry
    email_entry = tk.Entry(login_frame, font=("Elephant", 16), width=30)
    password_entry = tk.Entry(login_frame, font=("Elephant", 16), show="*", width=30)
    email_entry.grid(row=0, column=1, padx=10, pady=10)
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    tk.Button(login_frame, text="Login", font=("Elephant", 16), bg="#B5313C", fg="white", command=login).grid(row=2, column=0, columnspan=2, pady=20)
    tk.Button(login_frame, text="Register", font=("Elephant", 16), bg="#B5313C", fg="white", command=show_register_screen).grid(row=3, column=0, columnspan=2, pady=(5, 10))

    # Right Frame: Introduction of our project
    intro_frame = tk.Frame(main_frame, bg="#FFE4DC", bd=3, relief="flat")
    intro_frame.pack(side="right")

    intro_text = (
        "🔍 Welcome to the Disease prediction system!\n\n"
        "💡 An intelligent health assistant that helps you identify possible illnesses based on your symptoms.\n\n"
        "🧠 Using machine learning models trained on medical data, the system delivers fast and accurate predictions.\n\n"
        "💊 You'll also receive suggested remedies for quick help along with an e-mail :)\n\n"
        "🔐 Please login or register to begin!"
    )

    intro_label = tk.Label(intro_frame, text=intro_text, justify="left", font=("Arial", 13, "bold"), bg="#FFE4DC", fg="#B5313C", wraplength=350)
    intro_label.pack(padx=20, pady=20)

def show_register_screen():
    clear_screen()
    show_logo()
    frame = tk.Frame(root, bg="#EDBBAF")
    frame.pack(pady=80)

    def validate_phone(P):
        return (P.isdigit() or P == "") and len(P) <= 10

    global name_entry, email_entry, password_entry, phone_entry

    # Labels
    tk.Label(frame, text="Name:", font=("Elephant", 18), bg="#EDBBAF").grid(row=0, column=0, sticky='e', padx=10, pady=10)
    tk.Label(frame, text="Email:", font=("Elephant", 18), bg="#EDBBAF").grid(row=1, column=0, sticky='e', padx=10, pady=10)
    tk.Label(frame, text="Password:", font=("Elephant", 18), bg="#EDBBAF").grid(row=2, column=0, sticky='e', padx=10, pady=10)
    tk.Label(frame, text="Phone:", font=("Elephant", 18), bg="#EDBBAF").grid(row=3, column=0, sticky='e', padx=10, pady=10)

    # Entry Fields
    name_entry = tk.Entry(frame, font=("Elephant", 16), width=30)
    email_entry = tk.Entry(frame, font=("Elephant", 16), width=30)
    password_entry = tk.Entry(frame, font=("Elephant", 16), show="*", width=30)
    vcmd = root.register(validate_phone)
    phone_entry = tk.Entry(frame, font=("Elephant", 16), width=30, validate="key", validatecommand=(vcmd, "%P"))

    name_entry.grid(row=0, column=1, padx=10, pady=10)
    email_entry.grid(row=1, column=1, padx=10, pady=10)
    password_entry.grid(row=2, column=1, padx=10, pady=10)
    phone_entry.grid(row=3, column=1, padx=10, pady=10)

    # Buttons
    tk.Button(frame, text="Register", font=("Elephant", 16), bg="#B5313C", fg="white", command=register)\
        .grid(row=4, column=0, columnspan=2, pady=20)

    tk.Button(frame, text="Go to Login", font=("Elephant", 12), bg="#B5313C", fg="white", command=show_login_screen)\
        .grid(row=5, column=0, columnspan=2, pady=(5, 10))

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
        # print(accuracy_score(y_test, y_pred))
        #print(accuracy_score(y_test, y_pred, normalize=False))
        # print("Accuracy : ",accuracy_score(y_test, y_pred)*100)
        print("Accuracy Score : ",accuracy_score(y_test, y_pred, normalize=False))
        global l2
        l2 = [0] * len(l1)


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
        # print(accuracy_score(y_test, y_pred))
        #print(accuracy_score(y_test, y_pred, normalize=False))
        print("Accuracy : ",accuracy_score(y_test, y_pred)*100)
        #print("Accuracy Score : ",accuracy_score(y_test, y_pred, normalize=False))

        global l2
        l2 = [0] * len(l1)


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
- {Symptom3.get()}
- {Symptom4.get()}
- {Symptom5.get()}

To help manage your condition, you can try the following remedies:
- {remedy}

Please consult with a healthcare professional for further advice. Hope you Get well soon!!

Best regards,
Your Health Assistant
MediCareAi
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
- {Symptom3.get()}
- {Symptom4.get()}
- {Symptom5.get()}

Please consult with a healthcare professional for further advice. Hope you Get well soon!!

Best regards,
Your Health Assistant
MediCareAi
"""
            send_email("Your Prediction Results are ready",body)

    # Clear the window (for switching screens)
    for widget in root.winfo_children():
        widget.destroy()

    frame = tk.Frame(root, bg="#EDBBAF")
    frame.pack(fill="both", expand=True)

    background_image = tk.PhotoImage(file="image.png")
    background_label = tk.Label(frame, image=background_image)
    background_label.place(relwidth=1, relheight=1)
    frame.background_image = background_image 
    show_logo()
    
 
 # Center-align all widgets by configuring columns
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)
    frame.grid_columnconfigure(2, weight=1)

    w2 = tk.Label(frame, text="Predictive Analytics and Diagnosis for Diseases", font=("Monospace", 30), bg="#B5313C", fg="white")
    w2.grid(row=0, column=0, columnspan=3, padx=10, pady=(20, 10), sticky="n") 

    tk.Label(frame, text="Enter Your Symptoms:", font=("Elephant", 20), bg="#EDBBAF")\
        .grid(row=1, column=0, columnspan=3, pady=(10, 20), sticky="n")  

    labels = ["Symptom 1", "Symptom 2", "Symptom 3", "Symptom 4", "Symptom 5"]
    variables = []

    for i, text in enumerate(labels):
        tk.Label(frame, text=text, font=("Elephant", 15), bg="#EDBBAF")\
            .grid(row=2+i, column=1, pady=(10, 10), padx=(20, 0), sticky="w") 

    OPTIONS = sorted(l1)
    Symptom1, Symptom2, Symptom3, Symptom4, Symptom5 = StringVar(), StringVar(), StringVar(), StringVar(), StringVar()
    for sym in [Symptom1, Symptom2, Symptom3, Symptom4, Symptom5]:
        sym.set("None")
        variables.append(sym)

    def update_combobox(symptom_var, event):
        symptom_var.set('')
        symptom_var.set(OPTIONS)

    for i, var in enumerate(variables):
        cb = ttk.Combobox(frame, textvariable=var, values=OPTIONS)
        cb.grid(row=2+i, column=2, pady=(10, 10), padx=5, sticky="w")  # increased pady
        cb.bind("<Button-1>", lambda event, v=var: update_combobox(v, event))

    
    Symptom1.set("None")
    Symptom2.set("None")
    Symptom3.set("None")
    Symptom4.set("None")
    Symptom5.set("None")


    tk.Button(frame, text="Predict", font=("Elephant", 15), bg="#B5313C", fg="white", height=2, width=20, command=message)\
        .grid(row=7, column=0, columnspan=3, pady=(30, 10), sticky="n") 

    t3 = tk.Text(frame, height=2, width=30, font=("Elephant", 20), bg="#EDBBAF", bd=2, relief="solid")
    t3.grid(row=8, column=0, columnspan=3, sticky="n", pady=(20, 10)) 

    result_label = tk.Label(frame, text="", font=("Elephant", 15), bg="#EDBBAF", wraplength=600, justify="center")
    result_label.grid(row=9, column=0, columnspan=3, pady=(20, 30), sticky="n")

    logout_button = tk.Button(frame, text="Logout", font=("Elephant", 16), bg="#B5313C", fg="white", height=2, width=10, command=show_login_screen)
    logout_button.place(relx=0.95, rely=0.95, anchor="se")
    refresh_button = tk.Button(frame, text="Refresh", font=("Elephant", 16), bg="#B5313C", fg="white", height=2, width=10, command=show_prediction_screen)
    refresh_button.place(relx=0.95, rely=0.85, anchor="se")

      
# Call the login screen when the application starts
show_login_screen()
root.mainloop()