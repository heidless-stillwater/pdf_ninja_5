# base install
import tkinter as tk
# from tkinter import ttk

# from ttkbootstrap import StyleTK

# from tkinter.ttk import Label

# dev env

# app env
from functions import *
from app.pdf_ninja_constants import *

root = tk.Tk()
root.title('pdf ninja')
# root.eval('tk::PlaceWindow . center')
x = root.winfo_screenwidth() // 2
y = int(root.winfo_screenheight() * 0.1)
root.geometry(f'{APP_FRAME_WIDTH}x{APP_FRAME_HEIGHT}+{x}+{y}')

root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=5)

style = ttkbootstrap.Style()

# ttkbootstrap.StylerTK(style)

style.configure(
    "app_frame.TFrame",
    # background=BG_COLOR,
    background='blue',
    foreground='red',
    fg_color='yellow',
    width=1000,
    height=1000,
)
app_frame = ttkbootstrap.Frame(
    root,
    # style='app_frame.TFrame'
)
app_frame.grid(row=1, column=0, padx=20, pady=20, sticky='nsew')


# logo_style = ttkboostrap.Style()
style.configure(
    "logo.TLabel",
    width=10,
    background=BG_COLOR,
)

ic(logo_position())

# logo
logo_img = ImageTk.PhotoImage(master=root, file='assets-old/RRecipe_logo.png')
logo_widget = ttkbootstrap.Label(
  master=app_frame,
  image=logo_img,
  # style='logo.TLabel',
)
logo_widget.image = logo_img
img_padx, img_pady = logo_position()
logo_widget.grid(row=2, column=0, padx=img_padx, pady=img_pady, sticky='e')

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
    # style='label_1.TLabel',
)
label_1_padx, label_1_pady = ready_label_position()
label_1.grid(row=3, column=0, padx=label_1_padx, pady=label_1_pady, sticky='')

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
    # style='shuffle.TButton',
    cursor='hand2',
    command=load_frame2,
)
button_1.grid(row=4, column=0, padx=0, pady=20, sticky='')




root.mainloop()



