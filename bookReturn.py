import menu
import datetime

def return_Book():
    print("")
    print("What book would you like to return?")
    n=input("Type the book ID:")
    f=open("Book_Info.txt","r")
    flag=False
    #searches for the book in file with book ID 
    for l in f:
        list_Book=[]
        list_Book=list_Book+l.split(",")
        if n == list_Book[0]:
            print("")
            print(list_Book[2],"written by",list_Book[3])
            flag=True
    f.close()
    #if the book doesnt exist
    if flag==False:
        print("")
        print("Sorry we do not have a book with that ID")
        print("You will be sent back")
        print("")
        print("---------------------------------")
        return_Book()
        
    else:
        print("")
        print("Is this the book you want to return?")
        x=int(input("Press 1 for YES, 2 for NO:"))
        if x==1:
            print("")
            f=open("logfile.txt","r")
            libro=[]
            #creates new list with all book info for that book ID 
            pleasework=""
            for l in f:
                book_Data=[]
                book_Data=book_Data+l.split(",")
                if book_Data[0]==n:
                    pleasework=book_Data[4]
                    libro=libro+book_Data
                    please=pleasework[0]+pleasework[1]+pleasework[2]+pleasework[3]
            #if the book is completely available 
            if libro[-4] == "no":
                print("This book has already been checkout / is not on loan")
                print("You will be returned to the main menu")
                print("")
                print("---------------------------------")
                menu.main_Page()
            else:
                #if the book can be returned 
                if libro[-2] == "not":
                    print("This book can be returned")
                    print("Are you sure you want to return it?")
                    y=int(input("Press 1 for YES, 2 for NO"))
                    if y==1:
                        print("")
                        print("Ok it has been returned")
                        libro[-4]="no"
                        libro[-3]="nomember"
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
                    #if the book can be retruned and it has a reservation
                    print("This book can be returned")
                    print("Are you sure you want to return it?")
                    y=int(input("Press 1 for YES, 2 for NO"))
                    if y==1:
                        print("")
                        print("Ok it has been returned")
                        print("")
                        print("It has been reserved, so they will be the new owners")
                        current=datetime.datetime.now()
                        d1 = current.strftime("%d/%m/%Y")
                        d2= current + datetime.timedelta(days=14)
                        d3=d2.strftime("%d/%m/%Y")
                        print(d3)
                        xy=libro[-5]+","+d3+","+please+",not,"+"nomemberr"
                        s=open("logfile.txt","a")
                        s.write("\n")
                        s.write(xy)
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
                            
            f.close()
        elif x==2:
            print("")
            print("---------------------------------")
            return_Book()
