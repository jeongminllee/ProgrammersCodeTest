import math

def solution(numer1, denom1, numer2, denom2):
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    
    gcd_value = math.gcd(denom, numer)
    
    return [int(numer / gcd_value), int(denom / gcd_value)]


def solution(denum1, num1, denum2, num2):
    answer = []
    s = 0

    denum0 = (denum1*num2) +(denum2*num1)
    num0 = num1*num2

    for i in range(min(denum0,num0),0,-1):
        if denum0%i == 0 and num0%i == 0:
            s = i
            break

    denum0 /= s
    num0 /= s
    answer.append(denum0)
    answer.append(num0)

    return answer