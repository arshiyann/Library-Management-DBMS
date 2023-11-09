import sqlite3
def student():
    con = sqlite3.connect("lib_pro.db")
    cur = con.cursor()
    #q = "CREATE TABLE all_labs ( en     NUMERIC (10), sname  VARCHAR (15),  sclass VARCHAR (10),smob   NUMERIC (15) );"
    cur.execute("SELECT * FROM all_stud")
    con.commit()
    
    b = cur.fetchall()
    con.close()
    return list(b)
    
def book():
    con = sqlite3.connect("lib_pro.db")
    cur = con.cursor()
    #q = "CREATE TABLE all_labs ( en     NUMERIC (10), sname  VARCHAR (15),  sclass VARCHAR (10),smob   NUMERIC (15) );"
    cur.execute("SELECT * FROM all_book")
    con.commit()
    
    b = cur.fetchall()
    con.close()
    books = list(b)
    
    return books

def Search_Book():
    print("Enter Book Name: ",end="")
    bname = input()
    bk = book() 
    for all in bk:
        all = list(all) 
        if all[1].upper() == bname.upper():
             print("****Book Is Present ******")
             print(" |No |  |Book Name|\t|Author|\t   |Publication|")
             print(" |",all[0],"|\t  |",all[1],"|\t|",all[2],"|\t|",all[3],"|")
                  
             break 

def Student_History():
    print("Enter Roll No: ",end="")
    r = input()
    rd ="N\A"
    con = sqlite3.connect("lib_pro.db")
    cur = con.cursor()
    q  = "select * from all_issue where sroll = ? AND sroll = ?"
    cur.execute(q,(r,r))
    con.commit()
    res = cur.fetchall()
    
    con.close()
    
    print("Student History")
    print("|Roll No|   |Book|\t|Issue Date|\t\t|Returned Date|")

    for all in res:
        print(" |",all[0],"|\t  |",all[1],"|\t|",all[2],"|    \t|",all[3],"|")

def Book_History():
    print("Enter Book Name: ",end="")
    book = input()
    con = sqlite3.connect("lib_pro.db")
    cur = con.cursor()
    q  = "select * from all_issue where bname = ? AND bname = ?"
    cur.execute(q,(book,book))
    con.commit()
    res = cur.fetchall()
    
    con.close()
    
    print("Book History")
    print("|Roll No|   |Book|\t|Issue Date|\t\t|Returned Date|")
    for all in res:
        print(" |",all[0],"|\t  |",all[1],"|\t|",all[2],"|    \t|",all[3],"|")
    

def Search_Student():
    flag = False
    print("Enter Student Roll No: ",end="")
    roll = int(input())
    stdl = student()
    for all in stdl:
        all = list(all)
        if all[0] == roll:
            flag = True
            print("Student is Present")
            print("|Roll No|   |Name|\t|Class|\t\t|Mobile|")
            print(" |",all[0],"|\t  |",all[1],"|\t|",all[2],"|    \t|",all[3],"|")
    if flag == False:
        print("Student Not Present!!!")

def Issue_Book():
    print("Enter Roll No: ",end=" ")
    sroll = input()
    stud = student()
    flag = False
    flag1 = False
    bk = book()
    for all in stud:
        all = list(all)
        
        if all[0]==int(sroll):
            flag1 = True
            print("Enter Book Name: ",end="")
            bname = input()
            
            for bklist in bk:
                bklist = list(bklist)
                
                
                if bklist[1].upper() == bname.upper():
                  
                  flag = True
                  bookn = bklist[1]
                  
                  print("****Book is Present and issued to",all[1],"******")
                  print(" |No |  |Book Name|\t|Author|\t   |Publication|")
                  print(" |",bklist[0],"|\t  |",bklist[1],"|\t|",bklist[2],"|\t|",bklist[3],"|")
                  
                  break
    
    if flag1 == False:
        print("Student Not Present!!!")
    elif flag == False:
        print("Book Not Present!!!")
    else:        
     na = "N\A"       

     #2023-11-08
     import random
     dtoday = "2023-" + str(random.randint(1,11)) +"-"+ str(random.randint(1,31))
     
     q = "insert into all_issue(sroll, bname, issued, retd) values("+ sroll + ",'"+ bookn + "','"+ dtoday +"','"+ na +"'"+")"
     con = sqlite3.connect("lib_pro.db")
     con.execute(q)
     con.commit()
     con.close()      
    
