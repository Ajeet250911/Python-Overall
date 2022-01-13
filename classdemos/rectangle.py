class Rectangle:
    def setdim(self,width,height):
        self.width=width
        self.height=height

    def getdim(self):
        print("width is %d and height is %d" %(self.width,self.height))

    def getarea(self):
        area=self.width*self.height
        print("Area of rectangle is",area)

    def getparameter(self):
        parameter=2*(self.width+self.height)
        print("Parameter of rectangle is",parameter)

    def __str__(self):
        return "this is rectangle class"

rec=Rectangle()
rec.setdim(5,6)
rec.getdim()
rec.getarea()
rec.getparameter()
print(rec) #print the object representation