import math

def solution(fees, records):
    intime = {}     # 키 : 차량 번호, 값 : 입차 시간
    result = {}     # 키 : 차량 번호, 값 : 누적 주차 시간

    # 입차 기록 "IN"을 만나면 intime에 차량 번호와 입차를 저장
    # 출차 기록 "OUT"을 만나면 해당 차량의 입차 시간을 intime에서 찾아
    # 출차 시간과의 차이를 계산하여 result에 더한다.
    # 그리고 intime에서 해당 차량 번호를 삭제
    for r in records:
        time, num, inout = r.split()
        if inout == "IN":
            intime[num] = convert(time)
            if num not in result:
                result[num] = 0

        else:
            result[num] += convert(time) - intime[num]
            del intime[num]

    # 모든 기록을 처리한 후, 아직 intime에 남아있는 차량들은
    # 23:59에 출차한 것으로 간주하고 마지막 주차 시간을 계산
    for key, val in intime.items():
        result[key] += 23 * 60 + 59 - val

    # result에 저장된 각 차량의 누적 주차 시간을 기준으로 요금 계산
    # 기본 시간 이하면 기본 요금을, 그 이상이면 기본 요금에 추가 요금을 계산하여
    # answer 리스트에 추가

    answer = []
    for key, val in sorted(result.items()):
        if val <= fees[0]:
            answer.append(fees[1])
        else:
            # 추가 요금을 계산할 때 math.ceil함수를 사용하여 올림 처리를 함으로써,
            # 단위 시간으로 나누어 떨어지지 않을 때 추가 단위 요금을 더 부과한다.
            answer.append(fees[1] + math.ceil((val - fees[0]) / fees[2]) * fees[3])

    return answer

def convert(time):  # 시간을 HH:MM 형태의 문자열로부터 전체 분으로 변환
    hh, mm = time.split(':')
    return int(hh) * 60 + int(mm)