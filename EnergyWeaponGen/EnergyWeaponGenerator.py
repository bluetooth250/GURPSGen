from GURPS import DiceRounder


### BEAM TYPES ###

class BeamType:			# Defines the beam type.
	def __init__(self, name = "", TL = 0, E = 0, divisor = 0, baseAcc = 0, damageType = 0, Rb = 0, shotCapacity = 0, Bc = 0, baseLC = 0, diceMult = 1.0, keywords = []):
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
		self.diceMult = diceMult		#This is for random generation only - defines a multiplier for the damage dice to bring it in line with vanilla UT beams.
		self.keywords = keywords

BlankBeam = BeamType()

Blaster = BeamType("Blaster",10,3.0,5,5,"burn sur",32,34,2000,3,1.0)
Force = BeamType("Force beam",10,4.0,1,6,"cr dbkb",11,270,500,4,1.5,["NoShotgun","Superscience"])
Graser = BeamType("Graser",12,3.0,10,6,"burn",6000,28,1500,3,1.0,["Laser","Pulse"])
Graviton = BeamType("Graviton",11,1.5,1000,6,"cr",100,14,2000,3,0.5,["NoShotgun","Superscience"])
Laser = BeamType("Laser",9,3.0,2,6,"burn",40,225,500,3,1.0,["Laser","Pulse"])
Neutral = BeamType("Neutral particle beam",10,3.0,1,5,"burn rad sur",32,17,3000,3,1.0,[])
Pulsar = BeamType("Pulsar",11,6.0,3,5,"cr ex rad sur",8,135,3000,2,2.0,[])
Rainbow = BeamType("Rainbow laser",11,3.0,3,6,"burn",56,112,500,3,1.0,["Laser"])
Xray = BeamType("X-ray laser",11,3.0,5,6,"burn",2000,112,1000,3,1.0,["Laser","Pulse"])

Fire = BeamType("Blazar",10,3.0,1,5,"burn inc",56,112,500,3,1.0,["Incendiary","Superscience"])
Cold = BeamType("Cryobeam",10,4.0,1,6,"burn",11,270,750,3,1.0,["NoShotgun","Superscience"])
#Electric = BeamType("Lightning gun")		#electric = {'TL':10,"E':3.0,"Divisor':1,"BaseAcc':4,"DmgType':'burn sur","Rb':20,"ShotCap':450,"Bc':500,"BaseLC':3} diceMult = 1.0
#Corrosion = BeamType()				#corrosion = {'TL':10,"E':3.0,"Divisor':2,"BaseAcc':6,"DmgType':'cor","Rb':40,"ShotCap':375,"Bc':1000,"BaseLC':3} diceMult = 1.0
#Toxic = BeamType()				#toxic = {'TL':10,"E':1.5,"Divisor':10,"BaseAcc':6,"DmgType':'tox","Rb':32,"ShotCap':15.0,"Bc':4000,"BaseLC':3} diceMult = 0.5

### CONFIGURATIONS ###

class Configuration:		# Defines the properties of a weapon configuration.
	def __init__(self, name = "", accMult = 0, STMult = 0, bulkMult = 0, minBulk = 0):
		self.name = name
		self.accMult = accMult
		self.STMult = STMult
		self.bulkMult = bulkMult
		self.minBulk = minBulk

BlankConfiguration = Configuration()

Beamer = Configuration("Beamer",0.5,3.3,1.0,0)
Pistol = Configuration("Pistol",1.0,3.3,1.25,1)
Rifle = Configuration("Rifle",2.0,2.2,1.5,3)
Cannon = Configuration("Cannon",3.0,2.4,1.5,6)

### FOCAL ARRAYS ##

class FocalArray:		# Defines the property of a focal array.
	def __init__(self, name = "", Rf = 0.0, F = 0.0):
		self.name = name
		self.Rf = Rf
		self.F = F

BlankArray = FocalArray()

Tiny = FocalArray("Tiny",0.1,0.25)
VerySmall = FocalArray("Very small",0.3,0.5)
Small = FocalArray("Small",0.5,0.8)
Medium = FocalArray("Medium",1.0,1.0)
Large = FocalArray("Large",2.0,1.25)
VeryLarge = FocalArray("Very large",4.0,1.6)
ExtraLarge = FocalArray("Extra large",8.0,2.0)

