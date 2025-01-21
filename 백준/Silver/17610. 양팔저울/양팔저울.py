k = int(input())
weights = list(map(int, input().split()))
possible_weights = [weights[0]]

for i in range(1, k) :
    tmp = [weights[i]]
    for e in possible_weights :
        tmp += [weights[i] + e, abs(weights[i] - e)]

    possible_weights += tmp

possible_weights = set(possible_weights)
if 0 in possible_weights :
    possible_weights.remove(0)
    
print(sum(weights) - len(possible_weights))