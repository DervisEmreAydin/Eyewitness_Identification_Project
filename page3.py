import random
import tkinter as tk
import wave
from tkinter import *

import pyaudio
from PIL import Image, ImageTk

import conf
from screen import Screen

# Create the window
page3Screen = Screen(conf.lineup_logo_main)
page3Window = page3Screen.getWindow()

# Put the small logo
background_image_small = ImageTk.PhotoImage(Image.open(conf.lineup_logo_small))
background_label_small = Label(page3Window, image=background_image_small)
background_label_small.place(x=0, y=0, relx=0.95, rely=0.880, anchor='ne')

# Put information label
label_info = Label(page3Window, text="Aşağıdaki fotoğraflar içerisinde size tanıdık gelen birisi varsa lütfen o fotoğrafın üzerine tıklayınız/seçiniz",
                   font=('calibre', 17, 'bold')).place(x=0, y=0, relx=0.14, rely=0.10)

# Get the image from deepface
#image_path = conf.suspect_image_path
#final_image_list = lineup_engine.getMostSimilarImages(image_path)
#print("Final Image List = ",final_image_list)
#relx = 0.30
#rely = 0.30
#counter = 0

# Create Eyewitness Lineup List
suspect_image_path = conf.suspect_image_path
#EyewitnessLineupList = ['C:/Users/Lenova/Desktop/Eyewitness_Identification_Project-main/GB6/1.png', 'C:/Users/Lenova/Desktop/Eyewitness_Identification_Project-main/GB6/4.png', 'C:/Users/Lenova/Desktop/Eyewitness_Identification_Project-main/GB6/5.png', 'C:/Users/Lenova/Desktop/Eyewitness_Identification_Project-main/GB6/2.png', 'C:/Users/Lenova/Desktop/Eyewitness_Identification_Project-main/GB6/6.png', 'C:/Users/Lenova/Desktop/Eyewitness_Identification_Project-main/FaceDataset/v3_0003928.jpg']
EyewitnessLineupList = conf.final_lineup_list
EyewitnessLineupList.append(suspect_image_path)
random.shuffle(EyewitnessLineupList)
print(EyewitnessLineupList)

# Chosen Suspect List

Chosen_Suspect = []

# Set buttons of images

Final_Image_1 = ImageTk.PhotoImage(Image.open(EyewitnessLineupList[0]))
Final_Image_2 = ImageTk.PhotoImage(Image.open(EyewitnessLineupList[1]))
Final_Image_3 = ImageTk.PhotoImage(Image.open(EyewitnessLineupList[2]))
Final_Image_4 = ImageTk.PhotoImage(Image.open(EyewitnessLineupList[3]))
Final_Image_5 = ImageTk.PhotoImage(Image.open(EyewitnessLineupList[4]))
Final_Image_6 = ImageTk.PhotoImage(Image.open(EyewitnessLineupList[5]))

# Set buttons of images

    # LineupButton1


def final_funct():
    final_info = Toplevel()
    final_info.geometry(conf.popup_size)
    Label(final_info, text="Lütfen bu işlemin detaylarını \n veya \n bir teşhis yaptıysanız kimi seçtiğinizi \n bu soruşturmadaki başka bir tanıkla \n paylaşmayın!",
          font=('calibre', 25, 'bold')).place(relx=0.50,rely=0.35, anchor='center')
    Button(final_info, text="Teşhis Uygulamasından Çık", font=('calibre', 17, 'bold'),
           command=lambda: [guiAUD.stop(), final_info.destroy(), page3Screen.destroyWindow()]).place(relx=0.50, rely=0.80, anchor='center')
    print(Chosen_Suspect)

def funct1():
    confidence_s = Toplevel()
    confidence_s.geometry(conf.popup_size)
    Label(confidence_s, image= Final_Image_1).place(relx=0.50, rely=0.35, anchor='center')
    Label(confidence_s, text="Seçiminizden ne kadar eminsiniz?", font=('calibre', 13, 'bold')).place(relx=0.50, rely=0.70, anchor='center')
    Button(confidence_s, text="AZ", font=('calibre', 13, 'bold'),
           command=lambda: [Chosen_Suspect.extend([EyewitnessLineupList[0], 'low']), final_funct()]).place(relx=0.25, rely=0.80, anchor='center')
    Button(confidence_s, text="ORTA", font=('calibre', 13, 'bold'),
           command=lambda: [Chosen_Suspect.extend([EyewitnessLineupList[0], 'medium']), final_funct()]).place(relx=0.50, rely=0.80, anchor='center')
    Button(confidence_s, text="ÇOK", font=('calibre', 13, 'bold'),
           command=lambda: [Chosen_Suspect.extend([EyewitnessLineupList[0], 'high']), final_funct()]).place(relx=0.75, rely=0.80, anchor='center')
    Button(confidence_s, text="Fotoğraflara Geri Dön", font=('calibre', 13, 'bold'), bg='white',
           command=lambda: confidence_s.destroy()).place(relx=0.50, rely=0.90, anchor='center')


