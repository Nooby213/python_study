import sys
input = sys.stdin.readline
def make_comb(i, comb):
    if len(comb) == 3:
        comb_set.add(comb)
    for j in range(i, n + 1):
        if str(j) not in comb and j > int(comb[-1]):
            for k in comb:
                if j in nocomb_lst[int(k)]:
                    break
            else:
                make_comb(i + 1, comb + str(j))

n, m = map(int, input().split())
nocomb_lst = [[] for _ in range(n + 1)]
comb_set = set()
for _ in range(m):
    s, e = map(int, input().split())
    nocomb_lst[s].append(e)
    nocomb_lst[e].append(s)

for i in range(1, n + 1):
    make_comb(i, str(i))

print(len(comb_set))