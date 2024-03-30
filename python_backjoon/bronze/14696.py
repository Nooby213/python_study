# 라운드 N 은 1 이상 1,000 이하
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    print(A[i][1:])
    print(B[i][1:])
    if A[i].count(4) == B[i].count(4):
        print('D')
    elif A[i].count(4) != B[i].count(4):
        if A[i].count(4) == max(A[i].count(4), B[i].count(4)):
            print('A')
        else:
            print('B')
    elif A[i].count(3) == B[i].count(3):
        print('D')
    elif A[i].count(3) != B[i].count(3):
        if A[i].count(3) == max(A[i].count(3), B[i].count(3)):
            print('A')
        else:
            print('B')
    elif A[i].count(2) == B[i].count(2):
        print('D')
    elif A[i].count(2) != B[i].count(2):
        if A[i].count(2) == max(A[i].count(2), B[i].count(2)):
            print('A')
        else:
            print('B')
    elif A[i].count(1) == B[i].count(1):
        print('D')
    elif A[i].count(1) != B[i].count(1):
        if A[i].count(1) == max(A[i].count(1), B[i].count(1)):
            print('A')
        else:
            print('B')
    else:
        print('D')


