import function_operation
# this method will perform the addition operation on the given equation
# this will be a very simple addition operation on the provided functions.

def addition(list1, list2):

    new_list = function_operation.Function_LinkedList()  #linked list to store the sum

    while list1 and list2:
        if list1.power > list2.power:
            new_list.insert_data(list1.power,list1.coeff)
            list1 = list1.next
        elif list1.power < list2.power:
            new_list.insert_data(list2.power,list2.coeff)
            list2 = list2.next
        else:
            coeff = list1.coeff + list2.coeff
            if coeff:
                new_list.insert_data(list1.power, coeff)
            list1 = list1.next
            list2 = list2.next

    if list1 is None:
        new_list.next = list2
        return new_list

    if list2 is None:
        new_list.next = list1
        return new_list

    return new_list


# This method will perform the multiplication operation on the given 2 polynomial equations

def multiplication(equation1, equation2):

    list3 = function_operation.Function_LinkedList()  #linked list to store the product
    list1 = equation1
    list2 = equation2

    while list1 and list2:
        while list2:
            new_power = list1.power + list2.power
            new_coeff = list1.coeff * list2.coeff

            list3.insert_data(new_power,new_coeff)
            list2 = list2.next

        list1 = list1.next
        list2 = equation2

    new_list = list3

    print("\nbefore sorting")
    new_list.display()

    sorting_function(new_list)
    return new_list


# This method calls the sorting method, implemented in the Function_linkedList class
# The polynomial linked list  is arranged in the decreasing order of powers.
# Also same power variables are combined together

def sorting_function(equation):
    equation.sort_linked_list()

