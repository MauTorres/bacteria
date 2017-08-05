from random import randint

class Bacteria:
	def __init__(self, nombre):
		self.nombre = nombre
		self.genetica = []

	def setGenetica(self, genetica):
		self.genetica = genetica

	def reproducirse(self):
		pass

	def mutar(self):
		pass

class BacteriaA(Bacteria):
	def __init__(self, nombre):
		Bacteria.__init__(self, nombre)
		for e in range(6):
			self.genetica[e] = uniform(-10,10) 

	def reproducirse(self,bacteriaA):
		bacteriaB = BacteriaA(bacteriaA.nombre + self.nombre)
		for x in range(6):
			bacteriaB.genetica [x] = bacteriaA.genetica [x] + self.genetica [x]
		return bacteriaB

	def mutar(self):
		factor = randint(1,4)
		if factor != 4:
			return
		casilla = randint(0,5)
		mutageno = uniform(-1,1)
		self.genetica [casilla] += self.genetica [casilla]*mutageno

class Entorno:
	def __init__(self, nombreE):
		self.caracteristicas = []
		self.bacteriasSobrev = []
		self.bacteriasDie = []
		self.cunaReprod = []
		self.nombreE = nombreE

	def run(self):
		contNom = 1
		for x in range(randint(2,10)):
			B = BacteriaA(hex(cont).split('x')[-1])
			bacteriasSobrev.append(B)
			contNom++

	def seleccionNat(self):
		cont = 0
		for y in bacteriasSobrev
			for x in bacteriasSobrev[y.genetica]
				if caracteristicas[cont] >= genetica[x]
					A = remove(x)
					bacteriasDie.append(A)
					print("Murió la bacteria %s por las condiciones del entorno",bacteriaA.nombre)
			cont++ 

	def detallar(self):
		for x in bacteriasSobrev
			print("la bacteria %s está viva",x.nombre)
		for y in bacteriasDie
			print("la bacteria %s ha muerto",y.nombre)
			