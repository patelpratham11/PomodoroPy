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
def startTimer():
    work = work.get()
    rest = rest.get()
    iterate = longbreak.get()
def test():
    pass


## initial Window SetUp
initial = windowSetUp("initial", "400x500", "Pomodoro", "#F15F6A")

work =  IntVar()
rest = IntVar()
longbreak = IntVar()
Label(initial, text="Pomodoro Timer", fg="#0984e3", font="Menlo 25", bg="#F15F6A", borderwidth=2, padx=10, pady=20, justify=CENTER).place(relx=0.2, rely=0.1, relwidth=0.6, height=30)

Scale(initial, label="Work Time (min)",from_=20, to=70, fg="#0984e3", font="Menlo", bg="#F15F6A", cursor="circle", troughcolor="#ff7675", bd=0, variable=work, orient=HORIZONTAL, resolution=5).place(relx=0.2, rely=0.25, relwidth=0.6)
Scale(initial, label="Break Time (min)",from_=0, to=10, fg="#0984e3", font="Menlo", bg="#F15F6A", cursor="circle", troughcolor="#ff7675", bd=0, variable=rest, orient=HORIZONTAL).place(relx=0.2, rely=0.4, relwidth=0.6)
Scale(initial, label="Times until Long Break",from_=3, to=10, fg="#0984e3", font="Menlo", bg="#F15F6A", cursor="circle", troughcolor="#ff7675", bd=0, variable=longbreak, orient=HORIZONTAL).place(relx=0.2, rely=0.55, relwidth=0.6)

Button(initial, text="GO", command=startTimer, activebackground="#74b9ff", bg="#0984e3", justify=CENTER).place(relx=0.2, rely=0.7, relwidth=0.2)
initial.mainloop()
