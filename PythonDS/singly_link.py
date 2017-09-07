class node(object):

    def __init__(self, *args, **kwargs):
        if len(args) >= 2:
            self.value = args[0]
            if isinstance(args[1], node):
                self.next = args[1]
            else:
                raise TypeError("next should be an object of node.")
        elif 'value' in kwargs.keys() and 'next' in kwargs.keys():
            self.value = kwargs['value']
            if isinstance(kwargs['next'], node):
                self.next = kwargs['next']
            else:
                raise TypeError("next should be an object of node.")
        else:
            self.value = input("Enter value: ")
            self.next = None

print("Node created successfully!")


a = []
a.append(node(5, 2))
for x in range(1, 5):
    test = node(x, a[x-1])
    a.append(test)

for z in a:
    print("Value: " + str(z.value))


def main():
    choice = 99
    while choice != 0:
        message = """
1. Create List
2. Insert node at end
3. Insert node at the begining
4. Show list
5. Exit
Enter your choice:
        choice = int(input(message))
        if(choice == 1)