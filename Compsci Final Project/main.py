from player import Player
from team import Team
from coach import Coach
from random import choice, randint
import csv
import time

teams = []
positions = [1, 2, 3, 4, 5]
team_names = []
names = []
player_name = input("Hello there what is your name?: \n")
team_picked = None

def init():
    global teams, positions, team_names, names, player_name, team_picked
    print("Setting up teams...")
    csvfile=open('firstnames.csv')
    obj=csv.reader(csvfile)
    for row in obj:
        names.append(row[0])
    csvfile.close()
    csvfile=open('teams.csv')
    obj=csv.reader(csvfile)
    for row in obj:
        team_names.append(row[0])
    csvfile.close()
    print("Getting names...")

    for v in range(0, 30):
        positions = [1, 2, 3, 4, 5]
        temp_team = []
        reserves = []
        for x in range(0, 16):
            try:
                position = choice(positions)
            except:
                positions = [1, 2, 3, 4, 5]
                position = choice(positions)
            if x <= 13:
                temp_team.append(Player(randint(5, 8), position, randint(20, 100), randint(130, 250), randint(20, 100), randint(20, 100), choice(names) + " " + choice(names), randint(20, 100), randint(20, 100), randint(20, 29)))
                positions.remove(position)
            else:
                reserves.append(Player(randint(5, 8), position, randint(20, 50), randint(130, 250), randint(20, 50), randint(20, 50), choice(names) + " " + choice(names), randint(20, 50), randint(20, 50), randint(20, 39)))
            
            if x == 15:
                coach = Coach(randint(20, 100), randint(20, 100), randint(20, 100))
                team_name = team_names[v]
                temp_team = Team(team_name, coach, [0, 0], temp_team, reserves, None, None, [])
                teams.append(temp_team)
    print("\nHello {} what team would you like to be: ".format(player_name))
    for x in range(1, 31):
        print("({}) {}".format(x, teams[x-1].name))

    team_picked = input("")
    while True:
        try:
            team_picked = int(team_picked)
            teams[team_picked - 1].gm = player_name
            print("Your team is the {}".format(teams[team_picked - 1].name))
            break
        except:
            print("\nPlease pick a team associated with a number")
            format(player_name)
            for x in range(1, 31):
                print("({}) {}".format(x, teams[x-1].name))

            team_picked = input("")
    print("\nYour starting lineup is: ")
    lineup = get_starting_lineup(teams[team_picked - 1].players)
    for starter in lineup:
        print("\nName: {}".format(starter.name))
        print("Age: {}".format(starter.age))
        print("Position: {}".format(starter.position))
        print("Strength: {}".format(starter.strength))
        print("Weight: {}".format(starter.weight))
        print("Speed: {}".format(starter.speed))
        print("Height: {}".format(starter.height))
        print("Shooting: {}".format(starter.shooting))
        print("Injury Prone: {}".format(starter.injury_prone))
        print("Defence: {}".format(starter.defence))
    print("\nYour entire team is: ")
    for p in teams[team_picked - 1].players:
        print("\nName: {}".format(p.name))
        print("Age: {}".format(p.age))
        print("Position: {}".format(p.position))
        print("Strength: {}".format(p.strength))
        print("Weight: {}".format(p.weight))
        print("Speed: {}".format(p.speed))
        print("Height: {}".format(p.height))
        print("Shooting: {}".format(p.shooting))
        print("Injury Prone: {}".format(p.injury_prone))
        print("Defence: {}".format(p.defence))
    print("\nTeams set up")
    
# offensive
# 1 == "pick and roll" beats "Man to Man"
# 2 == "flex" beats "1-2-2"
# 3 == "basic motion" beats "Box and One"
# 4 == "4 out" beats "3-2"
# 5 == "5 out" beats "2-3"
# 6 == "High Low" beats "Diamond and One"
# 7 == "Corners" beats "1-3-1"

