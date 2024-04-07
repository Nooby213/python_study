import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dnas = [input() for _ in range(n)]
s = ''
cnt = 0
for i in range(m):
    cnts = [0, 0, 0, 0]
    for j in range(n):
        if dnas[j][i] == 'A':
            cnts[0] += 1
        if dnas[j][i] == 'C':
            cnts[1] += 1
        if dnas[j][i] == 'G':
            cnts[2] += 1
        if dnas[j][i] == 'T':
            cnts[3] += 1
    mini = cnts.index(max(cnts))
    if mini == 0:
        s += 'A'
    if mini == 1:
        s += 'C'
    if mini == 2:
        s += 'G'
    if mini == 3:
        s += 'T'
    cnt += n - max(cnts)

print(s)
print(cnt)