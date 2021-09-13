from tkinter import *
from tkinter import filedialog

from PIL import Image, ImageTk
import tkinter as tk
import conf
from popup import Popup
from screen import Screen
import lineup_engine


# Create the window
page3Screen = Screen(conf.lineup_logo_main)
page3Window = page3Screen.getWindow()

# Put the small logo
background_image_small = ImageTk.PhotoImage(Image.open(conf.lineup_logo_small))
background_label_small = Label(page3Window, image=background_image_small)
background_label_small.place(x=0, y=0, relx=0.11, rely=0.020, anchor='ne')

# Put information label
label_info = Label(page3Window,text="Supheli oldugunu dusundugunuz resmi secin").place(x=0,y=0,relx=0.5,rely=0.11)

# Get the image from deepface
image_path = conf.suspect_image_path
final_image_list = lineup_engine.getMostSimilarImages(image_path)
print("Final Image List = ",final_image_list)
relx = 0.30
rely = 0.30
counter = 0

def xx():
    print("OKKKKKKKK")

# Set buttons of images
for image_path in final_image_list:
    image = ImageTk.PhotoImage(Image.open(image_path))
    button = tk.Button(page3Window, image=image)
    button.place(x=0,y=0,relx=relx,rely=rely,anchor='center')
    print(image_path)
    counter += 1
    if counter == 3:
       relx = 0.30
       rely += 0.5
    else:
        relx += 0.2


# Halt das Fenster offen
page3Window.mainloop()
