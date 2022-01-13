from calculation import multiply,divide as d #specific functions used from module
#from calculation import * #astric means all functions are called

def calculate():
    print("Multipication of numbers is",multiply(4,5))
    division=d(10,2)
    print("Division of numbers is %d "%(division))

def main():
    calculate()
if __name__ == '__main__':
    main()