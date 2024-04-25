""" A software system for managing book acquisitions, removals, check-outs ans check-ins"""
# The system has these components.
# books in an ISBN number and title
# patrons with an ID number
import sys
import os.path

class BookNode():
    def __init__(self,ISBN,title,status="Available",next=None):
        try:
            len(ISBN)==10 and ISBN[0:9].isnumeric()
        except:
            print("Hey there you want to add an invalid book")
        self._ISBN_number=ISBN
        self._book_title=title #strings
        self._status=status
        self._next=next
        self._book_out_count=0
        self._status_num=1

    def get_ISBN_number(self):
        return self._ISBN_number

    def get_book_title(self):
        return self._book_title

    def get_status(self):
        return self._status

    def get_next(self):
        return self._next

    def get_status_num(self):
        return self._status_num

    def book_out_count(self):
        return self._book_out_count

    def set_status(self,this):
        self._status=this

    def increase_book_out_count(self):
        self._book_out_count+=1

class PatNode():
    def __init__(self,ID,next=None,status="patron"):
        try:
            ID.isnumeric()
        except:
            print("Your ID is invalid")
        self._ID=int(ID)
        self._next=next
        self._num_out_count=0
        self._pat_status=status

    def get_pat_ID(self):
        return self._ID

    def get_num_out_count(self):
        return self._num_out_count

    def get_next(self):
        return self._next

    def get_pat_status(self):
        return self._pat_status

    def increase_num_out_count(self):
        self._num_out_count+=1


class Library_cat():
    def __init__(self):
        self._head=None
        self._tail=None
        self._size=0
        self._ch_out_count=0
        self._ch_in_count=0

    def get_head(self):
        return self._head

    def get_tail(self):
        return self._tail

    def get_ch_out_count(self):
        return self._ch_out_count

    def get_ch_in_count(self):
        return self._ch_in_count

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size==0

    def increase_ch_out_count(self):
        self._ch_out_count+=1

    def increase_ch_in_count(self):
        self._ch_in_count+=1

    """ Add a copy of a book"""
    def add_book(self,ISBN,title):
        #Validate ISBN and title
        if self.is_empty():
            newest=BookNode(ISBN,title) # this creates a new node with element
            # as the domain_name next as None with a reference count of 1
            self._head=newest
            self._tail=newest
            self._size+=1
        elif len(self)==1:
            newest=BookNode(ISBN,title)
            if self._head.get_ISBN_number()==ISBN:
                self._status_num+=1
                self._size+=1
                return
            else:
                self._head._next=newest
                self._tail=newest
                self._size+=1
        else:
            newest=BookNode(ISBN,title)
            curr=self._head
            while curr:
                if curr.get_ISBN_number()==ISBN:
                    curr._status_num+=1
                    self._size+=1
                    return
                else:
                    curr=curr._next
            self._tail._next=newest
            self._tail=newest
            self._size+=1

    """ Remove a copy of a book"""
    def remove_book(self,ISBN):
        if self.is_empty():
            return "No book to remove"
        curr=self.get_head()
        if curr.get_ISBN_number()==ISBN:
            self._head=self._head._next
            curr=None
            self._size-=1
            return
        curr2=curr._next
        while curr2:
            if curr2.get_ISBN_number()==ISBN:
                curr._next=curr2._next
                curr2=None
                self._size-=1
                return
            curr=curr._next
            curr2=curr._next
        return "The book you want to remove is not there"

    """ check out a book"""
    def check_out(self,ISBN,ID,Patron):
#        Patron=Library_pat()
        if not len(ISBN)==10 and ISBN[0:9].isnumeric() and Patron.is_patron(ID):
            print("ISBN or/and ID is/are invalid")
        if self.is_empty():
            return "No book to check-out"
        curr=self.get_head()
        while curr:
            if curr.get_ISBN_number()==ISBN:
                if curr.get_status()=="Available":
                    if curr.get_status_num()==1:
                        curr._status="Unavailable"
                        curr._status_num-=1
                    else:
                        curr._status_num-=1
                    curr.increase_book_out_count()
                    self.increase_ch_out_count()
                    Patron.increase_pat_out_count(ID)
                    book=curr
                    return book
                else:
                    curr.increase_book_out_count()
                    print("Error: Book not available, all copies checked out")
            curr=curr._next
        return "Book is not in Library"

    """check in a book"""
    def check_in(self,ISBN,ID):
        Patron=Library_pat()
        try:
            len(ISBN)==10 and ISBN[0:9].isnumeric() and Patron.is_patron(ID)
        except:
            print("ISBN is invalid/Not a patron of the library")
        curr=self.get_head()
        while curr:
            if curr.get_ISBN_number()==ISBN:
                if curr.get_status()=="Unavailable":
                    curr._status="Available"
                    curr._status_num+=1
                else:
                    curr._status_num+=1
                self.increase_ch_in_count()
                book=curr
                return book
            curr=curr._next
        return " This book does not belong to this library"

