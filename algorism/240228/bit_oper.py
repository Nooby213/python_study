freinds = ['A', 'B', 'C', 'D', 'E']
print((5 << 5))
print((1 << len(freinds)) - (5 << 0) - 1)
n = len(freinds)
def get_count(tar):
    cnt = 0
    for i in range(n):
        # 1 비트 1인지 확인
        if tar & 0x1:
            cnt += 1
        # 오른쪽 끝 비트를 하나씩 제거
        tar >>= 1
    return cnt

result = 0
for tar in range(1 << n):
    if get_count(tar) >= 2: # bit가 2개이상 1이라면
        result += 1
print(result)
