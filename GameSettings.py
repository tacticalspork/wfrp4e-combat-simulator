class GameSettings():
    def __init__(self):
        self.maxOutnumbering = 3
        self.outnumberingPenalty = -10 #determines how much disadvantage per outnumbering

        self.usesInitiative = True
        
        self.maxAdvantage = 3

        self.groupFight = False