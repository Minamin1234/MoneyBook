import datetime

InitSum: int = 1000


class Book:
    Num: int = 0
    Date: str = ""
    Title: str = ""
    Paid: int = 0
    Get: int = 0
    Sum: int = 0
    Descrip: str = ""

    def __init__(self,num: int):
        if num == 0:
            self.Sum = InitSum
        self.Num = num

List = [Book(0)]

def Load():
    pass

def Save():
    pass

def Add(book: Book):
    global List
    dt = datetime.datetime.now()
    PrevBook = List[len(List) - 1]
    book.Num = PrevBook.Num + 1
    book.Date = str(dt)
    book.Sum = PrevBook.Sum + (book.Get - book.Paid)
    List += [book]

while True:
    print("Continue?")
    if(input() == "exit"):
        break

    print("Title: ")
    c: Book = Book(len(List))
    c.Title = input()
    print("Paid: ")
    c.Paid = int(input())
    print("Get; ")
    c.Get = int(input())
    print("Description: ")
    c.Descrip = input()
    Add(c)

for item in List:
    print(item.Num)
    print(item.Date)
    print(item.Title)
    print(item.Get)
    print(item.Paid)
    print(item.Sum)
    print(item.Descrip)
    print(" ")
