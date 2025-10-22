import pickle
def insertRec():
    bookname = (input('Enter the book name: '))
    category = (input('Enter book category: '))
    author = (input('Enter author name: '))
    bookid = (input('Enter book id: '))
    phone = (input('Enter phoneno. :'))
                   

    rec={'Bookname': bookname,'Category':category,'Author':author,'Book id':bookid,'Phone no.':phone}

    f= open('book.dat','ab')
    pickle.dump(rec,f)
    f.close()

def readRec():
    f= open('book.dat','rb')
    while True:
        try:
            rec= pickle.load(f)
            print('Book Name:',rec['Bookname'])
            print('Category:',rec['Category'])
            print('Author:',rec['Author'])
            print('Book Id:',rec['Book id'])
            print('Phone no.:',rec['Phone no.'])
        except EOFError:
            break
    f.close()

def searchBookid(r):
    f=open('book.dat','rb')
    flag = False
    while True:
        try:
            rec = pickle.load(f)
            if rec['Book id']== r:
                print('Author:',rec['Author'])
                print('Book Name:',rec['Bookname'])
                flag = True
        except EOFError:
            break
    if flag == False:
        print('No Records found')
    f.close()

def updateAuthor(r,a):
    f=open('book.dat','rb')
    reclst = []
    while True:
        try:
            rec = pickle.load(f)
            reclst.append(rec)
        except EOFError:
            break
    f.close()
    for i in range (len(reclst)):
        if reclst[i]['Book id']==r:
            reclst[i]['Author'] = a
    f = open('book.dat','wb')
    for x in reclst:
        pickle.dump(x,f)
    f.close()

def deleteRec(r):
    f = open('book.dat','rb')
    reclst = []
    while True:
        try:
            rec = pickle.load(f)
            reclst.append(rec)
        except EOFError:
            break
    f.close()

    f = open('book.dat','wb')
    deleted = False
    for x in reclst:
        if x['Book id'] == r:
            deleted = True
            continue
        pickle.dump(x, f)
    f.close()

def addUser():
    name = input('Enter user name: ')
    userid =int(input('Enter user ID: '))
    phone = int(input('Enter phone number: '))
    email = input('Enter email: ')
    address = input('Enter address: ')

    user = {'User Name': name,'User ID': userid,'Phone No.': phone,'Email': email,'Address': address}

    f= open('user.dat','ab')
    pickle.dump(user, f)
    print('User record added successfully.\n')
    f.close()


def readUsers():
    f= open('user.dat','rb')
    while True:
            try:
                user = pickle.load(f)
                print('User Name:', user['User Name'])
                print('User ID:', user['User ID'])
                print('Phone No.:', user['Phone No.'])
                print('Email:', user['Email'])
                print('Address:', user['Address'])
            except EOFError:
                break
    f.close()

def editUser(userid):
    print("1.Change name")
    print("2.Change phone no")
    print("3.Change email")
    print("4.Change address")
    ch=int(input('Enter your choice: '))
    f= open('user.dat','rb')
    reclst = []
    while True:
        try:
            user = pickle.load(f)
            reclst.append(user)
        except EOFError:
            break
    f.close()
    if(ch==1):
        n=input('Enter New name: ')
        
        for i in range(len(reclst)):
            if reclst[i]['User ID'] == userid:
                reclst[i]['User Name'] = n
    elif(ch==2):
        p=int(input('Enter new phone no.: '))
        for i in range(len(reclst)):
            if reclst[i]['User ID'] == userid:
                reclst[i]['Phone No.'] = p
    elif(ch==3):
        e=input('Enter new email: ')
        for i in range(len(reclst)):
            if reclst[i]['User ID'] == userid:       
                reclst[i]['Email'] = e
    elif(ch==4):
        d=input('Enter new address: ')
        for i in range(len(reclst)):
            if reclst[i]['User ID'] == userid:   
                reclst[i]['Address'] = d
    print(reclst)
    f= open('user.dat','wb')
    for x in reclst:
        pickle.dump(x, f)
    print('User details updated successfully.\n')
    f.close()


