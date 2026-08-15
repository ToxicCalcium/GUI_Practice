from tkinter import *
playerScore = 0
computerScore = 0
rps = [('rock', 0), ('paper', 0), ('scissors', 0)]

def compWins():
    global computerScore
    global playerScore
    computerScore = computerScore+1
    WinnerLabel.config(text = "Winner : Computer")
    CompScoreLabel.config(text = "Computer Score : " + str(computerScore))
    PlayerScoreLabel.config(text = "Your Score : " + str(playerScore))

def playerWins():
    global computerScore
    global playerScore
    playerScore = playerScore+1
    WinnerLabel.config(text = "Winner : You")
    CompScoreLabel.config(text = "Computer Score : " + str(computerScore))
    PlayerScoreLabel.config(text = "Your Score : " + str(playerScore))

root = Tk()
root.geometry("600x300")
root.config(background = "dark grey")
root.title("Rock Paper Scissors Game")
titleLabel = Label(root, text="Rock Paper Scissors", font=("Arial", 20, "bold"))
titleLabel.grid(row=0, column=2)
optionsLabel = Label(root, text="Your Options :")
optionsLabel.grid(row=2, column=0)
resultLabel = Label(root, text="")
resultLabel.grid(row=1, column=2)
rockButton = Button(root, text="Rock")
rockButton.grid(row=3, column=1)
paperButton = Button(root, text="Paper")
paperButton.grid(row=3, column=2)
ScissorsButton = Button(root, text="Scissors")
ScissorsButton.grid(row=3, column = 3)
playerChoiceLabel = Label(root, text="You Selected : _____")
playerChoiceLabel.grid(row=4, column=1)
PlayerScoreLabel = Label(root, text="Your Score : _____")
PlayerScoreLabel.grid(row=4, column=2)
CompChoiceLabel = Label(root, text="Computer Selected : _____")
CompChoiceLabel.grid(row=5, column=1)
CompScoreLabel = Label(root, text="Computer Score : _____")
CompScoreLabel.grid(row=5, column=2)
WinnerLabel = Label(root, text = "Winner : _____")
WinnerLabel.grid(row=6, column=2)

root.mainloop()