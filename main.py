import function_operation
import models

if __name__ == "__main__":
    print("\n ********   Test Case 1  *********")
    print("1. First polynomial is : ",end = "")
    List1 = function_operation.Function_LinkedList()
    List1.insert_data(2, 2)
    List1.insert_data(1, 1)
    List1.insert_data(0,1)
    List1.display()
    
    print("2. Second polynomial is : ",end = "")
    List2 = function_operation.Function_LinkedList()
    List2.insert_data(2, 2)
    List2.insert_data(1, 1)
    List2.insert_data(0, 1)
    List2.display()

    print("\nSum of above 2 polynomials is : ",end = "")
    models.addition(List1.head,List2.head).display()

    print("\nProduct of above 2 polynomials is : ",end = "")
    product_list = models.multiplication(List1.head, List2.head)
    product_list.display()

    print(" \n********   Test Case 2  *********")

    print("1. First polynomial is : ",end = "")
    List1 = function_operation.Function_LinkedList()
    List1.insert_data(2,3)
    List1.insert_data(1,2)
    List1.insert_data(0,2)
    List1.display()

    print("2. Second polynomial is : ",end = "")
    List2 = function_operation.Function_LinkedList()
    List2.insert_data(2,2)
    List2.insert_data(1,3)
    List2.insert_data(0,3)
    List2.display()

    print("\nSum of above 2 polynomials is : ",end = "")
    models.addition(List1.head, List2.head).display()

    print("\nProduct of above 2 polynomials is : ",end = "")
    models.multiplication(List1.head, List2.head).display()

