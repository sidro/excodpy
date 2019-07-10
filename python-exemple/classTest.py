class Test:
    def __init__(self, name):
        self.name = name

    def get(self, age):
        self.age = age
        data = f"{self.name} + {age}" # variabila data nu poate fi folosita decat in interiorul metodei
                                        # ea neputand fi apelata din exteriorul metodei sau clasei
        return self.data

    def test(self):
        print(data)



t = Test("Popa")
print(t.name)
print(t.get(23))
print(t.age)
t.test()
