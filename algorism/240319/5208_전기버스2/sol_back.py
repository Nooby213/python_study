import sys
sys.stdin = open('input.txt')

def go(now, cnt, b):
    global mini
    if cnt >= mini:
        return

    for i in range(1, b + 1):
        if now + i >= N - 1:
            mini = min(cnt, mini)
            return
        go(now + i, cnt + 1, stations[now + i])


T = int(input())
for t in range(1, T + 1):
    N, *stations = list(map(int, input().split()))
    battery = stations[0]
    # 초기 배터리 용량이 충분하면 모든 정류장을 방문할 수 있음
    if battery >= N:
        print(f'#{t} 0')
    else:
        mini = N
        go(0, 0, battery)
        print(f'#{t} {mini}')
