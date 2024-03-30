import sys
input = sys.stdin.readline
# 못듣 N
# 못보 M
N, M = map(int, input().split())
N_st = {input().rstrip() for _ in range(N)}
M_st = {input().rstrip() for _ in range(M)}
NM_st = sorted(list(N_st & M_st))
print(len(NM_st))
for i in range(len(NM_st)):
    print(NM_st[i])