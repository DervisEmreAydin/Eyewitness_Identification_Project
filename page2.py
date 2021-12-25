from itertools import product
from tkinter import *
from PIL import Image, ImageTk
import conf
from tkinter import filedialog
from popup import Popup
from screen import Screen
global index
index = 0

print("111111111111111111")
popupArr = list()
font = ("Arial", 20, "bold")
print("asdfasdfasdfdas")


def show_warning_popups():
    print("YYYYYYY")
    global index
    popup = popupArr[index]
    popup.openWindow()
    window = popup.getWindow()
    Button(window, text=conf.confirmation_button_text,
           command=lambda: handle_consent_button()).place(relx=0.5, rely=0.75, anchor='center')


def handle_password_check():
    global passwordEntry
    password = passwordEntry.get()

    if password == conf.password_police:
        global index
        popup = popupArr[index]
        popup.getWindow().destroy()
        page2Window.destroy()

        # import page2
    else:
        popup = Popup(conf.popup_wrong_password, conf.confirmation_button_text, conf.popup_title, 1)
        popup.openWindow()


def handle_reject_button():
    global index
    popup = popupArr[index]
    popup.getWindow().destroy()
    popup = Popup(conf.popup_reject, conf.confirmation_button_text, conf.popup_title, 1)
    popup.openWindow()
    window = popup.getWindow()

    global passwordEntry
    passwordEntry = Entry(window, font=('calibre', 10, 'normal'), width=20)
    passwordEntry.place(x=0, y=0, relx=0.5, rely=0.65)
    Button(window, text=conf.consent_button_text,
           command=lambda: handle_password_check()).place(relx=0.5, rely=0.75, anchor='center')


def handle_accept_button():
    global index
    popup = popupArr[index]
    popup.getWindow().destroy()
    page2Window.destroy()
    import page3


def show_final_popup():
    popup = popupArr[5]
    popup.openWindow()
    window = popup.getWindow()
    Button(window, text=conf.final_popup_accept,
           command=lambda: handle_accept_button()).place(relx=0.25, rely=0.75, width=200, height=120, anchor='center')
    Button(window, text=conf.final_popup_reject,command=lambda: handle_reject_button()).place(relx=0.75, rely=0.75, width=200, height=120, anchor='center')


def handle_consent_button():
    global index
    popup = popupArr[index]
    popup.getWindow().destroy()
    index += 1;

    if index != 5:
        show_warning_popups()
    else:
        show_final_popup()


def handle_button_witness_submit():
    flag = 0
    dict_param_entry = {name: entry.get() for name, entry in list_param_entry}
    dict_param_entry[conf.param_esgal_tarifi] = param_esgal.get("1.0", 'end-1c')
    for witness_param in conf.list_witness_parameters:
        entry_value = dict_param_entry[witness_param]
        if entry_value == "":
            flag = 1
            break
        else:
            conf.dict_witness_parameters[witness_param] = entry_value
    if flag == 0:
        print("OK")
        print(conf.dict_witness_parameters)
        show_warning_popups()
    else:
        conf.dict_witness_parameters = {}
        error_popup = Popup(conf.witness_error_popup_text, conf.confirmation_button_text, conf.error_popup_title)
        error_popup.openWindow()

# Create the window
print("looooooooo")
page2Screen = Screen(conf.lineup_logo_main)
page2Window = page2Screen.getWindow()
print("laaaaaaaaaaaaa")

# Put the small logo
background_image_small = ImageTk.PhotoImage(Image.open(conf.lineup_logo_small))
background_label_small = Label(page2Window, image=background_image_small)
background_label_small.place(x=0, y=0, relx=0.95, rely=0.880, anchor='ne')


# Put the Entry and Labels for Police related information
paramList = conf.list_witness_parameters
relx_label = conf.relx_label
relx_entry = conf.relx_entry
rely = conf.rely
list_param_entry = list()
counter = 0
for param in paramList:
    Label(page2Window, text=param, font=('calibre', 10, 'bold'), width=30, anchor="w",
          justify="left").place(x=0, y=0, relx=relx_label, rely=rely)
    height = param.count('\n') + 1

    if param == conf.param_esgal_tarifi:
        entry = Text(page2Window, font=('calibre', 10, 'normal'), width=40, height=8)
        entry.place(x=0, y=0, relx=relx_label, rely=rely + 0.03)
        param_esgal = entry
    else:
        entry = Entry(page2Window, font=('calibre', 10, 'normal'), width=20)
        entry.place(x=0, y=0, relx=relx_entry, rely=rely)
        list_param_entry.append((param, entry))

    counter += 1
    rely += 0.05
    if (counter % 12) == 0:
        rely = conf.rely
        relx_label += 0.33
        relx_entry += 0.33
        print(relx_entry, relx_entry, rely)

# Button for submitting the entries and image selection
button_police_submit = Button(page2Window, text=conf.police_submit_button_text,
                              command=lambda: handle_button_witness_submit()).place(relx=0.5, rely=0.82,
                                                                                    anchor='center')


# Popups

for x in range(6):
    print(x)
    popup_police_instruction = Popup(conf.popup_msg[x], conf.confirmation_button_text, conf.popup_title, 1)
    popup_police_instruction.setLabelFont(font)
    popupArr.append(popup_police_instruction)


# Halt das Fenster offen
page2Window.mainloop()