# defensive
# 1 == "2-3" beats "flex"
# 2 == "3-2" beats "basic motion"
# 3 == "1-2-2" beats "High Low"
# 4 == "Man to Man" beats "5 out"
# 5 == "Box and One" beats "Corners"
# 6 == "Diamond and One" beats "4 out"
# 7 == "1-3-1" beats "Pick and Roll"
def check_countered_or_not(team1_play, team2_play):
    if team1_play == 1:
        if team2_play == 7:
            return False
        elif team2_play == 4:
            return True
    elif team1_play == 2:
        if team2_play == 1:
            return False
        elif team2_play == 2:
            return True
    elif team1_play == 3:
        if team2_play == 2:
            return False
        elif team2_play == 5:
            return True
    elif team1_play == 4:
        if team2_play == 6:
            return False
        elif team2_play == 2:
            return True
    elif team1_play == 5:
        if team2_play == 4:
            return False
        elif team2_play == 1:
            return True
    elif team1_play == 6:
        if team2_play == 3:
            return False
        elif team2_play == 6:
            return True
    elif team1_play == 7:
        if team2_play == 5:
            return False
        elif team2_play == 7:
            return True

    return "Neither"

def get_starting_lineup(team):
    PG = []
    SG = []
    SF = []
    PF = []
    C = []
    lineup = []
    for player in team:
        if player.position == 1:
            PG.append(player)
        elif player.position == 2:
            SG.append(player)
        elif player.position == 3:
            SF.append(player)
        elif player.position == 4:
            PF.append(player)
        else:
            C.append(player)

    for x in range(1, 6):
        if x == 1:
            best_pg_stat = -10000
            best_pg = None
            for pg in PG:
                avg = (pg.shooting + pg.strength + pg.speed + pg.height - (pg.weight/2) - pg.injury_prone + pg.defence*1.5 + (100-pg.age))/8
                if avg > best_pg_stat:
                    best_pg_stat = avg
                    best_pg = pg
            lineup.append(best_pg)
        elif x == 2:
            best_sg_stat = -10000
            best_sg = None
            for sg in SG:
                avg = (sg.shooting + sg.strength + sg.speed + sg.height - (sg.weight/2) - sg.injury_prone + sg.defence*1.5 + (100-sg.age))/8
                if avg > best_sg_stat:
                    best_sg = sg
                    best_sg_stat = avg
            lineup.append(best_sg)
        elif x == 3:
            best_sf_stat = -10000
            best_sf = None
            for sf in SF:
                avg = (sf.shooting + sf.strength + sf.speed + sf.height + (sf.weight)/2 - sf.injury_prone + sf.defence + (100-sf.age))/8
                if avg > best_sf_stat:
                    best_sf = sf
                    best_sf_stat = avg
            lineup.append(best_sf)

        elif x == 4:
            best_pf_stat = -10000
            best_pf = None
            for pf in PF:
                avg = (pf.shooting + pf.strength*1.2 + pf.speed + pf.height + (pf.weight)/2 - pf.injury_prone + pf.defence + (100-pf.age))/8
                if avg > best_pf_stat:
                    best_pf_stat = avg
                    best_pf = pf
            lineup.append(best_pf)

        else:
            best_c_stat = -10000
            best_c = None
            for c in C:
                avg = (c.shooting + c.strength*1.5 + c.speed + c.height*2 + (c.weight)/2 - c.injury_prone + c.defence + (100-c.age))/8
                if avg > best_c_stat:
                    best_c_stat = avg
                    best_c = c
            lineup.append(best_c)
    return lineup

def print_record():
    global teams
    for team in teams:
        print(team.record[0] + team.record[1])

