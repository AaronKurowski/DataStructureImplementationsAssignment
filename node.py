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
            # No root? create one!
            self.root = Node(value)
        else:
            # compare value to current.data and place it correctly
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

    def search(self, root,  value):
        while root is not None:
            if value < root.data:
                root = root.left_child
            elif value > root.data:
                root = root.right_child
            else:
                print("Value is in the tree!")
                return True
        print("Value not in tree")
        return False

    def visit(self, node):
        print(node.data)

    def preorder(self, current):
        if current:
            self.visit(current)
            self.preorder(current.left_child)
            self.preorder(current.right_child)

    def inorder(self, current):
        if current:
            self.inorder(current.left_child)
            self.visit(current)
            self.inorder(current.right_child)

    def postorder(self, current):
        if current:
            self.postorder(current.left_child)
            self.postorder(current.right_child)
            self.visit(current)

    # def create_nodes(self):
    #     node1 = Node(12)
    #     node2 = Node(15)
    #     node3 = Node(9)
    #     node4 = Node(3)
    #     node5 = Node(16)
    #     node6 = Node(5)