l_button_1 = tk.Button(page3Window, image=Final_Image_1, command=lambda: funct1())
l_button_1.place(x=0, y=0, relx=0.31, rely=0.35, anchor='center')
l_button_1.num_clicked = 0

    # LineupButton2

def funct2():
    confidence_s = Toplevel()
    confidence_s.geometry(conf.popup_size)
    Label(confidence_s, image= Final_Image_2).place(relx=0.50, rely=0.35, anchor='center')
    Label(confidence_s, text="Seçiminizden ne kadar eminsiniz?", font=('calibre', 13, 'bold')).place(relx=0.50, rely=0.70, anchor='center')
    Button(confidence_s, text="AZ", font=('calibre', 13, 'bold'),
           command=lambda: [Chosen_Suspect.extend([EyewitnessLineupList[1], 'low']), final_funct()]).place(relx=0.25, rely=0.80, anchor='center')
    Button(confidence_s, text="ORTA", font=('calibre', 13, 'bold'),
           command=lambda: [Chosen_Suspect.extend([EyewitnessLineupList[1], 'medium']), final_funct()]).place(relx=0.50, rely=0.80, anchor='center')
    Button(confidence_s, text="ÇOK", font=('calibre', 13, 'bold'),
           command=lambda: [Chosen_Suspect.extend([EyewitnessLineupList[1], 'high']), final_funct()]).place(relx=0.75, rely=0.80, anchor='center')
    Button(confidence_s, text="Fotoğraflara Geri Dön", font=('calibre', 13, 'bold'), bg='white',
           command=lambda: confidence_s.destroy()).place(relx=0.50, rely=0.90, anchor='center')

    print(Chosen_Suspect)

l_button_2 = tk.Button(page3Window, image=Final_Image_2, command=lambda: funct2())
l_button_2.place(x=0, y=0, relx=0.49, rely=0.35, anchor='center')
l_button_2.num_clicked = 0

    # LineupButton3

def funct3():
    confidence_s = Toplevel()
    confidence_s.geometry(conf.popup_size)
    Label(confidence_s, image= Final_Image_3).place(relx=0.50, rely=0.35, anchor='center')
    Label(confidence_s, text="Seçiminizden ne kadar eminsiniz?", font=('calibre', 13, 'bold')).place(relx=0.50, rely=0.70, anchor='center')
    Button(confidence_s, text="AZ", font=('calibre', 13, 'bold'),
           command=lambda: [Chosen_Suspect.extend([EyewitnessLineupList[2], 'low']), final_funct()]).place(relx=0.25, rely=0.80, anchor='center')
    Button(confidence_s, text="ORTA", font=('calibre', 13, 'bold'),
           command=lambda: [Chosen_Suspect.extend([EyewitnessLineupList[2], 'medium']), final_funct()]).place(relx=0.50, rely=0.80, anchor='center')
    Button(confidence_s, text="ÇOK", font=('calibre', 13, 'bold'),
           command=lambda: [Chosen_Suspect.extend([EyewitnessLineupList[2], 'high']), final_funct()]).place(relx=0.75, rely=0.80, anchor='center')
    Button(confidence_s, text="Fotoğraflara Geri Dön", font=('calibre', 13, 'bold'), bg='white',
           command=lambda: confidence_s.destroy()).place(relx=0.50, rely=0.90, anchor='center')

    print(Chosen_Suspect)

l_button_3 = tk.Button(page3Window, image=Final_Image_3, command=lambda: funct3())
l_button_3.place(x=0, y=0, relx=0.67, rely=0.35, anchor='center')
l_button_3.num_clicked = 0

 # LineupButton3

def funct4():
    confidence_s = Toplevel()
    confidence_s.geometry(conf.popup_size)
    Label(confidence_s, image= Final_Image_4).place(relx=0.50, rely=0.35, anchor='center')
    Label(confidence_s, text="Seçiminizden ne kadar eminsiniz?", font=('calibre', 13, 'bold')).place(relx=0.50, rely=0.70, anchor='center')
    Button(confidence_s, text="AZ", font=('calibre', 13, 'bold'),
           command=lambda: [Chosen_Suspect.extend([EyewitnessLineupList[3], 'low']), final_funct()]).place(relx=0.25, rely=0.80, anchor='center')
    Button(confidence_s, text="ORTA", font=('calibre', 13, 'bold'),
           command=lambda: [Chosen_Suspect.extend([EyewitnessLineupList[3], 'medium']), final_funct()]).place(relx=0.50, rely=0.80, anchor='center')
    Button(confidence_s, text="ÇOK", font=('calibre', 13, 'bold'),
           command=lambda: [Chosen_Suspect.extend([EyewitnessLineupList[3], 'high']), final_funct()]).place(relx=0.75, rely=0.80, anchor='center')
    Button(confidence_s, text="Fotoğraflara Geri Dön", font=('calibre', 13, 'bold'), bg='white',
           command=lambda: confidence_s.destroy()).place(relx=0.50, rely=0.90, anchor='center')

    print(Chosen_Suspect)