def play_game(team1_players, team2_players, team1, team2):
    # print("Playing Game")
    team1_points = 0
    team2_points = 0
    team1_lineup = get_starting_lineup(team1_players)
    team2_lineup = get_starting_lineup(team2_players)
    ball = randint(1, 2)
    if ball == 1:
        ball = True
    else:
        ball = False
    for x in range(17):
        countered = False
        for x in range(0, 5):
            p1 = team1_lineup[x]
            p2 = team2_lineup[x]
            if ball:
                team1.play = randint(1, 7)
                team2.play = team2.coach.run_defensive_play(team1.play)
                team1.play = team1.coach.change_offensive_play(team2.play)
                countered = check_countered_or_not(team1.play, team2.play)
                if countered:
                    team1_points += randint(2, 3)
                    ball = False
                elif not countered:
                    ball = False
                else:
                    if p1.take_shot() == True:
                        if p2.block_shot() == True:
                            ball = False
                            foul = randint(1, 5)
                            if foul == 1:
                                if p1.take_shot() == True:
                                    team1_points += randint(1, 3)
                                ball = False
                        else:
                            team1_points += randint(2, 3)
                            ball = False
                    else:
                        if p2.steal_ball():
                            ball = False
                        else:
                            foul = randint(1, 5)
                            if foul == 1:
                                if p1.take_shot() == True:
                                    team1_points += 1
                                ball = False
            else:
                team2.play = randint(1, 7)
                team1.play = team1.coach.run_defensive_play(team2.play)
                team2.play = team2.coach.change_offensive_play(team1.play)
                countered = check_countered_or_not(team2.play, team1.play)
                if countered:
                    team2_points += randint(2, 3)
                    ball = True
                elif not countered:
                    ball = True
                else:
                    if p2.take_shot() == True:
                        if p1.block_shot() == True:
                            ball = False
                            foul = randint(1, 5)
                            if foul == 1:
                                if p2.take_shot() == True:
                                    team2_points += randint(1, 3)
                                ball = True
                        else:
                            team2_points += randint(2, 3)
                            ball = True
                    else:
                        if p1.steal_ball() == True:
                            ball = True
                        else:
                            foul = randint(1, 5)
                            if foul == 1:
                                if p2.take_shot() == True:
                                    team2_points += 1
                                ball = True
    while team1_points == team2_points:
        for x in range(10):
            for x in range(0, 5):
                p1 = team1_lineup[x]
                p2 = team2_lineup[x]
                if ball:
                    if p1.take_shot() == True:
                        if p2.block_shot() == True:
                            ball = False
                            foul = randint(1, 5)
                            if foul == 1:
                                if p1.take_shot() == True:
                                    team1_points += randint(1, 3)
                                ball = False
                        else:
                            team1_points += randint(2, 3)
                    else:
                        if p2.steal_ball() == True:
                            ball = False
                        else:
                            foul = randint(1, 5)
                            if foul == 1:
                                if p1.take_shot() == True:
                                    team1_points += 1
                                ball = False
                else:
                    if p2.take_shot() == True:
                        if p1.block_shot() == True:
                            ball = False
                            foul = randint(1, 5)
                            if foul == 1:
                                if p2.take_shot() == True:
                                    team2_points += randint(1, 3)
                                ball = True
                        else:
                            team2_points += randint(2, 3)
                    else:
                        if p1.steal_ball() == True:
                            ball = True
                        else:
                            foul = randint(1, 5)
                            if foul == 1:
                                if p2.take_shot() == True:
                                    team2_points += 1
                                ball = True
    return team1_points, team2_points

def change_record(team1_points, team2_points, team1, team2):
    if team1_points > team2_points:
        team1.record[0] += 1
        team2.record[1] += 1
    else:
        team1.record[1] += 1
        team2.record[0] += 1

