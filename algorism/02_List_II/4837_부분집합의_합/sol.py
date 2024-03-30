import sys
sys.stdin = open('input.txt')

T = int(input())
A = [i for i in range(1, 13)]
L = len(A)
# print(A)

for t in range(1, T + 1):
    N, K = map(int, input().split()) # N : 부분 집합의 원소 갯수, K : 부분 집합의 합
    K_count = 0
    for n in range(1 << L):
        part = []   # 부분 집합
        for i in range(L): # 부분 집합 구하기
            if n & (1 << i):
                part.append(A[i])

                # 부분 집합 갯수가 N을 초과하거나 합이 K를 초과 했을 때
            if len(part) > N or sum(part) > K:
                break

        if len(part) == N and sum(part) == K:  # 합이 K 라면 카운트 + 1
            K_count += 1
        # print(part)
    print(f'#{t} {K_count}')