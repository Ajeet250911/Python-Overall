class Fruit:
    def setDetails(self,color,taste):
        self.color=color
        self.taste=taste
    def getDetails(self):
        print(f"Color is {self.color} and taste is {self.taste}")

class Mango(Fruit):
    def __init__(self,variety,color,taste):
        super().setDetails(color,taste)
        self.variety=variety
    def getDetails(self):
        super().getDetails()
        print("It is of type",self.variety)

m=Mango("Dushahri","Yellow","Sweet")
#m.setDetails("Yellow","Sweet") #calling explicitly
m.getDetails()