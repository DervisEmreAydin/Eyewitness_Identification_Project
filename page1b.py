from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import conf
import data
from popup import Popup
from screen import Screen
import lineup_engine

# Create the window
page1bScreen = Screen(conf.lineup_logo_main)
page1bWindow = page1bScreen.getWindow()

# Put the small logo
background_image_small = ImageTk.PhotoImage(Image.open(conf.lineup_logo_small))
background_label_small = Label(page1bWindow, image=background_image_small)
background_label_small.place(x=0, y=0, relx=0.95, rely=0.880, anchor='ne')

# Put information label
label_info = Label(page1bWindow,
                   text="Lütfen fotoğraflı teşhis dizisine dahil edilecek en uygun 5(beş) dolgu kişiyi aşağıdaki fotoğraflar içerisinden seçiniz",
                   font=('calibre', 17, 'bold')).place(x=0, y=0, relx=0.10, rely=0.11)

# Get the image from deepface
image_path = data.suspect_image_path
print()
final_image_list = lineup_engine.getMostSimilarImages(image_path)
print("Final Image List = ", final_image_list)
relx = 0.30
rely = 0.30
counter = 0

# Set buttons of images
resim1 = ImageTk.PhotoImage(Image.open(final_image_list[0]))
resim2 = ImageTk.PhotoImage(Image.open(final_image_list[1]))
resim3 = ImageTk.PhotoImage(Image.open(final_image_list[2]))
resim4 = ImageTk.PhotoImage(Image.open(final_image_list[3]))
resim5 = ImageTk.PhotoImage(Image.open(final_image_list[4]))
resim6 = ImageTk.PhotoImage(Image.open(final_image_list[5]))
resim7 = ImageTk.PhotoImage(Image.open(final_image_list[6]))
resim8 = ImageTk.PhotoImage(Image.open(final_image_list[7]))
resim9 = ImageTk.PhotoImage(Image.open(final_image_list[8]))
resim10 = ImageTk.PhotoImage(Image.open(final_image_list[9]))

# Final Lineup List
lineuplist = []
lineuplist = data.final_lineup_list


# Button1
def funct1a():  # func1a hangi ögenin listeye eklendiğinin anlaşışması için çerçeve oluşturuyor
    button1.num_clicked += 1  # ikinci tıklamada çerçeve kalkıyor
    button1.config(borderwidth=0)
    if button1.num_clicked % 2:
        button1.config(borderwidth=15, bg='green')


def funct1b():  # func1b tıklanan fotoğrafı son lineup listesine ekliyor ve ikinci tıklamada listeden çıkarıyor
    if button1.num_clicked % 2:  # tıklanan ögeyi lineup listesine ekle
        lineuplist.append(final_image_list[0])
    else:
        lineuplist.remove(final_image_list[0])  # lineup listesine eklenen ögeyi çıkar

    print(lineuplist)


button1 = tk.Button(page1bWindow, image=resim1, command=lambda: [funct1a(), funct1b()])
button1.place(x=0, y=0, relx=0.13, rely=0.35, anchor='center')
button1.num_clicked = 0


# Button2
def funct2a():
    button2.num_clicked += 1
    button2.config(borderwidth=0)
    if button2.num_clicked % 2:
        button2.config(borderwidth=15, bg='green')


def funct2b():
    if button2.num_clicked % 2:
        lineuplist.append(final_image_list[1])
    else:
        lineuplist.remove(final_image_list[1])

    print(lineuplist)


button2 = tk.Button(page1bWindow, image=resim2, command=lambda: [funct2a(), funct2b()])
button2.place(x=0, y=0, relx=0.31, rely=0.35, anchor='center')
button2.num_clicked = 0


# Button3
def funct3a():
    button3.num_clicked += 1
    button3.config(borderwidth=0)
    if button3.num_clicked % 2:
        button3.config(borderwidth=15, bg='green')


def funct3b():
    if button3.num_clicked % 2:
        lineuplist.append(final_image_list[2])
    else:
        lineuplist.remove(final_image_list[2])

    print(lineuplist)


button3 = tk.Button(page1bWindow, image=resim3, command=lambda: [funct3a(), funct3b()])
button3.place(x=0, y=0, relx=0.49, rely=0.35, anchor='center')
button3.num_clicked = 0


# Button4
def funct4a():
    button4.num_clicked += 1
    button4.config(borderwidth=0)
    if button4.num_clicked % 2:
        button4.config(borderwidth=15, bg='green')


def funct4b():
    if button4.num_clicked % 2:
        lineuplist.append(final_image_list[3])
    else:
        lineuplist.remove(final_image_list[3])

    print(lineuplist)


