from FightRules import MeleeFight

class FightingGroup():
    def __init__(self, fighterOne = None, groupFighters = []):
        self.fighterOne = fighterOne
        self.groupFighters = groupFighters

    def PrintGroup(self):
        print(self.fighterOne.MeleeSkill)
        print(len(self.groupFighters))

    def Fight(self, maxOutnumbering, outnumberingPenalty):
        numFightersFighting = 1
        if(len(self.groupFighters) > maxOutnumbering):
            numFightersFighting = maxOutnumbering
        else:
            numFightersFighting = len(self.groupFighters)

        penalty = outnumberingPenalty * (numFightersFighting - 1)

        for i in range(numFightersFighting):
            MeleeFight(self.fighterOne, self.groupFighters[i], penalty)