#!/usr/bin/env python


import sys
import os


from interfaceROS import Robot_properties
 
class Tester:
	def __init__(self):
		self.robot = Robot_properties() #Objet contenant les infos du sub et sub (interface ROS et ici l'image IN et la position OUT


	def updater(self):
		self.traitFiltre(self.robot.imageBrut)#Exemple fonctionnel mais traitement long
	
	def outputPosiAndColor(self, posi, color):
		self.robot.publish(posi, color) 
	

	def traitFiltre(self, image_message):


		self.outputPosiAndColor(self.bord2, self.couleurGob)
		self.outputOpenCVImage(cv_imageCLRGoblet)




