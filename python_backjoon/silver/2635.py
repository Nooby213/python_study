# 0 <= N <= 30000
N = int(input())
num_lst = [N]
max_len = 0

for i in range(N, -1, -1):
    temp_lst = [N, i]
    j = N - i
    temp_len = 2

    while j >= 0:
        temp_lst.append(j)
        j = temp_lst[-2] - temp_lst[-1]
        temp_len += 1
    if temp_len > max_len:

        num_lst = temp_lst
        max_len = temp_len

print(max_len)
print(*num_lst)