def deleteUser(userid):
    f= open('user.dat','rb')
    reclst = []
    while True:
        try:
            user = pickle.load(f)
            reclst.append(user)
        except EOFError:
            break
    f.close()

    f= open('user.dat', 'wb')
    deleted = False
    for x in reclst:
        if x['User ID'] == userid:
            deleted = True
            continue
        pickle.dump(x, f)
    f.close()

def searchUserByPhone(phone):
    f= open('user.dat', 'rb')
    while True:
        try:
            user = pickle.load(f)
            if user['Phone No.'] == phone:
                print('User Name:', user['User Name'])
                print('User ID:', user['User ID'])
                print('Email:', user['Email'])
                print('Address:', user['Address'])
                flag = True
        except EOFError:
            break
    if flag == False:
        print('No records found')
    f.close()

def issueBook():
    bookid = input('Enter Book ID: ')
    userid = input('Enter User ID: ')
    issuedate = input('Enter Issue Date (DD-MM-YYYY): ')
    bookname = input('Enter book name: ')
    rec = {'Book ID': bookid,'User ID': userid,'Issue Date': issuedate,'Book Name': bookname}

    f= open('issue.dat', 'ab')
    pickle.dump(rec, f)
    print('Book issued successfully.\n')
    f.close()

def returnBook():
    bookid = input('Enter Book ID: ')
    userid = input('Enter User ID: ')
    returndate = input('Enter Return Date (DD-MM-YYYY): ')
    bookname = input('Enter book name: ')
    rec = {'Book ID': bookid,'User ID': userid,'Return Date': returndate,'Book Name': bookname}

    f= open('return.dat', 'ab') 
    pickle.dump(rec, f)
    print('Book returned successfully.\n')
    f.close()


def displayIssuedBooks():
    f = open('issue.dat', 'rb')
    print('\nIssued Book Records\n')
    while True:
        try:
            rec = pickle.load(f)
            print(rec)
            print('Book ID     :', rec['Book ID'])
            print('User ID     :', rec['User ID'])
            print('Issue Date  :', rec['Issue Date'])
            print('Book Name   :', rec['Book Name'])
            
        except EOFError:
            break
    f.close()

def displayReturnedBooks():
    f = open('return.dat', 'rb')
    print('\nReturned Book Records\n')
    while True:
        try:
            rec = pickle.load(f)
            print('Book ID      :', rec['Book ID'])
            print('User ID      :', rec['User ID'])
            print('Return Date  :', rec['Return Date'])
            print('Book Name   :', rec['Book Name'])
            
        except EOFError:
            break
    f.close()
        
   
    
while True:
    print('Type 1 to insert a book record.')
    print('Type 2 to display all records.')
    print('Type 3 to search a record by book ID.')
    print('Type 4 to update author name.')
    print('Type 5 to delete record.')
    print('Type 6 to add user.')
    print('Type 7 to display user details.')
    print('Type 8 to edit user details.')
    print('Type 9 to delete user details.')
    print('Type 10 to search by phone no.')
    print('Type 11 to enter book issue date.')
    print('Type 12 to enter book return date.')
    print('Type 13 to display book issue details.')
    print('Type 14 to display book return details.')
    print('Type 15 to exit program.')
    choice = int(input('Enter your choice: '))
    if choice==1:
        insertRec()
    elif choice==2:
        readRec()
    elif choice==3:
        r=input('Enter book id to search: ')
        searchBookid(r)
    elif choice==4:
        i=int(input('Enter Book ID: '))
        a= input('Enter new author name: ')
        updateAuthor(r,a)
    elif choice == 5:
        r = input('Enter Book ID: ')
        deleteRec(r)
    elif choice == 6:
        addUser()
    elif choice == 7:
        readUsers()
    elif choice == 8:
        userid = int(input('Enter user id: '))
        editUser(userid)
    elif choice == 9:
        deleteUser()
    elif choice == 10:
        phone =int(input('Enter phone no.: '))
        searchUserByPhone(phone)
    elif choice == 11:
        issueBook()
    elif choice == 12:
        returnBook()
    elif choice == 13:
        displayIssuedBooks()
    elif choice == 14:
        displayReturnedBooks()
    elif choice == 15:
        print('Exiting program...')
        exit()
        
        

