import matplotlib.pyplot as plt
import numpy as np
from numpy.random import choice
from random import randint, choice
import csv

birth_dates = []
birth_dates_weights = []
classroom = None
number_of_dupes = False
had_a_dupe = 0
bin_counted_class = None

classes_percentages = []


def open_csv():
    csvfile=open('US_births_2000-2014_SSA.csv')
    obj=csv.reader(csvfile)
    for row in obj:
        birth_dates.append(int(row[4]))
    get_weights()


def get_weights():
    global birth_dates, birth_dates_weights
    for num in birth_dates:
        birth_dates_weights.append(num / 4149598)


# def get_weighted_percentages():
#     global birth_dates_processed, birth_dates
#     index = 1
#     for num in birth_dates:
#         for x in range(num):
#             birth_dates_processed.append(index)
#         index += 1



def add_to_class(num):
    global classroom, bin_counted_class, birth_dates_weights
    classroom = np.random.choice(birth_dates, num, p=birth_dates_weights)
    bin_counted_class = np.bincount(classroom)


def check_dupes():
    global classroom
    global number_of_dupes
    global had_a_dupe, bin_counted_class
    for x in bin_counted_class:
        if x > 1:
            number_of_dupes = True
            had_a_dupe += 1
            break


def graph():
    global birth_dates, birth_dates_weights, classes_percentages
    plt.bar(range(15, 35), classes_percentages, 0.8, align="center")
    plt.show()

def main():
    global classroom, number_of_dupes, classes_percentages, had_a_dupe
    for z in range(15, 35):
        had_a_dupe = 0
        for y in range(1000):
            classroom = []
            number_of_dupes = False
            add_to_class(z)
            check_dupes()

        classes_percentages.append(had_a_dupe)
    graph()

open_csv()
main()