class Library_pat():
    """ a list of integers"""
    def __init__(self):
        self._head=None
        self._tail=None
        self._size=0

    def get_head(self):
        return self._head

    def get_tail(self):
        return self._tail

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size==0

    def is_patron(self,ID):
        try:
            ID.isnumeric()
        except:
            print("Your ID has a problem")
        curr=self.get_head()
        while curr:
            if curr.get_pat_ID()==int(ID):
                return True
            curr=curr._next
        return False

    """ add a patron"""
    def add_patron(self,ID):
        try:
            ID.isnumeric()
        except:
            print("Your ID has a problem")
        if self.is_empty():
            newest=PatNode(ID) # this creates a new node with element
            # as the domain_name next as None with a reference count of 1
            self._head=newest
            self._tail=newest
            self._size+=1
        elif len(self)==1:
            newest=PatNode(ID)
            if self._head.get_pat_ID()==int(ID):
                return "Patron already exists"
            else:
                self._head._next=newest
                self._tail=newest
                self._size+=1
        else:
            newest=PatNode(ID)
            curr=self._head
            while curr:
                if curr.get_pat_ID()==int(ID):
                    return "Patron already exists"
                else:
                    curr=curr._next
            self._tail._next=newest
            self._tail=newest
            self._size+=1

    """remove a patron"""
    def remove_patron(self,ID):
        try:
            ID.isnumeric()
        except:
            raise ValueError("patron ID invalid")
        if self.is_empty():
            return "Patron deos not exist"
        pat=int(ID)
        curr=self.get_head()
        while curr:
            if curr.get_pat_ID()==pat:
                curr._pat_status="removed"
                self._size-=1
                return
            curr=curr._next
        return "The patron you want to remove is not there"

    def increase_pat_out_count(self,ID):
        try:
            ID.isnumeric()
        except:
            print("invalid ID")
        curr=self.get_head()
        while curr:
            if curr.get_pat_ID()==int(ID):
                curr.increase_num_out_count()
                return
            curr=curr._next

def process_transaction(inputFileName,Books,Patrons):
    # For each line in the transaction, first word is the type of transaction. The rest depends on the
    # transaction type.
    inFile=open(inputFileName,"r")
    for line in inFile:
        b=line.strip()
        b=b.split(",") # b becomes a list transaction information
        action=b[0].strip()
        if action=="addPatron":
            ID=b[1].replace(" ","")
            if ID.isnumeric():
                Patrons.add_patron(ID)
        elif action=="addBook":
            ISBN=b[1].replace(" ","")
            title=b[2].strip()
            if len(ISBN)==10 and ISBN[0:9].isnumeric():
                Books.add_book(ISBN,title)
        elif action=="checkin":
            ID=b[1].replace(" ","")
            ISBN=b[2].replace(" ","")
            if len(ISBN)==10 and ISBN[0:9].isnumeric() and ID.isnumeric():
                Books.check_in(ISBN,ID)
            else:
                print("Error: Checkin not possible. Wrong ID/ISBN")
        elif action=="checkout":
            ID=b[1].replace(" ","")
            ISBN=b[2].replace(" ","")
            if len(ISBN)==10 and ISBN[0:9].isnumeric() and ID.isnumeric():
                Books.check_out(ISBN,ID,Patrons)
            else:
                print("Error: Check out impossible due to wrong ID/ISBN")
        elif action=="removeBook":
            ISBN=b[1].replace(" ","")
            if not len(ISBN)==10 and ISBN[0:9].isnumeric():
                print("Error: Book does not exist")
            else:
                Books.remove_book(ISBN)
        elif action=="removePatron":
            ID=b[1].strip()
            try:
                int(ID)
            except:
                print("Error: Patron does not exist")
            Patrons.remove_patron(ID)
        else:
            print("Error", action)
            print("  -Command not valid")
    inFile.close()
    return (books_cat,patrons_cat)
# Actions
""" the software will read and process a transaction log"""
# Validate all books(check for exiting and available) and patrons before Transactions

""" in the main"""
if __name__=="__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Lab 10")
    parser.add_argument("-i","--inputFileName", type=str, help="A transaction log file", required=True)
    args = parser.parse_args()

    if not (os.path.isfile(args.inputFileName)):
        print("error,", args.inputFileName, "does not exist, exiting.", file=sys.stderr)
        exit(-1)

""" A transaction log contains all actions that can be done. add, remove, check-in and check-out books, as
well as adding and removing patrons"""

# processes the transaction log and then display the following:
""" total books"""
books_cat=Library_cat()
patrons_cat=Library_pat()
Transactions=process_transaction(args.inputFileName,books_cat,patrons_cat)
print(len(Transactions[0]))
"""number of check-outs"""
print(Transactions[0].get_ch_out_count())
"""number of check-ins"""
print(Transactions[0].get_ch_in_count())
"""the ISBN, title, and check-out count of the book that was checked-out most often"""
curr=Transactions[0].get_head()
if curr==None:
    print(None,None,0)
else:
    max_count=curr.book_out_count()
    book=curr
    while curr:
        if max_count<curr.book_out_count():
            max_count=curr.book_out_count()
            book=curr
        curr=curr._next
    print(book.get_ISBN_number(),book.get_book_title(),max_count,sep=", ")
""" the ID and check-out count of the patron that checked-out the most books"""
max=Transactions[1].get_head()
if max==None:
    print(None,0)
else:
    rec=max.get_next()
    while rec:
        if max.get_num_out_count()<rec.get_num_out_count():
            max=rec
        rec=rec.get_next()
    print(max.get_pat_ID(),max.get_num_out_count(),sep=", ")
# Create a class Library
