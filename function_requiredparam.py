def checkemail(email):
    if email.count("@")==0 or email.count(".")==0:
        print("Invalid email")
    else:
        print("valid email")

def entrypoint():
    email=input("Enter Email")
    checkemail(email)
if __name__ == '__main__':entrypoint()
