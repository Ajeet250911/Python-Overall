class Company:
    Domain="Software Development" #class variable

    def setdetails(self,cname,email): #instance method
        self.cname=cname
        self.email=email
    def getdetails(self):
        print("Company name is",self.cname,"and","Company email is",self.email) #print instance method
        print("Company domain is",Company.Domain) #class variable print

    @classmethod
    def changedetails(cls):
        cls.Domain=cls.Domain+" and Training"

c=Company()
c.setdetails("TCS","tcs123@gmail.com")
c.getdetails()
Company.changedetails()
print()
c.getdetails()






