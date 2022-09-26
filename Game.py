from Army import Army
from FightingGroup import FightingGroup
from GameSettings import GameSettings
import random

class Game():
    def __init__(self):
        self.gameSettings = GameSettings()

    def run(self):
        self.teamOne = Army()
        self.teamTwo = Army()

        self.teamOne.CreateSkavenSwarmUnits()
        self.teamTwo.CreateGodUnits()

        turns = 50
        for i in range(turns):
            print("--------------------")
            print("Turn # " + str(i+1))
            winningArmy = self.fightArmy(self.teamOne, self.teamTwo)
            if(winningArmy != None):
                print("The battle has been decided, " + winningArmy.Name + " has won")
                break


    def fightArmy(self, teamOne, teamTwo):
        largerTeam = teamOne
        smallerTeam = teamTwo
        if(len(teamOne.AliveUnits) < len(teamTwo.AliveUnits)):
            largerTeam = teamTwo
            smallerTeam = teamOne
        
        if(self.gameSettings.groupFight):
            fightingGroups = self.CreateFightingGroups(smallerTeam, largerTeam)
            
            for i in range(len(fightingGroups)):
                fightingGroups[i].Fight(self.gameSettings.maxOutnumbering, self.gameSettings.outnumberingPenalty, self.gameSettings.maxAdvantage)
        else:
            #determine which unit has higher advantage, then have them attack first. Also determine outnumbering.
            
            pass



        return self.finishArmyFightRound(largerTeam, smallerTeam)

    def CreateFightingGroups(self, smallerTeam, largerTeam):
        fightingGroups = []

        largerTeamNumberOfUnits = len(largerTeam.AliveUnits)
        smallerTeamNumberOfUnits = len(smallerTeam.AliveUnits)

        for i in range(smallerTeamNumberOfUnits):
            fightingGroup = FightingGroup(smallerTeam.AliveUnits[i], [])
            fightingGroups.append(fightingGroup)

        for i in range(largerTeamNumberOfUnits):
            fightingGroups[(i % smallerTeamNumberOfUnits)].groupFighters.append(largerTeam.AliveUnits[i])

        return fightingGroups


    def finishArmyFightRound(self, largerTeam, smallerTeam):
        largerTeam.PurgeDeadUnits()
        smallerTeam.PurgeDeadUnits()

        largerTeam.StateArmy()
        smallerTeam.StateArmy()

        if(len(largerTeam.AliveUnits) == 0):
            return smallerTeam
        if(len(smallerTeam.AliveUnits) == 0):
            return largerTeam
        return None

    
