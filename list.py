list = [5, 3, "4dd", True]

list.append("Word")
b = [3, 4, 5, 7]

list.extend(b)
list.remove(5)
list.pop(0)
b.sort()
list.reverse()
print(list)
# print(b)

list.extend([3, 5, True])

print(list[::])
# print(list[2:-2:2])

cor = (5, "stroka", 3, True)  # кортеж менять элементы нельзя
# print(cor[3])

mult = set(list)
print(mult)

fmult = frozenset(list)  # не изменяемый
print(fmult)

dictionary = {'short': 'Gosha', 'long': 'Georgy'} # Словарь
print(dictionary['short'])


