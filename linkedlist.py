from node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def append_node(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node
            return
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def add_node_to_beginning(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def contains(self, value):
        """Searches linked list for a node that has value from parameter"""
        current_node = self.head

        # tracks position of node with value
        node_id = 1

        results = []

        while current_node is not None:
            if current_node.has_value(value):
                # appends location of node with value to results
                results.append(node_id)

            current_node = current_node.next
            node_id += 1

        return results
