# 4
# Оптовая закупка
file = open("in")
n, m = map(int, file.readline().split())
b, s = [], 0
for _ in range(n):
    price, num, type = file.readline().split()
    if type == "A":
        s += int(price) * int(num)
    else:
        b.append(tuple(int(price), int(num)))
file.close()
if s <= m:
    print("OK")
b.sort()
countB = 0
for price, num in b: # не нужно максимизировать последний элемент, так как про это не сказано 
    for _ in range(num):
        if s + price <= m:
            s += price
            countB += 1
print(countB, m - s)

# 6
#Организация купила для своих сотрудников все места в нескольких подряд идущих рядах на концертной площадке. 
# Известно, какие места уже распределены между сотрудниками. Найдите ряд с наибольшим номером, 
# в котором есть два соседних места, таких что слева и справа от них в том же ряду места уже распределены (заняты).
#  Гарантируется, что есть хотя бы один ряд, удовлетворяющий условию. 
# В ответе запишите два целых числа: номер ряда и наименьший номер места из найденных в этом ряду подходящих пар.

file = open("in")
n = int(file.readline())
d = {}
for _ in range(n):
    row, seat = map(int, file.readline().split())
    d[row] = d.get(row, []) + [seat]
file.close()
for row in sorted(d, reverse=True): # возвращает список отсортированных ключей словаря
    seats = sorted(d[row])
    for i in range(1, len(seats)):
        if seats[i] - seats[i-1] == 3:
            print(row, seats[i-1] + 1)
            break

# 7
# Предприятие производит закупку изделий A и B, на которую выделена определённая сумма денег. 
# У поставщика есть в наличии различные модификации этих изделий по различной цене.
#  При покупке необходимо руководствоваться следующими правилами:
# 1.  Нужно купить как можно больше изделий, независимо от их типа и модификации.
# 2.  Если можно разными способами купить максимальное количество изделий, нужно выбрать тот способ, 
# при котором будет куплено как можно больше изделий A.
# 3.  Если можно разными способами купить максимальное количество изделий с одинаковым количеством изделий A, 
# нужно выбрать тот способ, при котором вся покупка будет дешевле.
# Определите, сколько всего будет куплено изделий A и какая сумма останется неиспользованной.
file = open("in")
n, M = map(int, file.readline().split())
a = []
b = []
for _ in range(n):
    price, type = file.readline().split()
    if type == "A":
        a.append(int(price))
    else:
        b.append(int(price))
file.close()
a, b = sorted(a), sorted(b)
S, i, j = 0, 0, 0
while i < len(a) and j < len(b):
    if S + a[i] > M and S + b[j] > M:
        break
    if a[i] <= b[j]:
        if S + a[i] <= M:
            S += a[i]
            i += 1
    else:
        if S + b[j] <= M:
            S += b[j]
            j += 1
if i == len(a):
    while j < len(b):
        if S + b[j] <= M:
            S += b[j]
            j += 1
        else: break
if j == len(b):
    while i < len(a):
        if S + a[i] <= M:
            S += a[i]
            i += 1
        else: break
# i, j # индексы первых невлезших элементов a и b
# Если возможно i двигаем вперед, а j назад
j -= 1
while j >= 0 and i < len(a):
    if S - b[j] + a[i] <= M:
        S = S - b[j] + a[i]
        i += 1
        j -= 1
    else: break
print(i, M - S)

# 8
# UNIX время
# Процессы. Максимальное покрытие на отрезке
file = open("26.txt")
n = int(file.readline())
start_time = 1633305600
end_time = start_time + 604800
k = 0 # количество запущенных процессов на данный момент времени
time_line = [0] * 604800 # заданный временной отрезок (неделя в секундах)
# посекундный перебор
for _ in range(n):
    start_process, end_process = map(int, file.readline().split())
    if (start_process < start_time) and ((end_process > start_time) or (end_process == 0)):
        k += 1 # смотрим, сколько на начало недели у нас уже запущено процессов
    if start_process >= start_time and start_process <= end_time:
        time_line[start_process - start_time] += 1 # запущенные процессы (на какой секунде)
    if end_process >= start_time and end_process <= end_time: 
        time_line[end_process - start_time] -= 1 # закончившиеся процессы (на какой секунде)
file.close()
maxk_process = 0
sum_time = 0
for x in time_line:
    k += x
    if k > maxk_process:
        maxk_process = k
        sum_time = 0
    if k == maxk_process:
        sum_time += 1 # пока текущий макс процесс длится, считаем скольно секунд он длится
print(maxk_process, sum_time)

# 9
file = open("107_26.txt")
n = int(file.readline())
d = {}
for _ in range(n):
    row, place = map(int, file.readline().split())
    d[row] = d.get(row, []) + [place]
file.close()
for row in sorted(d, reverse=True):
    a = sorted(d[row])
    for i in range(len(a)-1):
        if a[i+1] - a[i] == 14:
            print(row, a[i] + 1)
            break 

# 10
size = 10001
pix = [[0] * size for _ in range(size)]
file = open('26.txt')
n = int(file.readline())
for _ in range(n):
    row, num = map(int, file.readline().split())
    pix[row][num] = 1
file.close()

min_row, maxk = 0, 0
for i in range(1, size):
    k = 0
    row = pix[i]
    for x in row:
        if x == 1:
            k += 1
            if k > maxk:
                maxk = k
                min_row = i
        else:
            k = 0
print(maxk, min_row)

