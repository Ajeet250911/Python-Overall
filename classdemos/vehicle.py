class Vehicle:
    def setDetails(self,color,price,model,company,no_of_wheels,seat_belt):
        self.color=color
        self.price=price
        self.model=model
        self.company=company
        self.no_of_wheels=no_of_wheels
        self.seat_belt=seat_belt
    def getDetails(self):
        print("Vehicle color is",self.color)
        print("Vehicle price is",self.price)
        print("Vehicle model is",self.model)
        print("Vehicle company name is",self.company)
        print("Vehicle number of wheels are",self.no_of_wheels)
        print("Vehicle has set belt",self.seat_belt)

class TwoWheeler(Vehicle):
    def setInfo(self,fuel_filled,distance_covered):
        self.fuel_filled=fuel_filled
        self.distance_covered=distance_covered
    def mileage(self):
        average=self.distance_covered/self.fuel_filled
        print("Mileage of the vehicle is",average)
        super().getDetails()

class Bike(TwoWheeler):
    def setBikeDetails(self,helmet,no_of_person):
        self. helmet= helmet
        self.no_of_person=no_of_person
    def mileage(self):
        super().mileage()
    def getBikeDetails(self):
        print("Biker wearing helmet",self.helmet)
        print("Number of person on the bike is",self.no_of_person)

b=Bike()
b.setDetails("Black",180000,"Version 4","Yamaha",2,bool(False))
b.getDetails()
b.setInfo(465,10)
b.mileage()
b.setBikeDetails(bool(True),2)
b.getBikeDetails()
