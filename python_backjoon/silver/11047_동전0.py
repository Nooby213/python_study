# N종류 동전, 1 ≤ N ≤ 10
# 가치의 합 K, 1 ≤ K ≤ 100,000,000
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
cnt = 0
i = N - 1
while K > 0:
    # 잔 돈이 크면
    if coins[i] > K:
        i -= 1
    # 딱 맞게 나눠지면
    elif K % coins[i] == 0:
        cnt += K // coins[i]
        break
    # 아니라면 나누고 K는 남은 돈으로 갱신
    else:
        cnt += K // coins[i]
        K = K % coins[i]

print(cnt)