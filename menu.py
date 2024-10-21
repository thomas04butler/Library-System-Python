#coursework#
import matplotlib.pyplot as plt
from datetime import date
from bookCheckout import *
from generalBrowse import *
from bookReturn import *
from bookSearch import *
from bookSelect import *

currentUserId=int(input("Please enter your user ID to login:"))
while True:
    if currentUserId <10000 and currentUserId >=1000:
        print("")
        print("You are now logged in")
        print("")
        print("---------------------------------")
        break
    else:
        print("")
        print("ID is invalid")
        print("")
        currentUserId=int(input("Please enter your user ID to login:"))
        
def main_Page():
    print("")
    print("Welcome to the Main Page")
    print("")
    print("General Browse --- 1")
    print("Book Search    --- 2")
    print("Book Checkout  --- 3")
    print("Return Book    --- 4")
    print("Purchase Books --- 5")
    menu1=int(input("Please enter the number:"))
    while True:
        if menu1 >=6:
            print("")
            print("Enter number between 1-5")
            print("")
            menu1=int(input("Please enter the number:"))
        else:
            break
        
    if menu1 == 1:
        print("")
        print("---------------------------------")
        print("")
        print("Welcome to General Browse")
        print("")
        print("|       Book ID       |       Genre       |       Title       |       Author       |       Purchase Price       |       Purchase Date       |")
        print("")
        general_browse()
    elif menu1 == 2:
        print("")
        print("---------------------------------")
        print("")
        print("Welcome to Book Search")
        print("")
        book_search()
    elif menu1 == 3:
        print("")
        print("---------------------------------")
        print("")
        print("Welcome to Book Checkout")
        book_Checkout_(currentUserId)
    elif menu1 == 4:
        print("")
        print("---------------------------------")
        print("")
        print("Welcome to Return Book")
        return_Book()
    elif menu1 == 5:
        print("")
        print("---------------------------------")
        print("")
        print("Welcome to Purchase Books")
        purchase_Order()

main_Page()
