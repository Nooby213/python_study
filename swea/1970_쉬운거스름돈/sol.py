import sys
sys.stdin = open('input.txt')

# 거스름돈 N, 10 ≤ N ≤ 1,000,000, 마지막 자릿수는 항상 0
# 피료한 돈의 종류과 개수

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    change = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    money = [0] * 8
    print(f'#{t}')
    for i in range(8):
        if N // change[i]:
            money[i] = N // change[i]
            N -= (N // change[i]) * change[i]
    else:
        print(*money)

