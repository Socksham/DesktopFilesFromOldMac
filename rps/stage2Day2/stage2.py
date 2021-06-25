from random import randint

first = True

wins = 0

losses = 0

wins3 = 0

ties = 0

available_moves_lizard = ["r", "p", "s", "l", "sp"]

p1_or_2 = None

play = True

p1wins = 0
p2wins = 0
p3wins = 0

player1_name = None
player2_name = None
player3_name = None

rounds = None

mode = None

data = ""

possibilities = []



# def add_rand_values():
#     global data
#     for x in range(100000):
#         rand = randint(1, 3)
#         if rand == 1:
#             data += "R"
#         elif rand == 2:
#             data += "P"
#         else:
#             data += "S"

# add_rand_values()

def aicomp():
    global data
    global possibilities

    possibilities = []
    last = data[-3:]

    for x in range(len(data)-4):
        at = data[x:x+3]
        add = data[x+4]
        if last == at:
            possibilities.append(add)
    try:
        answer =  max(possibilities, key=possibilities.count)
    except ValueError:
        print("ERROR")
        return comp_turn()
    print(answer)
    if answer == "R":
        answer = 2
    elif answer == "P":
        answer = 3
    else:
        answer = 1
    return answer


def menu():
    global mode
    print("\n(1) 1 player vs computer")
    print("(2) 2 player vs another person")
    print("(3) 3 player vs 2 other people")
    print("(4) Lizard Spock 2 player")
    print("(5) 1 Player vs AI\n")
    try:
        mode = int(input(""))
    except ValueError:
        menu()

def comp_turn():
    return randint(1, 3)


def won_series():
    global mode
    global p1wins, p2wins, p3wins
    global player1_name, player2_name, player3_name
    if mode == 1 or mode == 5:
        print("\nYou won {} times".format(p1wins))
        print("Computer won {} times".format(p2wins))
        if p1wins > p2wins:
            print("You won more times than the computer!")
        elif p1wins < p2wins:
            print("The computer more times than the you!")
        else:
            print("Both players won {} times".format(p1wins))
    elif mode == 2 or mode == 4:
        print("{} won {} times".format(player1_name, p1wins))
        print("{} won {} times".format(player2_name, p2wins))
        if p1wins > p2wins:
            print("{} won more times".format(player1_name))
        elif p1wins < p2wins:
            print("{} won more times".format(player2_name))
        else:
            print("Both players won {} times".format(p1wins))
    elif mode == 3:
        print("{} won {} times".format(player1_name, p1wins))
        print("{} won {} times".format(player2_name, p2wins))
        print("{} won {} times".format(player3_name, p3wins))

        if p1wins > p2wins and p1wins > p3wins:
            print("{} won more times".format(player1_name))
        elif p2wins > p1wins and p2wins > p3wins:
            print("{} won more times".format(player2_name))
        elif p3wins > p2wins and p3wins > p1wins:
            print("{} won more times".format(player3_name))
        else:
            print("All three players won {} times".format(p1wins))



def rounds_menu():
    global rounds
    print("(1) 1First to Win")
    print("(2) First to 3")
    print("(3) First to 5")

    rounds = int(input(""))

    if rounds == 2:
        rounds = 3
    elif rounds == 3:
        rounds = 5
    else:
        rounds = 1


def newGame():
    global mode
    global first
    global wins, ties, losses
    global p1wins, p2wins, p3wins
    print("\nWhat would you like to do")
    print("(1) New Game")
    print("(2) Continue Game")
    print("(3) Exit Game")
    try:
        again = int(input(""))
    except ValueError:
        newGame()
    if again == 1:
        first = True
        wins = 0
        losses = 0
        ties = 0
        won_series()
        p1wins = 0
        p2wins = 0
        p3wins = 0
        menu()
        rounds_menu()
        main()
    elif again == 2:
        wins = 0
        losses = 0
        ties = 0
        main()

    elif again == 3:
        won_series()
        return
    else:
        newGame()


def player_turn(player_num):
    return input("Player {} pick r, p or s: ".format(player_num))


