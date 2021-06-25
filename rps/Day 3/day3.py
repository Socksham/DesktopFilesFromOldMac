from random import randint

first = True

wins = 0

losses = 0

ties = 0

p1_or_2 = None


player1_name = None
player2_name = None



def menu():
    global mode
    print("(1) 1 player vs computer")
    print("(2) 2 player vs another person\n")
    mode = int(input(""))


menu()

play = True

error = False


def comp_turn():
    return randint(1, 3)


def newGame():
    global mode
    global first
    print("\nWhat would you like to do")
    print("(1) New Game")
    print("(2) Continue Game")
    print("(3) Exit Game")
    again = int(input("\n"))

    if again == 1:
        first = True
        menu()
        main()
    elif again == 2:
        main()

    elif again == 3:
        return
    else:
        newGame()


def player_turn():
    if p1_or_2 == 1:
        return input("Player 1 pick rock, paper or scissors: ")
    elif p1_or_2 == 2:
        return input("Player 2 pick rock, paper or scissors: ")
    else:
        return input("Pick rock, paper or scissors: ")


def play_again():
    global play
    while play:
        main()


def check_winner(comp, player):
    global error
    global wins, losses, ties

    if player != "rock" and player != "paper" and player != "scissors":
        print("Please pick rock, paper or scissors")
        error = True
        main()
    else:
        error = False
        if player == "rock" and comp == 1 or player == "paper" and comp == 2 or player == "scissors" and comp == 3:
            print("Tie")
            ties += 1
        elif player == "rock" and comp == 2:
            print("You Lost")
            print("Computer picked paper")
            losses += 1
        elif player == "rock" and comp == 3:
            print("You Won")
            print("Computer picked scissors")
            wins += 1
        elif player == "paper" and comp == 1:
            print("You Won")
            print("Computer picked rock")
        elif player == "paper" and comp == 3:
            print("You Lost")
            print("Computer picked scissors")
            losses += 1
        elif player == "scissors" and comp == 1:
            print("You Lost")
            print("Computer picked rock")
            losses += 1
        elif player == "scissors" and comp == 2:
            print("You Won")
            print("Computer picked paper")
            wins += 1



def check_winner2player(player1, player2):
    global error
    global wins, losses, ties
    if player1 != "rock" and player1 != "paper" and player1 != "scissors":
        print(player1_name + " please pick rock, paper or scissors")
        error = True
        main()
    elif player2 != "rock" and player2 != "paper" and player2 != "scissors":
        print(player2_name + " please pick rock, paper or scissors")
        error = True
        main()
    else:
        error = False
        if player1 == player2:
            print("Tie")
            ties += 1
        elif player1 == "rock" and player2 == "paper":
            print(player2_name + " you won!")
            print(player1_name + " you lost")
            losses += 1
        elif player1 == "rock" and player2 == "scissors":
            print(player1_name + " you won!")
            print(player2_name + " you lost")
            wins += 1
        elif player1 == "paper" and player2 == "rock":
            print(player1_name + " you won!")
            print(player2_name + " you lost")
            wins += 1
        elif player1 == "paper" and player2 == "scissors":
            print(player2_name + " you won!")
            print(player1_name + " you lost")
            losses += 1
        elif player1 == "scissors" and player2 == "rock":
            print(player2_name + " you won!")
            print(player1_name + " you lost")
            losses += 1
        elif player1 == "scissors" and player2 == "paper":
            print(player1_name + " you won!")
            print(player2_name + " you lost")
            wins += 1

def showScore():
    global wins, losses, ties
    print(wins)
    print(losses)
    print(ties)


def main():
    global first
    global wins, losses, ties
    global player1_name
    global player2_name
    global p1_or_2
    global mode
    global error
    if mode == 1:
        p1_or_2 = None
        player = player_turn()
        comp = comp_turn()
        check_winner(comp, player)
    elif mode == 2:
        if first:
            player1_name = input("What is player1's name: ")
            player2_name = input("What is player2's name: ")
            first = False
        p1_or_2 = randint(1, 2)
        if p1_or_2 == 1:
            player1 = player_turn()
            p1_or_2 = 2
            player2 = player_turn()
        else:
            player2 = player_turn()
            p1_or_2 = 1
            player1 = player_turn()

        check_winner2player(player1, player2)
    showScore()
    if not error:
        newGame()


main()