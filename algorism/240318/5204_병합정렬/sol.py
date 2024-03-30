import sys

sys.stdin = open('input.txt')

def merge_sort(alist):
    global cnt
    if len(alist) < 2:
        return alist

    mid = len(alist) // 2
    front = merge_sort(alist[:mid])
    back = merge_sort(alist[mid:])
    if front[-1] > back[-1]:
        cnt += 1
    front_idx = 0
    back_idx = 0
    lst = []
    while front_idx < len(front) and back_idx < len(back):
        # 앞의 수가 크거나 같다면
        if front[front_idx] <= back[back_idx]:
            lst.append(front[front_idx])
            front_idx += 1
            if front_idx == len(front):
                lst += back[back_idx:]

        # 뒤의 수가 크다면
        elif front[front_idx] > back[back_idx]:
            lst.append(back[back_idx])
            back_idx += 1
            if back_idx == len(back):
                lst += front[front_idx:]

    return lst

T = int(input())

for t in range(1, T + 1):
    # N개의 정수, 5 <= N<= 1,000,000
    N = int(input())
    # 0 <= ai <= 1,000,000
    num_lst = list(map(int, input().split()))
    cnt = 0
    print(f'#{t} {merge_sort(num_lst)[N//2]} {cnt}')
