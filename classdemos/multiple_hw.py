class SmartPhone:
    def setPhone(self,calling,gps):
        self.calling=calling
        self.gps=gps
    def getPhone(self):
        print("Phone can be used for",self.calling)
        print("Phone has a system of navigation",self.gps)

class Watch:
    def setWatch(self,cloacktype,):
        self.cloacktype=cloacktype
    def getWatch(self):
        print("Watch cloack type is",self.cloacktype)

class SmartWatch(SmartPhone,Watch):
    def setSmartWatch(self,company):
        self.company=company
    def getdetails(self):
        print("Company name is",self.company)

s=SmartWatch()
s.setPhone("Video calling","location")
s.setWatch("Digital cloack")
s.setSmartWatch("Apple")
s.getPhone()
s.getWatch()
s.getdetails()