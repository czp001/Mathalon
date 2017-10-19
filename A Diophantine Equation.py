#run in python3
from queue import Queue
limit = 10 ** 9
Hash = {}
q = Queue()
q.put([1, 1, 1])

while not q.empty():
    a = q.get()
    a.sort()
    if a[0] <= 0 or a[2] >= limit:
        continue
    if a[2] in Hash:
        continue
    Hash[a[2]] = a
    s = 3
    for i in a:
        s *= i
    q.put([s // a[0] - a[0], a[1], a[2]])
    q.put([s // a[1] - a[1], a[0], a[2]])
    q.put([s // a[2] - a[2], a[1], a[0]])

N = 10**9
count = 0
sol = []
for i in Hash:
    a = Hash[i]
    if a[2] <= N:
        sol.append(a)
        count += 1
sol.sort()
if count==0:
    print('No Solution')
else:
    print(count)
    for i in sol:
        print(i[0], i[1], i[2])
