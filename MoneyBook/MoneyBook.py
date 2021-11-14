import datetime

InitSum: int = 1000
LoadFilePath = "Users\kiroa\source\repos\MoneyBook\MoneyBook\Data.txt"
ExportPath = "Users\kiroa\source\repos\MoneyBook\MoneyBook\Export.txt"


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
    try:
        with open(LoadFilePath,"x") as f:
            pass

    except FileExistsError:
        with open(LoadFilePath,"a") as f:
            for line in f:
                Current: Book = Book(0)
                level: int = 0
                num: str = ""
                get: str = ""
                paid: str = ""
                sum: str = ""
                for s in line:
                    if s == ",":
                        level += 1

                    if level == 0:
                        num += s
                    if level == 1:
                        Current.Num = int(num)
                        Current.Date += s
                    if level == 2:
                        Current.Title += s
                    if level == 3:
                        get += s
                    if level == 4:
                        Current.Get = int(get)
                        paid += s
                    if level == 5:
                        Current.Paid = int(paid)
                        sum += s
                    if level == 6:
                        Current.Sum = int(sum)
                        Current.Descrip += s

                List += [Current]


def ExportCSV():
    for itm in List:
        try:
            with open(ExportPath,"x") as f:
                pass
        except FileExistsError:
            with open(ExportPath,"a") as f:
                line: str = ""
                line += itm.Num + ","
                line += itm.Date + ","
                line += itm.Title + ","
                line += str(itm.Get) + ","
                line += str(itm.Paid) + ","
                line += str(itm.Sum) + ","
                line += itm.Descrip + "\n"
                f.write(line)


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
    cmd = input()
    if(cmd == "exit"):
        break
    if(cmd == "save"):
        ExportCSV()
    if(cmd == "load"):
        pass

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