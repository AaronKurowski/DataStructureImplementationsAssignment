class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

    def has_value(self, value):
        """Method that compares the value with the node data"""
        if self.data == value:
            return True
        else:
            return False
