import math
M, N = map(int, input().split())
prime_lst = []
for i in range(2, N + 1):   # 어차피 1은 소수 아님
    if i == 2 or i == 3:
        prime_lst.append(i)
    else:
        for j in range(2, int(math.sqrt(i)) + 1):   # 제곱근을 기준으로 반복한다
            if i % j == 0:
                break
        else:
            prime_lst.append(i)

for p in prime_lst:
    print(p)

# def sieve_of_eratosthenes(m, n):
#     is_prime = [True] * (n + 1)
#     is_prime[0], is_prime[1] = False, False
#     for i in range(2, int(n**0.5) + 1):   # 제곱수까지
#         if is_prime[i]:
#             for j in range(i*2, n + 1, i):    # *2 ~ n 안의 i배수는 소수아님
#                 is_prime[j] = False
#     primes = [i for i in range(m, n + 1) if is_prime[i]]
#     return primes
# m, n = map(int, input().split())
# result = sieve_of_eratosthenes(m, n)
# for prime in result:print(prime)

# prime_lst = [2]
# for i in range(2, N + 1):
#     if i == 2 or i == 3:
#         print(i)
#     elif i % 2:
#         for j in prime_lst:
#             if i % j == 0:
#                 break
#         else:
#             prime_lst.append(i)
#             print(i)

# for i in range(2, N + 1):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i)