N = int(input())
for i in range(N):
    print(f'{" " * (N - i - 1)}{"*" * (i + 1)}')