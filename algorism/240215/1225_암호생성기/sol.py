import sys
sys.stdin = open('input.txt')

# 8개의 숫자를 입력받는다.
# 첫 번째 숫자를 1 감소한 뒤 맨뒤로 보낸다.
# -1, -2 , -3, -4, -5 가 한 사이클
# n <= 0, n = 0 끝으로 이동, 프로그램 종료 후 암호화

for _ in range(10):
    ts = int(input())   # 테스트 케이스
    code = list(map(int, input().split()))  # 코드
    # print(code)
    a = 1   # 처음엔 1
    while code[0] - a > 0:  # 0 보다 작거나 같으면 브레이크
        code[0] -= a
        code.append(code.pop(0))    # 첫번째를 pop해서 끝에 붙임
        # print(code)
        a = 1 + ((a) % 5)   # 1~5니까
    else:   # while 이 끝나면
        if code[-1] != 0 and code[0] - a <= 0:  # 끝이 0인지 확인
            code[0] = 0
            code.append(code.pop(0))
        print(f'#{ts}', end=' ')
        print(*code)