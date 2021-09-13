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
    df.head()
    product = df['identity'].values.tolist()
    #print(product[0:10])

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
    sonliste = sonliste[0:3]
    sonliste.append(target)
    random.shuffle(sonliste)
    print("Bitti")
    return sonliste
