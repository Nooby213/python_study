import sys
input = sys.stdin.readline

while True:
    sen = input().rstrip()
    if sen == '.':
        break
    stack = []
    for i in sen:
        if i in '[(':
            stack.append(i)
        elif stack and i in ')]':
            if i == ')' and stack[-1] == '(':
                stack.pop()
            elif i == ']' and stack[-1] == '[':
                stack.pop()
            else:
                print('no')
                break
        elif not stack and i in ')]':
            print('no')
            break
    else:
        if stack:
            print('no')
        else:
            print('yes')