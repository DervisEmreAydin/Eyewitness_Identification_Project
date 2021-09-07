from deepface import DeepFace
import pandas as pd
from deepface.basemodels import VGGFace, OpenFace, Facenet, FbDeepFace
from deepface.commons import functions
import cv2
import matplotlib.pyplot as plt
import tkinter as tk
from PIL import Image, ImageTk
import random

model = VGGFace.loadModel()

target = 'C:\\Users\\UNKNOWN\\Desktop\\Python_Egitim-master\\deepface-master\\Target\\DC.jpg'
img = cv2.imread(target)
plt.imshow(img[:, :, ::-1])
plt.show()

resp = DeepFace.analyze(target)

print(resp["age"])
print(resp["gender"])
print(resp["dominant_race"])
print(resp["dominant_emotion"])

imgTarget = 'C:\\Users\\UNKNOWN\\PycharmProjects\\suspectRecognition\\Target';
imgPath = imgTarget + '\\S48.jpg'
df = DeepFace.find(img_path=imgPath, db_path= 'FaceDataset',
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

sonuc = list(filter(lambda zipped: zipped[1] == 'white', zip(product, Irklist)))
print(sonuc)

for a, b in birlesmislist:  # daminant ırkı "white" ile eşleşen kişilerin bastırılması
    if b == 'white':
        print(a)

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
# resim3=ImageTk.PhotoImage(Image.open(ilk_uc[2]))
resim4 = ImageTk.PhotoImage(
    Image.open('C:\\Users\\UNKNOWN\\Desktop\\Python_Egitim-master\\deepface-master\\Target\\DC.jpg'))

buton = tk.Button(form, image=resim1)
buton.pack(side=tk.LEFT)

buton2 = tk.Button(form, image=resim2)
buton2.pack(side=tk.LEFT)

# buton3=tk.Button(form,image=resim3)
# buton3.pack(side=tk.LEFT)

buton4 = tk.Button(form, image=resim4)
buton4.pack(side=tk.LEFT)

form.mainloop()

