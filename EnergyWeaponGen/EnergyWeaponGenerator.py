
### BASIC OBJECTS AND RESOURCES ###

import random

from BeamLibrary import *
from PowerCellLibrary import *
from ConfigurationLibrary import *
from FocalLibrary import *
from GeneratorLibrary import *

from FunctionLibrary import AppendToGCSFile, DiceRounder

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
		self.WF = 1.0
		self.malf = 17
		self.qualityNum = 0
		self.shotMultiplier = 1.0
		self.powerCell = BlankCell
		self.expendableMod = 1.0
		self.cosmicMod = 1.0
		self.recoil = 1
		self.notes = ""
		self.keywords = self.beamType.keywords

	def generatorDecide(self):					#Uses the given rate of fire to pick the correct beam generator.
		for each in [SingleShot,SemiAuto,LightAuto,HeavyAuto]:
			if each.minRoF <= self.RoF <= each.maxRoF:
				return each
	def powerCellDecide(self):
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
	def powerCellOverride(self, OverrideString):
		if OverrideString[0] in ["1","2","3","4","5","6","7","8","9"]:
			self.cellNum = eval(OverrideString[0])
			self.powerCell = eval(OverrideString[1])
			if len(OverrideString) > 2:
				if OverrideString[2].casefold() == "x":
					self.expendableMod = 2.0
					print("Trigger 1")
				elif OverrideString[2].casefold() == "s":
					self.cosmicMod = 10.0
		else:
			self.cellNum = 1
			self.powerCell = eval(OverrideString[0])
			if len(OverrideString) > 1:
				if OverrideString[1].casefold() == "x":
					self.expendableMod = 2.0
					print("Trigger 2")
				elif OverrideString[1].casefold() == "s":
					self.cosmicMod = 10.0
	def randomise(self):						#Performs the random generation of internal attributes.
		if RandomGeneration == True:
			self.qualityNum = round(abs(random.gauss(0,0.5)))
		while self.qualityNum > 0 and RandomGeneration == True:
			pass
	def execute(self):						#Performs all the calculcations on internal properties.
		self.generator = self.generatorDecide()
		self.accuracy = round(self.beamType.baseAcc*self.configuration.accMult+0.0001)
		self.halfRange = round(self.damageDice**2*self.beamType.Rb*self.focalArray.Rf)
		self.fullRange = round(self.halfRange*3)
