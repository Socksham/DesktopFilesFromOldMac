import numpy as np
import matplotlib.pyplot as plt
from random import randint

num_of_rolls = []
num_of_die = None
die1 = None
die2 = None

die = 0

print("(1) Sum of Rolls")
print("(2) Averages")
print("(3) Standard Deviation")
print("(4) All")
choice = int(input(""))

def get_amount_of_rolls():
    global num_of_rolls
    global die
    global choice
    # for array in die:
    #     if die.index(array) == 0:
    #         num_of_rolls = array
    #     else:
    #         num_of_rolls += array
    # print(num_of_rolls)

    plt.hist(die, bins=range(min(die), max(die) + 2), ec="black")
    plt.title("Random Dice Rolls")
    plt.xlabel("Dice Roll")
    plt.ylabel("Frequency")
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)

    plt.show()


def get_dice_averages():
    global die, num_of_die
    global choice

    averages = []

    for x in die:
        averages.append(x/num_of_die)

    print(averages)
    plt.hist(averages, bins=range(int(min(averages)), int(max(averages)+1)), ec="black")
    plt.title("Random Dice Roll Averages")
    plt.xlabel("Averages")
    plt.ylabel("Frequencies")
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.show()


def get_standard_deviation():
    global die

    std_rolls = die1 + die2

    std = np.std(std_rolls)

    std_rolls_mean = np.mean(std_rolls)

    in_std = 0

    for x in std_rolls:
        if abs(x - std_rolls_mean) <= std:
            in_std += 1

    print("{}%".format(in_std/len(std_rolls) * 100))


def main():
    global die, num_of_die
    num_of_rolls_user = int(input("How many rolls would you like to do: "))
    num_of_die = int(input("How many die would you like: "))
    for y in range(num_of_die):
        s = np.random.randint(1, 7, num_of_rolls_user)
        die += s
    print(die)
    if choice == 1:
        get_amount_of_rolls()
    elif choice == 2:
        get_dice_averages()
    elif choice == 3:
        get_standard_deviation()
    else:
        get_amount_of_rolls()
        get_dice_averages()
        get_standard_deviation()


main()
