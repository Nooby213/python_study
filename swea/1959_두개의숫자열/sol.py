import sys

sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T + 1):
    # N 개의 숫자로 구성된 숫자열 Ai
    # M 개의 숫자로 구성된 숫자열 Bi
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bi = list(map(int, input().split()))
    if N == M:
        max_sum = sum(Ai) + sum(Bi)
    elif N > M:
        Ai_sum = sum(Ai)
        Bi_sum = sum(Bi[:N])
        max_sum = Ai_sum + Bi_sum
        for i in range(1, M - N):
            temp_sum = max_sum + Bi[i + N - 1] - Bi[i - 1]
            if temp_sum > max_sum:
                max_sum = temp_sum
    else:
        Ai_sum = sum(Ai[:M])
        Bi_sum = sum(Bi)
        max_sum = Ai_sum + Bi_sum
        for i in range(1, N - M):
            temp_sum = max_sum + Ai[i + M - 1] - Ai[i - 1]
            if temp_sum > max_sum:
                max_sum = temp_sum
    print(f'#{t} {max_sum}')