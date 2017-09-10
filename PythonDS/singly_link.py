# Single Linked List: Single Linked List is a list in python that contains various Nodes.

# Node: A node is also a list which is stored in a single linked list.
# Structure: [data, address]
# Address of Node: Address of Node is basically index of that node in single linked list.
# Data of Node: This is the data contained in a node. In Python, this can be anything.


singl = [
    ['Homamsh', 2],
    ['hfjg', None],
    ['jinun', 4],
    ['pinu', 1],
    ['himivya', 3],
]


# Stores the index of starting node in singl list
start = 0

# [[], ......]

def create():
    """
    To create a new node as per definition
    Ask input from user for data
    Convert it to int via int()
    Create a list [data, None]
    Return node (list)

    :return: node
    """
    return [int(input("Enter data: ")), None]


def insertafter(sl, curr):
    """
    To add created nodes in a single list
    create(): will return a node
    :param sl: list
        Single Linked List: contains list where nodes are stored
    :param curr: int
        Index of node after which we have to insert new node
        -1 -> To add in beginning
    :return:
    """
    global start
    new_node = create()
    sl.append(new_node)
    ind = sl.index(new_node)
    if curr == -1:
        # Adding node to start
        sl[ind][1] = start
        start = ind
    else:
        sl[curr][1] = ind


def read():
    global start
    print("Traversing Singlee linked List")

    print("Curent\tData\tNext")
    cur = start
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


read()