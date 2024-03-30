# 서로 붙어 있는 주사위의 면의 숫자는 같아야된다.
N = int(input())  # 1 <= N <= 10000
dices = [list(map(int, input().split())) for _ in range(N)]  # 주사위
re_dices = [[] for _ in range(N)]

# 주사위로 만들어졌을 때 붙는 숫자끼리 모음
for i in range(N):
    re_dices[i] = [dices[i][0], dices[i][5], dices[i][1], dices[i][3], dices[i][2], dices[i][4]]
max_score = 0

for i in range(6):
    score = 0
    a = re_dices[0][i]

    for j in range(N):
        a_idx = re_dices[j].index(a)
        if a_idx % 2:  # 홀수면 앞에 있는 애랑 세트
            b = re_dices[j][a_idx - 1]
        else:  # 짝수면 뒤에 있는 애랑 세트
            b = re_dices[j][a_idx + 1]
        a = b
        com_num = 0
        for k in range(6):
            if a_idx == k or re_dices[j].index(b) == k:  # a나 b면이면 패스
                continue
            else:  # 아니면 콤비네이션에 넣음
                if re_dices[j][k] > com_num:
                    com_num = re_dices[j][k]
        score += com_num

    if score > max_score:
        max_score = score

print(max_score)