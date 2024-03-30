# 1 <= L, H <= 1000
# 기둥 폭 1m
# 수평은 기둥 끝 - 기둥 시작

N = int(input())  # N 개 막대 기둥 1 <= N <= 1000
col_lst = [list(map(int, input().split())) for _ in range(N)]
col_sorted = sorted(col_lst, key=lambda x: x[0])  # 순서 별로 정렬

idx_highest_col = 0  # 최고 높은 기둥 인덱스
highest_col = 0  # 최고 높은 기둥 높이

for i in range(N):
    if col_sorted[i][1] > highest_col:
        highest_col = col_sorted[i][1]
        idx_highest_col = i


area = highest_col

# 최고층 기둥의 위치 전까지
mx_col = 0
for i in range(idx_highest_col):
    if col_sorted[i][1] > mx_col:
        mx_col = col_sorted[i][1]
    area += mx_col * (col_sorted[i + 1][0] - col_sorted[i][0])

# 뒤에서 최고층 기둥 앞까지
mx_col = 0
for i in range(N - 1, idx_highest_col, -1):
    if col_sorted[i][1] > mx_col:
        mx_col = col_sorted[i][1]
    area += mx_col * (col_sorted[i][0] - col_sorted[i - 1][0])

print(area)
