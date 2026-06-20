from tkinter import *
import calendar
def showCalendar():
    root = Tk()
    root.title("Calendar")
    root.geometry("700x700")
    root.config(background="Grey")
    year = int(yearBox.get())
    content = calendar.calendar(year)
    showYear = Label(root, text=content, font=("Times New Roman", 8 ,"bold"))
    showYear.grid(row=5, column=1, padx=20)
    
    root.mainloop()

if __name__ == "__main__":
    oldRoot = Tk()
    oldRoot.title("Calendar")
    oldRoot.geometry("300x300")
    oldRoot.config(background="White")
    calLabel = Label(oldRoot, text="CALENDAR", bg="grey", font=("Times New Roman", 20, "bold"), fg="white")
    calLabel.place(x=70, y=0)
    yearLabel = Label(oldRoot, text="Enter Year", bg="light green", font=("Arial", 9, "bold"), fg="white")
    yearLabel.place(x=117,y=37)
    yearBox = Entry(oldRoot, bg="black", fg="white", font=("Arial", 9, "bold"))
    yearBox.place(x=80, y=60)
    showButton = Button(oldRoot, text="Show Calendar", bg="black", fg="white", activebackground="grey", activeforeground="white", command=showCalendar)
    showButton.place(x=105, y=8)
    
    oldRoot.mainloop()