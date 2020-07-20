"""
    Data:
    Stores two pieces of data:
    1. The Value
    2. The Next Node
​
    Methods/Behavior/Operations:
    1. Get value
    2. Set value
    3. Get next
    4. Set next
"""


class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next
