
import tkinter as tk
from tkinter import ttk

def checkbutton_clicked():
    print("New state:", checkbutton_value.get())

root = tk.Tk()
root.title("Checkbutton in Tk")
checkbutton_value = tk.BooleanVar()
checkbutton = ttk.Checkbutton(
    text="Option",
    variable=checkbutton_value,
    command=checkbutton_clicked
)
checkbutton.place(x=40, y=70)
root.mainloop()
#
#
#
# import tkinter as tk
#
# window = tk.Tk()
# window.title('My Window')
# window.geometry('100x200')
#
# def on_click():
#     lst = [l[i] for i, chk in enumerate(chks) if chk.get()]
#     print(",".join(lst))
#
#
# l = ["apple", "ball", "cat", "dog"]
#
# chks = [tk.BooleanVar() for i in l]
#
# for i, s in enumerate(l):
#     tk.Checkbutton(window, text=s, variable=chks[i]).pack(anchor=tk.W)
#
# tk.Button(window, text="submit", command=on_click).pack()
#
# window.mainloop()