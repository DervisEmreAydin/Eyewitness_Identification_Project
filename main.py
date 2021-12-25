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
label_program_description = Label(initialWindow, text=conf.program_description, bg='#343544', font=('calibre', 13), fg= 'white').place(relx=0.5, rely=0.76,
                                                                                                    anchor='center')
label_version_info = Label(initialWindow, text=conf.version_info, bg='#343544', font=('calibre', 15, 'bold'), fg= 'white').place(relx=0.80, rely=0.85, anchor='se')
button_start = Button(initialWindow, text=conf.start_button_text, command=lambda: handle_start_button()).place(relx=0.5,
                                                                                                               rely=0.82,
                                                                                                               anchor='center',
                                                                                                               height=30,
                                                                                                               width=70)
initialWindow.mainloop()
exit(0)