#		self.shots = int((self.expendableMod*self.beamType.shotCapacity*self.powerCell.multiplier*self.cellNum)/(self.damageDice**3))
		self.shots = int((self.expendableMod*self.cosmicMod*self.beamType.shotCapacity*self.powerCell.multiplier*self.cellNum)/(self.damageDice**3))
		self.reload = self.powerCell.reload
		self.emptyWeight = self.focalArray.F*self.generator.G*(self.damageDice/self.beamType.E)**3
		self.keywordCheck()
		self.fullWeight = self.fullWeightCalc()
		self.ST = round(self.configuration.STMult*self.fullWeight**(0.5))
		self.bulk = self.bulkCalc()
		self.cost = round(self.CF*self.emptyWeight*self.beamType.Bc*self.generator.Gc)
		self.LC = self.LCCalc()
		self.skill = self.skillPick()

		if self.expendableMod == 2.0:
			self.appendNotes("Uses nonrechargeable power cells.")

		#Fiddle factors
		if self.configuration == Rifle and self.beamType in [Graser,Rainbow,Xray]:
			self.halfRange *= 1.95
			self.fullRange *= 1.95
	def output(self):
		if "ScatterDualMode" in self.keywords:
			outputString = "\nName: {}\nTL: {}\nDamage: {}\n    Or: {}\nAcc: {}\nRange: {}\nWeight: {}\nRoF: {}\n Or: {}\nShots: {}\nST: {}\nBulk: {}\nRecoil: {}\nMalf: {}\nCost: {}\nLC{}\nNotes: {}"
			print(outputString.format(self.name,self.getTLString(),self.getDamageString(),self.getAltDamageString(self),self.getAccString(),self.getRangeString(),self.getWeightString(),self.getRoFString(),self.getAltRoFString(),self.getShotsString(),self.getSTString(),self.getBulkString(),self.getRecoilString(),str(self.malf),self.getCostString(),self.LC,self.notes)) 
		elif "SecondaryMode" in self.keywords:
			outputString = "\nName: {}\nTL: {}\nDamage: {}\nOr: {}\nAcc: {}\nRange: {}\nWeight: {}\nRoF: {}\nShots: {}\nST: {}\nBulk: {}\nRecoil: {}\nMalf: {}\nCost: {}\nLC{}\nNotes: {}"
			print(outputString.format(self.name,self.getTLString(),self.getDamageString(),self.getAltDamageString(),self.getAccString(),self.getAltRangeString(),self.getWeightString(),self.getRoFString(),self.getAltShotsString(),self.getSTString(),self.getBulkString(),self.getRecoilString(),str(self.malf),self.getCostString(),self.LC,self.notes))
		else:
			outputString = "\nName: {}\nTL: {}\nDamage: {}\nAcc: {}\nRange: {}\nWeight: {}\nRoF: {}\nShots: {}\nST: {}\nBulk: {}\nRecoil: {}\nMalf: {}\nCost: {}\nLC{}\nNotes: {}"
			print(outputString.format(self.name,self.getTLString(),self.getDamageString(),self.getAccString(),self.getRangeString(),self.getWeightString(),self.getRoFString(),self.getShotsString(),self.getSTString(),self.getBulkString(),self.getRecoilString(),str(self.malf),self.getCostString(),self.LC,self.notes))
	def fullWeightCalc(self):
		if self.powerCell in [D,E,F]:
			return round(self.WF*self.emptyWeight,1)
		else:
			return round(self.WF*self.emptyWeight + self.cellNum*self.powerCell.weight,1)
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
	def skillPick(self):
		if "Projector" in self.keywords:
			return "Beam Weapons (Projector)"
		elif self.configuration == Rifle:
			return "Beam Weapons (Rifle)"
		elif self.configuration == Cannon:
			return "Gunner (Beams)"
		else:
			return "Beam Weapons (Pistol)"
	def appendNotes(self,AddedNotes):
		self.notes += AddedNotes + " "
	def getTLString(self):
		if "Superscience" in self.keywords:
			return (str(self.beamType.TL)+"^")
		else:
			return self.beamType.TL
	def getDamageString(self):
		if "Affliction" in self.keywords:
			return ("HT-{}{} aff".format(round(self.damageDice+0.005),self.getDivisorString()))
		elif "Pulsed" in self.keywords:
			return 	"{}{} cr ex".format(DiceRounder(self.damageDice),self.getAltDivisorString())
		elif "Scatterbeam" in self.keywords:
			return (DiceRounder(self.damageDice/4) + self.getDivisorString() + " " + self.beamType.damageType)
		else:
			return (DiceRounder(self.damageDice) + self.getDivisorString() + " " + self.beamType.damageType)
	def getAltDamageString(self):
		if "PulseDualMode" in self.keywords:
			return 	"{}{} cr ex".format(DiceRounder(self.damageDice),self.getAltDivisorString())
		elif "ScatterDualMode" in self.keywords:
			return (DiceRounder(self.damageDice/4) + self.getDivisorString() + " " + self.beamType.damageType)
		elif "StunCapable" in self.keywords:
			pass		# Placeholder for alt damage strings for lightning guns, electron beams and blasters.
		elif self.beamType == Electrolaser:
			pass		# Placeholder for alt damage string for electrolaser
		else:
			print("Warning: Tried to calculate an alternate firing mode when the weapon doesn't have one. No changes have been made.")
			return ""
	def getDivisorString(self):		
		if self.beamType.divisor == 1:
			return ""
		elif self.beamType.divisor > 10:
			return "(∞)"
		else:
			return ("({})".format(round(self.beamType.divisor+0.01)))
	def getAltDivisorString(self):
		if "SecondaryMode" not in self.keywords:
			print("Warning: Tried to calculate an alternate firing mode when the weapon doesn't have one. No changes have been made.")
			return ""
		if self.beamType.divisor == 2:
			return ""
		else:
			return ("({})".format(round((self.beamType.divisor/2)+0.01)))
	def getAccString(self):
		if "Jet" in self.keywords:
			return "Jet"
		else:
			return str(self.accuracy)
	def getRangeString(self):
		if self.beamType in [Graser,Xray] and self.halfRange > 1760:
			return "{}/{} mi.".format(round(self.halfRange/1760.0),round(self.fullRange/1760.0))
		else:
			return "{}/{}".format(self.halfRange,self.fullRange)
	def getAltRangeString(self):
		if self.beamType in [Graser,Xray] and self.halfAltRange > 1760:
			return "{}/{} mi.".format(round(0.5*self.halfRange/1760.0),round(0.5*self.fullRange/1760.0))
		else:
			return "{}/{}".format(0.5*self.halfAltRange,0.5*self.fullAltRange)
	def getWeightString(self):
		if self.cellNum > 1 and self.powerCell in [D,E,F]:
			return "{}/{}{}p".format(self.fullWeight,self.cellNum,self.powerCell.name)
		elif self.cellNum > 1 and self.powerCell not in [D,E,F]:
			return "{}/{}{}".format(self.fullWeight,self.cellNum,self.powerCell.name)
		elif self.cellNum == 1 and self.powerCell in [D,E,F]:
			return "{}/{}p".format(self.fullWeight,self.powerCell.name)
		elif self.cellNum == 1 and self.powerCell not in [D,E,F]:
			return "{}/{}".format(self.fullWeight,self.powerCell.name)
	def getRoFString(self):
		if "Scatterbeam" in self.keywords:
			return "{}x{}".format(self.RoF,self.RoF2)
		else:
			return self.RoF
	def getAltRoFString(self):
		if "ScatterDualMode" in self.keywords:
			return "{}x{}".format(self.RoF,self.RoF2)
	def getShotsString(self):
		return "{}({})".format(self.shots,self.reload)
	def getSTString(self):
		return self.ST
	def getBulkString(self):
		return -self.bulk
	def getRecoilString(self):
		return "Rcl 1"
	def getCostString(self):
		return "${}".format(self.cost)
	def keywordCheck(self):
		if "Cheap" in self.keywords:
			self.malf += -1
			self.CF += -0.5
			self.WF += 0.5
			self.appendNotes("Cheap.")
		if "Expensive" in self.keywords:
			self.CF += 1.0
			self.WF += -1/3
			self.appendNotes("Expensive.")
		if "Rugged" in self.keywords:
			self.CF += 1.0
			self.WF += 0.2
			self.appendNotes("Rugged: +2 HT and double DR.")
		if "Disguised" in self.keywords:
			if weapon.configuration == Beamer:
				self.CF += 1.0
			else:
				self.CF += 4.0
		if "Styled" in self.keywords:
			self.CF += self.styling
			self.appendNotes("Styled: +{} to reactions.".format(self.styling))
		if "Fine" in self.keywords:
			self.accuracy += 1
			self.malf += 1
			self.CF += 1.0
			self.appendNotes("Fine.")
		if "VeryFine" in self.keywords:
			self.accuracy += 2
			self.malf += 2
			self.CF += 5.0
			self.appendNotes("Very Fine.")
		if "FineAcc" in self.keywords:
			self.accuracy += 1
			self.CF += 0.75
			self.appendNotes("Fine (Accurate).")
		if "VeryFineAcc" in self.keywords:
			self.accuracy += 2
			self.CF += 3.75
			self.appendNotes("Very Fine (Accurate).")
		if "FineRel" in self.keywords:
			self.malf += 1
			self.CF += 0.25
			self.appendNotes("Fine (Reliable).")
		if "VeryFineRel" in self.keywords:
			self.malf += 2
			self.CF += 1.25
			self.appendNotes("Very Fine (Reliable).")
		if "Hotshotted" in self.keywords:
			self.malf += -3
			self.damageDice *= 1.3
			self.shots = int(self.shots/2)
			self.appendNotes("Hotshotted.")

		if "BlueGreen" in self.keywords:
			self.halfRange *= 2             # Needs to be rounded?
			self.fullRange *= 2             # Needs to be rounded?
			self.RoF = int(self.RoF/2)
			self.shots = int(self.shots/2)
			self.appendNotes("Blue-green laser: can fire undewater, see UT114.")
		if "Ultraviolet" in self.keywords:
			self.damageDice *= 0.5
			self.halfRange *= 3             # Needs to be rounded?
			self.fullRange *= 3             # Needs to be rounded?
			self.appendNotes("Ultraviolet laser: range in atmosphere cannot exceed 500 yards divided by atmospheric pressure; see UT115.")
		if "Pulsed" in self.keywords:
			pass
		if "PulseDualMode" in self.keywords:
			self.CF += 1.0
			self.appendNotes("Dual-mode beam/pulse laser.")
		if "Scatterbeam" in self.keywords:
			pass
		if "ScatterDualMode" in self.keywords:
			self.CF += 1.0
			self.appendNotes("Dual-mode scatterbeam.")

