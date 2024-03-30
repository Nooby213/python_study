import sys
sys.stdin = open('input.txt')

T = int(input())    # 테스트 케이스 갯수
exponent_list = [2, 3, 5, 7, 11]    # 지수 리스트
for t in range(1, T + 1):
    N = int(input())
    exponent_dict = {i : 0  for i in exponent_list} # 지수 갯수 초기화
    for i in exponent_list: # 지수로 나눠지면 +1
        while N % i == 0:
            N //= i
            exponent_dict[i] += 1
        if N == 1:  # 1까지 나눠줬을 때 브레이크
            break
    print(f'#{t} {exponent_dict[2]} {exponent_dict[3]} {exponent_dict[5]} {exponent_dict[7]} {exponent_dict[11]}')