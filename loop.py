i = 0
while i <= 10:
    print("Value: ", i)
    i += 1

list = [6, 6, 4, True, "String"]

k = 0
while k < len(list):
    # break выход из цикла
    if k % 2 == 0:
        k += 1
        continue # прерывание одной итерации
    print(list[k])
    k += 1

print('/****************/')

for item in list:
    print(item)


for char in "Hello world": # перебирает символы
    if char == 'o':
        print('o find')
        break
