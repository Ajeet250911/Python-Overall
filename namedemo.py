def func(name,place,**info):
    print("userid "+name)
    print("Location "+place)
    for keys,values in info.items():
        print(f"{keys} is {values}")
    print(" ")

def main():
    func("Ajeet","Lucknow",email="ajeet@gmail.com",phone=7548763847)
    func("Rohan","delhi",email="rohan@gmail.com",phone=3456345364,city="Gurgaon")
    func("Akash", "dehradun", email="akash@gmail.com", phone=8749874897, city="Delhi")

if __name__ == '__main__':
    main()
