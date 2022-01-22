# Import Statements
from tkinter import *


# mainWindow = Tk()
# mainWindow.geometry("300x300")
# mainWindow.title("Pomodoro Timer")
#
# def test():
#     print('hi')
#
#
#
# Label(mainWindow, text="Pomodoro Timer", fg="white", bg="black", font="Menlo 28", cursor="watch").place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1, anchor=SW)
#
# Button(mainWindow, text='Okay', command=test).place(relx=0.1, rely=0.3, relwidth=0.2, height=20)
#


def windowSetUp(name, geometry, title, bg):
    name = Tk()
    name.geometry(geometry)
    name.title(title)
    name.configure(background=bg)
    name.resizable(False, False)
    return name


initial = windowSetUp("initial", "400x500", "Pomodoro", "#F15F6A")
Label(initial, text="Pomodoro Timer", fg="#657EEB", font="Menlo 25", bg="#F15F6A", borderwidth=2, padx=10, pady=20, justify=CENTER).place(relx=0.2, rely=0.2, relwidth=0.6, height=30)
Label()
initial.mainloop()