### GENERATOR ###
class Generator:		# Defines the properties of the beam generator.
	def __init__(self, name = "", MinRoF = 0, MaxRoF = 0, G = 1.0, Gc = 1.0):
		self.name = name
		self.MinRoF = MinRoF
		self.MaxRoF = MaxRoF
		self.G = G
		self.Gc = Gc

BlankGenerator = Generator()

SingleShot = Generator("Single shot",1,1,1.0,1.0)
SemiAuto = Generator("Semi automatic",2,3,1.25,1.0)
LightAuto = Generator("Light automatic",4,10,1.25,2.0)
HeavyAuto = Generator("Heavy automatic",11,20,2.0,2.0)

### POWER CELLS ###

class PowerCell:		# Defines the properties of a power cell.
	def __init__(self, name = "", weight = 0.0, multiplier = 0.0, reload = 0):
		self.name = name
		self.weight = weight
		self.multiplier = multiplier
		self.reload = reload

BlankCell = PowerCell()

A = PowerCell("A",0.005,0.01,3)
B = PowerCell("B",0.05,0.1,3)
C = PowerCell("C",0.5,1.0,3)
D = PowerCell("D",5.0,10.0,5)
E = PowerCell("E",20.0,100.0,5)
F = PowerCell("F",200.0,1000.0,5)

### MAIN WEAPON OBJECT ###

