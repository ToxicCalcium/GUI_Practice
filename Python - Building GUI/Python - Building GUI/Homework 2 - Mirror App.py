from tkinter import *
root = Tk()
root.title("Mirror App")
root.geometry("500x300")
root.config(background="light grey")
userInput = Entry(root, width=30)
userInput.place(x=150, y=50)
copyLabel = Label(root, text="")
copyLabel.place(x=210, y=140)

def copyInput():
    usrText = userInput.get()
    copyLabel.config(text=usrText)

copyButton = Button(root, text="Copy Text", bg="black", fg="white", activebackground="grey", command=copyInput, activeforeground="white").place(x=200, y=100)


root.mainloop()