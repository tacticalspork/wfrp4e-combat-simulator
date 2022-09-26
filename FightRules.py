from Character import Character
import random

class FightRules():
    def MeleeFightNoInitiative(fighterOne, fighterTwo, penalty, maxAdvantage):
        fighterOneRoll = random.randint(1, 100)
        fighterTwoRoll = random.randint(1, 100)
        fightOutcome = (fighterOneRoll + fighterOne.MeleeSkill) - (fighterTwoRoll + fighterTwo.MeleeSkill) - penalty
        if(fightOutcome > 0):
            fighterOneDamage = fighterOne.MeleeDamage + (abs(fightOutcome) % 100) // 10 - fighterTwo.Armor - fighterTwo.ToughnessBonus
            if(fighterOneDamage < 0):
                fighterOneDamage = 1
            fighterTwo.Hitpoints = fighterTwo.Hitpoints - fighterOneDamage
        elif(fightOutcome < 0):
            fighterTwoDamage = fighterTwo.MeleeDamage + (abs(fightOutcome) % 100) // 10 - fighterOne.Armor - fighterOne.ToughnessBonus
            if(fighterTwoDamage < 0):
                fighterTwoDamage = 1
            fighterOne.Hitpoints = fighterOne.Hitpoints - fighterTwoDamage
        else:
            pass #tie

    def MeleeFightWithInitiative(fighterOne, fighterTwo, penalty, maxAdvantage):
        fighterOneRoll = random.randint(1, 100)
        fighterTwoRoll = random.randint(1, 100)
        fightOutcome = (fighterOneRoll + fighterOne.MeleeSkill) - (fighterTwoRoll + fighterTwo.MeleeSkill) - penalty