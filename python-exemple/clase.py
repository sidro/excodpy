class Lucruri:

    def setValoare(self, pret, putere, viteza):
        self.pret = pret
        self.putere = putere
        self.viteza = viteza

    def printValoare(self):
        print("""
Pret: {0!s}
Putere: {1!s}
Viteza: {2!s}""".format(self.pret, self.putere, self.viteza))


class Arma(Lucruri):

    print("o arma noua")


topor = Arma()
topor.setValoare(75, 60, 50)
topor.printValoare()
