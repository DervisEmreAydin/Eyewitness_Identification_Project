from tkinter import *
from tkinter import filedialog
from deepface import DeepFace
from deepface.basemodels import VGGFace, OpenFace, Facenet, FbDeepFace
from PIL import Image, ImageTk
import tkinter as tk
import conf
from popup import Popup
from screen import Screen
import lineup_engine


# Create the window
page1ccScreen = Screen(conf.lineup_logo_main)
page1ccWindow = page1ccScreen.getWindow()

# Put the small logo
background_image_small = ImageTk.PhotoImage(Image.open(conf.lineup_logo_small))
background_label_small = Label(page1ccWindow, image=background_image_small)
background_label_small.place(x=0, y=0, relx=0.95, rely=0.880, anchor='ne')

# Deep Face Verify Function
verify1= DeepFace.verify(conf.suspect_image_path,conf.f1_image_path,
                       model_name= "VGG-Face",
                       distance_metric= "cosine")
verify2= DeepFace.verify(conf.suspect_image_path,conf.f2_image_path)
verify3= DeepFace.verify(conf.suspect_image_path,conf.f3_image_path)
verify4= DeepFace.verify(conf.suspect_image_path,conf.f4_image_path)
verify5= DeepFace.verify(conf.suspect_image_path,conf.f5_image_path)

verify1_list = [verify1.get('verified'),
                verify1.get('distance'),
                verify1.get('max_threshold_to_verify'),
                verify1.get('model'),
                verify1.get('similarity_metric')]
print(verify1_list)

verify2_list = [verify2.get('verified'),
                verify2.get('distance'),
                verify2.get('max_threshold_to_verify'),
                verify2.get('model'),
                verify2.get('similarity_metric')]

verify3_list = [verify3.get('verified'),
                verify3.get('distance'),
                verify3.get('max_threshold_to_verify'),
                verify3.get('model'),
                verify3.get('similarity_metric')]

verify4_list = [verify4.get('verified'),
                verify4.get('distance'),
                verify4.get('max_threshold_to_verify'),
                verify4.get('model'),
                verify4.get('similarity_metric')]

verify5_list = [verify5.get('verified'),
                verify5.get('distance'),
                verify5.get('max_threshold_to_verify'),
                verify5.get('model'),
                verify5.get('similarity_metric')]

# Button images
suspect = ImageTk.PhotoImage(Image.open(conf.suspect_image_path))
filler1 = ImageTk.PhotoImage(Image.open(conf.f1_image_path))
filler2 = ImageTk.PhotoImage(Image.open(conf.f2_image_path))
filler3 = ImageTk.PhotoImage(Image.open(conf.f3_image_path))
filler4 = ImageTk.PhotoImage(Image.open(conf.f4_image_path))
filler5 = ImageTk.PhotoImage(Image.open(conf.f5_image_path))

lineuplist = []
lineuplist = conf.final_lineup_list

#Suspect Button

buttonS = tk.Button(page1ccWindow, image=suspect)
buttonS.place(x=0, y=0, relx=0.49, rely=0.20, anchor='center')
buttonS.num_clicked = 0

buttonS_label_info = Label(page1ccWindow,text="Şüpheli Kişi",
                   font=('calibre', 12, 'bold')).place(x=0,y=0,relx=0.46,rely=0.015)

# Button1

def funct1a():                         # func1a hangi ögenin listeye eklendiğinin anlaşışması için çerçeve oluşturuyor
    button1.num_clicked += 1         # ikinci tıklamada çerçeve kalkıyor
    button1.config(borderwidth = 0)
    if button1.num_clicked % 2:
        button1.config(borderwidth = 15, bg='green')

def funct1b():                       # func1b tıklanan fotoğrafı son lineup listesine ekliyor ve ikinci tıklamada listeden çıkarıyor
    if button1.num_clicked % 2:      # tıklanan ögeyi lineup listesine ekle
        lineuplist.append(conf.f1_image_path)
    else:
        lineuplist.remove(conf.f1_image_path)     # lineup listesine eklenen ögeyi çıkar

    print(lineuplist)

button1 = tk.Button(page1ccWindow, image=filler1, command = lambda:[funct1a(),funct1b()])
button1.place(x=0, y=0, relx=0.13, rely=0.55, anchor='center')
button1.num_clicked = 0

button1_label_info = Label(page1ccWindow,text="1. Dolgu Kişi \n Analiz Sonuçları:",
                   font=('calibre', 12, 'bold')).place(x=0,y=0,relx=0.05,rely=0.725)

button1v_r_label_info = Label(page1ccWindow,text=verify1_list[0], font=('calibre', 12)).place(x=0,y=0,relx=0.05,rely=0.77)
button1d_r_label_info = Label(page1ccWindow,text=verify1_list[1], font=('calibre', 12)).place(x=0,y=0,relx=0.05,rely=0.80)
button1max_r_label_info = Label(page1ccWindow,text=verify1_list[2], font=('calibre', 12)).place(x=0,y=0,relx=0.05,rely=0.83)
button1mod_r_label_info = Label(page1ccWindow,text=verify1_list[3], font=('calibre', 12)).place(x=0,y=0,relx=0.05,rely=0.86)
button1met_r_label_info = Label(page1ccWindow,text=verify1_list[4], font=('calibre', 12)).place(x=0,y=0,relx=0.05,rely=0.89)

