import sys

sys.stdin = open('input.txt')
# 수강생 N명, 2 ≤ N ≤ 100
# 제출 안 한 사람 오름차순으로 정렬
# 제출한 사람 K, 1 ≤ K ≤ N
T = int(input())
for t in range(1, T + 1):
    # # 수강생 N명, 2 ≤ N ≤ 100, 제출한 사람 K, 1 ≤ K ≤ N
    N, K = map(int, input().split())
    submits = list(map(int, input().split()))
    print(f'#{t}', end=' ')
    for i in range(1, N + 1):
        if i in submits:
            continue
        else:
            print(i, end=' ')
    print()
