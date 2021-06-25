class Team:
    def __init__(self, name, coach, record, players, reserves, play, gm, has_played):
        self.name = name
        self.coach = coach
        self.record = record
        self.players = players
        self.reserves = reserves
        self.gm = gm
        self.has_played = has_played

    def change_coach(self, coach):
        self.coach = coach

    def change_player(self, player_to_add, player_to_remove):
        if player_to_remove == None:
            self.player.append(player_to_add)
        elif player_to_add == None:
            self.players.remove(player_to_remove)
        else:
            self.players.remove(player_to_remove)
            self.player.append(player_to_add)
    
    def change_reserves(self, player_to_add, player_to_remove):
        if player_to_remove == None:
            self.reserves.append(player_to_add)
        elif player_to_add == None:
            self.reserves.remove(player_to_remove)
        else:
            self.reserves.remove(player_to_remove)
            self.reserves.append(player_to_add)

    def change_play(self, play):
        self.play = play