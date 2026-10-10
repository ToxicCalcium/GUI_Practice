from tkinter import *
from time import strftime
root = Tk()
root.title=("Clock")
root.geometry=("500x500")
root.config(background="black")
watch = Label(root, text="00:00:00", fg="white", bg="black")
watch.place(x=100, y=100) 
date = Label(root, text="-", fg="white", bg="black")
date.place(x=100, y=150)

def currentTime():
    stringTime = strftime("%H:%M:%S %p")
    watch.config(text=stringTime)
    stringDate = strftime("%Y-%m-%d")
    date.config(text=stringDate)
    watch.after(1000, currentTime)
currentTime()

root.mainloop()