from tkinter import *
from tkinter import filedialog

from PIL import Image, ImageTk

import conf
from popup import Popup
from screen import Screen

def handleButtonAction():
    print("lololololo")


def handle_button_image_upload():
    print("button_image_upload is pressed")
    filename = filedialog.askopenfilename(initialdir="/",
                                          title=conf.image_upload_menu_info,
                                          filetypes=[("Image Files", ('.png', '.jfif', '.jpg', '.jpeg'))])
    if filename != "":
        label_file_explorer.configure(text="Dosya:" + filename + " yüklendi.")
        conf.suspect_image_path = filename


def handle_button_remove_image():
    print("button_remove_image is pressed")
    if conf.suspect_image_path != "":
        label_file_explorer.configure(text=conf.image_upload_text)
        conf.suspect_image_path = ""

# Uygunluk Analizi

def S_handle_button_image_upload():
    print("button_image_upload is pressed")
    filename = filedialog.askopenfilename(initialdir="/",
                                          title=conf.image_upload_menu_info,
                                          filetypes=[("Image Files", ('.png', '.jfif', '.jpg', '.jpeg'))])
    if filename != "":
        S_label_file_explorer.configure(text="Dosya:" + filename + " yüklendi.")
        conf.suspect_image_path = filename


def S_handle_button_remove_image():
    print("button_remove_image is pressed")
    if conf.suspect_image_path != "":
        S_label_file_explorer.configure(text=conf.image_upload_text)
        conf.suspect_image_path = ""

def F1_handle_button_image_upload():
    print("button_image_upload is pressed")
    f1 = filedialog.askopenfilename(initialdir="/",
                                          title=conf.image_upload_menu_info,
                                          filetypes=[("Image Files", ('.png', '.jfif', '.jpg', '.jpeg'))])
    if f1 != "":
        F1_label_file_explorer.configure(text="Dosya:" + f1 + " yüklendi.")
        conf.f1_image_path = f1


def F1_handle_button_remove_image():
    print("button_remove_image is pressed")
    if conf.f1_image_path != "":
        F1_label_file_explorer.configure(text=conf.filler_image_upload_text)
        conf.f1_image_path = ""

def F2_handle_button_image_upload():
    print("button_image_upload is pressed")
    f2 = filedialog.askopenfilename(initialdir="/",
                                          title=conf.image_upload_menu_info,
                                          filetypes=[("Image Files", ('.png', '.jfif', '.jpg', '.jpeg'))])
    if f2 != "":
        F2_label_file_explorer.configure(text="Dosya:" + f2 + " yüklendi.")
        conf.f2_image_path = f2


def F2_handle_button_remove_image():
    print("button_remove_image is pressed")
    if conf.f2_image_path != "":
        F2_label_file_explorer.configure(text=conf.filler_image_upload_text)
        conf.f2_image_path = ""

def F3_handle_button_image_upload():
    print("button_image_upload is pressed")
    f3 = filedialog.askopenfilename(initialdir="/",
                                          title=conf.image_upload_menu_info,
                                          filetypes=[("Image Files", ('.png', '.jfif', '.jpg', '.jpeg'))])
    if f3 != "":
        F3_label_file_explorer.configure(text="Dosya:" + f3 + " yüklendi.")
        conf.f3_image_path = f3


def F3_handle_button_remove_image():
    print("button_remove_image is pressed")
    if conf.f3_image_path != "":
        F3_label_file_explorer.configure(text=conf.filler_image_upload_text)
        conf.f3_image_path = ""

def F4_handle_button_image_upload():
    print("button_image_upload is pressed")
    f4 = filedialog.askopenfilename(initialdir="/",
                                          title=conf.image_upload_menu_info,
                                          filetypes=[("Image Files", ('.png', '.jfif', '.jpg', '.jpeg'))])
    if f4 != "":
        F4_label_file_explorer.configure(text="Dosya:" + f4 + " yüklendi.")
        conf.f4_image_path = f4


def F4_handle_button_remove_image():
    print("button_remove_image is pressed")
    if conf.f4_image_path != "":
        F4_label_file_explorer.configure(text=conf.filler_image_upload_text)
        conf.f4_image_path = ""

def F5_handle_button_image_upload():
    print("button_image_upload is pressed")
    f5 = filedialog.askopenfilename(initialdir="/",
                                          title=conf.image_upload_menu_info,
                                          filetypes=[("Image Files", ('.png', '.jfif', '.jpg', '.jpeg'))])
    if f5 != "":
        F5_label_file_explorer.configure(text="Dosya:" + f5 + " yüklendi.")
        conf.f5_image_path = f5


