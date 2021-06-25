class GeneralManager:
    def __init__(self, IQ, persuade, name):
        self.IQ = IQ
        self.persuade = persuade
        self.name = name

    def trade(self, players_wanted, players_have):
        for team_player in players_have:
            if team_player.position == 1:
                avg = print()