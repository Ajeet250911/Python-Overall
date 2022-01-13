def user_details(name,*phone_number):
    print("Hello "+name,end=" ")
    for num in phone_number:
        print(num,end=" ")
    print(" ")

def main():
    user_details("Scott",943424554)
    user_details("Smith",92425425,914144623)

if __name__ == '__main__':
    main()