### FUNCTIONS ###

def RapidFireChance(weapon):	#Needs fixing; code should be keyword assignment, not execution.
	if "Laser" in weapon.beamType.keywords:
		weapon.RoF = random.choice([12,15,16,20])
		weapon.generatorDecide()
		weapon.keywords.append("RapidFire")
	elif weapon.RoF <= 3:
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
	else:
		pass

def PulseChance(weapon):
	if "PulseCapable" in weapon.keywords:
		PulseProbability = random.random()
		if PulseProbability <= 0.05:
			weapon.keywords.append("PulseDualMode")
			weapon.keywords.append("SecondaryMode")
		elif PulseProbability <= 0.25:
			weapon.keywords.append("Pulsed")

def WavelengthChance(weapon):
	if weapon.beamType == Laser:
		WavelengthProbability = random.random()
		if WavelengthProbability <= 0.05:
			weapon.keywords.append("BlueGreen")
		elif WavelengthProbability <= 0.1:
			weapon.keywords.append("Ultraviolet")

def ShotgunChance(weapon):
	if "NoShotgun" not in weapon.keywords:
		ShotgunProbability = random.random()
		if weapon.configuration.name == "Rifle" and ShotgunProbability <= 0.1:
			weapon.keywords.append("Scatterbeam")
		elif weapon.configuration.name == "Pistol" and ShotgunProbability <= 0.05:
			weapon.keywords.append("Scatterbeam")
	if "Scatterbeam" in weapon.keywords and random.random() <= 0.2:
		weapon.keywords.remove("Scatterbeam")
		weapon.keywords.append("ScatterDualMode")

