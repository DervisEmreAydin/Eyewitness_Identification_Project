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

def getMostSimilarImages(target):
    model = VGGFace.loadModel()
    resp = DeepFace.analyze(target)

    print(resp["age"])
    print(resp["gender"])
    print(resp["dominant_race"])
    print(resp["dominant_emotion"])
    df = DeepFace.find(img_path=target, db_path='FaceDataset',
                   model_name='VGG-Face', model=model)
    print("Deepface find bitti")

    AllSmilarImages = df['identity'].values.tolist()

    Analiz = DeepFace.analyze(AllSmilarImages[-15:])
    list(Analiz)

    Analiz.get('instance_1')

    Analiz1 = Analiz.get('instance_1')
    Analiz2 = Analiz.get('instance_2')
    Analiz3 = Analiz.get('instance_3')
    Analiz4 = Analiz.get('instance_4')
    Analiz5 = Analiz.get('instance_5')
    Analiz6 = Analiz.get('instance_6')
    Analiz7 = Analiz.get('instance_7')
    Analiz8 = Analiz.get('instance_8')
    Analiz9 = Analiz.get('instance_9')
    Analiz10 = Analiz.get('instance_10')
    Analiz11 = Analiz.get('instance_11')
    Analiz12 = Analiz.get('instance_12')
    Analiz13 = Analiz.get('instance_13')
    Analiz14 = Analiz.get('instance_14')
    Analiz15 = Analiz.get('instance_15')


    Racelist = [Analiz1['dominant_race'],
               Analiz2['dominant_race'],
               Analiz3['dominant_race'],
               Analiz4['dominant_race'],
               Analiz5['dominant_race'],
               Analiz6['dominant_race'],
                Analiz7['dominant_race'],
                Analiz8['dominant_race'],
                Analiz9['dominant_race'],
                Analiz10['dominant_race'],
                Analiz11['dominant_race'],
                Analiz12['dominant_race'],
                Analiz13['dominant_race'],
                Analiz14['dominant_race'],
                Analiz15['dominant_race'],
                ]

    print(Racelist)

    combine = zip(AllSmilarImages[-15:], Racelist)
    combinelist = list(combine)
    print(combinelist)

    sonliste = []  # hedef kişinin dominant ırkı ile eşleşen kişilerin dahil olduğu liste
    for a, b in combinelist:
        if b == resp["dominant_race"]:
            sonliste += [a]
    print(sonliste)
    ilk_uc = sonliste[-10:]
    #ilk_uc.append(target)
    random.shuffle(ilk_uc)
    print("Bitti")
    return ilk_uc
