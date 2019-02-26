class Jucator:

    def setNume(self, nume):
        self.__nume = nume.upper()

    def getNume(self):
        return self.__nume

    nume = property(getNume, setNume, '', "Proprietati")

if __name__ == '__main__':
    jucator = Jucator()
    jucator.nume = 'ionel'
    print(jucator.nume, Jucator.nume.__doc__)
