# Exeptions
a = int(input())
user_input_b = False

while user_input_b == False:
    try:
        b = int(input())
        user_input_b = True
    except ValueError:
        print("input num")
print(a + b)

print("/***************/")
# File
# str = input("Type text: ")
str = "22"

file = open('data/text.txt', 'a')
file.write(str)
file.close()

try:
    file = open('data/text2.txt', 'rt')
    print(file.read(10))
    for line in file:
        print(line)
    file.close()
except FileNotFoundError:
    print("File not found")
