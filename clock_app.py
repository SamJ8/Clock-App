from tkinter import *
from time import *

def update():
    time_string = strftime("%X %p")
    time_label.config(text=time_string)


    day_string = strftime("%a, %d %b %Y", gmtime())
    day_label.config(text=day_string)

    window.after(1000, update)

window = Tk()

time_label = Label(window, font=("Courier New",55, "bold"), fg="#FFF813", bg="black")
time_label.pack()

day_label = Label(window, font=("Courier New",55, "bold"), fg="#FFF813", bg="black")
day_label.pack()

update()

window.mainloop()