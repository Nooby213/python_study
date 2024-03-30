'''
10
-7 -5 2 3 8 -2 4 6 9 0'''
a = '-7 -5 2 3 8 -2 4 6 9 0'
N = 100
arr = list(range(1, 101))
# 부분집합의 합이 55 미만인 경우만 모은 리스트
print(arr)
print(2 ** N)
print(1 << N)
print(bin(1024))


for i in range(1, 1 << N):
    # print(i, '번째 경우의 수')
    lst = []
    for j in range(N): # 반대로는 for j in range(N-1, -1 ,-1)
        if i & (1 << j): 
            lst.append(arr[j])
            if sum(lst) >= 55: # 부분집합의 합이 55 이상이 되면 조사종료
                break
    if sum(lst) < 55: # 부분집합의 합이 55미만인 경우만 출력
        print(lst)
