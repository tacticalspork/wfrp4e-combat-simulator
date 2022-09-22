from SimplifiedCharacter import SimplifiedCharacter
import random

def MeleeFight(fighterOne, fighterTwo, penalty):
    fighterOneRoll = random.randint(1, 100)
    fighterTwoRoll = random.randint(1, 100)
    fightOutcome = (fighterOneRoll + fighterOne.MeleeSkill) - (fighterTwoRoll + fighterTwo.MeleeSkill) - penalty
    if(fightOutcome > 0):
        fighterOneDamage = fighterOne.MeleeDamage + (abs(fightOutcome) % 100) // 10 - fighterTwo.Armor - fighterTwo.ToughnessBonus
        fighterTwo.Hitpoints = fighterTwo.Hitpoints - fighterOneDamage
    elif(fightOutcome < 0):
        fighterTwoDamage = fighterTwo.MeleeDamage + (abs(fightOutcome) % 100) // 10 - fighterOne.Armor - fighterOne.ToughnessBonus
        fighterOne.Hitpoints = fighterOne.Hitpoints - fighterTwoDamage
    else:
        pass #tie