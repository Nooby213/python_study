# num = int(input())
# result = 1
# if num > 0:
#     for i in range(1, num + 1):
#         result *= i
# print(result)

num = int(input())

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(num))