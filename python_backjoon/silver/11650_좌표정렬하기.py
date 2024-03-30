import sys
input = sys.stdin.readline
# N 개의 점, 1 ≤ N ≤ 100,000
N = int(input())
# i 번 점의 위치 xi, yi, -100,000 ≤ xi, yi ≤ 100,000
spots = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: (x[0], x[1]))
for i in spots:
    print(*i)

