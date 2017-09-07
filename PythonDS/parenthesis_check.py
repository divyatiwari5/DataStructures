from .stack import Stack


def main():
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

            for i in exp:
                if "(" in i or "{" in i or "[" in i:
                    e = i
                    stobj.push(e)
                elif ")" in i  or "}" in i or "]" in i:
                    e = i
                    stobj.pop(e)

            print(stobj.top)



        else:
            exit()

main()
