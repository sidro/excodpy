class Jucator:

    def set_nume(self, nume):
        self.__nume = nume.upper()

    def get_nume(self):
        return self.__nume

    nume = property(get_nume, set_nume, '', "Proprietati")


def main():
    juc = Jucator()
    juc.nume = 'ionel'
    print(juc.nume, Jucator.nume.__doc__)


if __name__ == '__main__':
    main()

if __name__ == '__main__':
    jucator = Jucator()
    jucator.nume = 'ionel'
    print(jucator.nume, Jucator.nume.__doc__)
