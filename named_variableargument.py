def regdetails(userid,password,**otherdetails):
    print("userid is "+userid)
    print("password is "+password)
    for info in otherdetails.values():
        print(info,end=" ")
    print(" ")

def main():
    regdetails("scott@123","scottlang",email="scott@gmail.com")
    regdetails("smith@123", "dwanyesmith",phone=3903592342)
    regdetails("anant@123", "anantgupta",phone=309529521,cityname="America")

if __name__ == '__main__':
    main()