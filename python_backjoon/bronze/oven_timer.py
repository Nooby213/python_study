H, M = map(int,input().split())
cook_time = int(input())
H = H + cook_time // 60
M = M + cook_time % 60
if M >= 60:
    H += 1
    M = M - 60
if H >= 24:
    H = H - 24
print(f'{H} {M}')