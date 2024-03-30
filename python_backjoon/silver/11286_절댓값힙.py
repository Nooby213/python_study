import sys
input = sys.stdin.readline
from heapq import heappop,heappush

# 연산의 갯수 1 ≤ N ≤ 100,000
N = int(input())
# 빈 힙리스트
heap = []
# 음수 양수 방문 기록
check = [1] * N
# N번 연산
for i in range(N):
    act = int(input())
    # 인풋값이 0이 아니라면 push
    if act:
        # 절대값과 차례
        heappush(heap, (abs(act), i))
        # 음수라면 기록
        if act < 0:
            check[i] = -1
# print(heap)
# print(check)
    # 0이라면 pop
    elif act == 0:
        # 리스트에 내용이 있다면
        if heap:
            # 음수인지 확인
            if check[heap[0][1]] == -1:
                # pop하고 기록남김, 음수니까 -
                check[heap[0][1]] = 0
                print(-heappop(heap)[0])
            # 양수라면
            elif check[heap[0][1]] == 1:
                # 음수를 찾거나 제일 작은 수 인지 확인
                for j in range(len(heap)):
                    if heap[j][0] > heap[0][0]:
                        check[heap[0][1]] = 0
                        print(heappop(heap)[0])
                        break
                    # 음수라면
                    if check[heap[j][1]] == -1:
                        check[heap[j][1]] = 0
                        print(-heap.pop(j)[0])
                        break
                else:
                    check[heap[0][1]] = 0
                    print(heappop(heap)[0])
        # 비어있으면 0 출력
        else:
            print(0)