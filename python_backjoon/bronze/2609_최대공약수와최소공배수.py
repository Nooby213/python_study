# 최대 공약수
# 최소 공배수
N, M = map(int, input().split())
for i in range(min(N, M), 0, -1):
    if N % i == 0 and M % i == 0:
        print(i)
        break
for i in range(min(N, M), N*M + 1, min(N, M)):
    if i % max(N, M) == 0:
        print(i)
        break