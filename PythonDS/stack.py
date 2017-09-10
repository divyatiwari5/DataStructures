class Stack:
    """
    To create a class of stack. In this class, we can do all the functions of stack.
    """

    def __init__(self, size):

        # elements list will contain all the elements
        self.elements = list()

        # size of the stack
        self.size = size

        # Initialize the list with None so that we can add later on
        for x in range(self.size):
            self.elements.append(None)

        # current position of top pointer in stack
        self.top = -1

    def push(self, elem):
        """
        This function pushes element to the top of the stack.
        :param elem: Element to insert in the stack
        :return: bool
            True/False based on success.
        """
        if self.top < self.size -1:
            # First point top to next position
            self.top += 1
            # Then append the element
            self.elements[self.top] = elem
            print("Element pushed: "+ elem)

            return True
        else:
            print("Stack OverFlow")
            # TODO: raise an error
            return False

    def pop(self):
        if self.top < 0:
            print("Stack UnderFlow")
            # TODO: raise an error
            return None
        else:
            # print(self.elements[self.top])
            poped = self.elements[self.top]
            print("Element popped: "+ poped)
            self.elements[self.top] = None
            self.top -= 1
            return poped

    def isempty(self):
        return self.top == -1

    def topfunc(self):
        print(self.top)


def main():
    # What if user presses 2/3/4 without pressing 1
    # What if user enters string instead of integer
    # What if user enters size to be non positive
    # Add comments
    # paranthesis_check.py - Create a function where
    # You accept a parameter string -> DONE
    # Using stack you check if paranthesis system is okay
    # If there is an error, return False
    # Else return true
    while True:
        print("Menu")
        print("1. Initialize Stack")
        print("2. Push to Stack")
        print("3. Pop from Stack")
        print("4. Check Top of Stack")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            siz = int(input("Enter the size of stack: "))
            stobj = Stack(siz)
            print("Your new stack is created!")
        elif choice == 2:
            e = input("Enter the element that is to be pushed: ")
            stobj.push(e)
        elif choice == 3:
            stobj.pop()
        elif choice == 4:
            print(stobj.top)
        else:
            exit()

main()
