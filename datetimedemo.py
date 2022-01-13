import datetime

def display():
    v= datetime.date.today()
    print("Current date is :-",v)
    print("Current day is :-",v.weekday())
    print("Current month is :-",v.month)
    print("Current year is :-",v.year)
    print()

    v1=datetime.datetime.now()
    print("Current day in alphabet is :-",v1.strftime("%A"))
    print("Current month in alphabet is :-",v1.strftime("%B"))
    print("Last two digit of Current year is :-",v1.strftime("%y"))
    print()

    v3=datetime.datetime.now()
    print("Current Time is :-",v3.time())

def main():
    display()
if __name__ == '__main__':
    main()