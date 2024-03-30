# 가능한 채널인지 확인
def possible(channel):
    for c in str(channel):
        if int(c) in broken:
            return False
    else:
        return True


# 현재 채널 100 > 채널 N으로 이동, 0 ≤ N ≤ 500,000
N = input()
# # 고장난 버튼 M개, 0 ≤ M ≤ 10
M = int(input())
if M:
    broken = list(map(int, input().split()))
else:
    broken = []

min_press = abs(int(N) - 100)

# 모든 채널 확인
for channel in range(1000001):
    if broken and possible(channel):
        min_press = min(min_press, abs(channel - int(N)) + len(str(channel)))
    if not broken:
        min_press = min(min_press, abs(channel - int(N)) + len(str(channel)))
    if min_press == 0:
        break

print(min_press)