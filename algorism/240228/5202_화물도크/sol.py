import sys

sys.stdin = open('input.txt')
work = []


def doke(i, last_end):
    global max_work
    if i == N:
        max_work = max(max_work, len(work))
        return

    # 작업을 할 수 있다면
    if worksheets[i][0] >= last_end:
        work.append(worksheets[i][1])
        doke(i + 1, worksheets[i][1])
        work.pop()

    # 작업 못하면
    doke(i + 1, last_end)


# 최대 몇 대의 화물차가 도크 가능한지

T = int(input())
# 1 <= T <= 50
for t in range(1, T + 1):
    # 신청서 N, 1 <= N <= 100
    N = int(input())
    # 작업 시작 s, 종료 e, 0<=s<24, 0 ＜ e ＜= 24
    # worksheets = sorted(worksheets, key=lambda x: x[0])
    worksheets = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: x[0])

    max_work = 0
    doke(0, 0)
    print(f'#{t} {max_work}')
