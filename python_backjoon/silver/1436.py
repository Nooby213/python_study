import sys

input = sys.stdin.readline

a = int(input())    # 리스트의 길이
n = []  # 빈 리스트를 만들어서 작은 666 순서대로 채워 넣는다.
p = 666 # 첫 번째 666
while len(n) != a:  # 길이가 a가 되면 멈춤

    if '666' in str(p): # 문자열로 변환해 666이 있는지 찾아 리스트에 추가한다.
        n.append(p)

    p += 1  # 그 다음수로

else:
    print(int(n[-1]))   # 제일 큰 값은 마지막 값이니까 출력
