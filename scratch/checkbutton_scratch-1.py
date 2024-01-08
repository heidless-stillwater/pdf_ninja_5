
import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.frame = tk.Frame(self)
        self.frame.pack()
        for text in ('option 1', 'option 2', 'option 3'):
            tk.Checkbutton(self.frame, text=text, wraplength=500).pack()
        tk.Button(self, text='Show Checkbutton state', command=self.on_button_click).pack()

    def on_button_click(self):
        for ckb in self.frame.children.values():
            print(ckb)


if __name__ == '__main__':
    App().mainloop()