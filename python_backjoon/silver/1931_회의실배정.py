import sys
input = sys.stdin.readline

# 회의실 사용 최대 갯수
N = int(input().rstrip())
schedules = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: (x[1], x[0]))
cnt = 1
end = schedules[0][1]
for i in range(1, N):
    if schedules[i][0] >= end:
        cnt += 1
        end = schedules[i][1]
print(cnt)
