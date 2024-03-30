import sys
from pprint import pprint as pp
input = sys.stdin.readline
N, M = map(int,input().split()) # 세로 N 가로 M
board = [[c for c in (input().rstrip())] for _ in range(N)]
bw = 'BW' * 4
wb = 'WB' *4
sample1 = [0] * 8
sample2 = [0] * 8
for i in range(8):  # 견본 체스판
    if i % 2:
        sample1[i] = list(map(str,bw))
        sample2[i] = list(map(str,wb))
    else:
        sample1[i] = list(map(str,wb))
        sample2[i] = list(map(str,bw))
# pp(sample1)
# pp(sample2)
count_list = []
for n in range(N - 7):  # 8 * 8 로 자른 모든 경우의 수
    for m in range(M - 7):
        chess = [row[m : m + 8] for row in board[n : n + 8]]
        count_diff1 = 0
        count_diff2 = 0
        for j in range(8): # sample 이랑 비교
            for k in range(8):
                if chess[j][k] != sample1[j][k]:
                    count_diff1 += 1
                if chess[j][k] != sample2[j][k]:
                    count_diff2 += 1
        count_list.append(count_diff1)
        count_list.append(count_diff2)
        

print(min(count_list))

        

