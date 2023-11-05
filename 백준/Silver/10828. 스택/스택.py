import sys

def Stack() :
    stack = []
    T = int(sys.stdin.readline())
    for n in range(T) :

        cmd = sys.stdin.readline().rstrip()
        if cmd == 'pop' :
            print(stack.pop() if stack else -1)

        elif cmd == 'size' :
            print(len(stack))

        elif cmd == 'empty' :
            print(+(not stack))

        elif cmd == 'top' :
            print(stack[-1] if stack else -1)

        else :
            _, x = cmd.split()
            stack.append(x)

Stack()