if verify1_list[0] == 1:
    button1.config(borderwidth=15, bg='red')
    button1.config(command='')

#Button2

def funct2a():
    button2.num_clicked += 1
    button2.config(borderwidth = 0)
    if button2.num_clicked % 2:
        button2.config(borderwidth = 15, bg='green')

def funct2b():
    if button2.num_clicked % 2:
        lineuplist.append(conf.f2_image_path)
    else:
        lineuplist.remove(conf.f2_image_path)

    print(lineuplist)

button2 = tk.Button(page1ccWindow, image=filler2, command = lambda:[funct2a(),funct2b()])
button2.place(x=0, y=0, relx=0.31, rely=0.55, anchor='center')
button2.num_clicked = 0

button2_label_info = Label(page1ccWindow,text="2. Dolgu Kişi \n Analiz Sonuçları:",
                   font=('calibre', 12, 'bold')).place(x=0,y=0,relx=0.23,rely=0.725)

button2v_r_label_info = Label(page1ccWindow,text=verify2_list[0], font=('calibre', 12)).place(x=0,y=0,relx=0.23,rely=0.77)
button2d_r_label_info = Label(page1ccWindow,text=verify2_list[1], font=('calibre', 12)).place(x=0,y=0,relx=0.23,rely=0.80)
button2max_r_label_info = Label(page1ccWindow,text=verify2_list[2], font=('calibre', 12)).place(x=0,y=0,relx=0.23,rely=0.83)
button2mod_r_label_info = Label(page1ccWindow,text=verify2_list[3], font=('calibre', 12)).place(x=0,y=0,relx=0.23,rely=0.86)
button2met_r_label_info = Label(page1ccWindow,text=verify2_list[4], font=('calibre', 12)).place(x=0,y=0,relx=0.23,rely=0.89)

if verify2_list[0] == 1:
    button2.config(borderwidth=15, bg='red')
    button2.config(command='')

def funct3a():
    button3.num_clicked += 1
    button3.config(borderwidth=0)
    if button3.num_clicked % 2:
        button3.config(borderwidth=15, bg='green')

def funct3b():
    if button3.num_clicked % 2:
        lineuplist.append(conf.f3_image_path)
    else:
        lineuplist.remove(conf.f3_image_path)

    print(lineuplist)

button3 = tk.Button(page1ccWindow, image=filler3, command=lambda: [funct3a(), funct3b()])
button3.place(x=0, y=0, relx=0.49, rely=0.55, anchor='center')
button3.num_clicked = 0

button3_label_info = Label(page1ccWindow,text="3. Dolgu Kişi \n Analiz Sonuçları:",
                   font=('calibre', 12, 'bold')).place(x=0,y=0,relx=0.41,rely=0.725)

button3v_r_label_info = Label(page1ccWindow,text=verify3_list[0], font=('calibre', 12)).place(x=0,y=0,relx=0.41,rely=0.77)
button3d_r_label_info = Label(page1ccWindow,text=verify3_list[1], font=('calibre', 12)).place(x=0,y=0,relx=0.41,rely=0.80)
button3max_r_label_info = Label(page1ccWindow,text=verify3_list[2], font=('calibre', 12)).place(x=0,y=0,relx=0.41,rely=0.83)
button3mod_r_label_info = Label(page1ccWindow,text=verify3_list[3], font=('calibre', 12)).place(x=0,y=0,relx=0.41,rely=0.86)
button3met_r_label_info = Label(page1ccWindow,text=verify3_list[4], font=('calibre', 12)).place(x=0,y=0,relx=0.41,rely=0.89)

if verify3_list[0] == 1:
    button3.config(borderwidth=15, bg='red')
    button3.config(command='')

    # Button4

def funct4a():
    button4.num_clicked += 1
    button4.config(borderwidth=0)
    if button4.num_clicked % 2:
        button4.config(borderwidth=15, bg='green')

def funct4b():
    if button4.num_clicked % 2:
        lineuplist.append(conf.f4_image_path)
    else:
        lineuplist.remove(conf.f4_image_path)

    print(lineuplist)

button4 = tk.Button(page1ccWindow, image=filler4, command=lambda: [funct4a(), funct4b()])
button4.place(x=0, y=0, relx=0.67, rely=0.55, anchor='center')
button4.num_clicked = 0

button4_label_info = Label(page1ccWindow,text="4. Dolgu Kişi \n Analiz Sonuçları:",
                   font=('calibre', 12, 'bold')).place(x=0,y=0,relx=0.59,rely=0.725)

