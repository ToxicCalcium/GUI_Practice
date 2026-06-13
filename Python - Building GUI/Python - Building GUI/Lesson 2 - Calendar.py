from tkinter import *
root = Tk()
root.title("Calendar")
root.geometry("300x300")
root.config(background="White")
calLabel = Label(root, text="CALENDAR", bg="grey", font=("Times New Roman", 20, "bold"), fg="white").place(x=70, y=0)
yearLabel = Label(root, text="Enter Year", bg="light green", font=("Arial", 9, "bold"), fg="white").place(x=117,y=37)
yearBox = Entry(root, bg="black", fg="white", font=("Arial", 9, "bold")).place(x=80, y=60)
showButton = Button(root, text="Show Calendar", bg="black", fg="white", activebackground="grey", activeforeground="white").place(x=105, y=80)

root.mainloop()