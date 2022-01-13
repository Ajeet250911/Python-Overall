class Book:
    Author_name="Kathy Sierra"
    Publisher="McGrawb Hill Education"

    def setdetails(self,name,price):
        self.name = name
        self.price = price

    def __init__(self,name,price):
        self.name=name
        self.price=price

    def __str__(self):
        return "This is Book class"

    def getdetails(self):
        print("The name of book is",self.name,"and","the price of the book is",self.price)

    @staticmethod
    def book_details():
        print("Author name is",Book.Author_name,"and","the Publisher of the book is",Book.Publisher)

def main():
    book_list=[]
    for i in range(2):
        name=input("Enter the Book name ")
        price=int(input("Enter the Book price "))
        b=Book(name,price)
        book_list.append(b)
    for bk in book_list:
        print(bk)
        Book.book_details()
        bk.getdetails()
        print()

if __name__ == '__main__':
    main()
