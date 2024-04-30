from itertools import product

def solution(users, emoticons):
    answer = []
    # 이모티콘마다 할인율은 다를 수 있으며, 할인율은 10, 20, 30, 40 % 중 하나로 설정됩니다.
    discounts = list(product([10, 20, 30, 40], repeat = len(emoticons)))
    # [(10, 10), (10, 20), (10, 30), (10, 40),
    #  (20, 10), (20, 20), (20, 30), (20, 40),
    #  (30, 10), (30, 20), (30, 30), (30, 40),
    #  (40, 10), (40, 20), (40, 30), (40, 40)]

    for discount in discounts :
        local_subscriber = 0    # 이모티콘 플러스 서비스 가입자 수
        local_sell = 0          # 이모티콘 구입의 총합

        for user in users :
            local_user_subscriber = False       # 이모티콘 플러스 서비스 가입 여부
            local_user_sell = 0                 # 구매한 이모티콘의 가격
            user_dis, user_sell_limit = user    # 할인율 이하이면 이모티콘을 구힙하는 할인율, 구입가능한 최대 이모티콘 가격의 합

            # 이모티콘의 할인율이 원하는 할인율의 이하라면, 할인된 가격으로 이모티콘을 구매하고 구매한 가격을 local_user_sell에 저장
            # 이모티콘을 구매한 가격의 합이 user_sell_limit의 이상이면, 해당 user는 이모티콘을 구매하지 않고, 이모티콘 플러스 서비스에 가입.
            # 이모티콘 플러스 서비스에 가입하면, 더 이상 이모티콘을 구매하지 않기 때문에, break로 루프를 나오게 된다.
            for idx in range(len(emoticons)) :
                emo_dis, emo_price = discount[idx], emoticons[idx]
                if user_dis <= emo_dis :
                    local_user_sell += (emo_price * (100 - emo_dis) // 100)

                if local_user_sell >= user_sell_limit :
                    local_user_subscriber = True
                    break

            # 이모티콘 플러스 서비스에 가입했다면, local_subscriber += 1
            # 아니라면, 구매한 이모티콘의 가격의 합을 local_sell에 더해준다.
            if local_user_subscriber :
                local_subscriber += 1
            else :
                local_sell += local_user_sell

        # 리스트 answer에 이모티콘 플러스 가입자 수와 이모티콘 판매 가격의 합을 append로 넣어준다.
        # 첫 루프라면 answer에 1개의 원소만 들어있기 때문에, sort의 의미가 없지만, 2번째 부터는 큰 값이 앞으로 오게 된다.
        answer.append([local_subscriber, local_sell])
        
    return max(answer)