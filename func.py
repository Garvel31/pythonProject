
# Обычные функции
def func(words="значение по умолчанию"):
    print("Hello world", words)
    # pass ничего не выводит и не возвращает


str = "Gosha"
func(str)
func()


def summ(a, b, c=0):
    res = a + b + c
    return res


result = summ(3, 4, 5)
print(result, "   ", summ(1, 1))  # используется параметр по умолчанию, если подставить то перепишется


def printAll(*params):
    for el in params:
        print(el * 2)
    print("\n")


printAll(4, "word", False)
printAll(43, "wordee", True)


def printDict(**args):
    for key, value in args.items():
        print("Key: ", key, " value: ", value)


printDict(long="Georgy", short="Gosha", x=2)

# Анонимные функции

mult = lambda a, x = 23: a * x

print(mult(2, 5))
print(mult(2, 2))
print(mult(2)) # x задан по умочанию
