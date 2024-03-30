import sys

input = sys.stdin.readline

# +1 / +2, 연속된 계단 3개 못밟음, 마지막 계단 무조건 밟아야됨
# 계단 수 N, 1 <= N <= 300
N = int(input().rstrip())

# 점수 <= 10,000, 계단 별 점수
stairs = [int(input().rstrip()) for _ in range(N)]
stairs.insert(0, 0)
# 계단 올랐을 때 점수
score = [0] * (N + 1)

# 계단 1개이상 일때
if N >= 1:
    score[1] = stairs[1]

# 계단 2개 일때
if N >= 2:
    score[2] = stairs[1] + stairs[2]

# 계단 3개 이상일 때
if N >= 3:
    score[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

    for i in range(4, N + 1):
        score[i] = max(score[i - 3] + stairs[i - 1] + stairs[i], score[i - 2] + stairs[i])

print(score[N])
