import numpy as np
import matplotlib.pyplot as plt
from random import randint, choice

hermits_told = []
num_of_hermits_told = 0
num_of_hermits_told_array = []
got_bored = False

def reset():
    global hermits_told, num_of_hermits_told, got_bored
    hermits_told = []
    num_of_hermits_told = 0
    got_bored = False

def get_num_of_hermits_told():
    global hermits_told, num_of_hermits_told, got_bored, num_of_hermits_told_array

    hermits_told.append(randint(1, 6))
    if len(hermits_told) > 1:
        if hermits_told[-1] == hermits_told[-2]:
            got_bored = True
        else:
            for num in np.bincount(hermits_told):
                if num > 1:
                    got_bored = True
            else:
                num_of_hermits_told += 1
    else:
        num_of_hermits_told += 1


def main():
    global num_of_hermits_told_array
    for trial in range(1000):
        reset()
        while got_bored == False:
            get_num_of_hermits_told()
        num_of_hermits_told_array.append(num_of_hermits_told)
    plt.hist(num_of_hermits_told_array, bins=range(min(num_of_hermits_told_array), max(num_of_hermits_told_array) + 2), align="left", histtype="bar", ec="black")
    plt.title("Number of Hermits Told")
    plt.xlabel("Hermits Heard")
    plt.ylabel("Frequency")
    plt.show()
    print(sum(num_of_hermits_told_array)/len(num_of_hermits_told_array))
main()
