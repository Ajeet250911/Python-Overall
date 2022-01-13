class Square:
    def setdim(self,side):
        self.side=side

    def getdim(self):
        print("Side of square is",self.side)

    def getarea(self):
        area=self.side*self.side
        print("Area of square is",area)

s=Square()
s.setdim(6)
s.getdim()
s.getarea()
