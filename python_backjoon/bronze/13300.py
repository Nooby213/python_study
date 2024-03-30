# 남 남 여 여 같은 학년끼리
# 최대 인원 K
# 최소 방의 개수
# 1 ≤ N ≤ 1,000
N, K = map(int, input().split())
# 학년별 남, 녀 딕셔너리 만들어줌
students = {i: [0, 0] for i in range(1, 7)}
# 방 개수
cnt = 0
# 학년별 남, 녀 수 입력
for n in range(N):
    # S : 0 여 / 1 남, 1 ≤ Y ≤ 6
    S, Y = map(int, input().split())
    students[Y][S] += 1
# 방 개수 파악
for s in students:
    cnt += (students[s][0] // K)
    cnt += (students[s][1] // K)
    if students[s][0] % K:
        cnt += 1
    if students[s][1] % K:
        cnt += 1
print(cnt)
