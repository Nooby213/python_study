import sys
sys.stdin = open('input.txt')
T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    for i in range(N):
        if not M & 1 << i:
            print(f'#{t} OFF')
            break
    else:
        print(f'#{t} ON')
