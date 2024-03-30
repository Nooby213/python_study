def binary(target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1  # 이 부분을 수정해야 합니다.

    return -1

arr = [324, 32, 22114, 16, 48, 93, 422, 21, 316]
arr.sort()
print(arr)
print(binary(32))
