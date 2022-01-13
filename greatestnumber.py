def greatest(numberlist):
    num=max(numberlist)
    print("greatest number is ",num)

def main():
    numlist=[3,5,8,6]
    greatest(numlist)
if __name__ == '__main__':main()

# for input from keyboard
def greatest(numberlist):
    num=max(numberlist)
    print("greatest number is ",num)

def main():
    numlist=[] #emptylist
    for i in range(3):
        number=int(input("Enter number"))
        numlist.append(number)
    greatest(numlist)
if __name__ == '__main__':main()