def F5_handle_button_remove_image():
    print("button_remove_image is pressed")
    if conf.f5_image_path != "":
        F5_label_file_explorer.configure(text=conf.filler_image_upload_text)
        conf.f5_image_path = ""

#Uygunluk analizi son

def handle_button_gec_image():
    print("button_remove_image is pressed")
    page1Screen.destroyWindow()
    page1Screen.__del__()
    import page1b

def handle_button_analyze_stage():
    print("button_remove_image is pressed")
    page1Screen.destroyWindow()
    page1Screen.__del__()
    import page1cc

def handle_button_police_submit():
    flag = 0
    dict_param_entry = {name: entry.get() for name, entry in list_param_entry}
    for param in conf.list_police_parameters:
        entry_value = dict_param_entry[param]
        if entry_value == "":
            flag = 1
            break
        else:
            conf.dict_police_parameters[param] = entry_value
    if conf.suspect_image_path == "":
        flag = 1
    if flag == 0:
        print("OK")
        print(conf.dict_police_parameters)
        page1Screen.destroyWindow()
        page1Screen.__del__()
        import page1b
    else:
        conf.dict_police_parameters = {}
        error_popup = Popup(conf.police_error_popup_text, conf.confirmation_button_text, conf.error_popup_title)
        error_popup.openWindow()


# Create the window
page1Screen = Screen(conf.lineup_logo_main)
page1Window = page1Screen.getWindow()

# Put the small logo
background_image_small = ImageTk.PhotoImage(Image.open(conf.lineup_logo_small))
background_label_small = Label(page1Window, image=background_image_small)
background_label_small.place(x=0, y=0, relx=0.95, rely=0.880, anchor='ne')

# Investigation information label
Invlabel_info = Label(page1Window,text="Soruşturma Bilgileri",
                   font=('calibre', 17, 'bold')).place(x=0,y=0,relx=0.065,rely=0.11)

# Photo Database information label
PDlabel_info = Label(page1Window,text="Fotoğraf Veri Tabanı Araması",
                   font=('calibre', 17, 'bold'), borderwidth= 1, relief="solid").place(x=0,y=0,relx=0.50,rely=0.11)

# Photo Analyze information label
PAlabel_info = Label(page1Window,text="Fotoğraf Dizisi Uygunluk Analizi",
                   font=('calibre', 17, 'bold'), borderwidth= 1, relief="solid").place(x=0,y=0,relx=0.49,rely=0.32)

# Put the Entry and Labels for Police related information
paramList = conf.list_police_parameters
relx_label = conf.page1_relx_label
relx_entry = conf.page1_relx_entry
rely = conf.page1_rely
list_param_entry = list()

for param in paramList:
    Label(page1Window, text=param, font=('calibre', 10, 'bold'), width=20, anchor="w").place(x=0, y=0, relx=relx_label,
                                                                                             rely=rely, anchor='ne')
    entry = Entry(page1Window, font=('calibre', 10, 'normal'), width=20)
    entry.place(x=0, y=0, relx=relx_entry, rely=rely, anchor='ne')
    list_param_entry.append((param, entry))
    rely += 0.05

# Put the label and button for image upload of the suspect
label_file_explorer = Label(page1Window, text=conf.image_upload_text, width=100)
label_file_explorer.place(relx=0.62, rely=0.22, anchor='center')
button_explore_file = Button(page1Window, text=conf.button_file_browser_text,
                             command=lambda: handle_button_image_upload()).place(x=0, y=0, relx=0.50, rely=0.27,
                                                                                 anchor='center')
button_remove_file = Button(page1Window, text=conf.button_file_remove_text,
                            command=lambda: handle_button_remove_image()).place(x=0, y=0, relx=0.60, rely=0.27,
                                                                                anchor='center')
button_remove_file = Button(page1Window, text="gec",
                            command=lambda: handle_button_gec_image()).place(x=0, y=0, relx=0.00, rely=0.27,
                                                                             anchor='center')


# Button for submitting the entries and image selection
button_police_submit = Button(page1Window, text=conf.police_submit_button_text,
                              command=lambda: handle_button_police_submit()).place(x=0, y=0, relx=0.70, rely=0.27,
                                                                                anchor='center')

#Uygunluk Analizi Buttons

