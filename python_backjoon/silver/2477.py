K = int(input())  # 1 m^2 당 참외 K개
# 동쪽 : 1, 서쪽 : 2, 남쪽 : 3, 북쪽 : 4
arnd = [list(map(int, input().split())) for _ in range(6)]  # 육각형
total = []
width = 0
width_idx = 0
height = 0
height_idx = 0
cnt4 = 0

for i in range(6):
    total.append(arnd[i][1])
    # 가로 기록
    if arnd[i][0] == 1 or arnd[i][0] == 2:
        if arnd[i][1] > width:
            width = arnd[i][1]
            width_idx = i
    # 세로 기록
    if arnd[i][0] == 3 or arnd[i][0] == 4:
        if arnd[i][1] > height:
            height = arnd[i][1]
            height_idx = i
        # 북쪽 횟수
        if arnd[i][0] == 4:
            cnt4 += 1

area = width * height

if cnt4 == 1:
    s_area = total[width_idx - 3] * total[height_idx - 3]
else:
    s_area = total[width_idx - 3] * total[height_idx - 3]

print((area - s_area) * K)
