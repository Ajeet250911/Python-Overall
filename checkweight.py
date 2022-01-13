def checkage(age,weight):
    if 18<=age<=30:
        if (40<=weight<=60):
            print("Healthy")
        else:
            print("underweight")
    else:
        print("Unhealthy")
def main():
    age=(int(input("Enter the age")))
    weight=(int(input("Enter the weight")))
    checkage(age, weight)

if __name__ == '__main__':
    main()

