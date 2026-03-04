#python based library management system:
#defining library as class:
class library:
    #defining constructor:
    def __init__(self,num,books):
        self.no_of_books = num
        self.books = books
#defining function to show details:
    def show(self):
        print(f"there are {self.no_of_books} books and they are {self.books}")
#defining function for checking: 
    def check(self):
        if(self.no_of_books != len(self.books)):
            print("no of books is incorrect!!")
        else:
            print("yep!! totally correct")
#object defining and fuction calling:
a = library(3,["harry potter",'got','fire and blood'])
a.show()
a.check()
















