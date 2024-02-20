def rot(n, k) :
    idx = 0
    stack = [i for i in range(1, n + 1)]
    res = []

    while stack :
        idx = (idx + (k - 1)) % len(stack)
        res.append(str(stack.pop(idx)))

    return '<' + ', '.join(res) + '>'

n, k = map(int, input().split())
print(rot(n, k))

# class Queue :
#     def __init__(self, idx):
#         self.front = 0
#         self.stack = [i for i in range(1, idx + 1)]
#
#     def dequeue(self, k):
#         result = []
#         while self.stack :
#             self.front = (self.front + (k - 1)) % (len(self.stack))
#             result.append(str(self.stack[self.front]))
#             del self.stack[self.front]
#         return '<' + ', '.join(result) + '>'
#
# n, k = list(map(int, input().split()))
# a = Queue(n)
# print(a.dequeue(k))