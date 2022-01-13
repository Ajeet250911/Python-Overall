def sum(*numbers):
    add=0
    numlen=len(numbers)
    for num in numbers:
        add=add+num
    print("sum of %d numbers is %d "%(numlen,add)) #format specifier

def main():
    sum(3,67,98)
    sum(45,57,5,7,75)
    sum(325,53,433,635,224,465)

if __name__ == '__main__':
    main()
