import sys

sys.stdin = open('input.txt')


def go(now, cnt, battery):
    print("이동",now, battery)
    next = 0
    max_go = 0
    for i in range(1, battery):
        print(cnt, now + battery + stations[now + i] - i)
        if now + battery + stations[now + i] - i >= N - 1:
            return cnt + 1

        # if max_go >
    print("go", max_go)
    go(now + max_go, cnt + 1, battery - max_go + stations[now + max_go])

# 최소한의 교체횟수
# 1 <= T <= 50
T = int(input())
for t in range(1, T + 1):
    # N개의 정류장, 3 <= N <= 100
    N, *stations = list(map(int, input().split()))
    # 처음 배터리는 첫 충전소 배터리 용량
    s_battery = stations[0]
    # print(N, stations)
    print(f'#{t} {go(0, 0, s_battery)}')
