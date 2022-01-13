class Game:
    def setdetails(self,no_of_players,equipments):
        self.no_of_players=no_of_players
        self.equipments=equipments
    def getdetails(self):
        print("Number of players in the game is",self.no_of_players,"and the equipments used in the game is",self.equipments)

class IndoorGame(Game):
    def indoor_setdetails(self,type):
        self.type=type
    def getdetails(self):
        super().getdetails() #calling super class getdetails method
        print("It is a",self.type,"Game")

class Ludo(IndoorGame):
    def ludo_setdetails(self,boardtype):
        self.boardtype=boardtype
    def getdetails(self):
        super().getdetails()
        print("Board material type is",self.boardtype)

l=Ludo()
l.setdetails(4,"Board, Dice and Ludo pieces")
l.indoor_setdetails("Board")
l.ludo_setdetails("Cardboard")
l.getdetails()