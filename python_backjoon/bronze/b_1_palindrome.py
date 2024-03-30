import sys

input = sys.stdin.readline

while True:
    N = input().rstrip()

    if N == '0':
        break
    elif N == N[::-1]:
        print('yes')
    else:
        print('no')
