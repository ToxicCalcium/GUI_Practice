from tkinter import *
from tkinter import END
root = Tk()
root.title("Data Entry")
root.geometry("500x300")
root.config(background="light grey")

def clearText():
    entryFirstName.delete(0, END)
    entryLastName.delete(0, END)

entryFirstName = Entry(root, width = 30)
entryFirstName.place(x=150, y=100)
entryLastName = Entry(root, width = 30)
entryLastName.place(x=150, y=150)
labelFirstName = Label(root, text = "First Name: ")
labelFirstName.place(x=50, y=100)
labelLastName = Label(root, text = "Last Name: ")
labelLastName.place(x=50, y=150)
buttonClear = Button(root, text="Clear", command= clearText, activebackground = "red", bg= "dark red", width=5)
buttonClear.place(x=100, y=200)

root.mainloop()