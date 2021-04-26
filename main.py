from data1 import Data1
from linkedlist import LinkedList


if __name__ == '__main__':
    # data = Data1()
    # data.print_pi_day_month()

    # data.print_bday_locations()
    # data.sweepstakes_winner()

    # data.print_brothers()

    linked_list = LinkedList()
    linked_list.append_node(55)
    linked_list.append_node(60)
    linked_list.append_node(65)


    linked_list.add_node_to_beginning(50)

    linked_list.print_list()

    test = linked_list.contains(45)
    print(test)
