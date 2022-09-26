#Question 1.
#In a conventional linked list, we traverse the list from the head node and stop the traversal when we reach NULL. In a circular linked list, we stop traversal when we reach the first node again.
#code:
def printList(self):
    temp = self.head

    # If linked list is not empty
    if self.head is not None:
        while (True):

            # Print nodes till we reach first node again
            print(temp.data, end=" ")
            temp = temp.next
            if (temp == self.head):
                break

#Question 2.
#Applications of circular linked list are :
#Data structures such as stacks and queues are implemented with the help of the circular linked lists. Circular Linked List is also used in the implementation of advanced data structures such as a Fibonacci Heap. It is also used in computer networking for token scheduling.
