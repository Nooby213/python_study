import sys
sys.stdin = open('input.txt')

# 숫자는 stack에 넣는다.
# 연산자를 만나면 숫재 두 개를 꺼내 연산 후 스택에 다시 넣는다.
# . 은 숫자 출력한다.
# 형식이 잘못되었다면 error 출력.

T = int(input())
for t in range(1, T + 1):
    forth = list(map(str, input().split()))
    stack = []

    for f in forth:
        if f.isdecimal():
            stack.append(int(f))

        elif len(stack) >= 2 and f == '*':
            a = stack.pop()
            b = stack.pop()
            stack.append(a * b)
            # print(stack)

        elif stack[-1] != 0 and len(stack) >= 2 and f == '/':
            a = stack.pop()
            b = stack.pop()
            stack.append(b // a)
            # print(stack)

        elif len(stack) >= 2 and f == '+':
            a = stack.pop()
            b = stack.pop()
            stack.append(b + a)
            # print(stack)

        elif len(stack) >= 2 and f == '-':
            a = stack.pop()
            b = stack.pop()
            stack.append(b - a)
            # print(stack)

        elif len(stack) == 1 and f == '.':
            print(f'#{t} {stack.pop()}')
            break

        else:
            print(f'#{t} error')
            break
