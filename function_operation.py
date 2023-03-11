class Node:
    def __init__(self, power = 0, coeff = 0):    
        self.power = power
        self.coeff = coeff
        self.next = None

class Function_LinkedList: 


    def __init__(self):
        self.head = None
        self.power = 0
        self.coeff = 1
        self.next = None

    def insert_data(self, power, coeff):
        # creating new node for data insertion
        self.power = power
        self.coeff = coeff
        new_node = Node(self.power, self.coeff)
        # assigning head to the temp variable
        if self.head == None:
            self.head = new_node

        else:
            tmp = self.head
            while(tmp.next):
                tmp = tmp.next
            tmp.next = new_node

        return self.head

        
    def display(self):
        # print the content of the list
        # Initializing the temp variable for traversal
        temp = self.head
        # checking the condition if there are some elements are there in the linked list
        if self.head is not None:
            # running the loop till temp is traversed once completely
            # To print the equation without any confusion, we are iterating till the second last node of the list
            while(temp.next):
                # printing the data
                if temp.coeff == 0:
                    pass
                elif temp.power != 0:
                    if temp.coeff == 1: 
                        print("x", "^", temp.power, end = " + ")
                    else: 
                        print(temp.coeff, "*", "x", "^", temp.power, end = " + ")
                else:
                    if temp.coeff == 1: 
                        print(1, end = " + ")
                    else: 
                        print(temp.coeff, "*", "x", "^", temp.power, end = " + ")


                # moving to the next node
                temp = temp.next
            if(temp.power != 0):
                if temp.coeff == 1:
                    print("x", "^", temp.power)
                else:
                    print(temp.coeff, "*", "x", "^", temp.power)
            else:
                print(temp.coeff)


# The method sorts the given linked list in the decreasing order of power.
# Also combines variables with the same power, so that only one node with a given power
# Here the current node and the next node's powers are compared.
# If the powers are the same, then the coefficients are added and put in the first node

    def sort_linked_list(self):
        ptr1 = self.head
        ptr2 = None

        # pick elements one by one
        while (ptr1  and ptr1.next):
            ptr2 = ptr1;
            # Compare the picked node with rest of the nodes
            while (ptr2.next):

                # If power of the two nodes are same
                if (ptr1.power == ptr2.next.power):

                    # Add their coefficients and put it in first node
                    ptr1.coeff = ptr1.coeff + ptr2.next.coeff;
                    ptr2.next = ptr2.next.next;

                else:
                    ptr2 = ptr2.next;

            ptr1 = ptr1.next;



