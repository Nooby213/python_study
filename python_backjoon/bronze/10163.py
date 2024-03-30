# 색종이의 장수를 나타내는 정수 N (1 ≤ N ≤ 100)
N = int(input())
# 가로 1001칸, 세로 최대 1001칸
board = [[-1] * 1001 for _ in range(1001)]
papers = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    x, y, width, height = papers[i]
    for j in range(width):
        for k in range(height):
            board[x + j][y + k] = i

n = 0
while n < N:
    cnt = 0
    for i in range(1001):
        for j in range(1001):
            if board[i][j] == n:
                cnt += 1
    print(cnt)
    n += 1
