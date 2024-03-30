comb = []
cnt = 0
def roll(n):
    global cnt
    if n == 3:
        cnt += 1
        # print(comb)
        return
    
    for i in range(1, 7):
        comb.append(i)
        roll(n + 1)
        comb.pop()
roll(0)
print(cnt)
comb = []
cnt = 0
def roll(n, start):
    global cnt
    if n == 3:
        cnt += 1
        # print(comb)
        return
    
    for i in range(start, 7):
        comb.append(i)
        roll(n + 1, start)
        comb.pop()

roll(0, 1)
print(cnt)
