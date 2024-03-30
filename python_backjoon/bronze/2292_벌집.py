# 1 ≤ N ≤ 1,000,000,000
# 1 7 19 37 61
#  6 12 18 24
N = int(input())
n = 1
i = 1
while n < N:
    n += i * 6
    i += 1
else:
    print(i)