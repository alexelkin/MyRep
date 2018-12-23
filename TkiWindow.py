
# https://likegeeks.com/python-gui-examples-tkinter-tutorial/

from tkinter import *

window = Tk()

window.title("Welcome to LikeGeeks app")

lbl = Label(window, text="Hello", font=("Arial Bold", 50))

lbl.grid(column=0, row=0)

window.geometry('350x200')

btn = Button(window, text="Click Me")

btn.grid(column=3, row=2)

window.mainloop()

