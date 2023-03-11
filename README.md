# Mathematical Function-Solving

In this, we will use concepts such as searching, sorting, linked lists/dictionary and algorithmic
analysis in this assignment.
Assume that you are working for an educational institution, where physics researchers need
help to perform some mathematical computations for them so that they can focus on the actual
problem and save their time from trivial tasks. The requirement is to develop and provide a code
that can do the operations on mathematical functions. Let's assume that there are two functions
f(x) and g(x). Your task is to write python programs that can find the addition and multiplication
of f(x) and g(x) as an output. Also if a researcher wants to find the middle element of the output
equations, they should be able to do it with a minimum number of comparisons. Another
requirement is to save the output equations in decreasing order in terms of power.

Please find more details related to equation and their output in the expected_output.txt file


Housekeeping points
-------------------
● This is a minimal example and may not follow some standard practices
● The focus is on the main flow, with minimal error handling. Errors in validation logic
should be handled appropriately though.
● To keep the scope minimum, please assume that maximum power for input functions will
be 2 for f(x) and g(x).
● Also we can assume that both the functions are continuously increasing functions.


Program Organization
--------------------
● function_operation.py: This python file will have the class related to the linked list. It
will consist, constructor with some instance variables and class variables if required.
Creating an object for this class means, you have successfully created the nodes that
will have information of each part of the equation.

● __init__(): Define the constructor for the class with appropriate instance
variables. 

● main.py: This is the main driver program. It creates objects that will hold the initial heads
for f(x) and g(x). This python will consist of all the operations related to those equations such as addition, multiplication, finding the middle element, sorting the output list etc.

● models.py: In this python file all the implementations related to the task are mentioned. You should implement your logic in this file. There are methods named as addition,
multiplication, addition and sort are available. Internally these methods will call
LinkedList methods available in function_operation.py.


 
