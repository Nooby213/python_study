H, M = map(int,input().split())
M = M - 45

if M <= 0:
    M = 60 + M
    H -= 1

if M == 60:
    M = 0
    H += 1

if H <= 0:
    H = 24 + H

if H == 24:
    H= 0
    
print(H, M)