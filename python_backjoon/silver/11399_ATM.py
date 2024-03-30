# N 명, 1~N
N = int(input())
time = sorted(list(map(int, input().split())))
min = 0
temp = 0
for i in range(N):
    temp += time[i]
    min += temp
print(min)