def play_games_in_division(Atlantic, Pacific, Central, Southeast, Southwest, Northwest):
    for z in range(0, 4):
        for x in range(4):
            team1_points, team2_points = play_game(Atlantic[0].players, Atlantic[z+1].players, Atlantic[0], Atlantic[z+1])
            change_record(team1_points, team2_points, Atlantic[0], Atlantic[z+1])
        if z >= 1:
            for y in range(4):
                team1_points, team2_points = play_game(Atlantic[1].players, Atlantic[z+1].players, Atlantic[1], Atlantic[z+1])
                change_record(team1_points, team2_points, Atlantic[1], Atlantic[z+1])
        if z >= 2:
            for a in range(4):
                team1_points, team2_points = play_game(Atlantic[2].players, Atlantic[z+1].players, Atlantic[2], Atlantic[z+1])
                change_record(team1_points, team2_points, Atlantic[2], Atlantic[z+1])
        if z >= 3:
            for b in range(4):
                team1_points, team2_points = play_game(Atlantic[3].players, Atlantic[z+1].players, Atlantic[3], Atlantic[z+1])
                change_record(team1_points, team2_points, Atlantic[3], Atlantic[z+1])
    for z in range(0, 4):
        for x in range(4):
            team1_points, team2_points = play_game(Pacific[0].players, Pacific[z+1].players, Pacific[0], Pacific[z+1])
            change_record(team1_points, team2_points, Pacific[0], Pacific[z+1])
        if z >= 1:
            for y in range(4):
                team1_points, team2_points = play_game(Pacific[1].players, Pacific[z+1].players, Pacific[1], Pacific[z+1])
                change_record(team1_points, team2_points, Pacific[1], Pacific[z+1])
        if z >= 2:
            for a in range(4):
                team1_points, team2_points = play_game(Pacific[2].players, Pacific[z+1].players, Pacific[2], Pacific[z+1])
                change_record(team1_points, team2_points, Pacific[2], Pacific[z+1])
        if z >= 3:
            for b in range(4):
                team1_points, team2_points = play_game(Pacific[3].players, Pacific[z+1].players, Pacific[3], Pacific[z+1])
                change_record(team1_points, team2_points, Pacific[3], Pacific[z+1])
    for z in range(0, 4):
        for x in range(4):
            team1_points, team2_points = play_game(Central[0].players, Central[z+1].players, Central[0], Central[z+1])
            change_record(team1_points, team2_points, Central[0], Central[z+1])
        if z >= 1:
            for y in range(4):
                team1_points, team2_points = play_game(Central[1].players, Central[z+1].players, Central[1], Central[z+1])
                change_record(team1_points, team2_points, Central[1], Central[z+1])
        if z >= 2:
            for a in range(4):
                team1_points, team2_points = play_game(Central[2].players, Central[z+1].players, Central[2], Central[z+1])
                change_record(team1_points, team2_points, Central[2], Central[z+1])
        if z >= 3:
            for b in range(4):
                team1_points, team2_points = play_game(Central[3].players, Central[z+1].players, Central[3], Central[z+1])
                change_record(team1_points, team2_points, Central[3], Central[z+1])
    for z in range(0, 4):
        for x in range(4):
            team1_points, team2_points = play_game(Southwest[0].players, Southwest[z+1].players, Southwest[0], Southwest[z+1])
            change_record(team1_points, team2_points, Southwest[0], Southwest[z+1])
        if z >= 1:
            for y in range(4):
                team1_points, team2_points = play_game(Southwest[1].players, Southwest[z+1].players, Southwest[1], Southwest[z+1])
                change_record(team1_points, team2_points, Southwest[1], Southwest[z+1])
        if z >= 2:
            for a in range(4):
                team1_points, team2_points = play_game(Southwest[2].players, Southwest[z+1].players, Southwest[2], Southwest[z+1])
                change_record(team1_points, team2_points, Southwest[2], Southwest[z+1])
        if z >= 3:
            for b in range(4):
                team1_points, team2_points = play_game(Southwest[3].players, Southwest[z+1].players, Southwest[3], Southwest[z+1])
                change_record(team1_points, team2_points, Southwest[3], Southwest[z+1])
    for z in range(0, 4):
        for x in range(4):
            team1_points, team2_points = play_game(Southeast[0].players, Southeast[z+1].players, Southeast[0], Southeast[z+1])
            change_record(team1_points, team2_points, Southeast[0], Southeast[z+1])
        if z >= 1:
            for y in range(4):
                team1_points, team2_points = play_game(Southeast[1].players, Southeast[z+1].players, Southeast[1], Southeast[z+1])
                change_record(team1_points, team2_points, Southeast[1], Southeast[z+1])
        if z >= 2:
            for a in range(4):
                team1_points, team2_points = play_game(Southeast[2].players, Southeast[z+1].players, Southeast[2], Southeast[z+1])
                change_record(team1_points, team2_points, Southeast[2], Southeast[z+1])
        if z >= 3:
            for b in range(4):
                team1_points, team2_points = play_game(Southeast[3].players, Southeast[z+1].players, Southeast[3], Southeast[z+1])
                change_record(team1_points, team2_points, Southeast[3], Southeast[z+1])
    for z in range(0, 4):
        for x in range(4):
            team1_points, team2_points = play_game(Northwest[0].players, Northwest[z+1].players, Northwest[0], Northwest[z+1])
            change_record(team1_points, team2_points, Northwest[0], Northwest[z+1])
        if z >= 1:
            for y in range(4):
                team1_points, team2_points = play_game(Northwest[1].players, Northwest[z+1].players, Northwest[1], Northwest[z+1])
                change_record(team1_points, team2_points, Northwest[1], Northwest[z+1])
        if z >= 2:
            for a in range(4):
                team1_points, team2_points = play_game(Northwest[2].players, Northwest[z+1].players, Northwest[2], Northwest[z+1])
                change_record(team1_points, team2_points, Northwest[2], Northwest[z+1])
        if z >= 3:
            for b in range(4):
                team1_points, team2_points = play_game(Northwest[3].players, Northwest[z+1].players, Northwest[3], Northwest[z+1])
                change_record(team1_points, team2_points, Northwest[3], Northwest[z+1])
