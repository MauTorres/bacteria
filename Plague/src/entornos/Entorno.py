#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import *
from bacterias import Bacteria as Bac
from utils import constantes as const

class Entorno:
	def __init__(self, nombreE):
		self.caracteristicas = []
		self.bacteriasSobrev = []
		self.bacteriasDie = []
		self.cunaReprod = []
		self.nombreE = nombreE

	def poblar(self):
		contNom = 1
		for x in range(randint(const.LIMITE_INF,const.LIMITE_SUP)):
			B = Bac.BacteriaA(hex(contNom).split('x')[-1])
			self.bacteriasSobrev.append(B)
			contNom += 1

	def imprimeVals(self):
		vals = "Entorno "+ self.nombreE + "\n Temp = " + str(self.caracteristicas[0]) + "\n Luminicencia = " + str(self.caracteristicas[1]) + "\n Humedad = " + str(self.caracteristicas[2])
		print(vals)

	def imprimeBacs(self):
		for v in self.bacteriasSobrev:
			vals = "Bacteria: "+ str(v.nombre) + " TempMin = " + str(v.genetica[0]) + " TempMax = " + str(v.genetica[1]) + " Res.Lumínica = " + str(v.genetica[2]) + " Propagación = " + str(v.genetica[3]) + " Letalidad = " + str(v.genetica[4]) + " Humedad = " + str(v.genetica[5]) + " Tiempo de vida = " + str(v.genetica[6])
			print(vals)

	def weatherGenerate(self):
		self.caracteristicas.append(randint(const.TEMP_MIN,const.TEMP_MAX))					#temperatura del entorno
		self.caracteristicas.append(randint(const.LUMINOSIDAD_MIN,const.LUMINOSIDAD_MAX))	#Cantidad de luz del entorno
		self.caracteristicas.append(randint(const.HUMEDAD_MIN,const.HUMEDAD_MAX))			#Porcentaje de humedad del entorno

	def validar(self):
		for bSobrev in self.bacteriasSobrev:
			#for gen in range bSobrev.genetica: nos permitía recorrer cada gen entre valores del 0 al 100
			if self.caracteristicas[0] < bSobrev.genetica[0] or self.caracteristicas[0] > bSobrev.genetica[1]:
				print("La bacteria %s murió a causa de la temperatura en su entorno",bSobrev.nombre) #validando temp min y max
				#self.bacteriasDie.append(bSobrev)
				self.bacteriasSobrev.remove(bSobrev)
			elif	self.caracteristicas[1] >= bSobrev.genetica[2]:
				print("La bacteria %s murió a causa de una menor resistencia a la cantidad de luz  que la de su entorno",bSobrev.nombre)
				#self.bacteriasDie.append(bSobrev)
				self.bacteriasSobrev.remove(bSobrev)
			elif	self.caracteristicas[2] >= bSobrev.genetica[5]:
				print("La bacteria %s murió a por una mayor humedad en su entorno",bSobrev.nombre)
				#self.bacteriasDie.append(bSobrev)
				self.bacteriasSobrev.remove(bSobrev)
			elif bSobrev.genetica[6] == 1 :
				print("Terminó el tiempo de Vida de la bacteria %s",bSobrev.nombre)
				#self.bacteriasDie.append(bSobrev)
				self.bacteriasSobrev.remove(bSobrev)

	def seleccionNat(self):
		self.validar()
		numBacS=len(self.bacteriasSobrev)
		for x in range(numBacS-1):
			self.bacteriasSobrev[x].mutar()
			for y in range(numBacS):
				if (x + y + 1) == numBacS:
					continue
				child = self.bacteriasSobrev[x].reproducirse(self.bacteriasSobrev[x + y + 1])
				self.bacteriasSobrev.append(child)


	def detallar(self):
		for x in bacteriasSobrev:
			print("la bacteria %s está viva",x.nombre)
		for y in bacteriasDie:
			print("la bacteria %s ha muerto",y.nombre)
			
	def run(self):
		count = 0
		self.weatherGenerate()
		self.poblar()
		self.imprimeVals()
		while count < const.ITERACIONES_MAX:
			print(">>>>>>>>>>>>>>>>>>>>>            Generación " + str(count) + "        <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
			self.seleccionNat()
			self.imprimeBacs()
			count += 1