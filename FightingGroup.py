from FightRules import FightRules

class FightingGroup():
    def __init__(self, fighterOne = None, groupFighters = []):
        self.fighterOne = fighterOne
        self.groupFighters = groupFighters

    def PrintGroup(self):
        print(self.fighterOne.MeleeSkill)
        print(len(self.groupFighters))

    def Fight(self, maxOutnumbering, outnumberingPenalty, maxAdvantage):
        numFightersFighting = 1
        if(len(self.groupFighters) > maxOutnumbering):
            numFightersFighting = maxOutnumbering
        else:
            numFightersFighting = len(self.groupFighters)

        penalty = outnumberingPenalty * (numFightersFighting - 1)

        for i in range(numFightersFighting):
            FightRules.MeleeFightNoInitiative(self.fighterOne, self.groupFighters[i], penalty, maxAdvantage)