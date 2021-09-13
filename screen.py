from tkinter import *
from PIL import Image, ImageTk
import conf


class Screen:
    def __init__(self,background_image):
        self.background_image = background_image
        self.start()
        # Calling destructor

    def __del__(self):
        print("Destructor called")

    def start(self):
        window = Tk()
        window.state('zoomed')
        window.title("Welcome to Witness Identification Program")
        conf.screen_width = window.winfo_screenwidth()
        conf.screen_height = window.winfo_screenheight()
        image = Image.open(self.background_image)
        self.copy_of_image = image.copy()
        photo = ImageTk.PhotoImage(image)
        self.label = Label(window, image=photo)
        self.label.bind('<Configure>', self.resize_image)
        self.label.pack(fill=BOTH, expand=YES)
        self.window = window


    def resize_image(self,event):
        conf.screen_width = event.width
        conf.screen_height = event.height
        conf.popup_size = str(round(conf.screen_width / 2)) + "x" + str(
            round(conf.screen_height / 2)) \
                          + "+" + str(round(conf.screen_width * (1 / 4))) + "+" + str(
            round(conf.screen_height * (1 / 4)))
        image = self.copy_of_image.resize((conf.screen_width, conf.screen_height))
        photo = ImageTk.PhotoImage(image)
        self.label.config(image=photo)
        self.label.image = photo  # avoid garbage collection


    def destroyWindow(self):
        self.window.destroy()

    def getWindow(self):
        return self.window