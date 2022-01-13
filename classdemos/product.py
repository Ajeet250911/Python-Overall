class Product:
    def setDetails(self,name,price):
        self.name=name
        self.price=price

    def getdiscount(self):
        cal_discount=self.price-(0.20*self.price)
        print("Discounted price is",cal_discount)

    def getDetails(self):
        print("Product name is",self.name,"Product actual price is",self.price)

# p=Product()
# name=input("Enter name")
# price=float(input("Enter price"))
# p.setDetails(name,price)
# p.getdiscount()
# p.getDetails()
#
# p1=Product()
# name=input("Enter name")
# price=float(input("Enter price"))
# p1.setDetails(name,price)
# p1.getdiscount()
# p1.getDetails()

for i in range(2):
    p=Product()
    name = input("Enter name")
    price = int(input("Enter price"))
    p.setDetails(name, price)
    p.getdiscount()
    p.getDetails()




