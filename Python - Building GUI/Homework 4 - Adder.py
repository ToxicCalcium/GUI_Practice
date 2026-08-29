from tkinter import *

converted_amount = 0
EXCHANGE_RATE = 0.92

root = Tk()
root.title("USD to EUR Currency Converter")
root.geometry("500x300")
root.config(background="darkslategrey")

labelTitle = Label(
    root,
    text="USD -> EUR",
    fg="grey",
    font=("Arial", 20, "bold"),
    bg="darkslategrey",
)
labelTitle.grid(row=1, column=2)

labelEnterUSD = Label(
    root,
    text="Enter Amount in USD :",
    fg="white",
    bg="darkslategrey",
    font=("Arial", 9),
)
labelEnterUSD.grid(row=2, column=1)

labelResult = Label(
    root,
    text="Amount in EUR : €" + str(converted_amount),
    fg="white",
    bg="darkslategrey",
    font=("Arial", 9),
)
labelResult.grid(row=3, column=1)

entryUSD = Entry(root, fg="white", bg="black", width=30)
entryUSD.grid(row=2, column=2)


def convert():
    try:
        usd = float(entryUSD.get())
        converted_amount = round(usd * EXCHANGE_RATE, 2)
        labelResult.configure(
            text="Amount in EUR : €" + str(converted_amount)
        )
    except ValueError:
        labelResult.configure(text="Please enter a valid number")


convertButton = Button(
    root,
    text="Convert",
    bg="white",
    fg="black",
    activebackground="black",
    activeforeground="white",
    command=convert,
)
convertButton.grid(row=4, column=2)

root.mainloop()