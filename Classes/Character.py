from tokenize import Name


class Character():
    def __init__(self, Name, StatBlock = None, SkillBlock = None, Talents = None):
        self.Name = Name
        self.StatBlock = StatBlock
        self.SkillBlock = SkillBlock
        self.Talents = Talents
