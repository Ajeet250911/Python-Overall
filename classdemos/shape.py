class Shape:
    def getarea(self):
        print("Area has to be calculated")
    def setcolor(self,color):
        self.color=color
    def getcolor(self):
        print("Color of the shape is",self.color)

class Circle(Shape):
    def setdim(self,radius):
        self.radius=radius
    def getdim(self):
        print("Radius of the Circle is",self.radius)
    def getarea(self):
        area=3.14*self.radius*self.radius
        print("Area of the Circle is",area)

class Triangle(Shape):
    def setdim(self,witdh,height):
        self.width=witdh
        self.height=height
    def getdim(self):
        print("Width of the Triangle is",self.width,"and the Height of the Triangle is",self.height)
    def getarea(self):
        area=1/2*self.width*self.height
        print("Area of the Triangle is",area)

print("------Circle Sub Class------")
c=Circle()
color=input("Enter the color")
radius=int(input("Enter the radius"))
c.setcolor(color)
c.setdim(radius)
c.getcolor()
c.getdim()
c.getarea()
print()

print("------Triangle Sub Class------")
t=Triangle()
color=input("Enter the color")
width=int(input("Enter the width"))
height=int(input("Enter the height"))
t.setcolor(color)
t.setdim(width,height)
t.getcolor()
t.getdim()
t.getarea()
