def factorial(n):
#    종료 조건:    n이 0이면 1을 반환
    if n == 0:
        return 1
#    재귀 호출:    n과 n-1의 팩토리얼을 곱한 결과를 반환
    return n * factorial(n - 1)
#    팩토리얼 계산 예시
result = factorial(5)
print(result)

def fac(m):
    for j in range(0,m+1):
        k *= j
        return k
print(fac(5))

# 주어진 정수 n이 있을 때, 1~n 까지의 모든 합을 구하는 재귀함수 만들기.
def sum_of_indigit(i):
    if i == 0:
        return 0
    return i + sum_of_indigit(i - 1)
result_2 = sum_of_indigit(10)
print(result_2)