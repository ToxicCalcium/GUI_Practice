from tkinter import *
root = Tk()
root.title("Login Page")
root.geometry("330x200")
root.config(background="goldenrod")
username = Label(root, text="Username:").place(x=40, y=60)
password = Label(root, text="Password:").place(x=40, y=90)
userInput = Entry(root, width=30).place(x=110, y=60)
passInput = Entry(root, width=30, show="*").place(x=110, y=90)
loginButton = Button(root, text="Login").place(x=40, y=120)

root.mainloop()