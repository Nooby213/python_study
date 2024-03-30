wait = [10, 15, 30, 50]
time = 0
for i in range(1, len(wait) + 1):
    time += (wait.pop() * i)
print(time)