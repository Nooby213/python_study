import sys
input = sys.stdin.readline
# 오름차순 정렬
# 1 ≤ N ≤ 1,000,000
N = int(input())
n_lst = [int(input()) for _ in range(N)]
n_lst.sort()
for i in n_lst:
    print(i)