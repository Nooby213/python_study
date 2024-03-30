# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
from collections import deque
def front():
    if q:
        print(q[0])
    else:
        print(-1)
def push(x):
    q.append(x)


def pop():
    if q:
        print(q.popleft())
    else:
        print(-1)


def size(lst):
    print(len(lst))


def empty(lst):
    if lst:
        print(0)
    else:
        print(1)


def back():
    if not q:
        print(-1)
    else:
        print(q[-1])


N = int(input())
q = deque()
command = [list(input().split()) for _ in range(N)]
for i in range(N):

    if len(command[i]) == 2:
        push(int(command[i][1]))
    else:
        c = command[i][0]
        if c == 'pop':
            pop()
        elif c == 'size':
            size(q)
        elif c == 'empty':
            empty(q)
        elif c == 'back':
            back()
        elif c == 'front':
            front()
