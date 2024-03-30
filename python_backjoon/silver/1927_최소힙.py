import sys
input = sys.stdin.readline
from heapq import heappush, heappop
N = int(input())
heap = []
for _ in range(N):
    num = int(input().rstrip())
    if not num:
        if heap:
            print(heappop(heap))
        else:
            print(0)
    else:
        heappush(heap, num)
