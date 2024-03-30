'''
10
-7 -5 2 3 8 -2 4 6 9 0'''
a = '-7 -5 2 3 8 -2 4 6 9 0'
N = 10
arr = list(map(int, '-7 -5 2 3 8 -2 4 6 9 0'.split()))
print(arr)
print(2 ** N)
print(1 << N)
print(bin(1024))


for i in range(1, 2 ** N): # for i in range(1 << N):
    print(i, '번째 경우의 수')
    lst = []
    for j in range(N):
        # i번째 경우의 수에, j번째 요소가 포함 되어있는 부분집합인지 확인하는 코드
        # i번째가 3번째라면 -> bin(4)
        # j번째 요소 (0번째, 1번째, 2번째 ....) -> bin(8) 순회
        if i & (2 ** j): # if i & (1 << j)
            lst.append(arr[j])
    if sum(lst) == 0:
        print('멈춰')
        break
    print(lst)