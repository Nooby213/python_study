# 카드 합 M 넘으며 가까우면 이김
# N장의 카드 중 3개
# 3 ≤ N ≤ 100, 10 ≤ M ≤ 300,000
def winner(i, temp_sum):
    global win
    if temp_sum > M:
        return

    if i == 3:
        win = max(win, temp_sum)
        return


    for j in range(N):
        if visited[j] == 0:
            visited[j] = 1
            winner(i + 1, temp_sum + cards[j])
            visited[j] = 0


N, M = map(int, input().split())
cards = list(map(int, input().split()))
cards.sort(reverse=True)
visited = [0] * N
win = 0
winner(0, 0)
print(win)
