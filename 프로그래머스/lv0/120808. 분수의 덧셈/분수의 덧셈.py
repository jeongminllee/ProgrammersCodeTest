import math

def solution(numer1, denom1, numer2, denom2):
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    
    gcd_value = math.gcd(denom, numer)
    
    return [int(numer / gcd_value), int(denom / gcd_value)]