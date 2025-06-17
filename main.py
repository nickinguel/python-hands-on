print((15, "Nick"))

for i in range(10):
    print(f"--- ------  {i}")


class Person:
    God = "YHWH"

    def __init__(self, name, age):
        self.father: Person | None = None
        self.__name = name
        self.age = age

    def __str(self):
        return "Mbi la so"

p1 = Person("John", 36)

print(p1.__name)
print(Person.God)
