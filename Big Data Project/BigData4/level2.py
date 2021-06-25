import numpy as np
import matplotlib.pyplot as plt
from random import randint

happy_meals = [0, 0, 0, 0, 0, 0]

happy_meals_bought = 0

happy_meals_bought_array = []
all_not_found = True

restaurants = []
happy_meals_given = []


def get_happy_meals():
    global happy_meals, happy_meals_bought, all_not_found, happy_meals_bought_array, happy_meals_given, restaurants
    for trial in range(1000):
        restaurants = []
        happy_meals_given = []
        for x in range(100):
            restaurants.append(0)
            happy_meals_given.append(0)
        all_not_found = True
        happy_meals_bought = 0
        happy_meals = [0, 0, 0, 0, 0, 0]
        while all_not_found:
            if 
            happy_meal = randint(1, 6)
            happy_meals[happy_meal-1] += 1
            happy_meals_bought += 1
            if 0 not in happy_meals:
                all_not_found = False
                happy_meals_bought_array.append(happy_meals_bought)

    y_ticks = np.arange(len(happy_meals_bought_array))
    plt.hist(happy_meals_bought_array, bins=range(min(happy_meals_bought_array), max(happy_meals_bought_array)+2), ec="black")
    plt.title("Mc Donalds Happy Meal Toys")
    plt.xlabel("Number of Happy Meals")
    plt.ylabel("Frequency")
    plt.show()


def main():
    get_happy_meals()


main()