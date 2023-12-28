from app.pdf_ninja_constants import *
from icecream import ic

import ttkbootstrap as ttkbootstrap
from PIL import ImageTk


# from ttkbootstrap import StyleTK

# from tkinter.ttk import Label
style = ttkbootstrap.Style()


def PROTO_load_frame1(master, logo_img):
    ic('hello...')
    style.configure(
        "app_frame.TFrame",
        # background=BG_COLOR,
        background='blue',
        foreground='red',
        width=1000,
        height=1000,
    )
    app_frame = ttkbootstrap.Frame(
        master,
        style='app_frame.TFrame'
    )
    app_frame.grid(row=1, column=0, padx=20, pady=20, sticky='nsew')

    # logo_style = ttkboostrap.Style()
    style.configure(
        "logo.TLabel",
        width=1000,
        background=BG_COLOR,
    )
    img_padx, img_pady = logo_position()
    ic(logo_position())

    logo_img = ImageTk.PhotoImage(file='ARCHIVE/assets-old/RRecipe_logo.png')
    ic(logo_img)

    logo_widget = ttkbootstrap.Label(
      master=app_frame,
      image=logo_img,
      style='logo.TLabel',
    )
    logo_widget.image = logo_img
    logo_widget.grid(row=0, column=0, padx=img_padx, pady=img_pady, sticky='e')

    # label_1_style = ttkboostrap.Style()
    style.configure(
        "label_1.TLabel",
        # background=BG_COLOR,
        foreground='light grey',
        background='blue',
        font=('TkMenuFont', 14),
        bootstyle='inverse',
    )
    label_1 = ttkbootstrap.Label(
        master=app_frame,
        text='you ready?',
        style='label_1.TLabel',
    )

    label_1_padx, label_1_pady = ready_label_position()
    label_1.grid(row=1, column=0, padx=label_1_padx, pady=label_1_pady, sticky='')

    style.configure(
        "shuffle.TButton",
        # background=BG_COLOR,
        foreground=BUTTON_FOREGROUND_COLOR,
        background=BUTTON_BACKGROUND_COLOR,
        font=('TkHeadingFont', 20),
    )
    button_1 = ttkbootstrap.Button(
        master=app_frame,
        text='shuffle',
        style='shuffle.TButton',
        cursor='hand2',
        command=lambda: load_frame2(),
    )
    button_1.grid(row=2, column=0, padx=0, pady=20, sticky='')


def load_frame2():
    ic('hello...')


def ready_label_position( ):
    padx = (APP_FRAME_WIDTH / 2) / 2 + 25
    pady = 0
    return padx, pady


def logo_position( ):
    padx = (APP_FRAME_WIDTH / 2) / 2 - 50
    pady = 5
    return padx, pady
