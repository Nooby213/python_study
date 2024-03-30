# 연속적인 며칠 동안의 온도 합이 가장 큰 값
# 2 <= N <= 100000, 1 <= K <= N
N, K = map(int, input().split())
temp_lst = list(map(int, input().split()))
mx = memo = sum(temp_lst[:K])
min = 0

for t in range(1, N - K + 1):
    memo += (temp_lst[t + K - 1] - temp_lst[t - 1])
    if memo > mx:
        mx = memo

if min < 0:
    print(min)
else:
    print(mx)