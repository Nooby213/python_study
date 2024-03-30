# push_front X: 정수 X를 덱의 앞에 넣는다.
# push_back X: 정수 X를 덱의 뒤에 넣는다.
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 덱에 들어있는 정수의 개수를 출력한다.
# empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
# front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
from collections import deque
def push_front(x):
    q.appendleft(x)
def front():
    if q:
        print(q[0])
    else:
        print(-1)
def push_back(x):
    q.append(x)


def pop_front():
    if q:
        print(q.popleft())
    else:
        print(-1)

def pop_back():
    if q:
        print(q.pop())
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
        if command[i][0] == 'push_back':
            push_back(int(command[i][1]))
        else:
            push_front(int(command[i][1]))
    else:
        c = command[i][0]
        if c == 'pop_front':
            pop_front()
        elif c == 'pop_back':
            pop_back()
        elif c == 'size':
            size(q)
        elif c == 'empty':
            empty(q)
        elif c == 'back':
            back()
        elif c == 'front':
            front()