def check_winner(comp, player):
    global wins, losses, ties
    global player1_name
    if player != "r" and player != "p" and player != "s":
        print("Please pick r, p or s")
        main()
    else:
        if player == "r" and comp == 1 or player == "p" and comp == 2 or player == "s" and comp == 3:
            print("Tie")
            ties += 1
        elif player == "r" and comp == 2:
            print("{} Lost".format(player1_name))
            print("Computer picked p")
            losses += 1
        elif player == "r" and comp == 3:
            print("{} Won".format(player1_name))
            print("Computer picked s")
            wins += 1
        elif player == "p" and comp == 1:
            print("{} Won".format(player1_name))
            print("Computer picked r")
            wins += 1
        elif player == "p" and comp == 3:
            print("{} Lost".format(player1_name))
            print("Computer picked s")
            losses += 1
        elif player == "s" and comp == 1:
            print("{} Lost".format(player1_name))
            print("Computer picked r")
            losses += 1
        elif player == "s" and comp == 2:
            print("{} Won".format(player1_name))
            print("Computer picked p")
            wins += 1


def check_winner2player(player1, player2):
    global wins, losses, ties
    if player1 != "r" and player1 != "p" and player1 != "s":
        print(player1_name + " please pick r, p or s")
        main()
    elif player2 != "r" and player2 != "p" and player2 != "s":
        print(player2_name + " please pick r, p or s")
        main()
    else:
        if player1 == player2:
            print("Tie")
            ties += 1
        elif player1 == "r" and player2 == "p":
            print(player2_name + " you won!")
            print(player1_name + " you lost")
            losses += 1
        elif player1 == "r" and player2 == "s":
            print(player1_name + " you won!")
            print(player2_name + " you lost")
            wins += 1
        elif player1 == "p" and player2 == "r":
            print(player1_name + " you won!")
            print(player2_name + " you lost")
            wins += 1
        elif player1 == "p" and player2 == "s":
            print(player2_name + " you won!")
            print(player1_name + " you lost")
            losses += 1
        elif player1 == "s" and player2 == "r":
            print(player2_name + " you won!")
            print(player1_name + " you lost")
            losses += 1
        elif player1 == "s" and player2 == "p":
            print(player1_name + " you won!")
            print(player2_name + " you lost")
            wins += 1


def check_winner3player(player1, player2, player3):
    global wins, losses, ties, wins3
    global player1_name, player2_name, player3_name
    if player1 != "r" and player1 != "p" and player1 != "s":
        print("{} please pick r, p or s".format(player1_name))
        main()
    elif player2 != "r" and player2 != "p" and player2 != "s":
        print("{} please pick r, p or s".format(player2_name))
        main()
    elif player3 != "r" and player3 != "p" and player3 != "s":
        print("{} please pick r, p or s".format(player3_name))
        main()
    elif player1 != player2 and player1 != player3 and player3 != player2:
        print("Tie!")
        ties += 1
    elif player1 == player2 == player3:
        print("Tie!")
        ties += 1
    else:
        if player1 == "p" and player2 == "r" and player3 == "r":
            wins += 1
            print("{} you won!".format(player1_name))
            print("{} and {} lost!".format(player2_name, player3_name))
        elif player1 == "p" and player2 == "s" and player3 == "s":
            losses += 1
            wins3 += 1
            print("{} and {} won!".format(player2_name, player3_name))
            print("{} lost!".format(player1_name))
        elif player1 == "s" and player2 == "p" and player3 == "p":
            wins += 1
            print("{} you won!".format(player1_name))
            print("{} and {} lost!".format(player2_name, player3_name))
        elif player1 == "s" and player2 == "r" and player3 == "r":
            losses += 1
            wins3 += 1
            print("{} and {} won!".format(player2_name, player3_name))
            print("{} lost!".format(player1_name))
        elif player1 == "r" and player2 == "p" and player3 == "p":
            losses += 1
            wins3 += 1
            print("{} and {} won!".format(player2_name, player3_name))
            print("{} lost!".format(player1_name))
        elif player1 == "r" and player2 == "s" and player3 == "s":
            wins += 1
            print("{} you won!".format(player1_name))
            print("{} and {} lost!".format(player2_name, player3_name))
        elif player2 == "p" and player1 == "r" and player3 == "r":
            losses += 1
            print("{} you won!".format(player2_name))
            print("{} and {} lost!".format(player1_name, player3_name))
        elif player2 == "p" and player1 == "s" and player3 == "s":
            wins += 1
            wins3 += 1
            print("{} and {} won!".format(player1_name, player3_name))
            print("{} lost!".format(player2_name))
        elif player2 == "s" and player1 == "p" and player3 == "p":
            losses += 1
            print("{} you won!".format(player2_name))
            print("{} and {} lost!".format(player1_name, player3_name))
        elif player2 == "s" and player1 == "r" and player3 == "r":
            wins += 1
            wins3 += 1
            print("{} and {} won!".format(player1_name, player3_name))
            print("{} lost!".format(player2_name))
        elif player2 == "r" and player1 == "p" and player3 == "p":
            wins += 1
            wins3 += 1
            print("{} and {} won!".format(player1_name, player3_name))
            print("{} lost!".format(player2_name))
        elif player2 == "r" and player1 == "s" and player3 == "s":
            losses += 1
            print("{} you won!".format(player2_name))
            print("{} and {} lost!".format(player1_name, player3_name))
        elif player3 == "p" and player2 == "r" and player1 == "r":
            wins += 1
            print("{} you won!".format(player3_name))
            print("{} and {} lost!".format(player1_name, player2_name))
        elif player3 == "p" and player2 == "s" and player1 == "s":
            losses += 1
            wins += 1
            print("{} and {} won!".format(player1_name, player2_name))
            print("{} lost!".format(player3_name))
        elif player3 == "s" and player2 == "p" and player1 == "p":
            wins3 += 1
            print("{} you won!".format(player3_name))
            print("{} and {} lost!".format(player1_name, player2_name))
        elif player3 == "s" and player2 == "r" and player1 == "r":
            losses += 1
            wins += 1
            print("{} and {} won!".format(player1_name, player2_name))
            print("{} lost!".format(player3_name))
        elif player3 == "r" and player2 == "p" and player1 == "p":
            wins3 += 1
            print("{} you won!".format(player3_name))
            print("{} and {} lost!".format(player1_name, player2_name))
        elif player3 == "r" and player2 == "s" and player1 == "s":
            losses += 1
            wins += 1
            print("{} and {} won!".format(player1_name, player2_name))
            print("{} lost!".format(player3_name))


