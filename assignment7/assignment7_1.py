class BookStore:
    NoOfBooks = 0;

    def __init__(self,name, author):
        self.name = name;
        self.author = author;
        BookStore.NoOfBooks += 1;

    def display(self):
        print "Name of the book is - ", self.name;
        print "Author of the book is - ", self.author;
        print "No. of book is - ", self.NoOfBooks;


obj1 = BookStore("Linux System Programming", "Robert love");
obj1.display();

obj2 = BookStore("C Programming", "Dennis Ritchie");
obj2.display();


