# Stacks, Queues, and Deques
 
 For each, there exist two parts. First part deals is about designing and building implementations using the dynamicArray class as the underlying storage. The second part is about comparing the performance and ease of use of the hand-built data structures and the built-in equivalents available in Python. 

## PART 1
### Setup
The dynamicArray class is my hand-built class with associated methods and will be used as the basis of stacks, queues, and dequeues. These objects will be used to process a bunch of numbers and display some results. 

### Tasks
* A designed, coded, and tested integer stack class. It supports push(), pop(), and top() methods as well as __init__ and __len__ methods. 
* A designed, coded, and tested integer queue. It supports enqueue(), dequque(), and front() methods. as well as __init__ and __len__ methods.
* A sesigned, codedm and tested integer deque. It supports enqueueFront(), dequeueFront(), enqueueBack(), dequeueBack(), front(), and back() methods, as well as __init__ and __len__ methods.

The class definitions are packaged in `myDataStructures.py`. This is a source file with a main() section that tests the functionality of the classes and methods in it. 

`stack_driver.py` is a designed, coded, and tested script that contains:
* A function that requeires an input file of integers and a stack object of my design.
* A function that determines if the populated stack of integers are a palindrome. The stack can be changed by the function.
* A function that returns, given a populated stack, a new stack whose contents are in the reverse order of the original stack. Can also change the stack.
* A function that calculates and returns the count and sum of the values stored in a given stack. Can also change the stack. 
* My main function:
    * processes the command line argument for the input file.
    * instantiates one of my stack and calls my input function.
    * makes a copy of my stack, calls my palindrome function,passing it the copy of the stack.
    * print the results to stdout.
    * makes another copy of my stack, call my reverse function, passing it the second copy of the stack.
    * with the returned stack, calls my palindrome function again and prints the result.
    * print the top() of that stack to stdout.
    * calls my count and sum function, passing it my stack, and
    * prints the result to stdout.
* The output is a simple list of four items.

A similar process corresponds to `queue_driver.py`, and `deque_driver.py` for the queue and deque classes.

### Implementation Notes

(Designed my solution on paper first. Started by reviewing the whole enchilada, and then designed the low-level elements (the class/method definitions) and then moved to the higher level tasks. Then Updated it as I develop and refined my thinking.)
* My functions (e.g., palindrome, reverse, etc.) invokes only the public methods of stacks, queues, and deques (e.g., push, pop, enqueue, dequeue, etc.). No private methods or data from stacks or queues are referenced.
* The input file name is a required command line argument (-i).
* I check to make sure the file exists before trying to open it.
* `data*` files contain integers for testing. One is small, one is large.

## PART 2
This part compares my approach to the approach of using a python list as the underlying storage. This allows comparison between hand-built and built-in equivalents available in Python. Thus, the tasks and implementations are some but this time, using python lists.

# dynamicArray Class
An expandable array of ints which supports the usual operations.

## Setup
Two scripts. A `dynamic_array.py` and `da_driver.py` script. 

## Tasks
In da_driver.py, I: 
* designed and wrote a function populate(inputFileName) that, given an input file of integers, creates and populates a DynamicArray object and returns it to the caller.
* designed and wrote a function displayUnique(myArray) that, given a populated DynamicArray object determines the unique items in the array and displays them one by one.
* the __getitem__ function does not support negative indices.
* designed and wrote a new method insertEfficient(), so that, in the case of a resize, the elements are shifted into their final position during that operation, thereby avoiding the subsequent shifting. (used two (non-nested) loops.)
* designed and wrote a new method removeAll() that removes all occurrences of value from the given list, such that the worst-case running time of the function is O(n) on a list with n elements.
(Note: removeAll() does not rely on repeated calls to remove(), that would not be O(n).) 
* my main() in da_drive.py:
    * processes the command line argument,
    * populates a DynamicArray with the contents of the data file passed on the command line (using the insertEfficient() function),
    * displays the unique values found in the array,
    * displays the element at location -15, and
    * removes all the 7s from the array,
    * displays the element at location -15 again,
    * insert 7s again in original indexes by iteratively calling insertEfficient() function.
* For the output we have:
    * all unique integers from data-final.dat.
    * value at arr[-15] before 7s are removed.
    * value at arr[-15] after 7s are removed.

## Implementation
Use small, and large data files in `data_files` for testing. These are requred command line arguments (-i).