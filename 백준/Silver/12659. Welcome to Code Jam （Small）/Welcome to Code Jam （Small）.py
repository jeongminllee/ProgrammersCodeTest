def count_subsequences(text, pattern, text_pos=0, pattern_pos=0, memo=None) :
    '''
    Count the number of times parttern appears as a subsequence in text
    using dynamic programming with memoization
    '''
    if memo is None :
        memo = {}

    # Create a unique key for the current state
    key = (text_pos, pattern_pos)
    if key in memo :
        return memo[key]

    # Base cases
    if pattern_pos == len(pattern) :    # Found a complete match
        return 1
    if text_pos == len(text) :          # Reached end of text without complete match
        return 0

    # Count matches including and excluding current character
    cnt = 0

    # If current character match, we can either use it or skip it
    if text[text_pos] == pattern[pattern_pos] :
        cnt += count_subsequences(text, pattern, text_pos+1, pattern_pos+1, memo)

    # We can always skip the current character in text
    cnt += count_subsequences(text, pattern, text_pos+1, pattern_pos, memo)

    # Store result in memo befor returning
    memo[key] = cnt % 10000         # keep only last 4 digits
    return memo[key]

def solve_case(text) :
    pattern = "welcome to code jam"
    return str(count_subsequences(text, pattern)).zfill(4)

T = int(input())

for case in range(1, T + 1) :
    text = input()
    res = solve_case(text)
    print(f"Case #{case}: {res}")