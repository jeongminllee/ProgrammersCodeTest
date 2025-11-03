import sys
input = sys.stdin.readline
def find(a: int) :
    if parents[a] != a :
        parents[a] = find(parents[a])
    return parents[a]

def union(a: int, b: int) :
    global ANSWER
    a_root = find(a)
    b_root = find(b)
    if a_root == b_root :
        if good_works[a_root] :
            return
        if marks[a] == marks[b] :
            good_works[a_root] = True
            ANSWER += len(element_sets[a_root])
            return
        return
    size_a = len(element_sets[a_root])
    size_b = len(element_sets[b_root])

    if good_works[a_root] and good_works[b_root] :
        if size_a < size_b :
            parents[a_root] = b_root
            small_to_large(element_sets[a_root], element_sets[b_root])
        else :
            parents[b_root] = a_root
            small_to_large(element_sets[b_root], element_sets[a_root])

        return

    if good_works[a_root] :
        if size_a < size_b:
            parents[a_root] = b_root
            small_to_large(element_sets[a_root], element_sets[b_root])
        else:
            parents[b_root] = a_root
            small_to_large(element_sets[b_root], element_sets[a_root])
        ANSWER += size_b
        return

    if good_works[b_root] :
        if size_a < size_b :
            parents[a_root] = b_root
            small_to_large(element_sets[a_root], element_sets[b_root])
        else :
            parents[b_root] = a_root
            good_works[a_root] = True
            small_to_large(element_sets[b_root], element_sets[a_root])
        ANSWER += size_a
        return

    if marks[a] != marks[b] :
        if size_a < size_b :
            parents[a_root] = b_root
            small_to_large(element_sets[a_root], element_sets[b_root])
        else :
            parents[b_root] = a_root
            small_to_large(element_sets[b_root], element_sets[a_root])
    else :
        if size_a < size_b :
            parents[a_root] = b_root
            reverse_mark(element_sets[a_root])
            small_to_large(element_sets[a_root], element_sets[b_root])
        else :
            parents[b_root] = a_root
            reverse_mark(element_sets[b_root])
            small_to_large(element_sets[b_root], element_sets[a_root])


def small_to_large(small: set, large: set) :
    large.update(small)
    small.clear()

def reverse_mark(elements: set) :
    for e in elements :
        marks[e] = 1 - marks[e]


def main() :
    global ANSWER, parents, marks, element_sets, good_works
    ANSWER = 0
    N, Q = map(int, input().split())
    parents = [u for u in range(N+1)]
    marks = [0 for _ in range(N+1)]
    element_sets = [set([u]) for u in range(N+1)]
    good_works = [False for _ in range(N+1)]
    for _ in range(Q) :
        a, b = map(int, input().split())
        union(a, b)
        print(ANSWER)


if __name__ == "__main__" :
    main()