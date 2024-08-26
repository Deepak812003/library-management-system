class libary():
    def __init__(self,list):
        self.booklist=list
        self.availablebook=list
        self.lent={}
    def display(self):
        for book in self.booklist:
            print(book)
    def available(self):
      for book in self.availablebook:
          print(book)
    def barrow(self,name,book):
      if book not in self.booklist:
          print("The book is not in our library!!!!")
      if book in self.booklist:
          self.lent.update({book:name})
          self.availablebook.remove(book)
      else:
          print("That book is sold to "+self.lent[book])
    def submit(self,book):
        del self.lent[book]
        self.availablebook.append(book)


lib=libary(["Moby-Dick","War and Peace","Don Quixote","Madame Bovary","In Search of Lost Time"])
print("welcome to your library!!!!!")
while True:
    print("press 1 for display all the books....")
    print("press 2 for display available books....")
    print("press 3 for lenting the book....")
    print("press 4 for returning the book...")
    print("press 5 for exit......")
    user_choice = int(input())
    if user_choice==1:
       lib.display()
    elif user_choice==2:
       lib.available()
    elif user_choice==3:
        name=input("Enter your name:")
        book=input("Enter the book name:")
        lib.barrow(name,book)
    elif user_choice==4:
        book=input("Enter the book name:")
        lib.submit(book)
    elif user_choice==5:
        break
    else:
        print("please enter the correct option.....")