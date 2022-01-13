#default Arguement
def calculate_area(len,breath,color="Red"):
    area=len*breath
    print(f"Area of rectangle is {area} and color is {color}")

def main():
    calculate_area(4,6) #it will use default arugument
    calculate_area(6,7,"Blue")

if __name__ == '__main__':main()