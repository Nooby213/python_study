import sys
input = sys.stdin.readline
# 오름차순
# N 개의 수, 1 ≤ N ≤ 10,000,000
# 10000 보다 작은 자연수
counting = [0] * 10001
N = int(input())
for _ in range(N):
    counting[int(input())] += 1
cnt = 0
for i in range(10001):
    if counting[i] != 0:
        for j in range(counting[i]):
            print(i)
            cnt += 1
    if cnt == N:
        break