import math
import os
import mymodule as my
# from mymodule import printSome - импорт конкретной функции, обращаться напрямую

# print(math.fabs(-23))
# print(os.getcwd())
print(my.some)

my.printSome(my.some)
res = my.summ(2, 2, 4)
print(res)
print(my.summ(4, 5, 6))
