from SimplifiedCharacter import SimplifiedCharacter
import random

class Army():
    def __init__(self):
        self.Units = []
        self.AliveUnits = []

    def CreateUnits(self):
        print("What is the name of the army?")
        self.Name = input()
        print("What is the name of the individual unit?")
        self.UnitName = input()
        print("What are the stat blocks of these set of units")
        self.characterTemplate = SimplifiedCharacter()
        self.characterTemplate.CreateCharacter()
        print("How many of them are there?")
        self.numberOfUnits = input()

        self.Units = [self.characterTemplate for i in range(self.numberOfUnits)]
        self.AliveUnits = self.Units

    def CreateTestUnits(self):
        self.Name = "Test Army"
        self.UnitName = "Test Unit"
        self.numberOfUnits = random.randint(8, 12)
        for i in range(self.numberOfUnits):
            testUnit = SimplifiedCharacter(random.randint(40, 50), random.randint(40, 50), 7, 7, 3, 3, 20, 16)
            self.Units.append(testUnit)
            self.AliveUnits.append(testUnit)
    
    def CreateSkavenUnits(self):
        self.Name = "Skaven Army"
        self.UnitName = "Clanrat"
        self.numberOfUnits = 35
        for i in range(self.numberOfUnits):
            testUnit = SimplifiedCharacter(35, 35, 5, 5, 1, 3, 20, 10)
            self.Units.append(testUnit)
            self.AliveUnits.append(testUnit)
    
    def CreateSkavenSwarmUnits(self):
        self.Name = "Skaven Swarm"
        self.UnitName = "Clanrat"
        self.numberOfUnits = 350
        for i in range(self.numberOfUnits):
            testUnit = SimplifiedCharacter(35, 35, 5, 5, 1, 3, 20, 10)
            self.Units.append(testUnit)
            self.AliveUnits.append(testUnit)
    
    def CreateEliteUnits(self):
        self.Name = "Empire Knights"
        self.UnitName = "Empire Knight"
        self.numberOfUnits = 10
        for i in range(self.numberOfUnits):
            testUnit = SimplifiedCharacter(60, 60, 8, 8, 5, 5, 20, 20)
            self.Units.append(testUnit)
            self.AliveUnits.append(testUnit)

    def CreateGodUnits(self):
        self.Name = "High Elves"
        self.UnitName = "Tyrion"
        self.numberOfUnits = 1
        for i in range(self.numberOfUnits):
            testUnit = SimplifiedCharacter(120, 120, 10, 10, 7, 7, 20, 30)
            self.Units.append(testUnit)
            self.AliveUnits.append(testUnit)

    def GetAliveUnit(self):
        self.PurgeDeadUnits()
        if(len(self.AliveUnits) == 0):
            return None
        return random.choice(self.AliveUnits)

    def PurgeDeadUnits(self):
        self.AliveUnits = []
        for i in range(self.numberOfUnits):
            if(self.Units[i].Hitpoints > 0):
                self.AliveUnits.append(self.Units[i])
        


    def StateArmy(self):
        print("Army Name: " + self.Name)
        print("Unit name: " + self.UnitName)
        print("# of units: " + str(self.numberOfUnits))
        print("# of alive units: " + str(len(self.AliveUnits)))
        for i in range(len(self.Units)):
            print(self.UnitName + " " + str(i) + " " + "Hitpoints: " + str(self.Units[i].Hitpoints))