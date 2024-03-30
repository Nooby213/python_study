# D[1] = A
# D[n] = D[n-1]의 각 자리의 숫자를 P번 곱한 수들의 합
A, P = map(str, input().split())
P = int(P)

alist = []
while A not in alist:   # 같은 숫자가 나올 때까지 반복
    alist.append(A)
    B = 0
    for a in A:
        B += int(a) ** P
    A = str(B)

print(alist.index(str(B)))  # 같은 숫자가 나온 자리의 index가 남은 갯수
