num_list = list(int(input()) for _ in range(9))
# print(num_list)
c = 0
for i in num_list:
    if i > c:
        c = i
print(c)
print(num_list.index(c)+1)