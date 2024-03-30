from collections import deque
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
def check(i, j, color):
    q = deque([(i, j)])
    visited[i][j] = 1
    while q:
        i, j = q.popleft()
        # 4방향 탐색
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            # 범위 안에 있고, 색이 같고 방문한적 없다면
            if 0 <= ni < N and 0 <= nj < N and photo[ni][nj] in color and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                q.append((ni, nj))

def normal():
    cnt = 0
    # 순회하면서 방문한 곳이 아니라면 방문 후 구역나눈다.
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                check(i, j, photo[i][j])
                cnt += 1
    return cnt

def blind():
    cnt = 0
    # 순회하면서 방문한 곳이 아니라면 방문 후 구역나눈다.
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                # 적/녹 색이라면 같은 구역
                if photo[i][j] in 'RG':
                    check(i, j, 'RG')
                    cnt += 1
                else:
                    check(i, j, photo[i][j])
                    cnt += 1
    return cnt
# 1 ≤ N ≤ 100
N = int(input())
photo = [list(input().rstrip()) for _ in range(N)]
# 방문 기록 초기화
visited = [[0] * N for _ in range(N)]
print(normal(), end=' ')
# 방문 기록 초기화
visited = [[0] * N for _ in range(N)]
print(blind())