import menu

def book_search():
    print("Search by Genre  --- 1")
    print("Search by Title  --- 2")
    print("Search by Author --- 3")
    menu2=int(input("Please enter the number:"))
    while True:
        #checks the number is one of the options
        if menu2 >=4:
            print("")
            print("Enter number between 1-3")
            print("")
            menu2=int(input("Please enter the number:"))
        else:
            break
    if menu2 ==1:
        print("")
        n=input("Type a genre:")
        #this is incase they enter a value all lower or upper case
        n=n.capitalize()
        f=open("Book_Info.txt","r")
        flag=False
        for l in f:
            #this puts line into a list
            list_Book=[]
            list_Book=list_Book+l.split(",")
            y=list_Book[1]
            y=y.capitalize()
            #this only looks at line with the genre
            if n == y:
                print("Book ID:",list_Book[0])
                print("Genre:",list_Book[1])
                print("Title:",list_Book[2])
                print("Author:",list_Book[3])
                print("Purchase Price:",list_Book[4])
                print("Purchase Date:",list_Book[5])
                flag=True
        f.close()
        #this is it could not be found
        if flag==False:
            print("")
            print("Sorry could not find genre")
            print("")
            x=int(input("Type 1 for main menu: "))
            if x==1:
                print("")
                print("---------------------------------")
                menu.main_Page()
        else:
            print("")
            x=int(input("Type 1 for main menu: "))
            if x==1:
                print("")
                print("---------------------------------")
                menu.main_Page()
    
    if menu2 ==2:
        print("")
        n=input("Type a book title:")
        #this is incase they enter a value all lower or upper case
        n=n.capitalize()
        f=open("Book_Info.txt","r")
        flag=False
        for l in f:
            #this puts line into a list
            list_Book=[]
            list_Book=list_Book+l.split(",")
            y=list_Book[2]
            y=y.capitalize()
            #this only looks at line with the title
            if n == y:
                print("Book ID:",list_Book[0])
                print("Genre:",list_Book[1])
                print("Title:",list_Book[2])
                print("Author:",list_Book[3])
                print("Purchase Price:",list_Book[4])
                print("Purchase Date:",list_Book[5])
                flag=True
        if flag==False:
            print("")
            print("Sorry could not find title")
            print("")
            x=int(input("Type 1 for main menu: "))
            if x==1:
                print("")
                print("---------------------------------")
                menu.main_Page()
        else:
            print("")
            x=int(input("Type 1 for main menu: "))
            if x==1:
                print("")
                print("---------------------------------")
                menu.main_Page()
    if menu2 ==3:
        print("")
        n=input("Type an author:")
        n=n.capitalize()
        #this is incase they enter a value all lower or upper case
        f=open("Book_Info.txt","r")
        flag=False
        for l in f:
            #this puts line into a list
            list_Book=[]
            list_Book=list_Book+l.split(",")
            y=list_Book[3]
            y=y.capitalize()
            #this only looks at line with the title
            if n == y:
                print("Book ID:",list_Book[0])
                print("Genre:",list_Book[1])
                print("Title:",list_Book[2])
                print("Author:",list_Book[3])
                print("Purchase Price:",list_Book[4])
                print("Purchase Date:",list_Book[5])
                flag=True
        if flag==False:
            print("")
            print("Sorry could not find author")
            print("")
            x=int(input("Type 1 for main menu: "))
            if x==1:
                print("")
                print("---------------------------------")
                menu.main_Page()
        else:
            print("")
            x=int(input("Type 1 for main menu: "))
            if x==1:
                print("")
                print("---------------------------------")
                menu.main_Page()
                
