from collections import deque
def ripe():
    q = deque(ripened)
    cnt = 0
    while q:
        y, x, cnt = q.popleft()
        h = y // N
        for k in range(4):
            ny = y + di[k]
            nx = x + dj[k]
            if N*h <= ny < N*(h+1) and 0 <= nx < M and tomatoes[ny][nx] == 0:
                tomatoes[ny][nx] = 1
                q.append((ny, nx, cnt + 1))
        if h - 1 >= 0 and tomatoes[y - N][x] == 0:
            tomatoes[y - N][x] = 1
            q.append((y - N, x, cnt + 1))
        if h + 1 < H and tomatoes[y + N][x] == 0:
            tomatoes[y + N][x] = 1
            q.append((y + N, x, cnt + 1))
    else:
        return cnt

def check():
    for i in range(N * H):
        for j in range(M):
            if tomatoes[i][j] == 0:
                return False
    return True
# 가로 M, 세로 N, 높이 H
# 2 ≤ M ≤ 100, 2 ≤ N ≤ 100, 1 ≤ H ≤ 100
M, N, H = map(int, input().split())
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
tomatoes = [list(map(int, input().split())) for _ in range(N*H)]
ripened = []
unripe = 0
for i in range(N*H):
    for j in range(M):
        if tomatoes[i][j] == 1:
            ripened.append((i, j ,0))
        if tomatoes[i][j] == 0:
            unripe += 1

if unripe == 0:
    print(0)
else:
    result = ripe()
    if check():
        print(result)
    else:
        print(-1)