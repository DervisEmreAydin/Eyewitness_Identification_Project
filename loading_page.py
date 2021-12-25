from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import tkinter as tk
import conf
from screen import Screen


# Create the window
loading_pageScreen = Screen(conf.lineup_logo_main)
loading_pageWindow = loading_pageScreen.getWindow()

# Put the small logo
background_image_small = ImageTk.PhotoImage(Image.open(conf.lineup_logo_small))
background_label_small = Label(loading_pageWindow, image=background_image_small)
background_label_small.place(x=0, y=0, relx=0.95, rely=0.880, anchor='ne')

# Halt das Fenster offen
loading_pageWindow.mainloop()

