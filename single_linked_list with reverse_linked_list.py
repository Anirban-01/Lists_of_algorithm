# create Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    # create linkedlist function

    def linked_list(head):
        temp = head
        while temp is not None:
            print('Node:',str([temp.value]),'>>>',end=' ')
            temp = temp.next

    # create reverselist function

    def reverse_list(head):
        previous_node = None
        current_node = head

        while current_node:
            Next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = Next_node
        return previous_node


# creating node
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

# linking node
node1.next = node2
node2.next = node3
node3.next = None

# display linkedlist
#node1.linked_list()

node1.reverse_list()

# display reverselist
node3.linked_list()


