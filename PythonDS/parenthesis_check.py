from .stack import Stack


def main():

    open_bracket = ('(', '{', '[')
    close_bracket = (')', '}', ']')

    # What if user presses 2/3/4 without pressing 1
    # What if user enters string instead of integer
    # What if user enters size to be non positive
    # Add comments
    # paranthesis_check.py - Create a function where
    # You accept a parameter string
    # Using stack you check if paranthesis system is okay
    # If there is an error, return False
    # Else return true
    while True:
        print("Menu")
        print("1. Initialize Stack")
        print("2. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            exp = input("Enter expression: ")
            siz = len(exp)
            stobj = Stack(siz)
            print("Your new stack is created!")

            # exp -> {[()]$
            # Stack -> {
            # i -> $ position of i in close_bracket = 2
            # e -> [ position of e in open_bracket = 2
            exp = exp + "$"

            for i in exp:
                if i in open_bracket:
                    stobj.push(i)
                elif i in close_bracket:
                    e = stobj.pop()
                    if e is not None:
                        if not close_bracket.index(i) == open_bracket.index(e):
                            print("Invalid expression: Bracket series mismatch!")
                            break

                elif i == '$':
                    if stobj.isempty():
                        print("Success")
                    else:
                        print("Invalid Expression: Bracket number mismatch!")

        else:
            exit()

main()
