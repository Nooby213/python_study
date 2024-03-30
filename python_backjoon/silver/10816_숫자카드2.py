# N개 숫자 카드 중 M 개의 정수 몇 개 포함?
# 1 ≤ N ≤ 500,000
N = int(input())
# -10,000,000 <= Ni <= 10,000,000
N_lst = list(map(int, input().split()))
N_dict = {i: 0 for i in N_lst}
# 1 ≤ M ≤ 500,000
M = int(input())
# -10,000,000 <= Mi <= 10,000,000
M_lst = list(map(int, input().split()))

for i in N_lst:
    N_dict[i] += 1

for i in M_lst:
    if i in N_dict:
        print(N_dict[i], end=' ')
    else:
        print(0, end=' ')
