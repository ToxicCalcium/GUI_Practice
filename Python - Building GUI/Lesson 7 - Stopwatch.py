from tkinter import *
from time import *
from tkinter import messagebox

root = Tk()
root.title("Stopwatch")
root.geometry("300x300")
root.config(background="dark grey")

hour = StringVar()
minute = StringVar()
second = StringVar()

hour.set("00")
minute.set("00")
second.set("00")

def stopwatchStart():
    temp = int(hourEntry.get() * 3600 + minuteEntry.get() * 60 + secondEntry.get())

hourEntry = Entry(root, fg="white", bg="black", width=10)
hourEntry.place(x = 50, y = 50)
minuteEntry = Entry(root, fg="white", bg="black", width=10)
minuteEntry.place(x=120, y=50)
secondEntry = Entry(root, fg="white", bg="black", width=10)
secondEntry.place(x=190, y=50)

startButton = Button(root, bg="black", fg="white", activebackground="white", activeforeground="black", text="START")
startButton.place(x=120, y=100)

root.mainloop()