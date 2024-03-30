N = int(input())
papers = [list(map(int, input().split())) for _ in range(N)]
board = [[-1] * 1001 for _ in range(1001)]
cnt_lst = []
for i in range(N - 1, -1, -1):
    x, y, dx, dy = papers[i]
    cnt = 0
    for j in range(dy):
        for k in range(dx):
            if board[y + j][x + k] == -1:
                board[y + j][x + k] = i
                cnt += 1
    cnt_lst.append(cnt)
for i in range(N):
    print(cnt_lst.pop())
