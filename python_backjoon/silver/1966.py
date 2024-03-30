from collections import deque

T = int(input())
for t in range(T):
    N, idx = map(int, input().split())  # N개의 문서, 문서의 idx
    im = deque(list(map(int, input().split())))   # 문서의 중요도
    idx_lst = deque([i for i in range(N)])  # 인덱스 0부터

    num = 0

    while idx in idx_lst:
        if im[0] == max(im):    # 중요도 확인
            im.popleft()
            idx_lst.popleft()
            num += 1
        else:   # 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 가장 뒤에 배치
            im.append(im.popleft())
            idx_lst.append(idx_lst.popleft())
    print(num)