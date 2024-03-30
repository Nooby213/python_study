# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
def push(x):
    stack.append(x)


def pop():
    if stack:
        print(stack.pop())
    else:
        print(-1)


def size(lst):
    print(len(lst))


def empty(lst):
    if lst:
        print(0)
    else:
        print(1)


def top():
    if not stack:
        print(-1)
    else:
        print(stack[-1])


N = int(input())
stack = []
command = [list(input().split()) for _ in range(N)]
for i in range(N):

    if len(command[i]) == 2:
        push(int(command[i][1]))
    else:
        c = command[i][0]
        if c == 'pop':
            pop()
        elif c == 'size':
            size(stack)
        elif c == 'empty':
            empty(stack)
        elif c == 'top':
            top()