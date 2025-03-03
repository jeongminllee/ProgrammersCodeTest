import sys
input = sys.stdin.readline

# 미리 정의된 ASCII art 패턴 : 0~9와 +
DIGITS = {
    '0' : [
        'xxxxx',
        'x...x',
        'x...x',
        'x...x',
        'x...x',
        'x...x',
        'xxxxx',
    ],
    '1' : [
        '....x',
        '....x',
        '....x',
        '....x',
        '....x',
        '....x',
        '....x',
    ],
    '2' : [
        'xxxxx',
        '....x',
        '....x',
        'xxxxx',
        'x....',
        'x....',
        'xxxxx',
    ],
    '3' : [
        'xxxxx' ,
        '....x' ,
        '....x' ,
        'xxxxx' ,
        '....x' ,
        '....x' ,
        'xxxxx' ,
    ],
    '4' : [
        'x...x',
        'x...x',
        'x...x',
        'xxxxx',
        '....x',
        '....x',
        '....x',
    ],
    '5' : [
        'xxxxx',
        'x....',
        'x....',
        'xxxxx',
        '....x',
        '....x',
        'xxxxx',
    ],
    '6' : [
        'xxxxx',
        'x....',
        'x....',
        'xxxxx',
        'x...x',
        'x...x',
        'xxxxx',
    ],
    '7' : [
        'xxxxx',
        '....x',
        '....x',
        '....x',
        '....x',
        '....x',
        '....x',
    ],
    '8' : [
        'xxxxx',
        'x...x',
        'x...x',
        'xxxxx',
        'x...x',
        'x...x',
        'xxxxx',
    ],
    '9' : [
        'xxxxx',
        'x...x',
        'x...x',
        'xxxxx',
        '....x',
        '....x',
        'xxxxx',
    ],
    '+' : [
        '.....',
        '..x..',
        '..x..',
        'xxxxx',
        '..x..',
        '..x..',
        '.....',
    ]
}

# 역으로 ASCII art에서 문자로 매핑하기 위한 딕셔너리 생성
ART_TO_CHAR = {tuple(art): char for char, art in DIGITS.items()}

def sol_11613() :
    # 7줄 입력 받기
    lines = [input().rstrip('\n') for _ in range(7)]
    n = len(lines[0])
    # 한 글자(숫자 또는 +)의 폭은 5, 글자 사이에는 1열의 점이 있음.
    # 전체 글자 수는 (n + 1) // 6
    num_chars = (n + 1) // 6

    expression = ''

    for i in range(num_chars) :
        # 각 문자 영역은 시작열 : i * 6, 끝열 : i * 6 + 5
        char_art = [line[i*6:i*6 + 5] for line in lines]
        # char_art를 튜플로 만들어 매핑 딕셔너리에서 문자 찾기
        ch = ART_TO_CHAR.get(tuple(char_art))
        if ch is None :
            # 알 수 없는 문자가 있을 경우 (문제 조건상 없으므로)
            ch = '?'
        expression += ch

    # expression은 'a+b' 형태
    a_str, b_str = expression.split('+')
    res = str(int(a_str) + int(b_str))

    # 결과를 ASCII art로 변환
    res_art = [''] * 7
    for idx, digit in enumerate(res) :
        if idx > 0 :
            # 글자 사이에 한 열 점 추가
            for r in range(7) :
                res_art[r] += '.'
        digit_art = DIGITS[digit]
        for r in range(7) :
            res_art[r] += digit_art[r]

    # 결과 출력
    for line in res_art :
        print(line)

sol_11613()