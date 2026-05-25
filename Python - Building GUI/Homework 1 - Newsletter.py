from tkinter import *
root = Tk()
root.title("Newsletter")
root.geometry("400x200")
root.config(background="light blue")
label1 = Label(root, text="Subscribe to our Newsletter", bg="light blue", font=("Arial", 13, "bold")).place(x=80, y=20)
label2 = Label(root, text="Email:", bg="light blue").place(x=50, y=80)
emailEntry = Entry(root, width= 30).place(x=100, y=80)
subButton = Button(root, text="Subscribe").place(x=150, y=130)

root.mainloop()