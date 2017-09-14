node = [0,0,0]
double = []
start = None


def create():
    """
    To create a doubly linked dictionary & store it in a list
    :return: node
    """
    return {"Prev": None, "Data": input("Enter Data: "), "Next": None}


def insert_next(sl, curr):
    global start

    if curr >= len(sl):
        raise ValueError("Please enter valid position!")

    new_node = create()
    sl.append(new_node)
    index = sl.index(new_node)
    if curr == -1:
        if start is not None:
            sl[start]['Prev'] = index
        sl[index]['Next'] = start
        sl[index]['Prev'] = None
        start = index
    else:
        sl[sl[curr]['Next']]['Prev'] = index
        sl[index]['Next'] = sl[curr]['Next']
        sl[index]['Prev'] = curr
        sl[curr]['Next'] = index
    return True


def read():
    global start
    print("Traversing Doubly List!")
    print("Current\t\tPrevious\t\tData\t\tNext")
    cur = start
    while cur is not None:
        node_cur = double[cur]
        print(str(cur) + "\t\t\t" + str(node_cur['Prev']) + "\t\t\t" + str(node_cur['Data']) + "\t\t\t" + str(node_cur['Next']))
        cur = node_cur['Next']


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
                insert_next(double, p)
            except ValueError as err:
                print("Error: " + str(err))
        elif choice == 2:
            read()
        else:
            exit()


main()
