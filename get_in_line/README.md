# Get in Line
Uses a priority queue data structure to keep a bunch of things which have relative priority in order and retrieves them in order. 

## Setup
A customer shows-up, presents their priority and are placed in-line accordingly. If there is already someone or someones in-line with the same priority they are placed at the back of that priority “section”. If they don’t have a priority they are placed at the end of the line (that is the end of the no priority section), these are indicated by a 0 priority. After a bunch of customers arrive, they are conveniently packaged in one data file, and are queued, I display the
first customer in line and the last one.

## Tasks
Designed, wrote and tested:
* A class for an Item that holds a customer name (string) and a priority (integer). Higher numbers are higher priority, 0 is the lowest (new customer, or forgot their card, or a privacy hawk).
* A class for a Priority Queue that holds Items in order by priority, and within priority by arrival time.
* A mechanism to read a datafile of (name, priority) tuples and populate a Priority Queue with Items.
* A mechanism to display the first person in the Priority Queue.
* A mechanism to display the last person in Priority Queue.
* A mechanism to remove the first person from the Priority Queue.
* A main() function that reads the input file name from the command line, checks to see that it exists, and calls my populate method. After populating the Priority Queue I:
    * print the first person in the queue
    * remove the first person from the queue
    * display the new first person in the queue
    * display the last person in the queue
    * print the results to stdout

## Implementation
The `medium_input.dat` file is passed as an input file via the command line argument -i.
