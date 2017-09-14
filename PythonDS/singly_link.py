# Single Linked List: Single Linked List is a list in python that contains various Nodes.

# Node: A node is also a list which is stored in a single linked list.
# Structure: [data, address]
# Address of Node: Address of Node is basically index of that node in single linked list.
# Data of Node: This is the data contained in a node. In Python, this can be anything.
singl = []

# Stores the index of starting node in singl list
start = None


def create():
    """
    To create a new node as per definition
    Ask input from user for data
    Convert it to int via int()
    Create a list [data, None]
    Return node (list)

    :return: node
    """
    return [input("Enter data: "), None]


def insertafter(sl, curr):
    """
    To add created nodes in a single list
    create(): will return a node
    :param sl: list
        Single Linked List: contains list where nodes are stored
    :param curr: int
        Index of node after which we have to insert new node
        -1 -> To add in beginning
    :return: bool
    """
    import colorama

    global start
    if curr >= len(sl):
        # colorama.init()
        # print(colorama.Fore.RED + "Please  enter valid position!")
        # Raisinig ValueError if position after which element is to be added is more than the lenght of the list
        raise ValueError("Enter a valid position!")
        # return False
    new_node = create()
    sl.append(new_node)
    ind = sl.index(new_node)
    if curr == -1:
        # Adding node to start
        sl[ind][1] = start
        start = ind
    else:
        sl[ind][1] = sl[curr][1]
        sl[curr][1] = ind
    return True


def read():
    """
    To read nodes of single linked list

    :return:
    """
    global start
    print("Traversing Singlee linked List")

    print("Current\tData\tNext")
    cur = start       # cur = None
    while cur != None:
        node_cur = singl[cur]
        print(str(cur) + "\t\t" + str(node_cur[0]) + "\t\t" + str(node_cur[1]))
        cur = node_cur[1]

    # range(4)
    # x: 0                                    1
    # cur: 0                                  2                         1                           3
    # node_cur = singl[0] = [1,2]           singl[2] = [2,1]            singl[1] = [3,3]        singl[3] = [4,NOne]
    # singl[0][0] = [1,2][0] = 1            singl[2][0] = 2             singl[1][0] = 3         singl[3][0] = 3
    # singl[0][1] = [1,2][1] = 2            singl[2][1] = 1             singl[1][1] = 3         singl[3][1] = None
    # cur = singl[0][1] = 2                 cur = singl[2][1] = 1       cur = singl[1][1] = 3   cur = singl[3][1]


def main():
    while True:
        print("1. Add a Node")
        print("2. Read ")
        print("3. Exit")
        choice = int(input("Enter Choice: "))
        if choice == 1:
            read()
            try:
                p = int(input("Enter position after which you want to insert node: "))
                insertafter(singl, p)
            except ValueError as err:
                print("Error: " + str(err))

        elif choice == 2:
            read()
        else:
            exit()

main()