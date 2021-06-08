class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_list:
    def __init__(self):
        self.head = None

    # add elements in end of list
    def add_node(self, element):
        node = Node(element)
        if self.head is None:
            self.head = node
            return
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node

    # delete a first_node

    def delete_node(self):
        temp = self.head
        while temp:
            temp = self.head
            self.head = self.head.next
            temp = None

    # delete end_node

    def delete_end_node(self):
        curr = self.head.next
        prev = self.head
        while curr.next is not None:
            curr = curr.next
            prev = prev.next
        prev.next = None

    # display the linked list
    def display_list(self):
        temp = self.head
        while temp:
            print('Node',str(temp.data),'>>>', end=' ')
            temp = temp.next


linked_list = Linked_list()

linked_list.add_node(1)
linked_list.add_node(2)
linked_list.add_node(3)

#linked_list.display_list()

#linked_list.delete_node()
#linked_list.display_list()

linked_list.delete_end_node()
linked_list.display_list()
