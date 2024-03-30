import sys

input = sys.stdin.readline
# 3으로 나누어 떨어지면, 3으로 나눈다.
# 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.

# N > 1, 연산 횟수 최소값 출력11
# 1 <= N <= 10^6
N = int(input())
memo = [0] * (N + 1)

for i in range(2, N + 1):
    memo[i] = memo[i - 1] + 1
    if i % 2 == 0:
        memo[i] = min(memo[i], memo[i // 2] + 1)
    if i % 3 == 0:
        memo[i] = min(memo[i], memo[i // 3] + 1)

print(memo[N])
