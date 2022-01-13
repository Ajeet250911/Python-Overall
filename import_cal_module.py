#import calculation
import calculation as c # alias=nickname for calculation module

#sum=calculation.addition(2,3) # Syntax is module_name.functio_name for calling module but not a proper way
#proper way is to put it in a function

def docalculation():
    sum=c.addition(2,5) #calling module file function
    print("sum of number is ",sum)
    c.subtract(9,6)

def main():
    docalculation()
if __name__ == '__main__':
    main()