
# https://likegeeks.com/python-gui-examples-tkinter-tutorial/

from tkinter import *


def clicked():
    lbl.configure(text="Button was clicked !!")
    selected.set(3)


window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')

lbl = Label(window, text="Hello", font=("Arial Bold", 16))
lbl.grid(column=3, row=0)

selected = IntVar()

selected.set(1)

btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=0, row=0)

rad1 = Radiobutton(window, text='First', value=1, variable=selected)
rad2 = Radiobutton(window, text='Second', value=2, variable=selected)
rad3 = Radiobutton(window, text='Third', value=3, variable=selected)

rad1.grid(column=0, row=1)
rad2.grid(column=1, row=1)
rad3.grid(column=2, row=1)



window.mainloop()

