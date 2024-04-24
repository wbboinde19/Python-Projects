# Software Design
## Setup
A software system for managing book acquisitions, removals, check-outs, and check-ins. The system has these components:
* books with an ISBN number and title
* patrons with an ID number

The system supports these transactions:
* add a copy of a book, remove a copy of a book - remove_invalid_book_check.dat
* add a patron, remove a patron - remove_invalid_patron_check.dat
* check-out a book (if it’s available, and they are a patron)
* check-in a book

Fragments of transaction log with examples of each transaction can be found in the `data_files` directory

## Tasks
The software reads and processes transaction log. It rejects bad transactions such as: 
* check-out books with nonexistent patron IDs - test-1-invalid-patron-checkout.dat
* remove non-existing books/patrons - remove_invalid_patron_check.dat /
remove_invalid_book_check.dat
* or check-out books when there are no available copies, - checkout-ok-isbn-no-copy-
available.dat

The software is demonstrated by processing a transaction log and displaying the following statistics: total books held, number of check-outs, number of check-ins, the ISBN, title, and check-out count of the book that was checked-out most often, and the ID and check-out count of the patron that checked-out the most books.

## Implementation Notes
My script must has one command line argument, -i for the input transaction file and uses the main() technique. This helps organize the code and makes reuse much easier.

My solution also accounts for invalid transactions in log files. That is making sure that there are no duplicate patrons, making sure that there is no format error, making sure that a book is not checked in when it has not been checked out, and making sure that the same patron checks out and checks in a book. This can be tested using the `small` data file in `data_files` directory.