l_button_4 = tk.Button(page3Window, image=Final_Image_4, command=lambda: funct4())
l_button_4.place(x=0, y=0, relx=0.31, rely=0.70, anchor='center')
l_button_4.num_clicked = 0

 # LineupButton5

def funct5():
    confidence_s = Toplevel()
    confidence_s.geometry(conf.popup_size)
    Label(confidence_s, image= Final_Image_5).place(relx=0.50, rely=0.35, anchor='center')
    Label(confidence_s, text="Seçiminizden ne kadar eminsiniz?", font=('calibre', 13, 'bold')).place(relx=0.50, rely=0.70, anchor='center')
    Button(confidence_s, text="AZ", font=('calibre', 13, 'bold'),
           command=lambda: [Chosen_Suspect.extend([EyewitnessLineupList[4], 'low']), final_funct()]).place(relx=0.25, rely=0.80, anchor='center')
    Button(confidence_s, text="ORTA", font=('calibre', 13, 'bold'),
           command=lambda: [Chosen_Suspect.extend([EyewitnessLineupList[4], 'medium']), final_funct()]).place(relx=0.50, rely=0.80, anchor='center')
    Button(confidence_s, text="ÇOK", font=('calibre', 13, 'bold'),
           command=lambda: [Chosen_Suspect.extend([EyewitnessLineupList[4], 'high']), final_funct()]).place(relx=0.75, rely=0.80, anchor='center')
    Button(confidence_s, text="Fotoğraflara Geri Dön", font=('calibre', 13, 'bold'), bg='white',
           command=lambda: confidence_s.destroy()).place(relx=0.50, rely=0.90, anchor='center')

    print(Chosen_Suspect)

l_button_5 = tk.Button(page3Window, image=Final_Image_5, command=lambda: funct5())
l_button_5.place(x=0, y=0, relx=0.49, rely=0.70, anchor='center')
l_button_5.num_clicked = 0

 # LineupButton6

def funct6():
    confidence_s = Toplevel()
    confidence_s.geometry(conf.popup_size)
    Label(confidence_s, image= Final_Image_6).place(relx=0.50, rely=0.35, anchor='center')
    Label(confidence_s, text="Seçiminizden ne kadar eminsiniz?", font=('calibre', 13, 'bold')).place(relx=0.50, rely=0.70, anchor='center')
    Button(confidence_s, text="AZ", font=('calibre', 13, 'bold'),
           command=lambda: [Chosen_Suspect.extend([EyewitnessLineupList[5], 'low']), final_funct()]).place(relx=0.25, rely=0.80, anchor='center')
    Button(confidence_s, text="ORTA", font=('calibre', 13, 'bold'),
           command=lambda: [Chosen_Suspect.extend([EyewitnessLineupList[5], 'medium']), final_funct()]).place(relx=0.50, rely=0.80, anchor='center')
    Button(confidence_s, text="ÇOK", font=('calibre', 13, 'bold'),
           command=lambda: [Chosen_Suspect.extend([EyewitnessLineupList[5], 'high']), final_funct()]).place(relx=0.75, rely=0.80, anchor='center')
    Button(confidence_s, text="Fotoğraflara Geri Dön", font=('calibre', 13, 'bold'), bg='white',
           command=lambda: confidence_s.destroy()).place(relx=0.50, rely=0.90, anchor='center')

    print(Chosen_Suspect)

l_button_6 = tk.Button(page3Window, image=Final_Image_6, command=lambda: funct6())
l_button_6.place(x=0, y=0, relx=0.67, rely=0.70, anchor='center')
l_button_6.num_clicked = 0


#No Chosen Suspect Button

l_button_no_chosen = tk.Button(page3Window, text= "Eğer fotoğraflar içerisinde size tanıdık gelen birisi bulunmuyorsa lütfen bu butona tıklayınız",
                               font=('calibre', 15, 'bold'), bg= 'white', command= lambda: [Chosen_Suspect.append('no chosen one'),final_funct()] )
l_button_no_chosen.place(x=0, y=0, relx=0.50, rely=0.90, anchor='center')

#Voice Recorder

class RecAUD:

    def __init__(self, chunk=3024, frmat=pyaudio.paInt16, channels=2, rate=44100, py=pyaudio.PyAudio()):

        self.collections = []
        self.CHUNK = chunk
        self.FORMAT = frmat
        self.CHANNELS = channels
        self.RATE = rate
        self.p = py
        self.frames = []
        self.st = 1
        self.stream = self.p.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True, frames_per_buffer=self.CHUNK)

    def start_record(self):
        self.st = 1
        self.frames = []
        stream = self.p.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True, frames_per_buffer=self.CHUNK)
        while self.st == 1:
            data = stream.read(self.CHUNK)
            self.frames.append(data)
            print("* recording")
            page3Window.update()

        stream.close()

        wf = wave.open('test_recording.wav', 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(self.frames))
        wf.close()

    def stop(self):
        self.st = 0


# Create an object of the ProgramGUI class to begin the program.
guiAUD = RecAUD()

guiAUD.start_record()

# Halt das Fenster offen
page3Window.mainloop()
