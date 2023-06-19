# 8512
# Досрок 2023
with open("26_8512.txt") as file:
    k = int(file.readline())
    n = int(file.readline())
    a = []
    for line in file:
        a.append(tuple(map(int, line.split())))
        
a.sort()
c = [0] * k 
p = 0
last = 0
for i in range(n):
    for j in range(k):
        if a[i][0] > c[j]:
            c[j] = a[i][1]
            p += 1
            last = j+1
            break
print(p, last)

# 2480
with open("in") as file:
    n = int(file.readline())
    a = []
    for line in file:
        a.append(tuple(map(int, line.split())))
a.sort()
length = 0
s = a[0][0]
end = a[0][1]
k = 1
for i in range(1, n):
    if a[i][0] <= end:
        end = max(a[i][1], end)
    else:
        k += 1
        length += end - s
        s = a[i][0]
        end = a[i][1]
length += end - s
print(k, length)
