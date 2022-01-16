class User:
    name = ""
    surname = ""
    age = 0
    email = ""

    def __init__(self, name = "", surname = "", age = None): # Пустой конструктор
        self.name = name
        self.surname = surname
        self.age = age


    def set(self, name, surname, age):
        self.name = name
        self.age = age
        self.surname = surname

    def printAll(self):
        print("User:", self.name, self.surname, "age:", self.age)


admin = User()
admin.name = "Alex"
admin.age = 23
admin.surname = "Pobeda"
print(admin.name)

bob = User("Bob", "Rogers", 33)
# bob.set("Bob", "Rogers", 33)
print(bob.name, bob.age)
bob.printAll()

construc = User("Constructor", "Constructorovich", 111)
construc.printAll()
