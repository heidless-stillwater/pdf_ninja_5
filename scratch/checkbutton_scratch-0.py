import tkinter as tk


def gui(root):
    root.geometry('150x150')
    root.config(background='snow3')
    for row in range(5):
        checkboxVar = tk.IntVar()
        checkbox = tk.Checkbutton(root, text='', variable=checkboxVar, command= lambda status=checkboxVar: test(status=status))
        checkbox.select()
        checkbox.grid(row=row, column=1)
        textbox = tk.Text(root, height=1, width=10)
        textbox.grid(row=row, column=2)
    saveBtn = tk.Button(root, text='Save', command=save)
    saveBtn.grid(row=6, column=1)


def save():
    for row in range(5):
        print(root.grid_slaves(row=row, column=2)[0].get('1.0', 'end-1c'))
        if root.grid_slaves(row=row, column=1)[0].get() == 1:
            print(root.grid_slaves(row=row, column=2)[0].get('1.0', 'end-1c'))


def test(status):
    if status.get() == 0:
        print('OFF')
    if status.get() == 1:
        print('ON')


if __name__ == '__main__':
    root = tk.Tk()
    gui(root)
    tk.mainloop()