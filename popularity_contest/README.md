# Popularity Contest 1
Utilizes single linked structures in the context of parsing and analyzing access logs from a web server. 

## Setup
Earlham College CS department supports a number of web servers (Apache) and one of them hosts a bunch of virtual domains such as http://cs.earlham.edu, http://fieldscience.cs.earlham.edu etc. This program determines what the most popular virtual domain is and how many times it was referenced during the period of logfile covers. 

## Tasks
Designed, wrote and tested:
* A class for a list node to be used in a single linked list. it has fields for a domain
name, a reference count, and a pointer to the next node.
* A single linked list class. it has a field for the head pointer,
* A method that given an input log file populates a linked list with the domain names and
references found in the log file, returning the linked list to the caller (my main()). my
algorithm reads one line of file at a time, parses-out the domain name, removes the port number from it, and then searchs my list for it. If not found, it is added to the list with a reference count of 1. If found in my list then increment the reference count for that node/domain name by one.
* My main() function reads the log file name from the command line, checks to see that it exists, calls my populate method, and with the returned, populated list determines the following from it:
    * the total number of visits to all domains
    * the number of unique domain names
    * the most popular domain and how many visits it had
    * the % of total visits represented by that domain

## Implementation Notes
My script has one command line argument -i for the input logfile, uses the main() technique, runs in O(n) time. It reads the input file one line at a time and the percentage is rounded to two places. 

# Popularity Contest 2
Utilizes a tree data structure to do same work as popularity contest 1. 
## Tasks
* A class for a tree node used in a binary search tree (BST) with a constructor and fields for a domain name, a reference count, and pointers to its parent, left, and right children.
* A class for a binary search tree with a constructor, a field for the root pointer, an addOrIncrementDomainNameNode() method that either adds the domain to the BST at the appropriate place (by domain name) with a reference count of 1, or increments the reference count if the domain name is already there, and a printTree() method that displays the domain name and reference count in domain name order (ascending). This is a property of the way you visit nodes (inorder, preorder, etc.)
* The input logfile populates a Binary Search tree with the domain names and references.  
* My main() function reads the log file name from the command line, checks to see that it exists, calls my populate function, and then prints the returned populated tree using the printTree() method.