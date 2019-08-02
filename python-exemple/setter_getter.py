#!/usb/bin/python3


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("Too Young")


person = Person("Maria", 16)
print(person.age)
person.age = -23
print(person.age)
