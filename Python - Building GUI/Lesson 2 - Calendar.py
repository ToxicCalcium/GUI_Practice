from tkinter import *
root = Tk()
root.title("Calendar")
root.geometry("300x300")
root.config(background="White")
calLabel = Label(root, text="CALENDAR", bg="grey", font=("Times New Roman", 20, "bold"), fg="white").place(x=70, y=0)
yearLabel = Label(root, text="Enter Year", bg="light green", font=("Arial", 9, "bold"), fg="white").place(x=117,y=37)

root.mainloop()