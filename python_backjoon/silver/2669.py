# 1 <= x, y <= 100
board = [[0] * 101 for _ in range(101)]
area = 0
for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(y2 - y1):
        for k in range(x2 - x1):
            if board[y1 + j][x1 + k] == 0:
                board[y1 + j][x1 + k] = 1
                area += 1
print(area)