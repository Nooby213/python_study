# 가로 세로 100
# 가로 세로 10 색종이
# 색종이 넓이

# 색종이 수 N <= 100
N = int(input())
# 도화지를 벗어나지 않는다.
paper = [tuple(map(int, input().split())) for _ in range(N)]

area = [[0] * 100 for _ in range(100)]
cnt = 0
for i in range(N):
    x, y = paper[i]
    for j in range(10):
        for k in range(10):
            if area[y + j][x + k] == 0:
                cnt += 1
                area[y + j][x + k] = 1

print(cnt)

