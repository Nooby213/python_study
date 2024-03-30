# counts 배열에 기록하기
N = 6
K = 9   # 0 ~ k
data = [7, 2, 4, 5, 1, 3] # 0 ~ 9 , K = 9
counts = [0] * (K+1)
temp = [0] * N  # 정렬된 결과 저장
for x in data:
    counts[x] += 1
# counts 누접합 구하기
for i in range(1, K+1):
    counts[i] += counts[i-1]

# data의 마지막 원소부터 정렬하기
for i in range(N-1, -1, -1): # N-1 > 0번 인덱스
    counts[data[i]] -= 1
    temp[counts[data[i]]] = data[i]
print(*temp)