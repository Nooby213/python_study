import sys
# input = sys.stdin.readline
import math

# <M:N> 마지막해
# 1 ≤ M, N ≤ 40,000, 1 ≤ x ≤ M, 1 ≤ y ≤ N
T = int(input())
for _ in range(T):
    M, N, X, Y = map(int, input().split())
    # 각 리스트는 M, N만큼 반복
    x_lst = [i for i in range(1, M + 1)]
    y_lst = [i for i in range(1, N + 1)]

    # 최소 공약수보다 작은 범위에서 M만큼 이동
    for i in range(X, math.lcm(M, N) + 1, M):
        if y_lst[i % N - 1] == Y:
            print(i)
            break
    else:
        print(-1)
