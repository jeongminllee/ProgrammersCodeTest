from collections import deque
import sys
input = sys.stdin.readline

class Trie() :
    def __init__(self):
        self.next = [None] * 4
        self.fail = None
        self.output = 0

    def ConstFail(self):
        q = deque()
        q.append(self)
        self.fail = self

        while q :
            cur = q.popleft()

            for i in range(4) :
                childNode = cur.next[i]
                if not childNode :
                    continue

                if cur == self :
                    childNode.fail = self

                else :
                    f = cur.fail

                    while f != self and not f.next[i] :
                        f = f.fail
                    if f.next[i] :
                        f = f.next[i]

                    childNode.fail = f
                q.append(childNode)
    def Add(self, pattern):
        cur = self

        for i in range(len(pattern)) :
            for j in range(i + 1, len(pattern), 1) :
                fixedCur = cur

                for idx in range(i, len(pattern)) :
                    p = pattern[idx] if (idx < i or idx > j) else pattern[j - (idx - i)]
                    if not fixedCur.next[p] :
                        fixedCur.next[p] = Trie()
                    fixedCur = fixedCur.next[p]
                fixedCur.output = 1

            if not cur.next[pattern[i]] :
                cur.next[pattern[i]] = Trie()

            cur = cur.next[pattern[i]]
            if i == len(pattern) - 1 :
                cur.output = 1

    def Search(self, pattern):
        res = 0
        cur = self
        for p in pattern :
            while cur != self and not cur.next[p] :
                cur = cur.fail

            if cur.next[p] :
                cur = cur.next[p]

            if cur.output :
                res += 1

        return res

cvDict = {"A" : 0, "C" : 1, "G" : 2, "T" : 3}

def conv(string) :
    return [cvDict[s] for s in string]

T = int(input())
for _ in range(T) :
    N, M = map(int, input().split())
    s = conv(input().rstrip())
    m = conv(input().rstrip())

    root = Trie()
    root.Add(m)
    root.ConstFail()
    print(root.Search(s))