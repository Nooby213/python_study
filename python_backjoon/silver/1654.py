import sys

input = sys.stdin.readline

# N개의 랜선 만든다.
# K선 가지고 있다.
# K 개의 랜선으로 N개의 같은 길이
# 1 <= K <= 10 000
# 1 <= N <= 10 000 00
# k <= N
# length : min = 1, max = (2 ** 31) - 1 # 이진탐색으로 늘려간다

K, N = map(int, input().split())
line = [int(input()) for i in range(K)]
# print(line)

# 이진 탐색
def length(line, start, end):
    global N
    if start > end:
        return end
    mid = (start + end) // 2

    cnt = 0 # mid 길이로 잘랐을 때 나오는 줄의 갯수
    for l in line:
        cnt += (l // mid)

    if cnt >= N:  # 갯수보다 많으면 자르는 크기를 늘려도 된다
        return length(line, mid + 1, end)

    elif cnt < N:   # 갯수보다 적으면 자르는 크기 줄여야 된다.
        return length(line, start, mid - 1)


result = length(line, 1, max(line))
# print(max(mid_lst))
print(result)


# # 완전 탐색
# n = sum(line) // N
# # print(n)
# cnt = N - 1
# while cnt < N:
#     cnt = 0
#     for l in line:
#         cnt += (l // n)
#
#     if cnt >= N:
#         print(n + 1)
#         break
#     else:
#         n -= 1
