import sys
sys.stdin = open('input.txt')
# 8 방향 중 4 방향이상 탐색가능 지역
# 해당 지역보다 낮은 경우 탐색 가능

delta = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def find_area(y, x):
    cnt = 0
    for k in range(8):
        ny = y + delta[k][0]
        nx = x + delta[k][1]
        if 0 <= ny < N and 0 <= nx < M and area[ny][nx] < area[y][x]:
            cnt += 1
    return cnt


T = int(input())
for t in range(1, T + 1):
    # 구역 크기 N * M, 3 <= N, M <= 100
    N, M = map(int, input().split())
    # 0 <= Aij < 10
    area = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(M):
            can = find_area(i, j)
            if can >= 4:
                result += 1

    print(f'#{t} {result}')
