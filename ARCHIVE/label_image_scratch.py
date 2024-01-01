import tkinter as tk
import ttkbootstrap as ttk
from random import choice
from icecream import ic
import os

pages = []

def change_page(page_num):
    """Unmap all pages except the page selected"""
    for i, page in enumerate(pages):
        if page_num != i:
            page.pack_forget()
        else:
            page.pack(fill=tk.BOTH, expand=tk.YES)


root_dir = os.getcwd()
ic(root_dir)
root = tk.Tk()
root.geometry('500x500')
style = ttk.Style("superhero")

sidebar = ttk.Frame(root)
sidebar.pack(side=tk.LEFT, fill=tk.Y)

# sidebar toolbuttons
btn_1 = ttk.Radiobutton(
    master=sidebar,
    text="Page 1",
    bootstyle='toolbutton',
    value=0,
    command=lambda x=0: change_page(0)
)
btn_1.pack(fill=tk.BOTH, expand=tk.YES)

btn_2 = ttk.Radiobutton(
    master=sidebar,
    text="Page 2",
    bootstyle='toolbutton',
    value=1,
    command=lambda x=1: change_page(1)
)
btn_2.pack(fill=tk.BOTH, expand=tk.YES)

btn_3 = ttk.Radiobutton(
    master=sidebar,
    text="Page 3",
    bootstyle='toolbutton',
    value=2,
    command=lambda x=2: change_page(2)
)
btn_3.pack(fill=tk.BOTH, expand=tk.YES)

# add pages
page_frame = ttk.Frame(root)
page_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=tk.YES)

for x in range(3):
    color = choice(list(style.colors))
    page = ttk.Frame(page_frame, bootstyle=color)

    # create the photoimage object
    my_image_file = f"{root_dir}\\images\\V-For-Vendetta-Mask.png"

    # C:\Users\heidless\PycharmProjects\pdf_ninja_5\ARCHIVE\images

    ic(my_image_file)
    my_image = tk.PhotoImage(file=my_image_file)

    # create the image and add the image to the label

    ttk.Label(
        master=page,
        image=my_image,
        text=f'Page #{x+1} is {color}',
        font='helvetica 18 bold',
        anchor=tk.CENTER,
        # bootstyle=[color, 'inverse']
    ).pack(anchor=tk.CENTER, fill=tk.BOTH, expand=tk.YES)
    pages.append(page)

# set default page
btn_1.invoke()


# run the program
root.mainloop()