class Cuboid:
    def getdim(self,length,breadth,height):
        self.len=length
        self.bre=breadth
        self.hei=height
    def showdim(self):
        print("length of cube is",self.len,"Breadth of cube is",self.bre,"Height of cube is",self.hei)

    def getarea(self):
        a=2*(self.len*self.bre+self.bre*self.hei+self.len*self.hei)
        print("Area of cuboid is",a)

    def getvolume(self):
        v=self.len*self.bre*self.hei
        print("Volume of cuboid is",v)

c=Cuboid()
l=int(input("Enter the length"))
b=int(input("Enter the breadth"))
h=int(input("Enter the height"))
c.getdim(l,b,h)
c.showdim()
c.getarea()
c.getvolume()