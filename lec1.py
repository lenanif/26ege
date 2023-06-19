# 1 (Демо 2021)
with open("in") as file:
    s, n = map(int, file.readline().split())
    a = sorted(list(map(int, file.read().split())))
b = []
while sum(b) + a[0] <= s:
    b.append(a.pop(0))
for i in range(len(a)):
    if sum(b) - b[-1] + a[i] <= s:
        b[-1], a[i] = a[i], b[-1]
print(len(b), b[-1])

# 2
# Для перевозки партии грузов (последние в примере - 140 300)
# На оставшееся место стараются взять как можно большее количество грузов
# Самый большой груз должен иметь наиибольшую массу (второй самый большой - наибольший, третий - наибольший и тд.
# (если можно выбрать несколькими способами собрать)
with open("in") as file:
    n, m = map(int, file.readline().split())
    a = sorted(list(map(int, file.read().split())))
b = []
print(n, a)
for i in range(n):
    if 180 <= a[i] <= 200:
        b.append(a[i])
        a[i] = 0
a = [x for x in a if x != 0]
m = m - sum(b)
c = [] # в с отправляем грузы по возрастанию 
while sum(c) + a[0] <= m:
    c.append(a.pop(0))
c.sort(reverse=True) # по убыванию 
for i in range(len(c)): # перебираем все грузы, начиная с самого большого, и смотрим, можем ли заменить 
    for j in range(len(a)):
        if a[j] > c[i] and sum(c) - c[i] + a[j] <= m:
            c[i], a[j] = a[j], c[i] # замена

print(len(b + c), sum(b + c))

# 3
# Администратор написал скрипт раскладки N архивов на K дисков
with open("26-56.txt") as file:
    v, K, n = map(int, file.readline().split())
    a = list(map(int, file.read().split()))
a.sort(reverse = True)

disks = [0] * K
k = 0 # номер последнего диска, в который положили файл 
c = [] # мусорка
# Если файл помещается на диск, то следующий по размеру файл стараются поместить на следующий диск. 
# Как начинать со след диска?
for i in range(n):
    for j in range(k, k + K): #сдвигаемся кусочками (бесконечный цикл. закончится, когда переберем все n)
        if disks[j % K] + a[i] <= v:
            disks[j % K] += a[i]
            k = j + 1
            break
    else:
        c.append(a[i])
print(sum(c), len(c))

# 4
with open("26-45.txt") as file:
    n = int(file.readline())
    a = list(map(int, file.read().split()))
c = 0 # кол-во сред. арифм.
b = set(a)
m = 0
for i in range(n-1):
    for j in range(i+1, n):
        if (a[i] + a[j]) % 2 == 0:
            sr = (a[i] + a[j]) // 2 
            if sr in b: # поиск во множестве
                c += 1
                m = max(m, sr)
print(c, m)

# 5

# В текстовом файле записан набор натуральных чисел. Гарантируется, что все числа различны. 
# Для каждой пары различных чисел из набора вычисляется значение K – количество чисел из набора,
#  меньших среднего арифметического этой пары. Необходимо определить количество пар чисел с ненулевым значением K, 
# кратным ста, а также наибольшее K среди этих пар.
from bisect import *
with open("26-45.txt") as file:
    n = int(file.readline())
    a = sorted(list(map(int, file.read().split())))
ans = []
for i in range(n):
    for j in range(i+1, n):
        sr = (a[i] + a[j]) // 2
        count = bisect_left(a,sr)
        if count % 100 == 0:
            ans.append(count)
print(len(ans), max(ans))

# Задачи с ХРОНОЛОГИЕЙ

# 6
# Сколько участков дорги не требуют ремонта, и какова длина наибольшего из них
with open("in") as file:
    n = int(file.readline())
    a = [0] * 2_000_000 # дорога
    for i in range(n):
        st, end = map(int, file.readline().split())
        a[st] += 1
        a[end] -= 1
    k = 0 # сколько в текущем метре жалоб
    st, end = -1, 0
    count = 0
    max_length = 0
    for i in range(len(a)):
        k0 = k # предыдущее k
        k += a[i]
        if k == 0 and st == -1:
            st = i
        if k0 == 0 and (k > 0 or i == 2_000_000 - 1):
            end = i
            count += 1
            max_length = max(max_length, end-st)
            st, end = -1, 0
print(count, max_length)

# 7 Хронология 2
# Определите расстояние от начала дороги до 500-го неосвещенного участка и его длину в метрах
file = open("in")
n = int(file.readline())
road = [0] * 150_000
for i in range(n):
    lamp = int(file.readline())
    road[lamp - 20] += 1
    road[lamp + 20] += 1
k = 0
count = 0
st, end = -1, 0
for i in range(150_000):
    k0 = K
    k += road[i]
    if k == 0 and st == -1:
        st = i
    if k > 0 and k0 == 0:
        end = i
        count += 1
        if count == 500:
            print(st, end - st)
        st, end = -1, 0

# 8 #Хронология 3
# Найти длину неосвещенных участков
# Сопоставить их с фонарями на рынке 
# Гарантируется, что каждый неосвещенный участок можно покрыть одним фонарем

file = open("in")
L, N, M = map(int, file.readline().split())
# М количество фонарей на рынке
# N количество фонарей на дороге
# L расстояние от начала дороги до фонаря
road = [0] * (L + 1)
for i in range(N):
    x, h = map(int, file.readline().split())
    road[x-h//2] += 1 #писать условия по хорошему надо
    road[x+h//2] -= 1
lamp = [int(x) for x in file]
dark = []
k = 0
st, end = -1, 0
for i in range(L+1):
    k0 = k
    k += road[i]
    if k == 0 and st == -1:
        st = i
    if k0 == 0 and (k > 0 or i == L):
        end = i
        dark.append(end-st)
        st, end = -1, 0
dark.sort()
lamp.sort()
s, overpay = 0, 0
for i in range(len(dark)):
    for j in range(len(lamp)):
        if lamp[j] >= dark[i]:
            s += lamp[j]
            overpay += lamp[j] - dark[i]
            lamp[j] = 0
            break
print(s, overpay)

# 9 Хронология 4