class EnergyWeapon:
	def __init__(self, name = "no name assigned", weapTL = 0, beamType = BlankBeam, focalArray = BlankArray, RoF = 0, damageDice = 0.0, configuration = BlankConfiguration):
		#These are external properties read in during instantiation.
		self.name = name
		self.weapTL = weapTL
		self.beamType = beamType
		self.focalArray = focalArray
		self.RoF = RoF
		self.damageDice = damageDice
		self.configuration = configuration

		#These are internal properties initialised during instantiation, to be modified by internal functions.
		self.RoF2 = 1
		self.CF = 1.0
		self.malf = 17
		self.shotMultiplier = 1.0
		self.weightMultiplier = 1.0
		self.powerCell = BlankCell
		self.notes = ""
		self.keywords = []

	def generatorDecide(self):					#Uses the given rate of fire to pick the correct beam generator.
		if self.RoF >= 11:
			return HeavyAuto
		elif self.RoF >= 4:
			return LightAuto
		elif self.RoF >= 2:
			return SemiAuto
		elif self.RoF == 1:
			return SingleShot
		else:
			return BlankGenerator
	def powerCellDecide(self):					#Decides what type of power cell to use and how many. Use only one power cell method, not both.
		if self.configuration == Beamer:
			self.powerCell = B
			if self.damageDice >= 3.0:
				self.cellNum = 2
			else:
				self.cellNum = 1
		elif self.configuration == Pistol:
			self.powerCell = C
			if self.damageDice >= self.beamType.diceMult*3.65:
				self.cellNum = 2
			else:
				self.cellNum = 1
		elif self.configuration == Rifle:
			if self.damageDice >= self.beamType.diceMult*5.5:
				self.powerCell = D
				self.cellNum = 1
			else:
				self.powerCell = C
				self.cellNum = 2
		elif self.configuration == Cannon:
			pass
		else:
			self.powerCell = BlankCell
	def powerCellOverride(self,Number = 0,Cell = BlankCell):	#Reads in what type of power cell to use and how many. Use only one power cell method, not both.
		self.powerCell = Cell
		self.cellNum = Number
	def randomise(self):						#Performs the random generation of internal attributes.
		if RandomGeneration == True:
			PulseChance(self)
			WavelengthChance(self)
			ShotgunChance(self)
			QualityChance(self)
			ShotVariance(self)
			RapidFire(self)					#Not yet implemented
			Features(self)					#Not yet implemented
			Accessories(self)				#Not yet implemented
			Manufacturer(self)				#Not yet implemented
	def execute(self):						#Performs all the calculcations on internal properties.
		self.generator = self.generatorDecide()
		self.accuracy = self.accuracyCalc()
		self.halfRange = round(self.damageDice*self.beamType.Rb*self.focalArray.Rf)
		self.fullRange = round(self.halfRange*3)
		self.shots = 0.0						#Not yet implemented
		self.reload = self.powerCell.reload
		self.emptyWeight = self.weightMultiplier*self.focalArray.F*self.generator.G*(self.damageDice/self.beamType.E**3)
		self.fullWeight = self.fullWeightCalc()
		self.ST = round(self.configuration.STMult*self.fullWeight**(0.5))
		self.bulk = self.bulkCalc()
		self.cost = round(self.CF*self.emptyWeight*self.beamType.Bc*self.generator.Gc)
		self.LC = self.LCCalc()
		self.skill = self.skillChoice()
	def output(self):
		pass
	def accuracyCalc(self):
		TempAcc = round(self.beamType.baseAcc*self.configuration.accMult)
		if TempAcc == 2.5:
			return 3
		else:
			return TempAcc
	def fullWeightCalc(self):
		if self.powerCell in [D,E,F]:
			return round(self.emptyWeight,1)
		else:
			return round(self.emptyWeight + self.cellNum*self.powerCell.weight,1)
	def bulkCalc(self):
		TempBulk = round(self.configuration.bulkMult*self.fullWeight**(0.5))
		if TempBulk < self.configuration.minBulk:
			return self.configuration.minBulk
		else:
			return TempBulk
	def LCCalc(self):
		if self.fullWeight > 15.0:
			return self.beamType.baseLC-2
		elif self.fullWeight > 5.0:
			return self.beamType.baseLC-1
		else:
			return self.beamType.baseLC
	def skillChoice(self):
		if self.configuration == Rifle:
			return "Beam Weapons (Rifle)"
		elif self.configuration == Cannon:
			return "Gunner (Beams)"
		else:
			return "Beam Weapons (Pistol)"
	def pulseThing(self):
		pass
	def wavelengthThing(self):
		pass
	def shotgunThing(self):
		pass
	def appendNotes(self,AddedNotes):
		self.notes += AddedNotes + " "
	def getDamageString(self):
		return (DiceRounder(self.damageDice) + self.getDivisorString() + " " + self.beamType.damageType)
	def getDivisorString(self):
		if self.beamType.divisor == 1:
			return ""
		elif self.beamType.divisor == 2.5:
			return "(3)"
		elif self.beamType.divisor > 10:
			return "(∞)"
		else:
			return ("({})".format(str(self.beamType.divisor)))
	def getAccString(self):
		return str(self.accuracy)
	def getRangeString(self):
		return "{}/{}".format(str(self.halfRange),str(self.fullRange))
	def getWeightString(self):
		if self.cellNum > 1:
			return "{}/{}{}".format(str(self.fullWeight),str(self.cellNum),self.powerCell.name)
		else:
			return "{}/{}".format(str(self.fullWeight),self.powerCell.name)
		if self.powerCell in [D,E,F]:
			WeightString += "p"
	def getRoFString(self):
		if RoF2 == 1:
			return str(self.RoF)
		else:
			return "{}x{}".format(str(self.RoF),str(self.RoF2))
	def getShotsString(self):
		return "{}({})",format(str(self.shots),str(self.reload))
	def getSTString(self):
		return str(self.ST)
	def getBulkString(self):
		return self.bulk		#Can't remember whether it returns a negative value or not, test that and fix if necessary
	def getRecoilString(self):
		return "Rcl 1"
	def getCostString(self):
		return "${}".format(str(self.cost))
	def getLCString(self):
		return "LC{}".format(str(self.LC))


### FUNCTIONS ###

#To Do:
# Rapid fire
# Properties
# Manufacturers

def RapidFire(weapon):
	if weapon.RoF <= 3:
		weapon.RoF = 10
		weapon.generatorDecide()
		weapon.keywords.append("RapidFire")
	elif weapon.RoF < 10:
		weapon.RoF = random.choice([10,12])
		weapon.generatorDecide()
		weapon.keywords.append("RapidFire")
	elif weapon.RoF == 10:
		weapon.RoF = random.choice([12,15,16,20])
		weapon.generatorDecide()
		weapon.keywords.append("RapidFire")

