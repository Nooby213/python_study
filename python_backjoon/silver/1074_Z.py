# 1 ≤ N ≤ 15, 0 ≤ r, c < 2^N
# N이 주어졌을 때, r행 c열을 몇 번째로 방문
N, r, c = map(int, input().split())
result = 0
while N > 1:
    # 2 사분면
    if r < 2 ** (N - 1) and c < 2 ** (N - 1):
        N -= 1
    # 1 사분면
    elif r < 2 ** (N - 1) and c >= 2 ** (N - 1):
        c -= 2 ** (N - 1)
        result += (2 ** (N - 1)) ** 2
        N -= 1
    # 3 사분면
    elif r >= 2 ** (N - 1) and c < 2 ** (N - 1):
        r -= 2 ** (N - 1)
        result += (2 ** (N - 1)) ** 2 * 2
        N -= 1
    # 4 사분면
    elif r >= 2 ** (N - 1) and c >= 2 ** (N - 1):
        r -= 2 ** (N - 1)
        c -= 2 ** (N - 1)
        result += (2 ** (N - 1)) ** 2 * 3
        N -= 1
else:
    if r == 0 and c == 0:
        print(result)
    if r == 0 and c == 1:
        print(result + 1)
    if r == 1 and c == 0:
        print(result + 2)
    if r == 1 and c == 1:
        print(result + 3)
