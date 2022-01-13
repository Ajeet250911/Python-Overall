class WeighingMachine:
    def __init__(self,company,price):
        self.company=company
        self.price=price

    def getdetails(self):
        print("Company name is "+self.company)
        print("Machine price is",self.price)

    @staticmethod
    def checkweight(weight):
        if weight>=45 and weight<60:
            print("Healthy")
        elif weight>=60 and weight>100:
            print("Over weight")
        else:
            print("Unhealthy")

weight=int(input("Enter your weight"))
WeighingMachine.checkweight(weight) # method calling with class name
w=WeighingMachine("Casio",1500)
w.getdetails() #we need object to call instance method


