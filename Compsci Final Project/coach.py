from random import randint
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

class Coach:
    def __init__(self, energy, dIQ, oIQ):
        self.energy = energy
        self.dIQ = dIQ
        self.oIQ = oIQ

    def run_defensive_play(self, play):
        rand = randint(1, 100)
        correct_play = False
        if rand <= self.dIQ:
            correct_play = True

        if correct_play:
            if play == 1:
                return 7
            elif play == 2:
                return 1
            elif play == 3:
                return 2
            elif play == 4:
                return 6
            elif play == 5:
                return 4
            elif play == 6:
                return 3
            elif play == 7:
                return 5
        else:
            return randint(1, 7)
    
    def run_offensive_play(self, play):
        rand = randint(1, 100)
        correct_play = False
        if rand <= self.oIQ:
            correct_play = True
        
        if correct_play:
            if play == 1:
                return 5
            elif play == 2:
                return 4
            elif play == 3:
                return 2
            elif play == 4:
                return 1
            elif play == 5:
                return 3
            elif play == 6:
                return 6
            elif play == 7:
                return 7
        else:
            return randint(1, 7)

    def change_offensive_play(self, play):
        rand = randint(1, 100)
        if self.oIQ > rand:
            return self.run_offensive_play(play)

    def change_defensive_play(self, play):
        rand = randint(1, 100)
        if self.dIQ > rand:
            return self.run_defensive_play(play)