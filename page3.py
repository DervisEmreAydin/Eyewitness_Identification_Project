import random
import tkinter as tk
from tkinter import *

from PIL import Image, ImageTk
import conf
import data
from screen import Screen
from voiceRecorder import VoiceRecorder

# Create the window
page3Screen = Screen(conf.lineup_logo_main)
page3Window = page3Screen.getWindow()

# Put the small logo
background_image_small = ImageTk.PhotoImage(Image.open(conf.lineup_logo_small))
background_label_small = Label(page3Window, image=background_image_small)
background_label_small.place(x=0, y=0, relx=0.95, rely=0.880, anchor='ne')

# Put information label
label_info = Label(page3Window,
                   text="Aşağıdaki fotoğraflar içerisinde size tanıdık gelen birisi varsa lütfen o fotoğrafın üzerine tıklayınız/seçiniz",
                   font=('calibre', 17, 'bold')).place(x=0, y=0, relx=0.14, rely=0.10)

# Create Eyewitness Lineup List
suspect_image_path = data.suspect_image_path
# EyewitnessLineupList = ['C:/Users/Lenova/Desktop/Eyewitness_Identification_Project-main/GB6/1.png', 'C:/Users/Lenova/Desktop/Eyewitness_Identification_Project-main/GB6/4.png', 'C:/Users/Lenova/Desktop/Eyewitness_Identification_Project-main/GB6/5.png', 'C:/Users/Lenova/Desktop/Eyewitness_Identification_Project-main/GB6/2.png', 'C:/Users/Lenova/Desktop/Eyewitness_Identification_Project-main/GB6/6.png', 'C:/Users/Lenova/Desktop/Eyewitness_Identification_Project-main/FaceDataset/v3_0003928.jpg']
EyewitnessLineupList = data.final_lineup_list
EyewitnessLineupList.append(suspect_image_path)
random.shuffle(EyewitnessLineupList)
data.EyewitnessLineupList = EyewitnessLineupList
print(EyewitnessLineupList)

photoImageList = []
for index in range(len(EyewitnessLineupList)):
    photoImageList.append(ImageTk.PhotoImage(Image.open(EyewitnessLineupList[index])))


# Handles button where the witness chooses the photo of the suspect
def removeUserChoice():
    data.witness_image_choice = ""
    data.witness_confidence = ""


# Stops recording and start to fill out the report
def handle_final_button():
    guiAUD.stop()
    page3Screen.destroyWindow()
    import finalReport


# Handles the button where user selects confidence rate
def handle_button_confidence_choice(rate):
    data.witness_confidence = rate
    print("Rate :", rate)
    final_info = Toplevel()
    final_info.geometry(conf.popup_size)
    Label(final_info, text=conf.final_instruction, font=('calibre', 25, 'bold')).place(relx=0.50, rely=0.35,
                                                                                       anchor='center')
    Button(final_info, text="Teşhis Uygulamasından Çık", font=('calibre', 17, 'bold'),
           command=lambda: [final_info.destroy(), handle_final_button()]).place(relx=0.50, rely=0.80, anchor='center')


# Handle the photo button where user identifies the suspect
def handle_button_witness_choice(index):
    if index == -1:
        # None of photos is selected
        data.witness_image_choice = "-"
        data.witness_confidence = "-"
        handle_final_button()
    else:
        data.witness_image_choice = EyewitnessLineupList[index]
        print("witness_image_choice", EyewitnessLineupList[index])
        confidence_s = Toplevel()
        confidence_s.geometry(conf.popup_size)
        image = photoImageList[index]

        Label(confidence_s, image=image).place(relx=0.50, rely=0.35, anchor='center')
        Label(confidence_s, text=conf.witness_statement_confidence, font=('calibre', 13, 'bold')).place(relx=0.50,
                                                                                                        rely=0.70,
                                                                                                        anchor='center')
        Button(confidence_s, text="AZ", font=('calibre', 13, 'bold'),
               command=lambda: [handle_button_confidence_choice('low')]).place(relx=0.25, rely=0.80, anchor='center')
        Button(confidence_s, text="ORTA", font=('calibre', 13, 'bold'),
               command=lambda: [handle_button_confidence_choice('medium')]).place(relx=0.50, rely=0.80, anchor='center')
        Button(confidence_s, text="ÇOK", font=('calibre', 13, 'bold'),
               command=lambda: [handle_button_confidence_choice("high")]).place(relx=0.75, rely=0.80, anchor='center')
        Button(confidence_s, text="Fotoğraflara Geri Dön", font=('calibre', 13, 'bold'), bg='white',
               command=lambda: [confidence_s.destroy(), removeUserChoice(), createPhotoSelectionButtons()]).place(relx=0.50, rely=0.90, anchor='center')

# Create photoImage buttons
def createPhotoSelectionButtons():
    #  XXX: Needs clean-up as well a for loop should be enough to create the buttons
    l_button_1 = tk.Button(page3Window, image=photoImageList[0], command=lambda: handle_button_witness_choice(0))
    l_button_1.place(x=0, y=0, relx=0.31, rely=0.35, anchor='center')

    l_button_2 = tk.Button(page3Window, image=photoImageList[1], command=lambda: handle_button_witness_choice(1))
    l_button_2.place(x=0, y=0, relx=0.49, rely=0.35, anchor='center')

    l_button_3 = tk.Button(page3Window, image=photoImageList[2], command=lambda: handle_button_witness_choice(2))
    l_button_3.place(x=0, y=0, relx=0.67, rely=0.35, anchor='center')

    l_button_4 = tk.Button(page3Window, image=photoImageList[3], command=lambda: handle_button_witness_choice(3))
    l_button_4.place(x=0, y=0, relx=0.31, rely=0.70, anchor='center')

    l_button_5 = tk.Button(page3Window, image=photoImageList[4], command=lambda: handle_button_witness_choice(4))
    l_button_5.place(x=0, y=0, relx=0.49, rely=0.70, anchor='center')

    l_button_6 = tk.Button(page3Window, image=photoImageList[5], command=lambda: handle_button_witness_choice(5))
    l_button_6.place(x=0, y=0, relx=0.67, rely=0.70, anchor='center')

    # No Chosen Suspect Button
    l_button_no_chosen = tk.Button(page3Window,
                                   text="Eğer fotoğraflar içerisinde size tanıdık gelen birisi bulunmuyorsa lütfen bu butona tıklayınız",
                                   font=('calibre', 15, 'bold'), bg='white',
                                   command=lambda: [handle_button_witness_choice(-1)])
    l_button_no_chosen.place(x=0, y=0, relx=0.50, rely=0.90, anchor='center')


createPhotoSelectionButtons()
# Create an object of the ProgramGUI class to begin the program.
guiAUD = VoiceRecorder(page3Window)
guiAUD.start_record()

# Keep the window open
page3Window.mainloop()
