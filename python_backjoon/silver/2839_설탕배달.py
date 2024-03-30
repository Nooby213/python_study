# N kg
# 3kg, 5kg 적은 봉지
sugar = [-1] * 5001

N = int(input())
for i in range(3, N + 1, 3):
    sugar[i] = i // 3

for i in range(5, N + 1, 5):
    sugar[i] = i // 5

for i in range(8, N + 1, 8):
    if sugar[i] == -1:
        sugar[i] = (i // 8) * 2
    else:
        sugar[i] = min((i // 8) * 2, sugar[i])

for i in range(8, N + 1, 3):
    if sugar[i] == -1:
        sugar[i] = sugar[i - 3] + 1
    else:
        sugar[i] = min(sugar[i], sugar[i - 3] + 1)

for i in range(8, N + 1, 5):
    if sugar[i] == -1:
        sugar[i] = sugar[i - 5] + 1
    else:
        sugar[i] = min(sugar[i], sugar[i - 5] + 1)

print(sugar[N])
