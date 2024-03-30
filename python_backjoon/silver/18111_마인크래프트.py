# B개의 블록 인벤토리
# 블록을 제거하여 인벤토리 넣기 2초
# 블록을 꺼내어 블록 위에 놓는다 1초
# N * M 집터
# 1 ≤ M, N ≤ 500, 0 ≤ B ≤ 6.4 × 10^7
N, M, B = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(N)]
min_time = 1e9
highest = 0
# 시간이 같다면 높은 땅이 출력
for i in range(257):
    need_B = 0
    get_B = 0
    time = 0
    for j in range(N):
        for k in range(M):
            if land[j][k] > i:
                time += (land[j][k] - i) * 2
                get_B += land[j][k] - i
            else:
                time += i - land[j][k]
                get_B -= i - land[j][k]
    # 필요한 돌보다 가진 돌이 더 많아야된다.
    if need_B > get_B + B:
        break
    # 시간이 같거나 적다면 높이 변경
    if time <= min_time:
        min_time = time
        highest = i

print(min_time, highest)
