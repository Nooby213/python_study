# 배열 2
- 배열 : 2차원 배열
- 부분집합 생성
- 바이너리 서치 (Binary Search)
- 셀렉션 알고리즘 (Selection Algorithm)
- 선택 정렬 (Selection Sort)
---
## 2차원 배열의 선언
- 1차원 List를 묶어놓은 List
- 2차원 이상의 다차원 List는 차원에 따라 Index를 선언
- 2차원 List의 선언 : 세로길이(행의 개수), 가로 길이(열의 개수)를 필요로 함
- Python 에서는 데이터 초기화를 통해 변수 선언과 초기화가 가능함
```python
'''3
1 2 3
4 5 6
7 8 9
'''
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
print(arr)

arr2 = [[0] * N for _ in range(N)]

# 얕은 복사
arr3 = [[0] * N] * N
print(arr3) # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
arr3[0][0] = 1
print(arr3) # [[1, 0, 0], [1, 0, 0], [1, 0, 0]]
```
```python
#지그재그 순회
# i 행의 좌표
# j 열의 좌표

for i in ragne(n):
    for j in range(m):
        f(array[i][j + (m -1 - 2*j) * (i % 2)])
```
---
### 델타를 이용한 2차 배열 탐색
- 2차 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법
- 인덱스(i, j)인 칸의 상하좌우 칸 (ni, nj)
![델타예](/델타를이용한2차원배열.PNG)
```python
# 방법 1
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N = 5
arr = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                print(arr[ni][nj], end=' ')
        print()
```
```python
# 방법 2
# N = 5
arr = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                print(arr[ni][nj], end=' ')
        print()
```

- 전치 행렬
![전치행렬](/전치행렬.PNG)
---
### 부분집합 합(sub)
#### 비트 연산자
- & : 비트 단위로 AND 연산을 한다.
- | : 비트 단위로 OR 연산을 한다.
- < : 피연산자의 비트 열을 왼쪽으로 이동시킨다.
- \> : 피연산자의 비트 열을 오른쪽으로 이동시킨다.
- << 연산자
  - 1 << : 2^n 즉, 원소가 n개일 경우의 모든 부분집합의 수를 의미한다.
  - & 연산자
    - i & (1<<j) : i의 j번째 비트가 1인지 아닌지를 검사한다.
```python
arr = [3, 6, 7, 1, 5, 4]

n = len(arr)    # 원소의 개수
for i in range(1 << n): # 1<< n : 부분 집합의 개수, 공집합 제거할때 1, 1<<n
    s = 0
    for j in range(n):  # 원소의 수만큼 비트를 비교함
        if i & (1 << j):    # i의 j번 비트가 1인경우
            s += arr[j]
            print(arr[j], end=", ") #j번 원소 출력
    print('sum : ', s)
print()
# 맨 위의 빈칸은 공집합
```
---
### 검색 
