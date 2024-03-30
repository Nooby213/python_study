import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 문자열 -> iterable | 순회하며 정수로 변환
    ai = list(map(int, input()))
    print(ai)
    # 각 정수가 나온 횟수를 세기 위한 리스트
    counting_list = [0 for _ in range(10)]

    # 데이터 전체 순회하며 카운팅
    for num in ai:
        counting_list[num] += 1
    print(counting_list)
    max_count = 0   # 보유 개수
    result = 0      # 카드 번호
    # 0~9 전부 순회
    for i in range(10):
        # 보유 개수가 많거나 같다면
        # 같다면 -> 카드 번호가 더 큰 것
        if max_count <= counting_list[i]:
            max_count = counting_list[i]
            result = i

    print(f'#{tc} {result} {max_count}')