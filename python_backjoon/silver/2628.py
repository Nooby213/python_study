# 가로 세로 길이
width, height = map(int, input().split())
# 자르는 횟수
N = int(input())

# 가로 0, 세로 1
cut = [[] for _ in range(2)]
# 방향별 위치 저장
for _ in range(N):
    direction, num = map(int, input().split())
    cut[direction].append(num)

max_width = max_height = 0

# 방향별 자르는 위치 정렬 후 최대 길이 저장
for i in range(2):
    if cut[i]:
        cut[i].sort()
        max_diff = 0
        # 앞, 뒤 나머지 길이 비교
        if i == 0:
            max_diff = max(cut[i][0], height - cut[i][-1])
        elif i:
            max_diff = max(cut[i][0], width - cut[i][-1])
        # 자른 종이 길이 비교
        for j in range(1, len(cut[i])):
            max_diff = max(max_diff, cut[i][j] - cut[i][j - 1])

        if i == 0:
            max_height = max_diff
        else:
            max_width = max_diff

# 나머지 종이와 최대 길이 비교
max_height = max(max_height, height - cut[0][-1] if cut[0] else height)
max_width = max(max_width, width - cut[1][-1] if cut[1] else width)

area = max_width * max_height
print(area)
