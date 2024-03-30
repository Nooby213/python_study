# heapq / priority q
from queue import PriorityQueue
import heapq

# q = PriorityQueue()
# q.put((45, 'z'))
# q.put((17, 'x'))
# print(q.queue)

arr = [(45, 'z'), (17, 'x'), (6, 'a'), (100, 'b')]
heapq.heapify(arr)
print(arr)

heapq.heappush(arr, (4, 't'))
print(arr)
heapq.heappush(arr, (30, 't'))
print(arr)
print(heapq.heappop(arr))
print(arr)
arr.append((-1, 'z'))   # 이거는 단순 삽입
print(arr)