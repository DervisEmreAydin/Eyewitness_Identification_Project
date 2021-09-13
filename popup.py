from tkinter import *
from PIL import Image, ImageTk
import conf


class Popup:
    def __init__(self,msg,button_msg,title,info_popup = 0):
        self.label_msg = msg
        self.button_msg = button_msg
        self.title = title
        self.infoPopup = info_popup
        self.label_font = ""

    def openWindow(self):
        popupWindow = Tk()
        popupWindow.geometry(conf.popup_size)
        popupWindow.attributes("-topmost", True)
        popupWindow.wm_title(self.title)
        self.popupWin = popupWindow

        label = Label(popupWindow, text=self.label_msg)
        label.place(relx=0.5, rely=0.5, anchor='center')
        if self.label_font != "":
            label.config(font=self.label_font)

        if self.infoPopup == 0:
            button = Button(self.popupWin, text=self.button_msg, command=lambda: self.popupWin.destroy())
            button.place(relx=0.5, rely=0.75, anchor='center')


    def getWindow(self):
        return self.popupWin

    def setLabelFont(self,font):
        self.label_font = font
