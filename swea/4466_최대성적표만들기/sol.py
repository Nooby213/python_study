import sys

sys.stdin = open('input.txt')
T = int(input())
for t in range(1, T + 1):
    # N개의 과목 중 K개의 과목, 1 ≤ K ≤ N ≤ 100
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))
    scores.sort()
    i = 0
    max_sum = 0
    while scores and i < K:
        max_sum += scores.pop()
        i += 1
    print(f'#{t} {max_sum}')
