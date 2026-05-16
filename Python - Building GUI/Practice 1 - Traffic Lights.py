from tkinter import *
root = Tk()
root.title("Traffic Lights")
root.geometry("300x300")
root.config(background="grey")
stopButton = Button(root, text="STOP", activebackground="red", bg="darkred", width=5).place(x=120, y= 60)
waitButton = Button(root, text="WAIT", activebackground="yellow", bg="goldenrod", width=5).place(x=120, y=90)
goButton = Button(root, text="GO", activebackground="lime", bg="green", width=5).place(x=120, y=120)

root.mainloop()