def PulseChance(weapon):
	if "Pulse" in weapon.BeamType.keywords:
		PulseProbability = random.random()
		if PulseProbability >= 0.95:
			weapon.pulse = True
			weapon.keywords.append("Pulsed")
			#Dual-mode continuous/pulsed lasers not yet implemented
		elif PulseProbability >= 0.75:
			weapon.pulse = True
			weapon.keywords("Pulsed")
		else:
			weapon.pulse = False
	else:
		weapon.pulse = False

def WavelengthChance(weapon):
	if "Laser" in weapon.BeamType.keywords:
		WavelengthProbability = random.random()
		if WavelengthProbability >= 0.95:
			weapon.wavelength = "Ultraviolet"
		elif WavelengthProbability >= 0.9:
			weapon.wavelength = "Blue-green"
		else:
			weapon.wavelength = "Infrared"
	else:
		weapon.wavelength = ""

def ShotgunChance(weapon):
	if "NoShotgun" not in weapon.BeamType.keywords:
		ShotgunProbability = random.random()
		if weapon.configuration.name == "Rifle" and ShotgunProbability >= 0.9:
			weapon.keywords.append("Shotgun")
		elif weapon.configuration.name == "Pistol" and ShotgunProbability >= 0.95:
			weapon.keywords.append("Shotgun")
	if "Shotgun" in weapon.keywords and random.random() >= 0.8:
		weapon.CF += 1.0
		weapon.appendNotes("Scatterbeam: can be switched between ordinary moder and shotgun mode.")
		#Switchable scatterbeams are not yet implemented.

def ShotVariance(weapon):
	weapon.shotMultiplier = round(random.gauss(1.0,0.08),1)
	weapon.CF += (weapon.shotMultiplier**2)-1

def QualityChance(weapon):
	QualityProbability = random.gauss(0.0,1.0)
	if QualityProbability <= -1.0:
		weapon.keywords.append("Cheap")
		weapon.weightMultiplier *= 1.5
		weapon.CF += -0.5
		weapon.malf += -1
		weapon.appendNotes("Cheap.")
	elif QualityProbability >= 1.0:
		weapon.keywords.append("Expensive")
		weightMultiplier *= 2/3
		weapon.CF += 1.0
		weapon.appendNotes("Expensive.")



### RANDOM GENERATION ###

RandomGeneration = True					#Switch to enable random generation of properties

#Beam type

SuperscienceBeams = True				#Switch to enable superscience beam types
ElementalBeams = False					#Switch to enable elemental beam types
InputTL = 12						#A read-in TL for random generation

MasterBeamList = [Blaster,Graser,Laser,Neutral,Pulsar,Rainbow,Xray]
BeamChoiceList = []					#Creating a blank list of beam types to populate later

if SuperscienceBeams == True:				#Testing whether to add the vanilla superscience beams
	MasterBeamList.extend([Force,Graviton])
if ElementalBeams == True:				#Testing whether to add the elemental beams
	MasterBeamList.extend([Fire,Cold,Electric,Corrosion,Toxic])

for each in MasterBeamList:				#Populates the list of beam types to choose from
	if each.TL <= InputTL:
		BeamChoiceList.append(each)

#MyBeam = random.choice(BeamChoiceList)

#Focal array

#Rate of fire

#Damage dice

#Configuration

#MyConfiguration = random.choice([Beamer,Pistol,Rifle])

#Final running
#MyBeamGun = EnergyWeapon("MyName",InputTL,MyBeam,MyFocalArray,MyRoF,MyDamageDice,MyConfiguration)
#MyBeamGun.powerCellDecide()		#These methods should maybe be run by the execute method, so that only one command needs be issued after instantiating the object.
#MyBeamGun.randomise()			#The only thing to keep in mind is the order of randomly-generating properties internal to the weapon object. Things like pulsing,
#MyBeamGun.execute()			# shotguns, etc. are generated by methods within the object, so the order of the execute method needs to preserve that order,
#MyBeamGun.output()			# both when random generation is active, and when it is not.

### USER-DEFINED WEAPON ### 

RandomGeneration = False

VegaMachinePistol = EnergyWeapon("Vega Machine Pistol",12,Pulsar,VerySmall,10,7.0,Pistol)
VegaMachinePistol.powerCellOverride(4,B)
VegaMachinePistol.execute()
VegaMachinePistol.output()


