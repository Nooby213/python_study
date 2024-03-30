import math
N = int(input())
num_lst = list(map(int, input().split()))
cnt = 0
for i in num_lst:   # 어차피 1은 소수 아님
    if i == 1:  # 1은 소수아님
        continue

    if i == 2 or i == 3:    # 2나 3은 제곱근이 2보다 작은 소수
        cnt += 1

    else:
        for j in range(2, int(math.sqrt(i)) + 1):   # 제곱근을 기준으로 반복한다
            if i % j == 0:
                break
        else:
            cnt += 1

print(cnt)