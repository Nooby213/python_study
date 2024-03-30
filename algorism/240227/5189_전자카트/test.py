import sys
sys.stdin = open('input.txt')

'''
    1. n개의 방을 모두 한번씩은 방문해야한다.
        -> 최소 N번 탐색해야 한다.
        -> 이전에 방문한 곳은 방문해선 안된다
    2. 항상 0번에서 출발한다.
        -> 함수 시작점을 0으로 잡으면 되겠다.
    3. 마지막에 무조건 0번으로 돌아와야한다.
        -> 코드 짤 때 이부분은 어디에 써야할까?
    4. 갈 때, 올 때 값이 다르다.
'''
'''
 now -> 현재 위치 -> 현 위치에서 다음 위치로 이동 data[now][next]
'''

def search(now, acc):
    global result
    # global result
    # 언제까지 조사할 것이냐?
    '''
        이떄까지 우리는 어떻게 조사했는가?
        이 방식이 모든 상황을 조사했음을 판별 할 수 있느냐?
        if now == N:
    '''
    # if cnt == N-1:
    # if sum(visited) == N:
    if all(visited): # 모든 방을 방문했다면...
        # 마지막에 0번으로 돌아와야 한다.
        acc += data[now][0]
        if result > acc:
            result = acc
    else:
        # 내 위치에서 next 위치로 가는 비용 알아내기
        for next in range(1,N): # 0번 사무실에서 출발하고, 사무실은 조사대상 아님
            # 다음 조사 가능한 값은?
            # 내 위치에서 내 위치로 이동할 수는 없으니
            if now != next and not visited[next]:
                visited[next] = 1 # next번째 조사한다로 기록하고, 다음 조사
                # def search(now, acc)
                search(next, acc + data[now][next])
                visited[next] = 0

T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    visited = [0] * N
    visited[0] = 1
    # 최종 결과값
    result = N*101
    search(0,0)
    print(f'#{test_case} {result}')