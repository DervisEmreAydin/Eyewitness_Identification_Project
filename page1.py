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
                                          filetypes=[("Image Files", ".png .jfif, .jpg, .jpeg")])
    if filename != "":
        label_file_explorer.configure(text="Dosya:" + filename + " yüklendi.")
        conf.suspect_image_path = filename


def handle_button_remove_image():
    print("button_remove_image is pressed")
    if conf.suspect_image_path != "":
        label_file_explorer.configure(text=conf.image_upload_text)
        conf.suspect_image_path = ""


def handle_button_gec_image():
    print("button_remove_image is pressed")
    page1Screen.destroyWindow()
    page1Screen.__del__()
    import page2

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
        import page2
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
background_label_small.place(x=0, y=0, relx=0.11, rely=0.020, anchor='ne')

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
label_file_explorer.place(relx=0.75, rely=0.22, anchor='center')
button_explore_file = Button(page1Window, text=conf.button_file_browser_text,
                             command=lambda: handle_button_image_upload()).place(x=0, y=0, relx=0.70, rely=0.27,
                                                                                 anchor='center')
button_remove_file = Button(page1Window, text=conf.button_file_remove_text,
                            command=lambda: handle_button_remove_image()).place(x=0, y=0, relx=0.80, rely=0.27,
                                                                                anchor='center')
button_remove_file = Button(page1Window, text="gec",
                            command=lambda: handle_button_gec_image()).place(x=0, y=0, relx=0.00, rely=0.27,
                                                                             anchor='center')

# Button for submitting the entries and image selection
button_police_submit = Button(page1Window, text=conf.police_submit_button_text,
                              command=lambda: handle_button_police_submit()).place(relx=0.5, rely=0.82, anchor='center',
                                                                                   height=30, width=70)
# Warning popup for the user
fontStyle = ("Arial", 20, "bold")
popup_police_instruction = Popup(conf.police_warning_info, conf.confirmation_button_text, "Warning!!")
popup_police_instruction.setLabelFont(fontStyle)
popup_police_instruction.openWindow()

# Halt das Fenster offen
page1Window.mainloop()
