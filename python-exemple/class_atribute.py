class Animal:
    culoare_ = "albastru"

    def __init__(self, nume, culoare):
        self.nume = nume
        self.culoare = culoare


pisica = Animal("pisica", "alba")

print(Animal.culoare_)
Animal.culoare_ = "negru"
print(pisica.culoare_)

caine = Animal("caine", "maro")

Animal.culoare_ = "mov"
print(caine.culoare_)
