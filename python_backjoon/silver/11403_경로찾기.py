import sys
input = sys.stdin.readline
def can_go(i, start):
    # 방문했다면 안 해도됌
    if visited[i]:
        return
    # 방문표시
    visited[i] = 1
    for j in range(N):
        if adj_lst[i][j]:
            # 가능 표시
            can[start][j] = 1
            can_go(j, start)

# 정점의 개수 N, 1 ≤ N ≤ 100
N = int(input())
# 인접 리스트
adj_lst = [list(map(int, input().split())) for _ in range(N)]
# 방문 기록
can = [[0] * N for _ in range(N)]
# N번 반복
for i in range(N):
    visited = [0] * N
    can_go(i, i)

for c in can:
    print(*c)