import pygame
import position1 as Position
from labyManager1 import LabyManager
from pygame.locals import * 
from constantes import *

class Perso:
	def __init__(self, pos, lmanager, hasEther = False, hasTube = False, hasNeedle = False, alive = True):
		self.pos = pos
		self.lmanager = lmanager
		self.alive = alive
		self.hasEther = hasEther
		self.hasTube = hasTube
		self.hasNeedle = hasNeedle



	def __str__(self):
		description = "Perso position:\n" + str(self.pos) + "\n"
		description += "alive: " + str(self.alive) + '\n'
		description += "has needle: " + str(self.hasNeedle) + '\n'
		description += "has ether: " + str(self.hasEther) + '\n'
		description += "has tube: " + str(self.hasTube) + '\n'
		return description


	def goLeft(self):
		goingToPos = Position.Position(self.pos.line, self.pos.column - 1)
		self.willStepOnObject(goingToPos)
		if self.lmanager.charAtPosition(goingToPos) != "*" and self.pos.column > 0:
			self.lmanager.updatePersoPositionInLaby(self.pos, goingToPos)
			self.pos = goingToPos
		else:
			pass
    	

	def goRight(self):
		goingToPos = Position.Position(self.pos.line, self.pos.column + 1)
		self.willStepOnObject(goingToPos)
		if self.lmanager.charAtPosition(goingToPos) != "*" and self.pos.column < len(self.lmanager.laby[self.pos.line]) - 1:
			self.lmanager.updatePersoPositionInLaby(self.pos, goingToPos)
			self.pos = goingToPos
		else:
			pass
    	

	def goUp(self):
		goingToPos = Position.Position(self.pos.line - 1, self.pos.column)
		self.willStepOnObject(goingToPos)
		if self.lmanager.charAtPosition(goingToPos) != "*" and self.pos.line > 0:
			self.lmanager.updatePersoPositionInLaby(self.pos, goingToPos)
			self.pos = goingToPos
		else:
			pass
    	

	def goDown(self):
		goingToPos = Position.Position(self.pos.line + 1, self.pos.column)
		self.willStepOnObject(goingToPos)
		if self.lmanager.charAtPosition(goingToPos) != "*" and self.pos.line < len(self.lmanager.laby) - 1:
			self.lmanager.updatePersoPositionInLaby(self.pos, goingToPos)
			self.pos = goingToPos
		else:
			pass

	def willStepOnObject(self, pos):
		if self.lmanager.charAtPosition(pos) == 'N':
			self.hasNeedle = True
		elif self.lmanager.charAtPosition(pos) == 'E':
			self.hasEther = True
		elif self.lmanager.charAtPosition(pos) == 'T':
			self.hasTube = True
		elif self.lmanager.charAtPosition(pos) == 'X':
			if not self.hasAllObjects():
				self.alive = False
	

	def hasAllObjects(self):
		return self.hasNeedle and self.hasTube and self.hasEther


	

	
