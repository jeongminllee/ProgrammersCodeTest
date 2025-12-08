import sys

def main():
    total_cents = 0

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue  # 혹시 빈 줄이 있으면 건너뛴다

        euros, cents = line.split(".")  # 항상 소수점 아래 두 자리라고 문제에서 보장
        value = int(euros) * 100 + int(cents)
        total_cents += value

    # 다시 "XXXX.YY" 형식으로 출력
    euros = total_cents // 100
    cents = total_cents % 100
    print(f"{euros}.{cents:02d}")

if __name__ == "__main__":
    main()
