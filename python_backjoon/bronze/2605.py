# 학생 수 N <= 100
N = int(input())
num_lst = list(map(int, input().split()))
students = []
for i in range(N):
    students.insert(i - num_lst[i], i + 1)
print(*students)
