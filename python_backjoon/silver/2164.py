from collections import deque
N = int(input())    # 1 ~ N 번, N번 카드가 제일 아래
cards = deque([i for i in range(1, N + 1)])
while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())
else:
    print(*cards)