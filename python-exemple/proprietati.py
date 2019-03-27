class Jucator:

    def setNume(self, nume):
        self.__nume = nume.upper()

    def getNume(self):
        return self.__nume

    nume = property(getNume, setNume, '', "Proprietati")

<<<<<<< HEAD

def main():
    jucator = Jucator()
    jucator.nume = 'ionel'
    print(jucator.nume, Jucator.nume.__doc__)


if __name__ == '__main__':
    main()
=======
if __name__ == '__main__':
    jucator = Jucator()
    jucator.nume = 'ionel'
    print(jucator.nume, Jucator.nume.__doc__)
>>>>>>> 35741eacd0d09a3c0632de450c3f5630b20527cb
