num = int(input("input "))
bool = False

if num > 10 and bool:
    print("num > 10")
    if num > 50:
        print("num > 50")
elif num < 5:
    print("< 5")
else:
    print(" 5 - 10")
print("smthn else")

result = ">5" if num > 5 else "<5"
print(result)
