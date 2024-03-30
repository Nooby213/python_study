import sys

sys.stdin = open('input.txt')
di = [1, 0]  # 아래
dj = [0, 1]  # 오른쪽
from collections import deque


def find_mini(i, j):
    global mini
    q = deque([(i, j)])
    visited[i][j] = arr[i][j]
    while q:
        ni, nj = q.popleft()
        # 오른쪽/ 아래 탐색
        for k in range(2):
            nni = ni + di[k]
            nnj = nj + dj[k]
            if nni < N and nnj < N:
                # 첫 방문시 점수 기록
                if visited[nni][nnj] == 0:
                    visited[nni][nnj] = visited[ni][nj] + arr[nni][nnj]
                    q.append((nni, nnj))
                # 첫 방문 아닐 시 최솟값일 경우만 append
                else:
                    visited[nni][nnj] = min(visited[nni][nnj], visited[ni][nj] + arr[nni][nnj])
                    if visited[nni][nnj] == visited[ni][nj] + arr[nni][nnj]:
                        q.append((nni, nnj))


T = int(input())

for t in range(1, T + 1):
    # N * N 배열, 3 <= N <= 13
    N = int(input())
    # 1 <= arr[i][j] <= 9
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 점수판
    visited = [[0] * N for _ in range(N)]
    find_mini(0, 0)
    print(f'#{t} {visited[N - 1][N - 1]}')