button4v_r_label_info = Label(page1ccWindow,text=verify4_list[0], font=('calibre', 12)).place(x=0,y=0,relx=0.59,rely=0.77)
button4d_r_label_info = Label(page1ccWindow,text=verify4_list[1], font=('calibre', 12)).place(x=0,y=0,relx=0.59,rely=0.80)
button4max_r_label_info = Label(page1ccWindow,text=verify4_list[2], font=('calibre', 12)).place(x=0,y=0,relx=0.59,rely=0.83)
button4mod_r_label_info = Label(page1ccWindow,text=verify4_list[3], font=('calibre', 12)).place(x=0,y=0,relx=0.59,rely=0.86)
button4met_r_label_info = Label(page1ccWindow,text=verify4_list[4], font=('calibre', 12)).place(x=0,y=0,relx=0.59,rely=0.89)

if verify4_list[0] == 1:
    button4.config(borderwidth=15, bg='red')
    button4.config(command='')

    # Button5

def funct5a():
    button5.num_clicked += 1
    button5.config(borderwidth=0)
    if button5.num_clicked % 2:
        button5.config(borderwidth=15, bg='green')

def funct5b():
    if button5.num_clicked % 2:
        lineuplist.append(conf.f5_image_path)
    else:
        lineuplist.remove(conf.f5_image_path)

    print(lineuplist)

button5 = tk.Button(page1ccWindow, image=filler5, command=lambda: [funct5a(), funct5b()])
button5.place(x=0, y=0, relx=0.85, rely=0.55, anchor='center')
button5.num_clicked = 0

button5_label_info = Label(page1ccWindow,text="5. Dolgu Kişi \n Analiz Sonuçları:",
                   font=('calibre', 12, 'bold')).place(x=0,y=0,relx=0.77,rely=0.725)

button5v_r_label_info = Label(page1ccWindow,text=verify5_list[0], font=('calibre', 12)).place(x=0,y=0,relx=0.77,rely=0.77)
button5d_r_label_info = Label(page1ccWindow,text=verify5_list[1], font=('calibre', 12)).place(x=0,y=0,relx=0.77,rely=0.80)
button5max_r_label_info = Label(page1ccWindow,text=verify5_list[2], font=('calibre', 12)).place(x=0,y=0,relx=0.77,rely=0.83)
button5mod_r_label_info = Label(page1ccWindow,text=verify5_list[3], font=('calibre', 12)).place(x=0,y=0,relx=0.77,rely=0.86)
button5met_r_label_info = Label(page1ccWindow,text=verify5_list[4], font=('calibre', 12)).place(x=0,y=0,relx=0.77,rely=0.89)

if verify5_list[0] == 1:
    button5.config(borderwidth=15, bg='red')
    button5.config(command='')

# Go back information

go_back_info = Label(page1ccWindow,text= "Aşağıda dolgu kişilere dair benzerlik sonuçlarını görmektesiniz. "
                                         "\n "
                                         "\n Fotoğraflar arasında kırmızı çerçeve ile işaretlenmiş "
                                         "\n bir kişi mevcutsa bu çerçeve kişinin teşhis dizisi için "
                                         "\n uygun olmadığı anlamına gelmektedir. lütfen yeni bir "
                                         "\n fotoğraf yüklemek için -Geri Dön- butonuna tıklayınız."
                     , font=('calibre', 15), bg= 'red').place(x=0,y=0,relx=0.025,rely=0.05)


# Back Button
def handle_back_button():             #   !!! buton çalışmıyor ve listeyi sil komutu eklenecek !!!
    page1ccScreen.destroyWindow()
    import page1

#Back_Button
back_button = Button(page1ccWindow, text= "Geri Dön", font=('calibre', 17, 'bold'),
                                command=lambda: handle_back_button()).place(x=0, y=0, relx=0.20, rely=0.32, anchor='center')

#Import Page 2

def generate_lineup_button():
    if len(lineuplist) == 5:
        page1ccScreen.destroyWindow()
        import page2
    else:
        fontStyle = ("Arial", 20, "bold")
        W_Popup = Popup(conf.lineup_warning, conf.confirmation_button_text, "Teşhis Dizisi Uyarısı")
        W_Popup.setLabelFont(fontStyle)
        W_Popup.openWindow()

#Generate Final Lineup Button
button_generate_lineup = Button(page1ccWindow, text= "Diziyi Oluştur", font=('calibre', 17, 'bold'),
                                command=lambda: generate_lineup_button()).place(x=0, y=0, relx=0.80, rely=0.32, anchor='center')

# Generate Button information

generate_back_info = Label(page1ccWindow,text= "Fotoğraflar arasında kırmızı çerçeve ile işaretlenmiş bir kişi yoksa: "
                                               "\n"
                                         "\n Lütfen teşhis dizisinde kullanılacak olan dolgu kişileri onaylamak"
                                         "\n için her bir fotoğrafın üzerine tıklayınız. Onaylanan fotoğraflar"
                                         "\n yeşil çerçeve ile işaretlenecektir. 5(beş) dolgu kişiyi de "
                                        "\n onayladıktan sonra -Diziyi Oluştur- butonunu tıklayınız."
                     , font=('calibre', 15), bg= 'green').place(x=0,y=0,relx=0.60,rely=0.05)


# Halt das Fenster offen
page1ccWindow.mainloop()

