### CLASS LIBRARY ###

# This file stores definitions of the classes used for creating beam weapons. This file does not instantiate any of these objects; these are done in separate libraries.

## Beam Type ##

class BeamType:				# Defines the properties of a beam type.
	def __init__(self, name = "", TL = 0, E = 0, divisor = 0, baseAcc = 0, damageType = "", Rb = 0, shotCapacity = 0, Bc = 0, baseLC = 0, diceMult = 1.0, keywords = []):
		self.name = name
		self.TL = TL
		self.E = E
		self.divisor = divisor
		self.baseAcc = baseAcc
		self.damageType = damageType
		self.Rb = Rb
		self.shotCapacity = shotCapacity
		self.Bc = Bc
		self.baseLC = baseLC
		self.diceMult = diceMult
		self.keywords = keywords

## Power Cell ##

class PowerCell:			# Defines the properties of a power cell.
	def __init__(self, name = "", weight = 0.0, multiplier = 0.0, reload = 0):
		self.name = name
		self.weight = weight
		self.multiplier = multiplier
		self.reload = reload

## Configuration ##

class Configuration:			# Defines the properties of a weapon configuration.
	def __init__(self, name = "", accMult = 0, STMult = 0, bulkMult = 0, minBulk = 0, damageMean = 0.0, damageDeviation = 0.0):
		self.name = name
		self.accMult = accMult
		self.STMult = STMult
		self.bulkMult = bulkMult
		self.minBulk = minBulk
		self.damageMean = damageMean
		self.damageDeviation = damageDeviation

## Focal Array ##

class FocalArray:			# Defines the property of a focal array.
	def __init__(self, name = "", Rf = 0.0, F = 0.0):
		self.name = name
		self.Rf = Rf
		self.F = F

## Generator ##

class Generator:			# Defines the properties of the beam generator.
	def __init__(self, name = "", minRoF = 0, maxRoF = 0, G = 1.0, Gc = 1.0):
		self.name = name
		self.minRoF = minRoF
		self.maxRoF = maxRoF
		self.G = G
		self.Gc = Gc
