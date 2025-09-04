start = 100

N = int(input())    # 보려고 하는 채널
M = int(input())    # 고장난 버튼 개수
if M :
    broken = set(map(int, input().split()))
else :
    broken = set()

cnt = abs(start - N)

for nums in range(1000001) :
    nums = str(nums)

    for j in range(len(nums)) :
        if int(nums[j]) in broken :
            break
        elif j == len(nums) - 1 :
            cnt = min(cnt, abs(int(nums) - N) + len(nums))

print(cnt)