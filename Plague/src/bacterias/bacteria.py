#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import *

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
		minim = randint(-20,100)
		self.genetica.append(minim) 
		self.genetica.append(randint(minim,100))#temp max 
		for e in range(2,6):
			self.genetica.append(randint(0,100)) 

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
