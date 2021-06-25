from spaceship import *
from random import randint, choice
# from numpy.random import choice

ships = []
possible_ships = []
winners = []
def create_ships():
    global ships, possible_ships
    try:
        num_spaceships = int(input("How many spaceships: "))
        if num_spaceships == 0:
            print("There has to be another ship other than yours")
            create_ships()
    except ValueError:
        create_ships()
    ships = []
    for i in range(num_spaceships):
        ships.append(spaceship(randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), "Ship {}".format(i+1)))
    
    for x in ships:
        print(x.get_name() + ": ")
        print("Damage: {}".format(x.get_weapon_power()))
        print("Accuracy: {}".format(x.get_accuracy()))
        print("Health: {}".format(x.get_health()))
        print("Shields: {}\n".format(x.get_shields()))
    
    ships.append(spaceship(randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), "Your ship"))
    possible_ships = ships
    print(ships)
    print(possible_ships)

    print(ships[-1].get_name() + ": ")
    print("Damage: {}".format(ships[-1].get_weapon_power()))
    print("Accuracy: {}".format(ships[-1].get_accuracy()))
    print("Health: {}".format(ships[-1].get_health()))
    print("Shields: {}\n".format(ships[-1].get_shields()))


def fight_ships(ship1, ship2):
    global ships, possible_ships
    one_not_dead = True

    print("{} and {} are going against each other!".format(ship1.get_name(), ship2.get_name()))
    damage1 = ship1.get_weapon_power()
    damage2 = ship2.get_weapon_power()
    accuracy1 = ship1.get_weapon_power()
    accuracy2 = ship2.get_weapon_power()
    health1 = ship1.get_health()
    health2 = ship2.get_health()
    shields1 = ship1.get_shields()
    shields2 = ship2.get_shields()
    print(ship1.get_name() + ": ")
    print("Damage: {}".format(damage1))
    print("Accuracy: {}".format(accuracy1))
    print("Health: {}".format(health1))
    print("Shields: {}\n".format(ship1.get_shields()))

    print(ship2.get_name() + ": ")
    print("Damage: {}".format(damage2))
    print("Accuracy: {}".format(accuracy2))
    print("Health: {}".format(health2))
    print("Shields: {}\n".format(ship2.get_shields()))
    while one_not_dead:
        r = randint(0, 100)
        if r < accuracy1:
            ship2.take_damage(damage1)
        r = randint(0, 100)
        if r < accuracy2:
            ship1.take_damage(damage2)
        
        if ship1.get_health() <= 0 and ship2.get_health() <= 0:
            print("{} and {} tied! A coin is being flipped.".format(ship1.get_name(), ship2.get_name()))
            r = randint(0, 100)
            if r > 49:
                ship1.change_health(health1)
                winners.append(ship1)
            else:
                ship2.change_health(health2)
                winners.append(ship2)
            one_not_dead = False
        elif ship1.get_health() <= 0:
            print("{} won!".format(ship2.get_name()))
            winners.append(ship2)
            ship2.change_health(health2)

            one_not_dead = False
        elif ship2.get_health() <= 0:
            print("{} won!".format(ship1.get_name()))
            ship1.change_health(health1)
            winners.append(ship1)
            one_not_dead = False
    if ship1 == ships[-1]:
        fool = True
        while fool:
            upgrade = int(input("What would you like to upgrade for your ship: (1)Weapon Power (2)Speed (3)Shields (4)Health (5)Accuracy: "))
            fool = False
        if upgrade == 1:
            ships[-1].change_weapon_power(5)
        elif upgrade == 2:
            ships[-1].change_speed(5)
        elif upgrade == 3:
            ships[-1].change_shields(5)
        elif upgrade == 4:
            ships[-1].change_health(5)
        elif upgrade == 5:
            ships[-1].change_accuracy(5)
        
        r = randint(1, 6)
        if r == 1:
            ship2.change_weapon_power(5)
        elif r == 2:
            ship2.change_speed(5)
        elif r == 3:
            ship2.change_shields(5)
        elif r == 4:
            ship2.change_health(5)
        else:
            ship2.change_accuracy(5)
    elif ship2 == ships[-1]:
        fool = True
        while fool:
            upgrade = int(input("What would you like to upgrade for your ship: (1)Weapon Power (2)Speed (3)Shields (4)Health (5)Accuracy: "))
            fool = False
        if upgrade == 1:
            ships[-1].change_weapon_power(5)
        elif upgrade == 2:
            ships[-1].change_speed(5)
        elif upgrade == 3:
            ships[-1].change_shields(5)
        elif upgrade == 4:
            ships[-1].change_health(5)
        elif upgrade == 5:
            ships[-1].change_accuracy(5)

        r = randint(1, 6)
        if r == 1:
            ship1.change_weapon_power(5)
        elif r == 2:
            ship1.change_speed(5)
        elif r == 3:
            ship1.change_shields(5)
        elif r == 4:
            ship1.change_health(5)
        else:
            ship1.change_accuracy(5)
        
    else:
        r = randint(1, 6)
        if r == 1:
            ship1.change_weapon_power(5)
        elif r == 2:
            ship1.change_speed(5)
        elif r == 3:
            ship1.change_shields(5)
        elif r == 4:
            ship1.change_health(5)
        else:
            ship1.change_accuracy(5)
        
        r = randint(1, 5)
        if r == 1:
            ship2.change_weapon_power(5)
        elif r == 2:
            ship2.change_speed(5)
        elif r == 3:
            ship2.change_shields(5)
        elif r == 4:
            ship2.change_health(5)
        else:
            ship2.change_accuracy(5)

    


def tourney():
    global possible_ships, winners
    ships_to_hold = possible_ships
    # while len(ships_to_hold) > 1:
    #     while len(possible_ships)/2 >= 2:
    possible_ships += winners
    if len(possible_ships)%2 != 0:
        rand_ship = choice(possible_ships)
        winners.append(rand_ship)
        possible_ships.remove(rand_ship)

    
    ship1 = choice(possible_ships)
    possible_ships.remove(ship1)
    ship2 = choice(possible_ships)
    possible_ships.remove(ship2)
    fight_ships(ship1, ship2)



# def tourney():
#     global ships, possible_ships, next
#     next = possible_ships
#     while len(next) > 1:
#         possible_ships = next
#         ship1 = choice(possible_ships)
#         possible_ships.remove(ship1)
#         ship2 = choice(possible_ships)
#         possible_ships.remove(ship2)
#         fight_ships(ship1, ship2)
#         while len(possible_ships)/2 >= 2:
#             ship1 = choice(possible_ships)
#             possible_ships.remove(ship1)
#             ship2 = choice(possible_ships)
#             possible_ships.remove(ship2)
#             if len(possible_ships) % 2 != 0:
#                 rand_ship = choice(possible_ships)
#                 next.append(rand_ship)
#                 possible_ships.remove(rand_ship)
#             fight_ships(ship1, ship2)
#         upgradeships(next[-1])
#         names = [s.get_name() for s in next]
#         print(names)


def main():
    create_ships()
    tourney()

main()