a = input()
b = input()
sum_digit = 0
for i in range(2, -1 , -1):
    print(int(a) * int(b[i]))
    sum_digit += (int(a) * int(b[i])) * (10**(2-i))
else:
    print(sum_digit)