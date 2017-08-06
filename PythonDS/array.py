def show_array(ary):
    print(ary)


def insert(ary, value):
    ary = ary.copy()
    ary.append(value)
    return ary


def insert_by_pos(ary, pos, item):
    # [1, 2, 5, 6, 15, 16] -> initial = 6
    # pos = 3, item = 10
    # [1, 2, 5, 10, 6, 15, 16] -> final = 7
    # Step 1: [1, 2, 5, 6, 15, 16, 0] -> ary.append(0) (Let i = initial) if i>pos
    # Step 2: [1, 2, 5, 6, 15, 16, 16] -> ary[i] = ary[i-1] (i = i-1) i = 6
    # Step 3: [1,2, 5, 6, 15, 15, 16] -> ary[i] = ary[i-1] (i = i-1) i = 5
    # Step 4: [1, 2, 5, 6, 6, 15, 16] -> ary[i] = ary[i-1] (i = i-1) i = 4
    # Step 5: [1, 2, 5, 10, 6, 15, 16] -> ary[i] = item (i == pos) i = 3
    # Step 6: exit from loop
    ary = ary.copy()
    if pos > len(ary):
        print("Invalid position!")
        return ary
    initial = len(ary)
    ary.append(0)

#    while initial > pos:
#        ary[initial] = ary[initial - 1]
#        initial -= 1

    for i in range(initial, pos, -1):
        ary[initial] = ary[initial - 1]
    ary[pos] = item
    return ary


def update_array_pos(ary, pos, new_val):
    # ary = [1, 2,3, 4]
    # pos = 2, new_val = 10
    # ary = [1, 2, 10, 4]
    ary = ary.copy()
    try:
        ary[pos] = new_val
    except:
        print("Invalid Position!")
    return ary


def search_value(ary, element):
    for i in range(len(ary)):
        if ary[i] == element:
            return i
    return None


def update_array_value(ary, old_value, new_value):
    return update_array_pos(ary, search_value(ary, old_value), new_value)


def delete_by_pos(ary, pos):
    # [5, 3, 7, 9, 2]       pos = 5. size = 5,
    # Step 1: [5, 3, 9, 9, 2] ary[i-1] = ary[i] i=3  i = i+1
    # Step 2: [5, 3, 9, 2, 2] ary[i-1] = ary[i] i=4 i = i+1
    # Step 3: [5, 3, 9, 2]1 ary.pop()
    ary = ary.copy()
    if pos is not None:
        if pos >= len(ary):
            print("Invalid position")
        else:
            for i in range(pos+1, len(ary)):
                ary[i-1] = ary[i]
            ary.pop()
    else:
        print("The position supplied is None!")
    return ary


def delete_by_value(ary, value):
    return delete_by_pos(ary, search_value(ary, value))


def main():
    array = list()
    choice = 99
    while choice != 0:
        message = """
1. Insert an element
2. Insert an element at specific position
3. Search an Element
4. Update by Position
5. Update by Value
6. Delete by Position
7. Delete by Value
8. Show Array
0. Exit
Enter your choice: """
        choice = int(input(message))
        if choice == 1:
            val = int(input("Enter value: "))
            array = insert(array, val)
        elif choice == 2:
            pos = int(input("Enter position: "))
            val = int(input("Enter value: "))
            array = insert_by_pos(array, pos, val)
        elif choice == 3:
            val = int(input("Enter value: "))
            sv = search_value(array, val)
            if sv:
                print("Item found at:" + str(sv))
            else:
                print("Item not found!")
        elif choice == 4:
            pos = int(input("Enter position: "))
            val = int(input("Enter value: "))
            array = update_array_pos(array, pos, val)
        elif choice == 5:
            old = int(input("Enter old value: "))
            new = int(input("Enter new value: "))
            array = update_array_value(array, old, new)
        elif choice == 6:
            pos = int(input("Enter position: "))
            array = delete_by_pos(array, pos)
        elif choice == 7:
            val = int(input("Enter value: "))
            array = delete_by_value(array, val)
        elif choice == 8:
            show_array(array)
        else:
            print("Thank You!")
            break

main()
