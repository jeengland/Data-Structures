"""
Node class to keep track of
the data internal to individual nodes
"""


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


"""
A tree class to keep track of things like the
balance factor and the rebalancing logic
"""


class AVLTree:
    def __init__(self, node=None):
        self.node = node
        # init height to -1 because of 0-indexing
        self.height = -1
        self.balance = 0

    """
    Display the whole tree. Uses recursive def.
    """
    def display(self, level=0, pref=''):
        self.update_height()  # Update height before balancing
        self.update_balance()

        if self.node is not None:
            print('-' * level * 2, pref, self.node.key,
                  f'[{self.height}:{self.balance}]',
                  'L' if self.height == 0 else ' ')
            if self.node.left is not None:
                self.node.left.display(level + 1, '<')
            if self.node.right is not None:
                self.node.right.display(level + 1, '>')

    """
    Computes the maximum number of levels there are
    in the tree
    """
    def update_height(self):
        if self.node is None:
            self.height = 0

        else:
            if self.node.left:
                left = self.node.left.update_height()
            else:
                left = 0
            if self.node.right:
                right = self.node.right.update_height()
            else:
                right = 0

            if left is None:
                left = 0
            if right is None:
                right = 0

            if (left > right):
                self.height = left
                return left + 1
            else:
                self.height = right
                return right + 1

    """
    Updates the balance factor on the AVLTree class
    """
    def update_balance(self):
        left = 0
        right = 0
        if self.node:
            if self.node.left:
                self.node.left.update_height()
                left = self.node.left.height
            if self.node.right:
                self.node.right.update_height()
                right = self.node.right.height
        self.balance = left - right

    """
    Perform a left rotation, making the right child of this
    node the parent and making the old parent the left child
    of the new parent.
    """
    def left_rotate(self):
        newRoot = self.node.right.node
        newLeft = self.node
        newLeftRight = None
        if self.node.right.node.left:
            newLeftRight = self.node.right.node.left.node
        self.node = newRoot
        if self.node.left:
            self.node.left.node = newLeft
        else:
            self.node.left = AVLTree(newLeft)
        if newLeftRight:
            self.node.left.node.right.node = newLeftRight
        else:
            self.node.left.node.right.node = None

    """
    Perform a right rotation, making the left child of this
    node the parent and making the old parent the right child
    of the new parent.
    """
    def right_rotate(self):
        newRoot = self.node.left.node
        newRight = self.node
        newRightLeft = None
        if self.node.left.node.right:
            newRightLeft = self.node.left.node.right.node
        self.node = newRoot
        if self.node.right:
            self.node.right.node = newRight
        else:
            self.node.right = AVLTree(newRight)
        if newRightLeft:
            self.node.right.node.left.node = newRightLeft
        else:
            self.node.right.node.left = None

    """
    Sets in motion the rebalancing logic to ensure the
    tree is balanced such that the balance factor is
    1 or -1
    """
    def rebalance(self):
        self.update_balance()

        if self.balance > 1:
            if self.node.left:
                self.node.left.update_balance()
                if self.node.left.balance < 0:
                    self.node.left.left_rotate()
            self.right_rotate()

        if self.balance < -1:
            if self.node.right:
                self.node.right.update_balance()
                if self.node.right.balance > 0:
                    self.node.right.right_rotate()
            self.left_rotate()
    """
    Uses the same insertion logic as a binary search tree
    after the value is inserted, we need to check to see
    if we need to rebalance
    """
    def insert(self, key):
        if self.node is None:
            self.node = Node(key)
        elif key < self.node.key:
            if self.node.left is None:
                self.node.left = AVLTree(Node(key))
            else:
                self.node.left.insert(key)
        elif key >= self.node.key:
            if self.node.right is None:
                self.node.right = AVLTree(Node(key))
            else:
                self.node.right.insert(key)
        self.rebalance()