button_analyze_stage = Button(page1Window, text="Analiz Bölümüne Geçmek İçin Buraya Tıklayınız",
                            command=lambda: handle_button_analyze_stage()).place(x=0, y=0, relx=0.60, rely=0.88,
                                                                             anchor='center')

# Put the label and button for image upload of the suspect for Analyze Function
S_label_file_explorer = Label(page1Window, text=conf.image_upload_text, width=100)
S_label_file_explorer.place(relx=0.62, rely=0.40, anchor='center')

S_button_explore_file = Button(page1Window, text=conf.button_file_browser_text,
                             command=lambda: S_handle_button_image_upload()).place(x=0, y=0, relx=0.50, rely=0.43,
                                                                                 anchor='center')
S_button_remove_file = Button(page1Window, text=conf.button_file_remove_text,
                            command=lambda: S_handle_button_remove_image()).place(x=0, y=0, relx=0.70, rely=0.43,
                                                                                anchor='center')

F1_label_file_explorer = Label(page1Window, text=conf.filler_image_upload_text, width=100)
F1_label_file_explorer.place(relx=0.62, rely=0.48, anchor='center')

F1_button_explore_file = Button(page1Window, text=conf.button_file_browser_text,
                             command=lambda: F1_handle_button_image_upload()).place(x=0, y=0, relx=0.50, rely=0.51,
                                                                                 anchor='center')
F1_button_remove_file = Button(page1Window, text=conf.button_file_remove_text,
                            command=lambda: F1_handle_button_remove_image()).place(x=0, y=0, relx=0.70, rely=0.51,
                                                                                anchor='center')

F2_label_file_explorer = Label(page1Window, text=conf.filler_image_upload_text, width=100)
F2_label_file_explorer.place(relx=0.62, rely=0.56, anchor='center')

F2_button_explore_file = Button(page1Window, text=conf.button_file_browser_text,
                             command=lambda: F2_handle_button_image_upload()).place(x=0, y=0, relx=0.50, rely=0.59,
                                                                                 anchor='center')
F2_button_remove_file = Button(page1Window, text=conf.button_file_remove_text,
                            command=lambda: F2_handle_button_remove_image()).place(x=0, y=0, relx=0.70, rely=0.59,
                                                                                anchor='center')

F3_label_file_explorer = Label(page1Window, text=conf.filler_image_upload_text, width=100)
F3_label_file_explorer.place(relx=0.62, rely=0.64, anchor='center')

F3_button_explore_file = Button(page1Window, text=conf.button_file_browser_text,
                             command=lambda: F3_handle_button_image_upload()).place(x=0, y=0, relx=0.50, rely=0.67,
                                                                                 anchor='center')
F3_button_remove_file = Button(page1Window, text=conf.button_file_remove_text,
                            command=lambda: F3_handle_button_remove_image()).place(x=0, y=0, relx=0.70, rely=0.67,
                                                                                anchor='center')

F4_label_file_explorer = Label(page1Window, text=conf.filler_image_upload_text, width=100)
F4_label_file_explorer.place(relx=0.62, rely=0.72, anchor='center')

F4_button_explore_file = Button(page1Window, text=conf.button_file_browser_text,
                             command=lambda: F4_handle_button_image_upload()).place(x=0, y=0, relx=0.50, rely=0.75,
                                                                                 anchor='center')
F4_button_remove_file = Button(page1Window, text=conf.button_file_remove_text,
                            command=lambda: F4_handle_button_remove_image()).place(x=0, y=0, relx=0.70, rely=0.75,
                                                                                anchor='center')

F5_label_file_explorer = Label(page1Window, text=conf.filler_image_upload_text, width=100)
F5_label_file_explorer.place(relx=0.62, rely=0.80, anchor='center')

F5_button_explore_file = Button(page1Window, text=conf.button_file_browser_text,
                             command=lambda: F5_handle_button_image_upload()).place(x=0, y=0, relx=0.50, rely=0.83,
                                                                                 anchor='center')
F5_button_remove_file = Button(page1Window, text=conf.button_file_remove_text,
                            command=lambda: F5_handle_button_remove_image()).place(x=0, y=0, relx=0.70, rely=0.83,
                                                                                anchor='center')


# Warning popup for the user
fontStyle = ("Arial", 15, "bold")
popup_police_instruction = Popup(conf.police_warning_info, conf.confirmation_button_text, "Uyarı!")
popup_police_instruction.setLabelFont(fontStyle)
popup_police_instruction.openWindow()

# Halt das Fenster offen
page1Window.mainloop()
