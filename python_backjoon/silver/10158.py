dcross = [(1, 1), (-1, 1), (-1, -1), (1, -1)]
# 세로 h 가로 w 2 ≤ w,h ≤ 40,000
H, W = map(int, input().split())
# 0 < x < w과 0 < y < h
y, x = map(int, input().split())
# 1 ≤ t ≤ 200,000,000
t = int(input())
# 제자리로 돌아오는 시간
return_t = 0
route = [(y, x)]
visited = [[0] * W for _ in range(H)]
cnt = 0
# 직사각형이면 (H * W) t만에 한 바퀴 돈다
if H != W:
    while cnt < H * W or cnt < t:
        for i in range(4):
            ny = y + dcross[i][0]
            nx = x + dcross[i][1]
            while 0 <= ny <= H and 0 <= nx <= W:
                if len(route) > 1 and route[-2] == (ny, nx):
                    if 0 <= y + dcross[i - 1][0] <= H and 0 <= x + dcross[i - 1][1] <= W:
                        break
                    elif 0 <= y + dcross[i - 2][0] <= H and 0 <= x + dcross[i - 2][1] <= W:
                        break
                    elif 0 <= y + dcross[i - 3][0] <= H and 0 <= x + dcross[i - 3][1] <= W:
                        break
                    else:
                        y = ny
                        x = nx
                        route.append((ny, nx))
                        cnt += 1
                else:
                    y = ny
                    x = nx
                    route.append((ny, nx))
                    cnt += 1
                if cnt >= H * W or cnt >= t:
                    break
                ny = ny + dcross[i][0]
                nx = nx + dcross[i][1]
        if cnt >= H * W or cnt >= t:
            break
    print(*route[t % (H * W)])
# 정사각형이면 (H + W) t만에 한 바퀴 돈다.
elif H == W:
    while cnt < (H + W):
        for i in range(4):
            ny = y + dcross[i][0]
            nx = x + dcross[i][1]
            while 0 <= ny <= H and 0 <= nx <= W:
                if len(route) > 1 and route[-2] == (ny, nx):
                    if 0 <= y + dcross[i - 1][0] <= H and 0 <= x + dcross[i - 1][1] <= W:
                        break
                    elif 0 <= y + dcross[i - 2][0] <= H and 0 <= x + dcross[i - 2][1] <= W:
                        break
                    elif 0 <= y + dcross[i - 3][0] <= H and 0 <= x + dcross[i - 3][1] <= W:
                        break
                    else:
                        y = ny
                        x = nx
                        route.append((ny, nx))
                        cnt += 1
                else:
                    y = ny
                    x = nx
                    route.append((ny, nx))
                    cnt += 1
                if cnt >= (H + W) or cnt >= t:
                    break
                ny = ny + dcross[i][0]
                nx = nx + dcross[i][1]
        if cnt >= (H + W) or cnt >= t:
            break
    print(*route[t % (H + W)])
