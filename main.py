from data1 import Data1
from linkedlist import LinkedList
from node import *


if __name__ == '__main__':
    # data = Data1()
    # data.print_pi_day_month()

    # data.print_bday_locations()
    # data.sweepstakes_winner()

    # data.print_brothers()

    # linked_list = LinkedList()
    # linked_list.append_node(55)
    # linked_list.append_node(60)
    # linked_list.append_node(65)
    #
    #
    # linked_list.add_node_to_beginning(50)
    #
    # linked_list.print_list()
    #
    # test = linked_list.contains(45)
    # print(test)

    # bst = BST()
    # bst.root = Node(12)
    # bst.add(bst.root, 10)
    # bst.add(bst.root.left_child, 11)
    #
    # print(bst.root.data)
    # print(bst.root.left_child.data)
    # print(bst.root.left_child.right_child.data)
    #
    # bst.search(10)
    #
    # print("\n")
    # bst.preorder(bst.root)

    # bst = BST()
    # bst.add(None, 10)
    # print(bst.root.data)
    # bst.add(bst.root, 8)
    # print(bst.root.left_child.data)
    # bst.add(bst.root, 9)
    # print(bst.root.left_child.right_child.data)
    # bst.add()

    bst = BST()
    bst.root = Node(12)
    # bst.root.left_child = Node(10)
    # bst.root.right_child = Node(9)
    # bst.root.left_child.left_child = Node(5)
    # bst.root.left_child.right_child = Node(11)

    bst.add(bst.root, 10)
    bst.add(bst.root, 9)
    bst.add(bst.root, 99)
    bst.add(bst.root, 15)
    bst.add(bst.root, 2)
    bst.add(bst.root, 4)
    bst.add(bst.root, 7)

    bst.preorder(bst.root)
    bst.search(bst.root, 99)
