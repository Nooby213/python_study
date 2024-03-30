def binary_search_count(A, B):
    A.sort()  # 리스트 A를 정렬
    count = 0

    for num in B:
        left = 0
        right = len(A) - 1
        found = False

        while left <= right:
            mid = (left + right) // 2

            if A[mid] == num:
                found = True
                break
            elif A[mid] < num:
                left = mid + 1
            else:
                right = mid - 1

        if found:
            count += 1
            continue

        # 위의 이진 탐색 과정에서 찾지 못했을 경우,
        # 번갈아가며 선택하게 되는지 확인
        if (left > 0 and A[left - 1] < num) or (right < len(A) - 1 and A[right + 1] > num):
            count += 1

    return count


# 테스트 케이스의 수 입력
T = int(input())

for case in range(1, T + 1):
    # A와 B에 속한 정수의 개수 N, M 입력
    N, M = map(int, input().split())
    # 리스트 A와 B에 대한 정수 입력
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 결과 출력
    result = binary_search_count(A, B)
    print(f"#{case} {result}")
