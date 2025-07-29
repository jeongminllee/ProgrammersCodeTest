def solution(participant, completion):
    hashmap = {}
    for parti in participant :
        hashmap[parti] = hashmap.get(parti, 0) + 1
        
    for complete in completion :
        hashmap[complete] -= 1
        
    for key, val in hashmap.items() :
        if val :
            return key