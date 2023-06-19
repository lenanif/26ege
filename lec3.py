# 1
# досрок
f = open("in")
k = int(f.readline())
n = int(f.readline())
a = []
for i in range(n):
    st, end = map(int, f.readline().split())
    a.append((st, end))
a.sort()
# время окончания хранения багажа в ячейках 
k = 0
last = 0
camera = [0] * k
for i in range(n):
    st, end = a[i]
    for j in range(k):
        if camera[j] < st:
            camera[j] = end
            k += 1
            last = j + 1
            break
print(k, last)

# 2'
