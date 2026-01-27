class library:
    def __init__(self,num,books):
        self.no_of_books = num
        self.books = books

    def show(self):
        print(f"there are {self.no_of_books} books and they are {self.books}")

    def check(self):
        if(self.no_of_books != len(self.books)):
            print("no of books is incorrect!!")
        else:
            print("yep!! totally correct")

a = library(3,["harry potter",'got','fire and blood'])
a.show()
a.check()

class library:
    def __init__(self,num,books):
        self.no_of_books = num
        self.books = books

    def show(self):
        print(f"there are {self.no_of_books} books and they are {self.books}")

    def check(self):
        if(self.no_of_books != self.books):
            print("no of books is incorrect")
        else:
            print("yep!! totally correct")

a = library(5,["harry potter","got","fire and blood"])
a.show()
a.check()













