import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T + 1):
    # 인덱스 값을 1, 2, 3 ...으로 주기위해 10으로 나누어 준다.
    ground = int(input()) // 10
    # 땅의 가로 길이가 인덱스가 되고 경우의 수가 값이 되는 리스트를 만들어준다.
    paper = [0] * (ground + 1)
    paper[0] = 0
    paper[1] = 1
    paper[2] = 3
    # print(ground)

    # 경우의 수는 10 * 20 1개 쓴다면 i - 1의 경우의 수와 같고,
    # 20 * 10 이나 20 * 20 을 쓴다면 i - 2의 경우의 수와 같다.
    for i in range(3, ground + 1):
        paper[i] = paper[i-1] + 2 * paper[i-2]

    print(f'#{t} {paper[ground]}')