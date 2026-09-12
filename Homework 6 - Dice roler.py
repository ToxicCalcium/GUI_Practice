from tkinter import *
from random import *
root = Tk()
root.title("Dice Roller")
root.geometry("300x300")
root.config(background="light grey")
instructionLabel = Label(root, text="Roll the Dice!")
instructionLabel.place(x=110, y=30)

def rollDice():
    dice = randint(1, 6)
    if dice == 6:
        diceLabel.config(text=str(dice), fg="red")
    else:
        diceLabel.config(text=str(dice), fg="black")

diceLabel = Label(root, text="-", font=("Arial", 30))
diceLabel.place(x=135, y=100)
rollButton = Button(root, text="ROLL", command=rollDice)
rollButton.place(x=130, y=200)

root.mainloop()