A = int(input())
T = int(input())
C = int(input())
def bundegi():
    cnt0 = cnt1 = 0
    n = 0
    while True:
        for i in range(4):
            if i % 2 == 0:
                cnt0 += 1
            else:
                cnt1 += 1
            if C == 0 and cnt0 == T:
                return cnt0 + cnt1
            elif C == 1 and cnt1 == T:
                return cnt0 + cnt1

        for i in range(n + 2):
            cnt0 += 1
            if C == 0 and cnt0 == T:
                return cnt0 + cnt1

        for i in range(n + 2):
            cnt1 += 1
            if C == 1 and cnt1 == T:
                return cnt0 + cnt1
        n += 1
result = (bundegi() - 1) % A
print(result)