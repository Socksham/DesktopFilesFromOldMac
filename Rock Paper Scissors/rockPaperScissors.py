from random import randint

import matplot.lib.pyplot as matplot

print("eruyfge")

possibleMoves = ["ROCK", "PAPER", "SCISSORS"]

ties = 0

wins = 0

losses = 0

def play():
    global ties
    global wins
    global losses

    playerMove = input("What is your choice: ").upper()

    compMove = possibleMoves[randint(0, len(possibleMoves)-1)]
    if playerMove not in possibleMoves:
        print("ERROR")
    elif playerMove == compMove:
        print("TIE")
        ties += 1
    elif playerMove == "ROCK" and compMove == "PAPER":
        print("LOSS")
        losses += 1
    elif playerMove == "ROCK" and compMove == "SCISSORS":
        print("WIN")
        wins += 1
    elif playerMove == "PAPER" and compMove == "ROCK":
        print("WIN")
        wins += 1
    elif playerMove == "PAPER" and compMove == "SCISSORS":
        print("LOSS")
        losses += 1
    elif playerMove == "SCISSORS" and compMove == "PAPER":
        print("WIN")
        wins += 1
    elif playerMove == "SCISSORS" and compMove == "ROCK":
        print("LOSS")
        losses += 1
    elif playerMove == "ROCK" and compMove == "PAPER":
        print("WIN!")
        wins += 1
while True:
    play()