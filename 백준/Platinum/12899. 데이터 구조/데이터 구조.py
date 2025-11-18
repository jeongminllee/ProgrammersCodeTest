MAX = 2_000_000
size = 1
while size < MAX :
    size <<= 1

def update(pos, diff) :
    i = pos + size - 1
    while i :
        tree[i] += diff
        i >>= 1

def kth(k) :
    node = 1
    while node < size :
        left = node * 2
        if tree[left] >= k :
            node = left
        else :
            k -= tree[left]
            node = left + 1

    return node - size + 1, node


if __name__ == "__main__" :
    N = int(input())
    output = []

    tree = [0] * (2 * size)

    for _ in range(N) :
        T, X = map(int, input().split())
        if T == 1 :
            update(X, 1)

        else :
            val, node = kth(X)
            output.append(str(val))

            while node :
                tree[node] -= 1
                node >>= 1

    print("\n".join(output))