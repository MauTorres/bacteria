#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import *
from bacterias import Bacteria as Bac

class Entorno:
	def __init__(self, nombreE):
		self.caracteristicas = []
		self.bacteriasSobrev = []
		self.bacteriasDie = []
		self.cunaReprod = []
		self.nombreE = nombreE
		self.poblar()
		self.weatherGenerate()

	def poblar(self):
		contNom = 1
		for x in range(randint(2,10)):
			B = Bac.BacteriaA(hex(contNom).split('x')[-1])
			self.bacteriasSobrev.append(B)
			contNom += 1

	def imprimeVals(self):
		vals = "Entorno "+ self.nombreE + "\n Temp = " + str(self.caracteristicas[0]) + "\n Luminicencia = " + str(self.caracteristicas[1]) + "\n Humedad = " + str(self.caracteristicas[2])
		print(vals)

	def imprimeBacs(self):
		for v in self.bacteriasSobrev:
			vals = "Bacteria: "+ v.nombre + "\n TempMin = " + str(v.genetica[0]) + "\n TempMax = " + str(v.genetica[1]) + "\n Res.Lumínica = " + str(v.genetica[2]) + "\n Propagación = " + str(v.genetica[3]) + "\n Letalidad = " + str(v.genetica[4]) + "\n Humedad = " + str(v.genetica[5])
			print(vals)

	def weatherGenerate(self):
		self.caracteristicas.append(randint(-20,100))
		self.caracteristicas.append(randint(0,100))
		self.caracteristicas.append(randint(0,100))

	def seleccionNat(self):
		cont = 0
		for y in bacteriasSobrev:
			for x in bacteriasSobrev[y.genetica]:
				if caracteristicas[cont] >= genetica[x]:
					A = remove(x)
					bacteriasDie.append(A)
					print("Murió la bacteria %s por las condiciones del entorno",bacteriaA.nombre)
			cont += 1 

	def detallar(self):
		for x in bacteriasSobrev:
			print("la bacteria %s está viva",x.nombre)
		for y in bacteriasDie:
			print("la bacteria %s ha muerto",y.nombre)
			