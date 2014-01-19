class Lucruri:

    def __init__(self, pret, putere, viteza):
            self.pret = pret
            self.putere = putere
            self.viteza = viteza

    def printValoare(self):
        print("""\nPret: {0!s} \nPutere: {1!s}\nViteza: {2!s}"""
              .format(self.pret, self.putere, self.viteza))


class Arma(Lucruri):

    def __init__(self, pret, putere, viteza):
        super().__init__(pret, putere, viteza)
        #daune = self.putere


topor = Arma(30, 50, 60)
topor.printValoare()
