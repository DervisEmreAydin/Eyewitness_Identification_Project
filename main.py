from deepface import DeepFace
import pandas as pd
from deepface.basemodels import VGGFace, OpenFace, Facenet, FbDeepFace
from deepface.commons import functions
import cv2
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import random
import conf
from screen import *


def handle_start_button():
    initialScreen.destroyWindow()
    import page1

initialScreen = Screen(conf.lineup_logo_initial)
initialWindow = initialScreen.getWindow()

# Set the labels and buttons on the initial window
label_program_description = Label(initialWindow, text=conf.program_description, bg='#343544').place(relx=0.5, rely=0.78,
                                                                                                    anchor='center')
label_version_info = Label(initialWindow, text=conf.version_info, bg='#343544').place(relx=0.80, rely=0.85, anchor='se')
button_start = Button(initialWindow, text=conf.start_button_text, command=lambda: handle_start_button()).place(relx=0.5,
                                                                                                               rely=0.82,
                                                                                                               anchor='center',
                                                                                                               height=30,
                                                                                                               width=70)
initialWindow.mainloop()
exit(0)

model = VGGFace.loadModel()

target = 'C:\\Users\\baris\\Desktop\\WIP\\Eyewitness_Identification_Project-main\\Eyewitness_Identification_Project-main\\Target\\S48.jpg'
img = cv2.imread(target)
plt.imshow(img[:, :, ::-1])
plt.show()

resp = DeepFace.analyze(target)

print(resp["age"])
print(resp["gender"])
print(resp["dominant_race"])
print(resp["dominant_emotion"])

imgTarget = 'C:\\Users\\baris\\Desktop\\WIP\\Eyewitness_Identification_Project-main\\Eyewitness_Identification_Project-main\\Target';
imgPath = imgTarget + '\\S48.jpg'
df = DeepFace.find(img_path=imgPath, db_path='FaceDataset',
                   model_name='VGG-Face', model=model)

df.head()

product = df['identity'].values.tolist()
print(product[0:10])

Analiz = DeepFace.analyze(product[0:10])

list(Analiz)

Analiz.get('instance_1')

Analiz1 = Analiz.get('instance_1')
Analiz2 = Analiz.get('instance_2')
Analiz3 = Analiz.get('instance_3')
Analiz4 = Analiz.get('instance_4')
Analiz5 = Analiz.get('instance_5')
Analiz6 = Analiz.get('instance_6')

Irklist = [Analiz1['dominant_race'],
           Analiz2['dominant_race'],
           Analiz3['dominant_race'],
           Analiz4['dominant_race'],
           Analiz5['dominant_race'],
           Analiz6['dominant_race']]

print(Irklist)

birlestir = zip(product, Irklist)
birlesmislist = list(birlestir)
print(birlesmislist)

sonliste = []  # hedef kişinin daminant ırkı ile eşleşen kişilerin dahil olduğu liste
for a, b in birlesmislist:
    if b == resp["dominant_race"]:
        sonliste += [a]
print(sonliste)

ilk_uc = sonliste[0:3]

random.shuffle(ilk_uc)
ilk_uc

form = tk.Tk()
random.shuffle(ilk_uc)  # Random sırala

resim1 = ImageTk.PhotoImage(Image.open(ilk_uc[0]))
resim2 = ImageTk.PhotoImage(Image.open(ilk_uc[1]))
resim3 = ImageTk.PhotoImage(Image.open(ilk_uc[2]))
resim4 = ImageTk.PhotoImage(
    Image.open(
        'C:\\Users\\baris\\Desktop\\WIP\\Eyewitness_Identification_Project-main\\Eyewitness_Identification_Project-main\\Target\\S48.jpg'))

buton = tk.Button(form, image=resim1)
buton.pack(side=tk.LEFT)

buton2 = tk.Button(form, image=resim2)
buton2.pack(side=tk.LEFT)

buton3 = tk.Button(form, image=resim3)
buton3.pack(side=tk.LEFT)

buton4 = tk.Button(form, image=resim4)
buton4.pack(side=tk.LEFT)

form.mainloop()
