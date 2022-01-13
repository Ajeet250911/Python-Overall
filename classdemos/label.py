class Label:
    def setdetails(self,color,text,width,height):
        self.color=color
        self.text=text
        self.width=width
        self.height=height

    def getdetails(self):
        print("Label Color is",self.color)
        print(f"label Text is {self.text} , Width is {self.width} and Height is {self.height}")

    # def __init__(self):  #initailised ,like a constructor in java
    #     print("in init method") #default init

    def __init__(self,color,text,width,height):  #it is also called dunder method #parameterised inint(constructor)
        self.color = color
        self.text = text
        self.width = width
        self.height = height

# label1=Label()
# label1.setdetails("Red","Name",100,40)
# label1.getdetails()

print("****Using __init()__ function****")
label2=Label("Blue","Age",120,60) #__init__ gets called automatically
label2.getdetails()
label2.setdetails("Yellow","Age",120,60) #__init__ overridding
label2.getdetails()