def ShotVariance(weapon):
	weapon.shotMultiplier = round(random.gauss(1.0,0.08),1)
	weapon.CF += (weapon.shotMultiplier**2)-1

def QualityChance(weapon):
	QualityProbability = random.gauss(0.0,1.0)
	if QualityProbability <= -1.0:
		weapon.keywords.append("Cheap")
	elif QualityProbability >= 1.0:
		weapon.keywords.append("Expensive")

def HotshotChance(weapon):
	HotShotProbability = random.random()
	if HotShotProbabilty >= 0.85:
		weapon.keywords.append("Hotshotted")


### RANDOM GENERATION ###

def RandomGen(InputTL):
	SuperscienceBeams = True				#Switch to enable superscience beam types
	MasterBeamList = [Blaster,Graser,Laser,Neutral,Pulsar,Rainbow,Xray]
	BeamChoiceList = []					#Creating a blank list of beam types to populate later
	
	if SuperscienceBeams == True:				#Testing whether to add superscience beams
		MasterBeamList.extend([Force,Graviton])

	for each in MasterBeamList:				#Populates the list of beam types to choose from
		if each.TL <= InputTL:
			BeamChoiceList.append(each)
	
	while True:
		MyBeam = random.choice(BeamChoiceList)
		MyFocalArray = random.choice([Tiny,VerySmall,VerySmall,Small,Small,Small,Small,Medium,Medium,Medium,Medium,Large,Large,VeryLarge])
		MyConfiguration = random.choice([Beamer,Pistol,Pistol,Pistol,Pistol,Rifle,Rifle,Rifle])
		MyRoF = 3
		MyDamageDice = MyBeam.diceMult*random.gauss(MyConfiguration.damageMean,MyConfiguration.damageDeviation)
	
		MyBeamGun = EnergyWeapon(MyBeam.name,MyBeam.TL,MyBeam,MyFocalArray,MyRoF,MyDamageDice,MyConfiguration)
		MyBeamGun.powerCellDecide()		#These methods should maybe be run by the execute method, so that only one command needs be issued after instantiating the object.
		#MyBeamGun.randomise()			#The only thing to keep in mind is the order of randomly-generating properties internal to the weapon object. Things like pulsing,
		MyBeamGun.execute()			# shotguns, etc. are generated by methods within the object, so the order of the execute method needs to preserve that order,
		MyBeamGun.output()			# both when random generation is active, and when it is not.
		#WeaponNumber += 1
		
		if str.casefold(input("\nDo you want to write this weapon to a GCS equipment file? Y/N\n")) == "y":
			AppendToGCSFile(MyBeamGun)
			
		if input("\nHit enter to design another weapon, enter 'back' to go back.\n") == "":
			print("\n - - -\n")
			continue
		else:
			break

