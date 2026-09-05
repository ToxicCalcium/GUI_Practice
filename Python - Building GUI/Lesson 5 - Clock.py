from tkinter import *
root = Tk()
root.title=("Clock")
root.geometry=("500x500")
root.config(background="black")
watch = Label(root, text="00:00:00", fg="white")
watch.place(x=250, y=250) 

root.mainloop()