def Return_Book():
    roll, flag = Show_Not_Return_Books()
    if flag == False:
     print("Enter Book Name To Return: ",end="")
     name = input()
     con = sqlite3.connect("lib_pro.db")
     cur = con.cursor()
     from datetime import date
     dt  = str(date.today())
    
     q  = '''UPDATE all_issue
             SET retd = ?
          WHERE sroll = ?;'''
     cur.execute(q,(dt,roll))
     con.commit()
     con.close()
     print("Successfully Returned Book On",dt)

def Show_Not_Return_Books():
    print("Enter Roll No: ",end="")
    r = input()
    rd ="N\A"
    con = sqlite3.connect("lib_pro.db")
    cur = con.cursor()
    q  = "select * from all_issue where sroll = ? AND retd = ?"
    cur.execute(q,(r,rd))
    con.commit()
    res = cur.fetchall()
    
    con.close()
    flag = False
    print("Books Not Returned")
    print("|Roll No|   |Book|\t|Issue Date|\t\t|Returned Date|")
    if res == []:
        print("NO BOOKS TO RETURN")
        flag = True

    for all in res:
        print(" |",all[0],"|\t  |",all[1],"|\t|",all[2],"|    \t|",all[3],"|")
    return r,flag

def Add_New_Student():
    print("Enter Student Enrollment: ",end="")
    en = input()
    print("Enter Student Name: ",end="")
    n = input()
    print("Enter Student Class: ",end="")
    r = input()
    print("Enter Student Mobile No: ",end="")
    c = input()
    
    q = "insert into all_stud(en, sname, sclass, smob) values("+ en + ",'"+ n +"','"+ r +"',"+ c + ")"
    con = sqlite3.connect("lib_pro.db")
    con.execute(q)
    con.commit()
    con.close()
    print("Student Added Successfully!!")

def Add_New_Book():
    print("Enter Book No: ",end="")
    bn = input()
    print("Enter Book Title: ",end="")
    bname = input()
    print("Enter Author: ",end="")
    bauth = input()
    print("Enter Publication: ",end="")
    bpub = input()
    q = "insert into all_book(bno, bname, bauth, bpub) values(" + bn + ",'"+ bname + "','"+bauth+"','"+ bpub +"'"+")"
    con = sqlite3.connect("lib_pro.db")
    con.execute(q)
    con.commit()
    con.close()

def Show_All():
    print("----------------------BELOW DATABASE------------------")
    b = student()
    print("Enrollment No |\t| Name    |\t| Class |\t| Mobile |")
    for all in b:
        all = list(all)
        print(" |",all[0],"|\t  \t|",all[1],"|\t|",all[2],"|    \t|",all[3],"|")
    
   
    
while True:
    con = sqlite3.connect("lib_pro.db")
    con.close()
    print("Select operation")
    print("1 - Issue Book")
    print("2 - Return Book")
    print("3 - Student History")
    print("4 - Book History")
    print("5 - Search Student")
    print("6 - Search Book")
    print("7 - Add New Book")
    print("8 - Add New Student")
    print("9 - Show Not Return Books")
    print("10 - Show All")
    print("11- Exit")
    ch = int(input("Select an option : "))
    if ch==1:
        Issue_Book()
    elif ch==2:
        Return_Book()
    elif ch==3:
        Student_History()
    elif ch==4:
        Book_History()
    elif ch==5:
        Search_Student()
    elif ch==6:
        Search_Book()
    elif ch==7:
        Add_New_Book()
    elif ch==8:
        Add_New_Student()
    elif ch==9:
        Show_Not_Return_Books()
    elif ch==10:
        Show_All()
    elif ch==11:
        exit(0)