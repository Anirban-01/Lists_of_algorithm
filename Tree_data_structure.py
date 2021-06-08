class Node:
    def __init__(self, data):
        self.left_node = None
        self.right_node = None
        self.data = data

    def insert_node(self, data):
        node = Node(data)
        # when root node is not null
        if self.data is not None:
            # when new data is less then root data
            if data < self.data:
                # when left node has no data
                if self.left_node is None:
                    # when left node is present, insert new data
                    self.left_node = node
                else:
                    # when left node is not present, insert new node and data
                    self.left_node.insert_node(data)
            # when right node has no data
            elif data > self.data:
                # when right node has no data
                if self.right_node is None:
                    # when right node is present, insert new data
                    self.right_node = node
                else:
                    # when right node is not present, insert new node and data
                    self.right_node.insert_node(data)
        else:
            self.data = data

    def print_Tree(self):
        if self.left_node:
            self.left_node.print_Tree()
        if self.right_node:
            self.right_node.print_Tree()
        print(str(self.data))

# binary_search algorithm to find any target element


def binary_search(arr, left_element, right_element, target_element):
    """base case"""
    # if target element in array then return element, else return -1
    while right_element >= left_element:
        mid_element = left_element + (right_element - left_element) // 2
        if arr[mid_element] == target_element:
            return mid_element
        elif arr[mid_element] > target_element:
            return binary_search(arr, left_element, mid_element - 1, target_element)
        else:
            return binary_search(arr, mid_element + 1, right_element, target_element)
    return -1


arr = [2, 3, 4, 5, 6, 7, 8]
target_element = int(input('Enter the element:', ))


return_value = binary_search(arr, 0, len(arr) - 1, target_element)

# data= (2,3,4,5,6,7,1)
# create object for class Node
root = Node(2)
root.insert_node(8)
root.insert_node(3)
root.insert_node(4)
root.insert_node(5)
root.insert_node(6)
root.insert_node(7)

root.print_Tree()

if return_value != -1:
    print('result: ', str(return_value))
else:
    print('No valid value: ', -1)
