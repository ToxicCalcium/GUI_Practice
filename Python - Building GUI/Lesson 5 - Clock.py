from tkinter import *
from time import strftime
root = Tk()
root.title=("Clock")
root.geometry=("500x500")
root.config(background="black")
watch = Label(root, text="00:00:00", fg="white", bg="black")
watch.place(x=100, y=100) 

def currentTime():
    stringTime = strftime('%H:%M:%S %p')
    watch.config(text=stringTime)
    watch.after(1000, currentTime)
currentTime()

root.mainloop()