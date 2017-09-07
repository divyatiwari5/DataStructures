"""a = list()
b = list()

a.append(1)
a.append(2)
a.append(3)
a.append(4)
a.pop()
a.pop()
a.pop()
a.pop()

for x in range(4):
    b.append(None)

b[0] = 1
b[1] = 2
b[2] = 3
"""


def push(stk, t, e, siz):
    if t < siz:
        t += 1
        stk[t] = e
        print(e)
    else:
        print("Stack Overflow")
    return t


def pop(stk, t):
    if t < 0:
        print("Stack underflow")
    else:
        print(stk[t])
        stk[t] = None
        t -= 1
    return t


def main():
    print("This is not")

    elements = list()
    size = int(input("Enter size of stack: "))
    top = -1

    for x in range(size):
        elements.append(None)

    while True:
        print("Menu: ")
        print("1. Push")
        print("2. Pop")
        print("3. Exit")
        ch = int(input("Enter choice: "))

        if ch == 1:
            top = push(elements, top, input("Enter item to push: "), size)
        elif ch == 2:
            top = pop(elements, top)
        else:
            exit()

print("This is executed")

if __name__ == '__main__':
    main()