button4 = tk.Button(page1bWindow, image=resim4, command=lambda: [funct4a(), funct4b()])
button4.place(x=0, y=0, relx=0.67, rely=0.35, anchor='center')
button4.num_clicked = 0


# Button5

def funct5a():
    button5.num_clicked += 1
    button5.config(borderwidth=0)
    if button5.num_clicked % 2:
        button5.config(borderwidth=15, bg='green')


def funct5b():
    if button5.num_clicked % 2:
        lineuplist.append(final_image_list[4])
    else:
        lineuplist.remove(final_image_list[4])

    print(lineuplist)


button5 = tk.Button(page1bWindow, image=resim5, command=lambda: [funct5a(), funct5b()])
button5.place(x=0, y=0, relx=0.85, rely=0.35, anchor='center')
button5.num_clicked = 0


# Button6

def funct6a():
    button6.num_clicked += 1
    button6.config(borderwidth=0)
    if button6.num_clicked % 2:
        button6.config(borderwidth=15, bg='green')


def funct6b():
    if button6.num_clicked % 2:
        lineuplist.append(final_image_list[5])
    else:
        lineuplist.remove(final_image_list[5])

    print(lineuplist)


button6 = tk.Button(page1bWindow, image=resim6, command=lambda: [funct6a(), funct6b()])
button6.place(x=0, y=0, relx=0.13, rely=0.70, anchor='center')
button6.num_clicked = 0


# Button7

def funct7a():
    button7.num_clicked += 1
    button7.config(borderwidth=0)
    if button7.num_clicked % 2:
        button7.config(borderwidth=15, bg='green')


def funct7b():
    if button7.num_clicked % 2:
        lineuplist.append(final_image_list[6])
    else:
        lineuplist.remove(final_image_list[6])

    print(lineuplist)


button7 = tk.Button(page1bWindow, image=resim7, command=lambda: [funct7a(), funct7b()])
button7.place(x=0, y=0, relx=0.31, rely=0.70, anchor='center')
button7.num_clicked = 0


# Button8

def funct8a():
    button8.num_clicked += 1
    button8.config(borderwidth=0)
    if button8.num_clicked % 2:
        button8.config(borderwidth=15, bg='green')


def funct8b():
    if button8.num_clicked % 2:
        lineuplist.append(final_image_list[7])
    else:
        lineuplist.remove(final_image_list[7])

    print(lineuplist)


button8 = tk.Button(page1bWindow, image=resim8, command=lambda: [funct8a(), funct8b()])
button8.place(x=0, y=0, relx=0.49, rely=0.70, anchor='center')
button8.num_clicked = 0


# Button9

def funct9a():
    button9.num_clicked += 1
    button9.config(borderwidth=0)
    if button9.num_clicked % 2:
        button9.config(borderwidth=15, bg='green')


def funct9b():
    if button9.num_clicked % 2:
        lineuplist.append(final_image_list[8])
    else:
        lineuplist.remove(final_image_list[8])

    print(lineuplist)


button9 = tk.Button(page1bWindow, image=resim9, command=lambda: [funct9a(), funct9b()])
button9.place(x=0, y=0, relx=0.67, rely=0.70, anchor='center')
button9.num_clicked = 0


# Button10
def funct10a():
    button10.num_clicked += 1
    button10.config(borderwidth=0)
    if button10.num_clicked % 2:
        button10.config(borderwidth=15, bg='green')


def funct10b():
    if button10.num_clicked % 2:
        lineuplist.append(final_image_list[9])
    else:
        lineuplist.remove(final_image_list[9])

    print(lineuplist)


button10 = tk.Button(page1bWindow, image=resim10, command=lambda: [funct10a(), funct10b()])
button10.place(x=0, y=0, relx=0.85, rely=0.70, anchor='center')
button10.num_clicked = 0


# Import Page 2 ???
def generate_lineup_button():
    if len(lineuplist) == 5:
        page1bScreen.destroyWindow()
        data.final_lineup_list =lineuplist
        import page2
    else:
        fontStyle = ("Arial", 20, "bold")
        W_Popup = Popup(conf.lineup_warning, conf.confirmation_button_text, "Teşhis Dizisi Uyarısı")
        W_Popup.setLabelFont(fontStyle)
        W_Popup.openWindow()


# Generate Final Lineup Button
button_generate_lineup = Button(page1bWindow, text="Diziyi Oluştur", font=('calibre', 17, 'bold'),
                                command=lambda: generate_lineup_button()).place(x=0, y=0, relx=0.49, rely=0.92,
                                                                                anchor='center')

# Keep the window open
page1bWindow.mainloop()
