class Character():
    def __init__(self, MeleeSkill = 0, RangedSkill = 0, MeleeDamage = 0, RangedDamage = 0, Armor  = 0, Toughness = 0, Dodge = 0, Hitpoints = 0):
        self.MeleeSkill = MeleeSkill
        self.RangedSkill = RangedSkill
        self.MeleeDamage = MeleeDamage
        self.RangedDamage = RangedDamage
        self.Armor = Armor
        self.Toughness = Toughness
        self.ToughnessBonus = Toughness // 10
        self.Dodge = Dodge
        self.Hitpoints = Hitpoints

    def CreateCharacter(self):
        print("What is their melee skill?")
        self.MeleeSkill = input()
        print("What is their ranged skill?")
        self.RangedSkill = input()
        print("What is their melee damage?")
        self.MeleeDamage = input()
        print("What is their ranged damage?")
        self.RangedDamage = input()
        print("What is their armor?")
        self.Armor = input()
        print("What is their toughness?")
        self.Toughness = input()
        self.ToughnessBonus = self.Toughness // 10
        print("What is their dodge skill?")
        self.Dodge = input()
        print("What is their hitpoints?")
        self.Hitpoints = input()

    def printSkills():
        print("Melee skill, ranged skill, armor, toughness, dodge, hitpoints")
