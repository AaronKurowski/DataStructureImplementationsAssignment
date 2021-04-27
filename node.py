class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

        self.left_child = None
        self.right_child = None

    def has_value(self, value):
        """Method that compares the value with the node data"""
        if self.data == value:
            return True
        else:
            return False


class BST(Node):
    def __init__(self):
        self.root = None
        super().__init__(data=None)

    def add(self, current, value):
        """Creates a bst from scratch"""
        if self.root is None:
            # if no root, create one!
            self.root = Node(value)
        else:
            # compare root to one being added and correctly place it
            if value < current.data:
                if current.left_child is None:
                    current.left_child = Node(value)
                else:
                    self.add(current.left_child, value)
            else:
                if current.right_child is None:
                    current.right_child = Node(value)
                else:
                    self.add(current.right_child, value)
