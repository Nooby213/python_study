from queue import Queue

q = Queue()
print(q)
q.put('a')
q.put('b')
q.put('c')
print(q.queue)
print(q.qsize())
print(q.get())
print(q.queue)

# 멀티스레드 프로그래밍
q = Queue(3)
q.put('a')
q.put('b')
q.put('c')
print(q.queue)
q.put('d')