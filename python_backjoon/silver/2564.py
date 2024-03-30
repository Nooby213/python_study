# 가로 세로
width, height = map(int, input().split())

# 상점 개수 1 <= N <= 100
N = int(input())
# 북 1, 남 2, 서 3, 동 4 / 왼쪽 꼭지점에서의 거리
stores = [list(map(int, input().split())) for _ in range(N)]
# 동근이 위치
D_dirction, D_distance = map(int, input().split())
sum_of_distance = 0
for i in range(N):
    # 상점 위치
    direction, distance = stores[i]
    if D_dirction == 1:
        if direction == 1:
            sum_of_distance += abs(D_distance - distance)
        elif direction == 2:
            if D_distance + distance > width:
                sum_of_distance += (2 * width - D_distance - distance + height)
            else:
                sum_of_distance += (D_distance + distance + height)
        elif direction == 3:
            sum_of_distance += (D_distance + distance)
        elif direction == 4:
            sum_of_distance += (width - D_distance + distance)
    elif D_dirction == 2:
        # 북쪽
        if direction == 1:
            if D_distance + distance < width:
                sum_of_distance += (D_distance + distance + height)
            else:
                sum_of_distance += (2 * width - D_distance - distance + height)

        # 남쪽
        elif direction == 2:
            sum_of_distance += abs(D_distance - distance)

        # 서쪽
        elif direction == 3:
            sum_of_distance += (D_distance + (height - distance))

        # 동쪽
        elif direction == 4:
            sum_of_distance += ((width - D_distance) + (height - distance))
    elif D_dirction == 3:
        if direction == 1:
            sum_of_distance += (D_distance + distance)
        if direction == 2:
            sum_of_distance = ((height - D_distance) + distance)
        if direction == 3:
            sum_of_distance += abs(D_distance - distance)
        if direction == 4:
            if D_distance + distance > height:
                sum_of_distance += (width + 2 * height - D_distance - distance)
            else:
                sum_of_distance += (width + D_distance + distance)
    elif D_dirction == 4:
        if direction == 1:
            sum_of_distance += (D_distance + width - distance)
        if direction == 2:
            sum_of_distance += (height - D_distance + width - distance)
        if direction == 3:
            if D_distance + distance > height:
                sum_of_distance += (width + 2 * height - D_distance - distance)
            else:
                sum_of_distance += (width + D_distance + distance)
        if direction == 4:
            sum_of_distance += abs(D_distance - distance)

print(sum_of_distance)
