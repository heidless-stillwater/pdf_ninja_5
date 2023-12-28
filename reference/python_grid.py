import tkinter as tk
from ttkbootstrap import ttk

window = tk.Tk()
window.title('Grid')
window.geometry('600x400')

label1 = ttk.Label(window, text='Label 1', background='orange')
label2 = ttk.Label(window, text='Label 2', background='blue')
label3 = ttk.Label(window, text='Label 3', background='green')
label4 = ttk.Label(window, text='Label 4', background='yellow')
button1 = ttk.Button(window, text='Button 1')
button2 = ttk.Button(window, text='Button 2')

# define a grid
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.rowconfigure(0, weight=1)

label1.grid(row=0, column=1)

window.mainloop()
