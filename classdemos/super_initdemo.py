class Frame:
    def __init__(self,width,height,color):
        self.width=width
        self.height=height
        self.color=color
    def getDetails(self):
        print(f"Frame width is {self.width}, height is {self.height} and color is {self.color}")

class PhotoFrame(Frame):
    def __init__(self,width,height,color,picname):
        super().__init__(width,height,color)
        self.picname=picname
    def getDetails(self):
        super().getDetails()
        print("PhotoFrame location is",self.picname)

p=PhotoFrame(400,300,"Red","abc.jpg")
p.getDetails()