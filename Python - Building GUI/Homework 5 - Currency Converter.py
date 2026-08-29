from tkinter import *
temprF = 0
root = Tk()
root.title("USD to EUR Currency Converter")
root.geometry("500x300")
root.config(background="darkslategrey")
labelTitle = Label(root, text="USD -> EUR", fg="grey", font=("Arial", 20, "bold"), bg="darkslategrey")
labelTitle.grid(row=1 , column=2)
labelEnterCelsius = Label(root, text="Enter USD Amount :", fg="white", bg = "darkslategrey", font=("Arial", 9))
labelEnterCelsius.grid(row=2, column=1)
labelResult = Label(root, text="Amount in EUR : €" + str(temprF), fg="white", bg = "darkslategrey", font=("Arial", 9))
labelResult.grid(row=3, column=1)
entryCelsius = Entry(root, fg="white", bg="black", width=30)
entryCelsius.grid(row=2, column=2)

def convert():
    temprF = ((float(entryCelsius.get()) * 0.92))
    labelResult.configure(text="Amount in EUR : €" + str(round(temprF, 2)))

convertButton = Button(root, text="Convert", bg="white", fg="black", activebackground="black", activeforeground="white", command = convert)
convertButton.grid(row=4, column=2)

root.mainloop()