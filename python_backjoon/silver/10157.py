# 우 하 좌 상 순서
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# 가로 C * 세로 R
# 5 ≤ C, R ≤ 1,000
C, R = map(int, input().split())
# 대기번호 K, 1 ≤ K ≤ 100,000,000
K = int(input())
# 90도 회전
seats = [[0] * R for _ in range(C)]
wait = 1
i, j = 0, 0
# 대기번호가 관객석수보다 많으면
if K <= C * R:
    while wait < K:
        seats[i][j] = wait
        for n in range(4):
            ni = i + di[n]
            nj = j + dj[n]
            while 0 <= ni < C and 0 <= nj < R and seats[ni][nj] == 0 and wait < K:
                wait += 1
                seats[ni][nj] = wait
                i = ni
                j = nj
                ni = i + di[n]
                nj = j + dj[n]
    # 인덱스 + 1
    print(i + 1, j + 1)
# 자리 없으면
else:
    print(0)
