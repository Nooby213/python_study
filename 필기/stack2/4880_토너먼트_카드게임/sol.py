import sys
sys.stdin = open('input.txt')

# 1 ~ N 카드 나눠 갖는다.
# 전체를 두 개의 그룹으로 나누고, 이긴 사람이 최종 승자
# i ~ (i+j)//2 | (i+j)//2+1 ~ j
# 가위 1, 바위 2, 보 3
# 비기면 idx 작은 쪽이 승자
def rsp_winner(alist, l):
    if len(alist) == 2: # 사람이 2명 남으면
        if win[cards[alist[0]]] == cards[alist[1]] or cards[alist[0]] == cards[alist[1]]:
            return [alist[0]]
        else:
            return [alist[1]]

    elif len(alist) == 1:   # 혼자라면 // 최후의 승자라면
        return alist

    else:
        pivot = l // 2
        if l % 2:   # 홀수면
            lsp = alist[:pivot+1]
            gtp = alist[pivot+1:]
        else:   # 짝수면
            lsp = alist[:pivot]
            gtp = alist[pivot:]
            # 각 토너먼트 팀에서 승자 리스트 반환
        return rsp_winner(lsp, len(lsp)) + rsp_winner(gtp, len(gtp))

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    cards = list(map(int, input().split()))

    L = len(cards)
    win = [0, 3, 1, 2]  # 이길려면

    idx = [i for i in range(L)] # 인덱스

    result2 = rsp_winner(idx, L)    # 1차전
    while len(result2) > 1:    # 결승전까지
        result2 = rsp_winner(result2, len(result2))

    print(f'#{t} {result2[0] + 1}') # 인덱스 + 1 해야됌