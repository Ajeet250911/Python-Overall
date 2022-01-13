class Library:
    def setdeatils(self,librarian_name,address,timings):
        self.librarian_name=librarian_name
        self.address=address
        self.timings=timings
    def getdetails(self):
        print("Librarian name is",self.librarian_name)
        print("Library address is",self.address)
        print("Library opening timings is",self.timings)

class SchoolLibrary(Library):
    def set(self,principal_name):
        self.principal_name=principal_name
    def getdetails(self):
        super().getdetails()
        print("School principal name is",self.principal_name)

    @staticmethod
    def fine(no_of_days):
        if no_of_days<10:
            print("Fine will be",1*(no_of_days),".rs")
        elif 10<=no_of_days<20:
            print("Fine will be",5*(no_of_days-10)+10,".rs")
        elif no_of_days>=20:
            print("Fine will be",10*(no_of_days-20)+60,".rs")

l=SchoolLibrary()
l.setdeatils("Scott","Lucknow","9:00 AM to 4:00 PM ")
l.set("Mr.Josh")
l.getdetails()
no_of_days=int(input("Enter the number of days"))
SchoolLibrary.fine(no_of_days)
