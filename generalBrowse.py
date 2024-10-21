import menu
import datetime

def general_browse():
        f=open("Book_Info.txt","r")
        for l in f:
            list_Book=[]
            list_Book=list_Book+l.split(",")
            print("%12s%24s%24s%24s%15s%35s"%(list_Book[0],list_Book[1],list_Book[2],list_Book[3],list_Book[4],list_Book[5]))
        f.close()
        print("")
        x=int(input("Type 1 for main menu: "))
        if x==1:
            print("")
            print("---------------------------------")
            menu.main_Page()
        else:
            quit()

def book_Checkout_(currentUserId):
    print("")
    print("What book would you like to checkout?")
    n=input("Type the book ID:")
    f=open("Book_Info.txt","r")
    flag=False
    for l in f:
        list_Book=[]
        list_Book=list_Book+l.split(",")
        if n == list_Book[0]:
            print("")
            #this prints the key details of the book
            print(list_Book[2],"written by",list_Book[3])
            flag=True
    f.close()
    #the flag is used so that inace the book isn't found
    if flag==False:
        print("")
        print("Sorry we do not have a book with that ID")
        print("You will be sent back")
        print("")
        print("---------------------------------")
        book_Checkout_(currentUserId)
        
    else:
        print("")
        print("Is this the book you want?")
        x=int(input("Press 1 for YES, 2 for NO:"))
        if x==1:
            print("")
            f=open("logfile.txt","r")
            libro=[]
            for l in f:
                book_Data=[]
                book_Data=book_Data+l.split(",")
                if book_Data[0]==n:
                    libro=libro+book_Data

            if libro[-4] == "no":
                print("This book is available for checkout")
                print("Would you like it?")
                g=int(input("Enter 1 for YES, 2 for NO:"))
                if g == 1:
                    print("This book has now been checked out")
                    current=datetime.datetime.now()
                    d1 = current.strftime("%d/%m/%Y")
                    d2= current + datetime.timedelta(days=14)
                    d3=d2.strftime("%d/%m/%Y")
                    libro[-4]=d3
                    libro[-3]=currentUserId
                    s=open("logfile.txt","a")
                    s.write("\n")
                    s.write("%s,%s,%s,%s,%s"%(libro[-5],libro[-4],libro[-3],libro[-2],libro[-1]))
                    s.close() 
                    print("")
                    print("---------------------------------")
                    menu.main_Page()
                elif g==2:
                    print("")
                    print("---------------------------------")
                    book_Checkout_()
                else:
                    print("")
                    print("Please enter 1 or 2")
            else:
                if libro[-2] == "not":
                    print("This book is currently on loan until",libro[-4])
                    print("But it is available for reserve after")
                    print("Would you like to reserve it?")
                    y=int(input("Press 1 for YES, 2 for NO"))
                    if y==1:
                        print("")
                        print("Ok you have reserved it")
                        libro[-2]="reserved"
                        libro[-1]=currentUserId
                        s=open("logfile.txt","a")
                        s.write("\n%s,%s,%s,%s,%s"%(libro[-5],libro[-4],libro[-3],libro[-2],libro[-1]))
                        s.close() 
                        print("")
                        print("---------------------------------")
                        menu.main_Page()
                    else:
                        print("")
                        print("")
                        print("---------------------------------")
                        print("You will be sent back to main menu")
                        menu.main_Page()
                else:
                    print("This book is currently on loan until",book_Data[1])
                    print("It has also been reserved for after")
                    print("So this book is currently unavailable to you")
                    print("")
                    print("Press 1 to checkout a different book")
                    z=int(input("Press 2 for main menu:"))
                    if z == 1:
                        print("")
                        print("---------------------------------")
                        book_Checkout(currentUserId)
                    elif z==2:
                        print("")
                        print("---------------------------------")
                        menu.main_Page()
                    else:
                        print("")
                        print("Please enter 1 or 2")
                            
                            
            f.close()
        elif x==2:
            print("")
            print("---------------------------------")
            book_Checkout_(currentUserId)

