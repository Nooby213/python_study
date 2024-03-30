# 팩토리얼
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)
print(fact(5))

def fact_while(n):
    # 종료 조건 ~동안
    result = 1
    while n:
        result *= n
        n -= 1
    return result

print(fact_while(5))

def fact_for(n):
    # 최종 결과물 
    result = 1
    # 정해진 범위 내 순회
    for i in range(n, 0, -1):
        # print(i)
        result *= i
    return result
print(fact_for(5))

# 피보나치
def fibo(n):
    if n <= 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)
for i in range(4):
    # if n <= 1:
    #     return 1
    # else:
    #     return fibo(n - 1) + fibo(n - 2)
    pass
while True:
    pass
print(fibo(4))