def player_turn_lizard(player_num):
    return input("Player {} pick r, p, s, l or sp: ".format(player_num))


def check_winner_lizard(player1, player2):
    global available_moves_lizard
    global player1_name, player2_name
    global wins, losses
    if player1 not in available_moves_lizard:
        print("{} please pick r, p, s, l or sp".format(player1))
    elif player2 not in available_moves_lizard:
        print("{} please pick r, p, s, l or sp".format(player2))
    elif player1 == player2:
        print("Tie!")
        ties += 1
    elif player1 == "r":
        if player2 == "p":
            print("{} won!".format(player2_name))
            print("{} you lost!".format(player1_name))
            print("Paper covers rock!")
            losses += 1
        elif player2 == "sp":
            print("{} won!".format(player2_name))
            print("{} you lost!".format(player1_name))
            print("Spock vaporizes rock!")
            losses += 1
        elif player2 == "s":
            print("{} won!".format(player1_name))
            print("{} you lost!".format(player2_name))
            print("Rock crushes scissors!")
            wins += 1
        elif player2 == "l":
            print("{} won!".format(player1_name))
            print("{} you lost!".format(player2_name))
            print("Rock crushes lizard!")
            wins += 1
    elif player1 == "p":
        if player2 == "r":
            print("{} won!".format(player1_name))
            print("{} you lost!".format(player2_name))
            print("Paper covers rock!")
            wins += 1
        elif player2 == "s":
            print("{} won!".format(player2_name))
            print("{} you lost!".format(player1_name))
            print("Scissors cuts paper!")
            losses += 1
        elif player2 == "l":
            print("{} won!".format(player2_name))
            print("{} you lost!".format(player1_name))
            print("Lizard eats paper!")
            losses += 1
        elif player2 == "sp":
            print("{} won!".format(player1_name))
            print("{} you lost!".format(player2_name))
            print("Paper disproves Spock!")
            wins += 1
    elif player1 == "s":
        if player2 == "r":
            print("{} won!".format(player2_name))
            print("{} you lost!".format(player1_name))
            print("Rock crushes paper!")
            losses += 1
        elif player2 == "p":
            print("{} won!".format(player1_name))
            print("{} you lost!".format(player2_name))
            print("Scissors cuts paper!")
            wins += 1
        elif player2 == "l":
            print("{} won!".format(player1_name))
            print("{} you lost!".format(player2_name))
            print("Scissors beheads lizard!")
            wins += 1
        elif player2 == "sp":
            print("{} won!".format(player2_name))
            print("{} you lost!".format(player1_name))
            print("Spock smashes scissors!")
            losses += 1
    elif player1 == "l":
        if player2 == "r":
            print("{} won!".format(player2_name))
            print("{} you lost!".format(player1_name))
            print("Rock crushes lizard!")
            losses += 1
        elif player2 == "p":
            print("{} won!".format(player1_name))
            print("{} you lost!".format(player2_name))
            print("Lizard eats paper!")
            wins += 1
        elif player2 == "s":
            print("{} won!".format(player2_name))
            print("{} you lost!".format(player1_name))
            print("Scissors beheads lizard!")
            losses += 1
        elif player2 == "sp":
            print("{} won!".format(player1_name))
            print("{} you lost!".format(player2_name))
            print("Lizard poisons Spock!")
            wins += 1
    elif player1 == "sp":
        if player2 == "r":
            print("{} won!".format(player1_name))
            print("{} you lost!".format(player2_name))
            print("Spock vaporizes rock!")
            wins += 1
        elif player2 == "p":
            print("{} won!".format(player2_name))
            print("{} you lost!".format(player1_name))
            print("Paper disproves Spock!")
            losses += 1
        elif player2 == "s":
            print("{} won!".format(player1_name))
            print("{} you lost!".format(player2_name))
            print("Spock smashes scissors!")
            wins += 1
        elif player2 == "l":
            print("{} won!".format(player2_name))
            print("{} you lost!".format(player1_name))
            print("Lizard poisons Spock!")
            losses += 1


