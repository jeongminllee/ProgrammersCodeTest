from collections import deque
import sys
input = sys.stdin.readline

class Trie :
    def __init__(self):
        self.next = [None] * 4
        self.fail = None
        self.output = 0

def insert(trie, s, idx):
    if idx >= len(s) :
        trie.output = 1
        return
    x = ord(s[idx]) - ord('0')
    if not trie.next[x] :
        trie.next[x] = Trie()
    insert(trie.next[x], s, idx + 1)

def construct_fail(root) :
    q = deque()
    root.fail = root
    q.append(root)
    while q :
        cur = q.popleft()
        for i in range(4) :
            nxt = cur.next[i]
            if not nxt :
                continue
            if root == cur :
                nxt.fail = root
            else :
                tmp = cur.fail
                while tmp != root and not tmp.next[i] :
                    tmp = tmp.fail
                if tmp.next[i] :
                    tmp = tmp.next[i]
                nxt.fail = tmp
            nxt.output += nxt.fail.output
            q.append(nxt)

def solve(s, root) :
    ret = 0
    cur = root
    for char in s :
        nxt = ord(char) - ord('0')
        while cur != root and not cur.next[nxt] :
            cur = cur.fail
        if cur.next[nxt] :
            cur = cur.next[nxt]
        ret += cur.output
    return ret


T = int(input())
for _ in range(T) :
    N, M = map(int, input().split())
    s = list(input().rstrip())
    m = list(input().rstrip())

    root = Trie()
    for i in range(N) :
        if s[i] == 'A' :
            s[i] = '0'
        elif s[i] == 'C' :
            s[i] = '1'
        elif s[i] == 'G' :
            s[i] = '2'
        else :
            s[i] = '3'

    for i in range(M) :
        if m[i] == 'A' :
            m[i] = '0'
        elif m[i] == 'C' :
            m[i] = '1'
        elif m[i] == 'G' :
            m[i] = '2'
        else :
            m[i] = '3'

    insert(root, m, 0)
    for i in range(M + 1) :
        for j in range(i + 2, M + 1) :
            m[i : j] = reversed(m[i : j])
            insert(root, m, 0)
            m[i : j] = reversed(m[i : j])

    construct_fail(root)
    print(solve(s, root))