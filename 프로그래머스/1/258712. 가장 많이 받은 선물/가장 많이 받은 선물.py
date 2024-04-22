from collections import defaultdict
def solution(friends, gifts):
    answer = {}
    # 선물을 보낸 수, 선물을 받은 수
    sent_received = {}
    # 선물을 주고 받은 관계를 키로, 선물의 개수를 저장합니다
    sender_receiver = defaultdict(int)

    for f in friends :
        # 선물의 개수를 저장하기 위해 0, 0으로 초기화
        # 앞의 0이 선물을 보낸 수, 뒤에 0이 선물을 받은 수를 의미
        sent_received[f] = [0, 0]

        # 다음달에 친구들이 받을 선물을 저장할 변수
        answer[f] = 0

    for sr in gifts :
        # sender는 선물을 보낸 사람
        # receiver 는 선물을 받는 사람
        sender, receiver = sr.split(' ')
        # 선물을 보낸 사람에게, 보낸 선물 1 증가
        sent_received[sender][0] += 1
        # 선물 받은 사람에게, 받은 선물 1 증가
        sent_received[receiver][1] += 1

        # 선물을 주고 받은 관계에 선물의 개수 1 증가
        sender_receiver[(sender, receiver)] += 1

    # 이제 선물을 주고 받은 개수를 sent_received 딕셔너리에 모두 저장하였음.
    # 선물 지수를 계산
    for key in sent_received.keys() :
        # v 선물 지수는, 내가 보낸 선물 개수 - 내가 받은 선물 개수
        v = sent_received[key][0] - sent_received[key][1]
        # 이제 내가 보낸 선물 개수, 내가 받은 선물 개수와 함께 선물 지수도 함께 저장
        sent_received[key] = [sent_received[key][0], sent_received[key][1], v]

    # 이제 모든 친구들을 서로 비교해서, 다음 달에 받을 선물의 개수를 계산할 차례
    # 선물을 보낸 친구 sender
    for sender in friends :
        # 여기서 추가로 선물을 받을 개수를 저장할 변수를 선언
        not_receiver_present_idx = 0

        for receiver in friends :
            # 선물을 받은 친구는 receiver
            # 보낸 사람과 받은 사람이 같은 친구일 경우 skip
            if sender == receiver :
                continue

            # 두 사람이 선물을 주고 받은 기록이 있다면
            if ((sender, receiver) in sender_receiver.keys()\
                or (receiver, sender) in sender_receiver.keys()) :
                # 두 사람 사이에 더 많은 선물을 준 사람이 다음 달에 선물을 하나 더 받습니다.
                if sender_receiver[(sender, receiver)] > sender_receiver[(receiver, sender)] :
                    answer[sender] += 1
                # 주고 받은 수가 같다면,
                elif sender_receiver[(sender, receiver)] == sender_receiver[(receiver, sender)] :
                    # 선물 지수가 더 큰 사람이 선물을 하나 더 받습니다
                    if sent_received[sender][2] > sent_received[receiver][2] :
                        not_receiver_present_idx += 1

            # 두 사람이 선물을 주고 받은 기록이 하나도 없거나
            else :
                # 선물 지수가 큰 사람이 하나 받습니다.
                if sent_received[sender][2] > sent_received[receiver][2] :
                    not_receiver_present_idx += 1

        answer[sender] += not_receiver_present_idx

    # 이렇게 2중 루프를 모두 실행하고 나면, answer에 각 친구들 별로 다음달에 받을 선물 개수가 저장되어 있음.
    values = list(answer.values())
    
    return max(values)