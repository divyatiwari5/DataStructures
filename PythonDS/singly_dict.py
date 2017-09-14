singl = []
start = None


def create():
    """
    To create a singly dictionary which is stored in a list
    :return: node
    """
    global start
    return {'Data': input("Enter data: "), 'Next': None}


def insert_update(sl, curr):
    """
    To insert node in a single list
    :param sl: single list
            contains dict in a single list
    :param curr: index after which node is to be inserted
    :return:
    """
    global start
    if curr >= len(sl):
        raise ValueError("Please enter valid position!")

    new_node = create()
    sl.append(new_node)
    index = sl.index(new_node)
    if curr == -1:
        sl[index]['Next'] = start
        start = index
    else:
        sl[index]['Next'] = sl[curr]['Next']
        sl[curr]['Next'] = index
    return True


def delete(sl, curr): # delete(singl, -1)
    """
    To delete node
    :param sl: single list, consists of nodes
    :param curr: index of the node which is to be deleted
    :return:

    start = None
    """
    global start

    if start is None:
        raise ValueError("Linked List is empty")

    if curr == -1:
        start = sl[start]['Next']
    else:
        if sl[curr]['Next'] is None:
            raise ValueError("Next node is None. Nothing to Delete!")

        del_var = sl[curr]['Next']
        sl[curr]['Next'] = sl[del_var]['Next']
        sl[del_var]['Next'] = start


def read():
    global start
    print("Traversing Single linked List")

    print("Current\tData\tNext")
    cur = start  # cur = None
    while cur is not None:
        node_cur = singl[cur]
        print(str(cur) + "\t\t" + str(node_cur['Data']) + "\t\t" + str(node_cur['Next']))
        cur = node_cur['Next']


def main():
    while True:
        print("1. Add a Node")
        print("2. Read ")
        print("3. Delete")
        print("4. Exit")
        choice = int(input("Enter Choice: "))
        if choice == 1:
            read()
            try:
                p = int(input("Enter position after which you want to insert node: "))
                insert_update(singl, p)
            except ValueError as err:
                print("Error: " + str(err))
        elif choice == 2:
            read()
        elif choice == 3:
            read()
            try:
                k = int(input("Enter position after which you want to delete node:"))
                delete(singl, k)
            except ValueError as err:
                print("Error: " + str(err))

        else:
            exit()

main()
