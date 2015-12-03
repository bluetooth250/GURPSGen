#Generate type by skill (Broadsword, Shortsword, Two-handed Sword, etc.)
#Generate specific weapon (e.g. Thrusting broadsword)
#Generate blade quality (cheap, fine, very fine, superfine)
#Generate blade composition (nanomaterial, monoblade, laser, thermal)
#Generate extra qualities (balanced...)
#Generate flavour

#LaserBlade = {'Damage':4.0,'Divisor':2,'CF':4.0,'Power':'28 strikes'}
#MonoBlade = {'Damage':0.5,'Divisor':10,'CF':8.0,'Power':''}
#NanoBlade = {'Damage':0.0,'Divisor':1,'CF':1.0,'Power':''}
#ThermalBlade = {'Damage':0.5,'Divisor':10,'CF':,'Power':}

import random

### Melee weapon object ###

class MeleeWeapon:
	def __init__(self):			#not finished
		self.swingDam
		self.thrustDam
		self.divisor
		self.CF
		self.notes = ""
	def someFunc(self):
		pass
	def appendNotes(self, notes):
		self.notes += notes

### Quality functions ###

QualityList = ['Cheap','Fine','VeryFine','Superfine','Balanced']
def QualityCheap(MeleeWeapon):
	if ["Fine","VeryFine","SuperFine"] not in MeleeWeapon.keywords:
		pass		#changes go here
	else:
		print("Minor error: tried to assign more than one quality grade to a single weapon.")

def QualityFine(MeleeWeapon):
	if ["Cheap","VeryFine","SuperFine"] not in MeleeWeapon.keywords:
		pass		#changes go here
	else:
		print("Minor error: tried to assign more than one quality grade to a single weapon.")

def QualityVeryFine(MeleeWeapon):
	if ["Cheap","Fine","SuperFine"] not in MeleeWeapon.keywords:
		pass		#changes go here
	else:
		print("Minor error: tried to assign more than one quality grade to a single weapon.")

def QualitySuperFine(MeleeWeapon):
	if ["Cheap","Fine","VeryFine"] not in MeleeWeapon.keywords:
		pass		#changes go here
	else:
		print("Minor error: tried to assign more than one quality grade to a single weapon.")

def QualityBalanced(MeleeWeapon):

### Property functions ###

def MakeLaserBlade(MeleeWeapon):
	MeleeWeapon.damageDice = 4.0
	MeleeWeapon.divisor = 2
	MeleeWeapon.CF += 4.0
	MeleeWeapon.appendNotes("C/28 uses.")

def MakeMonoblade(MeleeWeapon):
	MeleeWeapon.damageDice = 0.0			#???
	MeleeWeapon.divisor = 10
	MeleeWeapon.CF += 8.0
	MeleeWeapon.appendNotes("C/28 uses.")

def MakeNanoblade(MeleeWeapon):
	MeleeWeapon.damageDice = 0.0			#???
	MeleeWeapon.divisor = 2
	MeleeWeapon.CF += 1.0

def MakeThermalBlade(MeleeWeapon):
	MeleeWeapon.damageDice = 0.0			#???
	MeleeWeapon.divisor = 2
	MeleeWeapon.CF += 4.0
	MeleeWeapon.appendNotes("C/28 uses.")		#Not right, but close?

def MakeVibroblade(MeleeWeapon):
	MeleeWeapon.damageDice = 0.0			#???
	MeleeWeapon.divisor = 2
	MeleeWeapon.CF += 4.0
	MeleeWeapon.appendNotes("C/30 uses.")		#Dependent on weight?

###

