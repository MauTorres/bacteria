#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import *
from utils import constantes as const

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
		minim = randint(const.TEMP_MIN,const.TEMP_MAX)
		self.genetica.append(minim) #temp min
		self.genetica.append(randint(minim,const.TEMP_MAX))#temp max 
		for e in range(2,6):
			self.genetica.append(randint(0,100)) 
		self.genetica.append(3) #tiempo de vida

	def reproducirse(self,bacteriaA):
		self.genetica[6] -= 1
		bacteriaA.genetica[6] -= 1
		bacteriaB = BacteriaA(bacteriaA.nombre + self.nombre)
		for x in range(5):
			bacteriaB.genetica [x] = (bacteriaA.genetica [x] + self.genetica [x])/2
			self.mutar()
		return bacteriaB

	def mutar(self):
		factor = randint(1,4)
		if factor != 4:
			return
		casilla = randint(0,5)
		mutageno = uniform(-1,1)
		self.genetica [casilla] += self.genetica [casilla]*mutageno
		
		if self.genetica[0] < -20: 				#temp min
			self.genetica[0] = -20
			return
		
		elif self.genetica[1] > 100:			#temp max
			self.genetica[1] > 100
			return

		for x in range(2,6):
			if self.genetica[casilla] < 0:			#min val permitido en genetica
				self.genetica[x] = 0
				return
		
			elif self.genetica[casilla] > 100:	#max val permitido en genetica
				self.genetica[x] = 100
				return