import menu
import matplotlib.pyplot as plt

def purchase_Order():
    print("")
    print("what is the library budget?")
    budget=int(input("Budget:"))
    print("")
    f=open("logfile.txt","r")
    Genre=["Action","Fantasy","Fiction","Crime","Classics","Thriller","Suspense","Mystery","Romance","Biogrpahy"]
    Genre_Counter=[0,0,0,0,0,0,0,0,0,0]
    counter=0
    #this goes through everyline and adds one to the counter for its specific genre using a 2d array
    for l in f:
            counter=counter+1
            book_Info=[]
            book_Info=book_Info+l.split(",")
            ID=book_Info[0]
            s=open("Book_Info.txt","r")
            for l in s:
                get_Genre=[]
                get_Genre=get_Genre+l.split(",")
                if get_Genre[0]==ID:
                        for i in range (len(Genre)):
                                if get_Genre[1]==Genre[i]:
                                        Genre_Counter[i]=Genre_Counter[i]+1
    f.close()
    percentage_List1=[]
    #this creates the percentage for each genre using the counter#    
    for i in range(len(Genre)):
            div=Genre_Counter[i]/counter
            percentage=div*100
            percentage_List1.append(percentage)

    percentage_List2=[]
    #this creates how much should be spent on each genre dependng on the budget. 
    for i in range(len(Genre)):
            decimal=percentage_List1[i]/100
            how_Much=decimal*budget
            percentage_List2.append(how_Much)

    print("Based on Popularity and given the budget")
    print("This is how much should be spent on each Genre;")
    #this pprints it out for each genre. 
    for i in range(len(Genre)):
            print(Genre[i]+": %3.2f%% so %1.2f£"%(percentage_List1[i],percentage_List2[i]))
    

    print("")
    #the following code uses the same strategy as before and gets the most popular books. 
    f=open("logfile.txt","r")
    book_ID=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]
    book_Counter=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    counter=0
    for l in f:
            counter=counter+1
            book_Info=[]
            book_Info=book_Info+l.split(",")
            for i in range (len(book_ID)):
                    if book_Info[0]==book_ID[i]:
                            book_Counter[i]=book_Counter[i]+1
    print("")
    temp=0
    temp1=0
    for i in range(len(book_Counter)):
            if book_Counter[i]>temp:
                    temp=book_Counter[i]
                    temp1=i
    f.close()
    #prints out the most popular book 
    f=open("Book_Info.txt","r")
    del book_Counter[temp1]
    temp1=temp1+1
    temp1=str(temp1)
    for l in f:
            book_Info=[]
            book_Info=book_Info+l.split(",")
            if book_Info[0]==temp1:
                    print("The most popular book is:")
                    print("Genre:",book_Info[1])
                    print("Title:",book_Info[2])
                    print("Author:",book_Info[3])
                    print("Purchase Price:",book_Info[4])
    f.close()

    print("")
    temp=0
    temp1=0
    for i in range(len(book_Counter)):
            if book_Counter[i]>temp:
                    temp=book_Counter[i]
                    temp1=i
    f.close()
    f=open("Book_Info.txt","r")
    #prints out the second most popular book
    del book_Counter[temp1]
    temp1=temp1+2
    temp1=str(temp1)
    for l in f:
            book_Info=[]
            book_Info=book_Info+l.split(",")
            if book_Info[0]==temp1:
                    print("The secomd most popular book is:")
                    print("Genre:",book_Info[1])
                    print("Title:",book_Info[2])
                    print("Author:",book_Info[3])
                    print("Purchase Price:",book_Info[4])
    f.close()
    
    print("")
    temp=0
    temp1=0
    for i in range(len(book_Counter)):
            if book_Counter[i]>temp:
                    temp=book_Counter[i]
                    temp1=i
    f.close()
    f=open("Book_Info.txt","r")
    #prints out the third most popular book
    del book_Counter[temp1]
    temp1=temp1+2
    temp1=str(temp1)
    for l in f:
            book_Info=[]
            book_Info=book_Info+l.split(",")
            if book_Info[0]==temp1:
                    print("The third most popular book is:")
                    print("Genre:",book_Info[1])
                    print("Title:",book_Info[2])
                    print("Author:",book_Info[3])
                    print("Purchase Price:",book_Info[4])
    f.close()

    #create pie chart for each percentage of the genre using ,atmplotlib
    labels="Action","Fantasy","Fiction","Crime","Classics","Thriller","Suspense","Mystery","Romance","Biogrpahy"
    colors=['green', 'brown', 'blue', 'red', 'orange', 'gold', 'indigo', 'aqua', 'silver', 'yellow']
    plt.pie(percentage_List2, labels=labels, colors=colors)

    plt.axis('equal')
    plt.title('Pie Plot')
    plt.show()
    print("")
    x=int(input("Type 1 for main menu: "))
    if x==1:
        print("")
        print("---------------------------------")
        menu.main_Page()
    else:
        quit()
