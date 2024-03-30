'''
(6 + 5 * (2 - 8) / 2)
'''
top = -1
stack = [0] * 100
icp = {'(' : 3, '*' : 2, '/' : 2, '+' : 1, '-' : 1}
isp = {'(' : 0, '*' : 2, '/' : 2, '+' : 1, '-' : 1}

fx = '(6 + 5 * (2 - 8) / 2)'
postfix = ''
for tk in fx:
    # 여는 괄호 push, top 원소보다 우선 순위가 높으면 push
    if tk == '(' or (tk in '*/+-' and isp[stack[top]] < icp[tk]):
        # push
        top += 1
        stack[top] = tk
    # 연산자이고 top 원소보다 우선순위가 높지 않으면
    elif tk in '*/+-' and isp[stack[top]] >= icp[tk]:
        # top 원소보다 우선순위가 낮을 때까지 pop
        while isp[stack[top]] >= icp[tk]:
            top -= 1
            postfix += stack[top + 1]
        top += 1
        stack[top] += tk
    elif tk == ')': # 닫는 괄호면, 여는 괄호를 만날 때까지 pop
        while stack[top] != '(':
            top -= 1
            postfix += stack[top + 1]
        
        top -= 1
        stack[top + 1]
    else:
        postfix += tk
print(postfix)