def add_player_turn(player):
    global data
    data += player.upper()


def showScore():
    global wins, losses, ties, wins3
    global mode
    global player1_name, player2_name, player3_name
    global p1wins, p2wins, p3wins

    if mode == 1 or mode == 5:
        print("\nWins: {}".format(wins))
        print("Losses: {}".format(losses))
        print("Ties: {}".format(ties))
        if wins > losses:
            print("You won the series!")
            p1wins += 1
        else:
            print("The computer won the series")
            p2wins += 1
    elif mode == 2 or mode == 4:
        print("\n{} Wins: {}".format(player1_name, wins))
        print("{} Wins: {}".format(player2_name, losses))
        print("Ties: {}".format(ties))
        if wins > losses:
            print("{} won the series".format(player1_name))
            p1wins += 1
        else:
            print("{} won the series".format(player2_name))
            p2wins += 1
    elif mode == 3:
        print("\n{} Wins: {}".format(player1_name, wins))
        print("{} Wins: {}".format(player2_name, losses))
        print("{} Wins: {}".format(player3_name, wins3))
        print("Ties: {}".format(ties))
        if wins > losses and wins > wins3:
            print("{} won the series".format(player1_name))
            p1wins += 1
        elif wins3 > wins and wins3 > losses:
            print("{} won the series".format(player3_name))
            p3wins += 1
        else:
            print("{} won the series".format(player2_name))
            p2wins += 1


def main():
    global p1wins, p2wins
    global first
    global wins, losses, ties
    global player1_name
    global player2_name, player3_name
    global p1_or_2
    global mode
    global rounds
    global data
    if mode == 1:
        if first:
            player1_name = input("What is your name: ")
            first = False
        player = player_turn(1)
        comp = comp_turn()
        check_winner(comp, player)
    elif mode == 2:
        if first:
            player1_name = input("What is player1's name: ")
            player2_name = input("What is player2's name: ")
            first = False
        p1_or_2 = randint(1, 2)
        if p1_or_2 == 1:
            player1 = player_turn(1)
            p1_or_2 = 2
            player2 = player_turn(2)
        else:
            player2 = player_turn(2)
            p1_or_2 = 1
            player1 = player_turn(1)

        check_winner2player(player1, player2)

    elif mode == 3:
        if first:
            player1_name = input("What is player1's name: ")
            player2_name = input("What is player2's name: ")
            player3_name = input("What is player3's name: ")
            first = False
        player1 = player_turn(1)
        player2 = player_turn(2)
        player3 = player_turn(3)

        check_winner3player(player1, player2, player3)
    elif mode == 4:
        if first:
            player1_name = input("What is player1's name: ")
            player2_name = input("What is player2's name: ")
            first = False
        player1 = player_turn_lizard(1)
        player2 = player_turn_lizard(2)
        check_winner_lizard(player1, player2)
    elif mode == 5:
        if first:
            player1_name = input("What is your name: ")
            first = False
        if len(data) >= 6:
            comp_move = aicomp()
        else:
            comp_move = comp_turn()
        player = player_turn(1)
        add_player_turn(player)

        check_winner(comp_move, player)

    if wins == rounds or losses == rounds or wins3 == rounds:
        showScore()
        newGame()
    else:
        main()


menu()
rounds_menu()
main()
