import numpy as np
import matplotlib.pyplot as plt
from random import choice

hermits = [1, 2, 3, 4, 5, 6]
hermits_told = []
num_of_hermits_told_array = []
num_of_hermits_told = 0
got_bored = False

def reset():
    global hermits_told, hermits, num_of_hermits_told_array, num_of_hermits_told, got_bored

    hermits = [1, 2, 3, 4, 5, 6]
    hermits_told = []
    num_of_hermits_told = 0
    got_bored = False

def get_hermits_told():
    global hermits_told, hermits, num_of_hermits_told_array, num_of_hermits_told, got_bored
    teller = choice(hermits)
    if hermits_told[-1] == teller:
        get_hermits_told()
        return
    else:
        hermits_told.append(teller)

    hermits_told_bincounted = np.bincount(hermits_told)
    for num in hermits_told_bincounted:
        if num > 1:
            got_bored = True
    else:
        num_of_hermits_told += 1

def graph_num_of_hermits_told_array():
    global hermits_told, hermits, num_of_hermits_told_array, num_of_hermits_told, got_bored


def main():
    global hermits_told, hermits, num_of_hermits_told_array, num_of_hermits_told, got_bored
    for trial in range(1000):
        reset()
        while not got_bored:
            get_hermits_told()
            
        num_of_hermits_told_array.append(num_of_hermits_told)
    plt.hist(num_of_hermits_told_array, bins=range(min(num_of_hermits_told_array), max(num_of_hermits_told_array) + 2), align="left", histtype="bar", ec="black")
    plt.title("Number of Hermits Told")
    plt.xlabel("Hermits Heard")
    plt.ylabel("Frequency")
    plt.show()
    print(np.sum(num_of_hermits_told_array)/len(num_of_hermits_told_array))


main()
        
    