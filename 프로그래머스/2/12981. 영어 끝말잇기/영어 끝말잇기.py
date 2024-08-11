def solution(n, words):
    # 순서 1, 2, 3, 1, 2, 3 으로 돌아가니까 
    # % 연산을 이용해서 len(words) % n 을 하면 순서가 나오고 
    # // 연산으로 차례를 return
    used_words = list()
    prev_word = words[0][0]
    
    for i, word in enumerate(words) :
        if word in used_words or word[0] != prev_word :
            return [(i % n) + 1, (i // n) + 1]
        
        used_words.append(word)
        prev_word = word[-1]
    
    return [0, 0]