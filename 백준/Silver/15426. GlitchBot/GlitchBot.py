class RobotState :
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = 0  # 0 : 북, 1 : 동, 2 : 남, 3 : 서

    def execute(self, instruction):
        if instruction == 'Left' :
            self.direction = (self.direction - 1) % 4
        elif instruction == 'Right' :
            self.direction = (self.direction + 1) % 4
        else :
            if self.direction == 0 :    # 북
                self.y += 1
            elif self.direction == 1 :  # 동
                self.x += 1
            elif self.direction == 2 :  # 남
                self.y -= 1
            else :                      # 서
                self.x -= 1

def simulate_path(instructions) :
    robot = RobotState()
    for instruction in instructions :
        robot.execute(instruction)
    return robot.x, robot.y

def find_correction(target_x, target_y, instructions):
    possible_instructions = ["Left", "Right", "Forward"]

    # 각 라인에 대해 다른 명령어로 교체
    for line in range(len(instructions)) :
        original = instructions[line]

        for new_instruction in possible_instructions :
            if new_instruction == original :
                continue

            # 명령어를 교체한 새로운 리스트로 시뮬레이션
            modified = instructions.copy()
            modified[line] = new_instruction

            final_x, final_y = simulate_path(modified)
            if (final_x, final_y) == (target_x, target_y) :
                return line + 1, new_instruction    # 라인 번호는 1부터 시작

    return None


def main() :
    # 입력
    target_x, target_y = map(int, input().split())
    n = int(input())
    instructions = [input() for _ in range(n)]

    result = find_correction(target_x, target_y, instructions)

    print(*result)
    
main()