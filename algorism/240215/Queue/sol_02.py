class Queue:
    def __init__(self, maxsize):
        self.size = maxsize
        self.items = [None] * maxsize
        self.rear = -1
        self.front = -1

    def enQueue(self, item):
        self.rear += 1
        self.items[self.rear] = item

    def deQueue(self):
        self.front += 1
        return self.items[self.front]

q = Queue(3)
# print(q.front, q.rear)
q.enQueue('a')
q.enQueue('b')
q.enQueue('c')
# print(q.items)
# print(q.front, q.rear)
print(q.deQueue())
print(q.deQueue())
print(q.deQueue())
print(q.front, q.rear)
print(q.items)
