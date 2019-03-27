#! /usr/bin/env    python3.6


class Variabile:
<<<<<<< HEAD

    global fred, pete, maria
    maria = 5
    fred = 1
    pete = 2

    def vari(self):
        self.maria = 3
        self.dave = fred + pete + self.maria
        print(pete)
        # return

    print(maria)


v = Variabile()
v.vari()
print(v.dave)
print(v.maria)
=======

	def __init__(self, fred = 1, pete = 2):
		self.fred = fred
		self.pete = pete


	def variabile(self):
		self.dave = self.fred + self.pete
		return vars()

if __name__ == "__main__":
	v = Variabile()
	print(v.variabile())
	print(v.dave)
>>>>>>> 35741eacd0d09a3c0632de450c3f5630b20527cb
