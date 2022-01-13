import random

def r1():
    rm=random.randint(2,5)
    print("Random number is",rm)
    print()

    name=["Scott","Josh","Drake","Mike","kevin"]
    random.shuffle(name)
    randomname = random.choice(name)
    print("Random suffling is",name)
    print("Random name is", randomname)

def main():
     r1()
if __name__ == '__main__':
    main()