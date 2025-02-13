def sol_12172() :
    x, r, c = map(int, input().split())
    if x == 1 :
        return ('GABRIEL')
        
    elif x == 2 and r * c % x == 0 :
        return ('GABRIEL')
        
    elif x == 3 and r * c % x == 0 and (r >= 2 and c >= 2) :
        return ('GABRIEL')
    
    elif x == 4 and r * c % x == 0 and (r >= 3 and c >= 3) :
        return ('GABRIEL')
    
    else :
        return ('RICHARD')

T = int(input())
for t in range(1, T+1) :
    print(f"Case #{t}: {sol_12172()}")