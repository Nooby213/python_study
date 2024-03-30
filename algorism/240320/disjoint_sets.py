# 1 ~ 6번까지 노드
# 1. make_set
def make_set(n):
    rank = [0] * n
    return [i for i in range(n)], rank
# 1 ~ 6번 까지 사용 0은 버림

parents, rank = make_set(7)
print(parents)
print(rank)

# 2. find_set : 대표자를 찾아보자
# 부모 노드를 보고, 부모 노드도 연결이 되어 있다면 다시 반복
# 자기 자신이 대표인 데이터를 찾을 때까지
def find_set(x):
    if parents[x] == x:
        return x

    return find_set(parents[x])

def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x != root_y:
        if rank[root_x] < rank[root_y]:
            parents[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parents[root_y] = root_x
        # 두 집단의 rank가 동일하다면 둘중 하나를 붙이고 해당 집단의 rank += 1
        else:
            parents[root_y] = root_x
            rank[root_x] += 1

union(1, 3)
union(2, 3)
print(find_set(3))
print(rank)
print(parents)
