#! /usr/bin/env	python3.6

class Variabile:

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