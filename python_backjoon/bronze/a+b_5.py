# while True:
#     num_list = list(map(int,input().split()))
#     if 0 in num_list:
#         break
#     else:
#         print(num_list[0] + num_list[1])

while True:
    a, b = map(int,input().split())
    if a == 0 and b == 0:
        break
    else:
        print(a + b)