def play_games_against_6_out_of_conference(Atlantic, Pacific, Central, Southeast, Southwest, Northwest):
    teams_possible = []
    for team in Atlantic:
        teams_possible = Central + Southeast
        for played_team in team.has_played:
            if played_team in teams_possible:
                teams_possible.remove(played_team)
        number_of_teams_to_play = 6 - len(team.has_played)
        for x in range(number_of_teams_to_play):
            opposing_team = choice(teams_possible)
            teams_possible.remove(opposing_team)
            team.has_played.append(opposing_team)
            opposing_team.has_played.append(team)
            for z in range(4):
                team1_points, team2_points = play_game(team.players, opposing_team.players, team, opposing_team)
                change_record(team1_points, team2_points, team, opposing_team)
    
    for team in Central:
        teams_possible = Atlantic + Southeast
        for played_team in team.has_played:
            if played_team in teams_possible:
                teams_possible.remove(played_team)
        number_of_teams_to_play = 6 - len(team.has_played)
        for x in range(number_of_teams_to_play):
            opposing_team = choice(teams_possible)
            teams_possible.remove(opposing_team)
            team.has_played.append(opposing_team)
            opposing_team.has_played.append(team)
            for z in range(4):
                team1_points, team2_points = play_game(team.players, opposing_team.players, team, opposing_team)
                change_record(team1_points, team2_points, team, opposing_team)

    for team in Southeast:
        teams_possible = Atlantic + Southeast
        for played_team in team.has_played:
            if played_team in teams_possible:
                teams_possible.remove(played_team)
        number_of_teams_to_play = 6 - len(team.has_played)
        for x in range(number_of_teams_to_play):
            opposing_team = choice(teams_possible)
            teams_possible.remove(opposing_team)
            team.has_played.append(opposing_team)
            opposing_team.has_played.append(team)
            for z in range(4):
                team1_points, team2_points = play_game(team.players, opposing_team.players, team, opposing_team)
                change_record(team1_points, team2_points, team, opposing_team)


    for team in Northwest:
        teams_possible = Pacific + Southwest
        for played_team in team.has_played:
            if played_team in teams_possible:
                teams_possible.remove(played_team)
        number_of_teams_to_play = 6 - len(team.has_played)
        for x in range(number_of_teams_to_play):
            opposing_team = choice(teams_possible)
            teams_possible.remove(opposing_team)
            team.has_played.append(opposing_team)
            opposing_team.has_played.append(team)
            for z in range(4):
                team1_points, team2_points = play_game(team.players, opposing_team.players, team, opposing_team)
                change_record(team1_points, team2_points, team, opposing_team)

    for team in Southwest:
        teams_possible = Pacific + Northwest
        for played_team in team.has_played:
            if played_team in teams_possible:
                teams_possible.remove(played_team)
        number_of_teams_to_play = 6 - len(team.has_played)
        for x in range(number_of_teams_to_play):
            opposing_team = choice(teams_possible)
            teams_possible.remove(opposing_team)
            team.has_played.append(opposing_team)
            opposing_team.has_played.append(team)
            for z in range(4):
                team1_points, team2_points = play_game(team.players, opposing_team.players, team, opposing_team)
                change_record(team1_points, team2_points, team, opposing_team)

    for team in Pacific:
        teams_possible = Northwest + Southwest
        for played_team in team.has_played:
            if played_team in teams_possible:
                teams_possible.remove(played_team)
        number_of_teams_to_play = 6 - len(team.has_played)
        for x in range(number_of_teams_to_play):
            opposing_team = choice(teams_possible)
            teams_possible.remove(opposing_team)
            team.has_played.append(opposing_team)
            opposing_team.has_played.append(team)
            for z in range(4):
                team1_points, team2_points = play_game(team.players, opposing_team.players, team, opposing_team)
                change_record(team1_points, team2_points, team, opposing_team)
# 4 games against the other 4 division opponents (4×4=16 games),
# 4 games* against 6 (out-of-division) conference opponents (4×6=24 games),
# 3 games against the remaining 4 conference teams (3×4=12 games),
# 2 games against teams in the opposing conference (2×15=30 games).

def main():
    global teams
    init()
    next_teams = []

    Atlantic = teams[0:5]
    Pacific = teams[5:10]
    Central = teams[10:15]
    Southwest = teams[15:20]
    Southeast = teams[20:25]
    Northwest = teams[25:]

    divisions = [Atlantic, Pacific, Central, Southwest, Southeast, Northwest]

    play_games_in_division(Atlantic, Pacific, Central, Southeast, Southwest, Northwest)
    play_games_against_6_out_of_conference(Atlantic, Pacific, Central, Southeast, Southwest, Northwest)
    print_record()
main()