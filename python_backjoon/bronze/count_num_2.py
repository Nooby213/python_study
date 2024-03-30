A, B, C = [int(input()) for _ in range(3)]

N = str(A * B * C)
num_dict = {str(i) : 0 for i in range(10)}

for n in N:
    num_dict[n] += 1

for i in num_dict:
    print(num_dict[i])