### USER-DEFINED WEAPON ### 

BeamNameList = """
Blaster (TL11)
Cryobeamer (TL10^)
CyclonicBeam (TL10^)
Electrolaser (TL9)
ElectronBeam (TL10^)
EMP (TL9)
Force (TL10^)
Graviton (TL11^)
Graser (TL12)
Laser (TL10)
Lightning (TL7^)
Neural (TL11^)
Neutral (TL11)
PlasmaBeam (TL10^)
PlasmaFlamer (TL9^)
PlasmaGun (TL11^)
Pulsar (TL12^)
Rainbow (TL11)
SonicScreamer (TL9^)
SonicStun (TL10)
Xray (TL11)
\n"""

GeneratorNameList = """
Tiny
VerySmall
Small
Medium
Large
VeryLarge
ExtraLarge
\n"""

PropertyList = """
Cheap
Expensive
Rugged
Disguised
Styled
Fine
VeryFine
FineAcc
VeryFineAcc
FineRel
VeryFineRel
Hotshotted
"""

def UserDefined():
	#UserDefinedWeapon = eval(InputString)
	UserDefinedWeapon = EnergyWeapon()
	while True:
		WeapConf = eval(input("Input configuration: Beamer, Pistol or Rifle\n"))
		WeapBeam = eval(input("Input beam type:" + BeamNameList))
		WeapDice = eval(input("Input damage dice:\n"))
		WeapRoF = eval(input("Input rate of fire: \n"))
		WeapFocal = eval(input("Input focal array:" + GeneratorNameList))
		WeapCell = input("Input power cell combination in the form C, 1A, 2D, etc. Add an X for nonrechargable cells or an S for cosmic/superscience cells (e.g. 4BX, 2CS). Leave blank for automatic power cell allocation.\n")

		WeapWavelength = ""
		WeapScatter = ""
		WeapPulse = ""

		if WeapBeam == Laser:
			WeapWavelength = input("Is this laser near-infrared, blue-green or ultraviolet?\nNear-infrared: Press Enter\nBlue-green: Enter BG\nUltraviolet: Enter UV\n")
		if "NoShotgun" not in WeapBeam.keywords:
			WeapScatter = input("Is this a normal beam weapon, a scatterbeam, or a dual-mode weapon?\nNormal: Press Enter\nScatterbeam: Enter Sc\nDual-mode: Enter Sw\n")
		if "PulseCapable" in WeapBeam.keywords:
			WeapPulse = input("Is this a beam laser, pulse laser, or dual-mode laser?\nBeam: Press Enter\nPulse:Enter P\nDual-mode: Enter D\n")

		WeapTL = WeapBeam.TL
		WeapName = input("Input weapon name, or leave blank for automatic naming.\n")

		if WeapName == "":
			WeapName = "{} {}".format(WeapBeam.name,WeapConf.name)

		UserDefinedWeapon = EnergyWeapon(WeapName,WeapBeam.TL,WeapBeam,WeapFocal,WeapRoF,WeapDice,WeapConf)

		if WeapCell == "":
			UserDefinedWeapon.powerCellDecide()
		else:
			UserDefinedWeapon.powerCellOverride(WeapCell)
			
		if WeapWavelength.casefold() == "bg":
			UserDefinedWeapon.keywords.append("BlueGreen")
		if WeapWavelength.casefold() == "uv":
			UserDefinedWeapon.keywords.append("Ultraviolet")
		if WeapScatter.casefold() == "sc":
			UserDefinedWeapon.keywords.append("Scatterbeam")
		if WeapScatter.casefold() == "sw":
			UserDefinedWeapon.keywords.append("ScatterDualMode")
			UserDefinedWeapon.keywords.append("SecondaryMode")
		if WeapPulse.casefold() == "p":
			UserDefinedWeapon.keywords.append("Pulsed")
		if WeapPulse.casefold() == "d":
			UserDefinedWeapon.keywords.append("PulseDualMode")
			UserDefinedWeapon.keywords.append("SecondaryMode")

		print("Add any extra keywords you'd like, leave blank to stop adding keywords:" + PropertyList)
		WeapKeyword = "."
		while WeapKeyword != "":
			WeapKeyword = input("Input keyword:\n")
			UserDefinedWeapon.keywords.append(WeapKeyword)
			if WeapKeyword == "Styled":
				UserDefinedWeapon.styling = eval(input("Enter the level of styling (must be an integer):\n"))

		UserDefinedWeapon.execute()
		UserDefinedWeapon.output()
		#WeaponNumber += 1

		if str.casefold(input("\nDo you want to write this weapon to a GCS equipment file? Y/N\n")) == "y":
			AppendToGCSFile(UserDefinedWeapon)

		if input("\nHit enter to design another weapon, enter 'back' to go back.\n") == "":
			print("\n - - -\n")
			continue
		else:
			break

def VegaTest():
	VegaMachinePistol = EnergyWeapon("Vega Machine Pistol",12,Pulsar,VerySmall,10,7.0,Pistol)
	VegaMachinePistol.powerCellOverride(4,B)
	VegaMachinePistol.execute()
	VegaMachinePistol.output()


### INPUT ###

RandomGeneration = False					#Just a default to avoid anything breaking
WeaponNumber = 1

while True:
	OpenDecision = input("Hit enter to manually design a beam weapon, or enter a TL for a randomly-generated beam weapon. Enter 'exit' to stop the program.\n")
	if OpenDecision == "":
		UserDefined()
		#UserDefined("Weapon"+str(WeaponNumber))
		WeaponNumber += 1
		continue
	elif OpenDecision in ["9","10","11","12"]:
		InputTL = int(OpenDecision)
		RandomGen(InputTL)
		continue
	elif str.casefold(OpenDecision) == "exit":
		break
	else:
		OpenDecision = input("The TL must be between 9 and 12. Please enter again:\n")
		continue

