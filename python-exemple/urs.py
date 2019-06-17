# from pudb import set_trace
# pentru a rula acest debuger (pudb) el trebuie instalat


class Mono:
    # set_trace()

    def __init__(self, nume="Vulpea", culoare="portocalie", inaltime=65):
        self.nume = nume
        self.culoare = culoare
        self.inaltime = inaltime

    def prezinta(self):
        print(f'El/Ea este {self.nume}, are culoarea {self.culoare} \
si inaltimea de {self.inaltime} cm.')


m = Mono("Urs", "bruna", 200)
m.prezinta()
# m2 = Mono()  # Prima varianta de a construi
# m2.prezinta()  # un obiect Mono si a apela functia prezinta
Mono().prezinta()  # A doua metoda
