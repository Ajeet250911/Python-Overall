class Player:
    def setdetails(self,name,country):
        self.name=name
        self.country=country

    def getdetails(self):
        print(f"Player name is {self.name} and Player belongs to {self.country}")

class CricketPlayer(Player):
    def setinfo(self,type):
        self.type=type

    def getinfo(self):
        print(self.name,"is a Cricket Player of type",self.type)

class HockeyPlayer(Player):
    def setinfo(self,type,shoestype):
            self.type = type
            self.shoestype=shoestype

    def getinfo(self):
            print(self.name, "is a Hockey Player of type", self.type,"and with shoes type",self.shoestype)

print("-------Cricket Sub class---------")
cp=CricketPlayer()
cp.setdetails("M.S Dhoni","India")
cp.getdetails()
cp.setinfo("All Rounder")
cp.getinfo()

print("-------Hockey Sub class---------")
hp=HockeyPlayer()
hp.setdetails("Ajeet","India")
hp.getdetails()
hp.setinfo("Defender","Spikes")
hp.getinfo()

