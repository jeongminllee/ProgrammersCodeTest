def solution(price):
    answer = 0
    if price >= 100000 and price < 300000:
        return int(price * 0.95)
    elif price >= 300000 and price < 500000:
        return int(price * 0.90)
    elif price >= 500000 :
        return int(price * 0.80)
    else :
        return price
    


def solution(price):
    discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
    for discount_price, discount_rate in discount_rates.items():
        if price >= discount_price:
            return int(price * discount_rate)    