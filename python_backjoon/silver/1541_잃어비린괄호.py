# 0 <= N <= 99999
# input <= 50
# 괄호를 쳐서 최소로 만들기
expression = input()
stack = []
i = 0

while i < len(expression):
    # 숫자면 묶어서 가져온다.
    if expression[i].isdecimal():
        word = ''
        for j in range(i, len(expression)):
            if expression[j] in '+-':
                stack.append(word)
                stack.append(expression[j])
                i = j + 1
                break
            elif j == len(expression) - 1:
                word += expression[j]
                stack.append(word)
                i = j + 1
            else:
                word += expression[j]
num = int(stack[0])
k = 1
while k < len(stack):
    # - 부호 나오기 전까지 계속 더해준다.
    if stack[k] == '-':
        k += 1
        while k < len(stack) and stack[k] != '-':
            num -= int(stack[k])
            k += 1
            if k < len(stack) and stack[k] == '+':
                k += 1

    if k < len(stack) and stack[k] == '+':
        k += 1
        num += int(stack[k])
        k += 1

print(num)
