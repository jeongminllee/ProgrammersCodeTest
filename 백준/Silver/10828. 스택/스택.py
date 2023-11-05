import sys
input = sys.stdin.readline


def sol():
    stack = []
    N = int(input())

    for n in range(N):
        command = input().rstrip()
        if command == "pop":
            print(stack.pop() if stack else -1)
        elif command == "size":
            print(len(stack))
        elif command == "empty":
            print(+(not stack))
        elif command == "top":
            print(stack[-1] if stack else -1)
        else:
            _, x = command.split()
            stack.append(x)


sol()
