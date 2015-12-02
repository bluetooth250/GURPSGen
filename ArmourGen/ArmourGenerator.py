
### SURFACE AREAS ###
  # Defines the hit locations on a humanoid body by their surface area in square feet.

Vitals = 1.0
Groin = 0.35

Skull = 1.4
Face = 0.7
Neck = 0.35
Chest = 5.25
Abdomen = 1.75
Shoulders = 0.7
UpperArms = 0.7
lbows = 0.35
Forearms = 1.75
Hands = 0.7
Thighs = 3.15
Knees = 0.35
Shins = 3.5
Feet = 0.7

Head = 2.1
Torso = 7.0
Arms = 3.5
Legs = 7.0

### CONSTRUCTIONS ###
  # Defines the class used for armour constructions and instantiates the known construction types.

class ArmourConstruction:
	def __init__(self, name = "BLANK CONSTRUCTION", TL = 0, CW = 0.0, CC = 0.0, don = 0.0, minDR = 0, keywords = []):
		self.name = name
		self.TL = TL
		self.CW = CW
		self.CC = CC
		self.don = don
		self.minDR = minDR
		self.keywords = keywords

#Structure for declaring new types is: Name = ArmourConstruction("Name",TL,CW,CC,don,minDR,["KeywordOne","KeywordTwo"])
  #TL and minDR should be integers; all other numbers should be floats.
  #If no keywords are being used, the keywords should be given as [] so the list is empty, rather than [""] (which is a list containing a single empty string)

  #Keywords:
	#HalfVsNonCrushing - normal DR vs. crushing, half against anything else.
	#WeakToCrushing - suffers reduced DR to crushing attacks (usually mail or scale, etc.).
	#WeakToImpaling - suffers reduced DR to impaling attacks (usually fabric armours).

Fabric = ArmourConstruction("Fabric",0,1.0,1.0,2.14,1,["WeakToImpaling"])
LayeredFabric = ArmourConstruction("Layered fabric",0,1.2,1.5,4.28,2,[])
Scale = ArmourConstruction("Scale",1,1.1,0.8,4.28,2,["WeakToCrushing"])
Mail = ArmourConstruction("Mail",2,0.9,1.2,2.14,2,["WeakToCrushing"])
SegmentedPlate = ArmourConstruction("Segmented plate",2,1.45,1.5,6.42,3,[])
Plate = ArmourConstruction("Plate",1,0.8,5.0,6.42,3,[])
Solid = ArmourConstruction("Solid",1,1.0,1.0,2.0,10,[])

ImpactAbsorbing = ArmourConstruction("Impact-absorbing",6,0.65,5.0,6.42,2,["HalfVsNonCrushing"])
OptimisedFabric = ArmourConstruction("Optimised fabric",6,0.8,2.0,2.14,2,[])


### MATERIALS ###
  # Defines the class used for armour materials and instantiates the known material types.

# Todo DF: dragonhide, meteoric iron, dragonbone
# Todo Py: add ImpactAbsorbing and OptimisedFabric constructions to existing materials; reconcile naming and stats of Pyramid 85 materials with regular ones

class ArmourMaterial:
	def __init__(self, name = "BLANK MATERIAL", TL = 0, WM = 0, CM = 0, maxDR = 0, constructions = [], keywords = []):
		self.name = name
		self.TL = TL
		self.WM = WM
		self.CM = CM
		self.maxDR = maxDR
		self.constructions = constructions
		self.keywords = keywords

# Structure for declaring new types is: Name = ArmourMaterial("Name",TL,WM,CM,maxDR,[Construction1,Construction2],["KeywordOne","KeywordTwo"])
  #TL and maxDR should be integers; all other numbers should be floats.
  #If no keywords are being used, the keywords should be given as [] so the list is empty, rather than [""] (which is a list containing a single empty string).

  # Keywords:
	# Ballistic - has increased DR against piercing and cutting attacks; the multiplier is defined at the bottom of this section.
	# Bio - has 3x DR against burning and cutting attacks and can self-repair.
	# Combustible - if DR is penetrated by burning damage, can catch on fire.
	# EnergyAblative - 6x DR against lasers but increased DR is ablative.
	# FireResistant - 4x DR against burning damage.
	# Flexible - if the armour has less than a quarter of the material's DR per inch it's flexible but easier to don.
	# LaserOnly - DR protects against lasers only; no DR against any other attacks.
	# ReactionsP2 - gives +2 to reactions.
	# ReactionsP3 - gives +3 to reactions.
	# SemiAblative - DR is semi-ablative.
	# SilkBenefits - has benefits against infection, barbed attacks, and blood agents and contact poisons.
	# Transparent - the material can be transparent, providing no DR vs visible-light lasers for double cost.

	#TL0-4 - Low-Tech materials. 
#TL0:
Bone = ArmourMaterial("Bone",0,1.0,12.5,4,[Scale,Solid],["SemiAblative"])
Cloth = ArmourMaterial("Cloth",0,0.85,8.0,4,[Fabric],["Combustible","Flexible"])
Horn = ArmourMaterial("Horn",0,1.0,12.5,4,[Scale,Solid],[])
Leather = ArmourMaterial("Leather",0,0.9,10.0,4,[Fabric,LayeredFabric,Scale],["Combustible","Flexible"])
Silk = ArmourMaterial("Silk",0,0.85,160,4,[Fabric],["Combustible","Flexible","SilkBenefits"])
Wood = ArmourMaterial("Wood",0,1.4,3.0,2,[Scale,Solid],["Combustible","SemiAblative"])
#TL1:
CheapBronze = ArmourMaterial("Bronze, cheap",1,0.9,60.0,9,[Mail,Plate,SegmentedPlate,Scale,Solid],[])
GoodBronze = ArmourMaterial("Bronze, good",1,0.6,100.0,14,[Mail,Plate,SegmentedPlate,Scale,Solid],[])
Copper = ArmourMaterial("Copper",1,1.6,80.0,5,[Mail,Plate,SegmentedPlate,Scale,Solid],[])
Stone = ArmourMaterial("Stone",1,1.2,12.5,5,[Scale,Solid],["SemiAblative"])
Jade = ArmourMaterial("Jade",1,1.2,62.5,5,[Scale,Solid],["ReactionsP2","SemiAblative"])
GemJade = ArmourMaterial("Jade, gem-quality",1,1.2,125.0,5,[Scale,Solid],["ReactionsP3","SemiAblative"])
#TL2:
CheapIron = ArmourMaterial("Iron, cheap",2,0.8,15.0,10,[Mail,Plate,SegmentedPlate,Scale,Solid],[])
GoodIron = ArmourMaterial("Iron, good",2,0.6,25.0,14,[Mail,Plate,SegmentedPlate,Scale,Solid],[])
Lead = ArmourMaterial("Lead",2,2.0,12.5,4,[Plate,SegmentedPlate,Scale,Solid],[])
#TL3:
StrongSteel = ArmourMaterial("Steel, strong",3,0.58,50.0,14,[Mail,Plate,SegmentedPlate,Scale,Solid],[])
#TL4:
HardSteel = ArmourMaterial("Steel, hard",4,0.5,250.0,16,[Mail,Plate,SegmentedPlate,Scale,Solid],[])

	#TL5-8 - High-Tech materials.
#TL6:
Aluminium = ArmourMaterial("Aluminium",6,0.45,15.0,5.0,[Mail,Plate,SegmentedPlate,Scale,Solid],[])
#TL7:
VeryHardSteel = ArmourMaterial("Steel, very hard",7,0.45,20.0,18,[Mail,Plate,SegmentedPlate,Scale,Solid],[])
Titanium = ArmourMaterial("Titanium",7,0.4,50.0,12,[Mail,Plate,SegmentedPlate,Scale,Solid],[])
#TL8:
Aramid = ArmourMaterial("Aramid fabric",8,0.16,80.0,6,[Fabric,LayeredFabric],["Ballistic","Flexible"])

	#TL9-12 - Ultra-Tech materials.
#TL9:
Ablative = ArmourMaterial("Ablative",9,0.071,150,7,[Fabric,LayeredFabric],["EnergyAblative","Flexible"])
AdvMetallicLaminate = ArmourMaterial("Advanced metallic laminate",9,0.071,10,45,[Plate,SegmentedPlate,Scale,Solid],[])
Reflec = ArmourMaterial("Reflec",9,0.0048,150,30,[Fabric,LayeredFabric],["LaserOnly","Flexible"])
Reflex = ArmourMaterial("Reflex",9,0.071,150,7,[Fabric,LayeredFabric],["Ballistic","Flexible"])
#TL10:
AblativeNanoplas = ArmourMaterial("Ablative nanoplas",10,0.048,150,10,[Fabric,LayeredFabric],["EnergyAblative","Flexible"])
Nanocomposite = ArmourMaterial("Nanocomposite",10,0.048,10,60,[Mail,Plate,SegmentedPlate,Scale,Solid],[])
Bioplas = ArmourMaterial("Bioplas",10,0.034,600,7,[Fabric,LayeredFabric],["Bio","Flexible","Transparent"])
Nanoweave = ArmourMaterial("Nanoweave",10,0.048,150,10,[Fabric,LayeredFabric],["Ballistic","Flexible"])
#TL11:
Monocrys = ArmourMaterial("Monocrys",11,0.036,150,15,[Fabric,LayeredFabric],["Ballistic","Flexible"])
Diamondoid = ArmourMaterial("Diamondoid",11,0.036,10,90,[Mail,Plate,SegmentedPlate,Scale,Solid],[])
#TL12:
EnergyCloth = ArmourMaterial("Energy cloth",12,0.0095,500,45,[Fabric,LayeredFabric],["Flexible"])
ExoticLaminate = ArmourMaterial("Exotic laminate",12,0.024,10,135,[Mail,Plate,SegmentedPlate,Scale,Solid],[])

	#TL^ - Superscience, mythical and divergent materials. The TL property is approximate, since this is not given in the article.
Adamant = ArmourMaterial("Adamant",1,0.33,900.0,15,[Scale,Solid],["SemiAblative","Superscience"])
EssentialWood = ArmourMaterial("Essential wood",0,0.467,300.0,12,[Plate,SegmentedPlate,Scale,Solid],["SemiAblative","Superscience"])
Orichalcum = ArmourMaterial("Orichalcum",1,0.2,3000.0,41,[Mail,Plate,SegmentedPlate,Scale,Solid],["Superscience"])
Spidersilk = ArmourMaterial("Spidersilk",1,0.16,80.0,6,[Fabric,LayeredFabric],["Ballistic","Flexible","SilkBenefits","Superscience"]) #Clone of aramid. Use stats from LT/DF?

MeteoricIron = ArmourMaterial("Meteoric iron",2,[Mail,Plate,SegmentedPlate,Scale,Solid],["Superscience"])		#Clone of strong steel, with extra cost and some notes.
Dragonbone = ArmourMaterial("Dragonbone",0,[Plate,SegmentedPlate,Scale],["Superscience"])				#Clone of strong steel, with extra cost and some notes.
Dragonhide = ArmourMaterial("Dragonhide",0,[Fabric,LayeredFabric,Scale],["Flexible","Superscience"])			#Leather that is heavier, stronger, and much more expensive.

#

BallisticDRMult = {Spidersilk:3.0,Aramid:3.0,Reflex:3.0,Nanoweave:3.0,Monocrys:3.0,}
#BallisticDRMult = {Spidersilk:3.0,Aramid:3.0,Reflex:3.0,Nanoweave:3.0,Monocrys:3.0,Nylon:2.0,BallisticPolymer:2.5,ImpBallisticPolymer:2.5,Kevlar:4.0,ImpKevlar:3.0,Arachnoweave:4.0,BasicNanoweave:3.0,MagneticLiquidArmour:2.0,STFLiquidArmour:3.0}

DRPerInch = {Cloth:4.0,Leather:8.0,Silk:4.0,Aramid:12.0,Ablative:24+4,Reflec:120,Reflex:24+4,AblativeNanoplas:36+4,Bioplas:30.0,Nanoweave:36+4,Monocrys:48+4,EnergyCloth:180.0,Spidersilk:12.0}

# No DR/inch quantity is known for the Ultra-Tech materials. UT allows these armours to be made in heavy versions, which have 1.5x DR and are still flexible. Since this is the
# max DR they can have, then the limit for them being flexible is either equal to this or higher. And since this is their maixmum DR, the difference is not important. Thus, the
# lower bound of the material's DR per inch is baseDR*1.5*4, or baseDR*6. An extra +4 has been added, since their max DR is given by the tactical vests' DR, which is 1 more than
# the value used above (thus needs to be multiplied by 4 because we're checking for 25%).

BoneDesc = "Animal bone is strong but brittle, and can be made into scale armour or helmets."
ClothDesc = "This is tough padded cloth fabric."
HornDesc = "This includes horns and various natural materials such as ivory, shells, and hooves; used to make scale armour."
LeatherDesc = "This is prepared cured animal hide."
SilkDesc = "Silk can be used to make cloth armour that helps to prevent infection, and reduces the effectiveness of some barbed weapons."
WoodDesc = "This is dense wood such as oak or teak."
CheapBronzeDesc = "The copper-tin alloy is the most common material for TL1 armour and still in use at TL2, but rarer at higher TLs due to its cost."
GoodBronzeDesc = "This is the typical quality of bronze used in most armour."
CopperDesc = "Too soft to make good armour, but useful for ceremonial armor or very early TL1, or for some fey folk or mages who cannot abide the touch of iron."
StoneDesc = "This is used for scale armour assembled from pieces of chipped stone."
JadeDesc = "Jade can be used to make scale armour, like stone, but is visually impressive and expensive."
GemJadeDesc = "Gem-quality jade can be used to make scale armour, like stone, but is visually impressive and very expensive."
CheapIronDesc = "This represents average-quality smith-forged iron, roughly the equivalent of mass-produced mild steel of today."
GoodIronDesc = "This represents low-tech, high-quality smith-forged iron. Limitations on the technology mean that larger iron plates are unavailable until TL4."
LeadDesc = "Too soft and heavy to make good metal armour, but some super-strong races that don’t like the touch of iron may use it anyway."
StrongSteelDesc = "Roughly equivalent to modern RHA steel, but requiring a lot more effort to make."
HardSteelDesc = "This represents the highest-quality smith forged steel."
AdamantDesc = "This is a magical crystal or stone with triple the strength of stone, as detailed in GURPS Fantasy. It may represent other fantastic crystalline materials."
OrichalcumDesc = "This is a legendary metal with triple the strength of bronze, as detailed in Fantasy. It may represent various super-strong fantasy metals."
AluminiumDesc = "One-third the density of steel, but only half as strong."
VeryHardSteelDesc = "Armour incorporating high-hardness steel alloys."
TitaniumDesc = "This is an early 'wonder material' (first refined in 1946). Titanium is very strong for its weight, and retains that strength well at high temperatures."
AramidDesc = "The material used in Kevlar soft body armour; can also represent ballistic plastic fabric."
AblativeDesc = "A material similar to reflex armour, but made of plastic fabric designed to vaporise when struck by a laser beam."
AdvMetallicLaminateDesc = "Titanium, aluminum, beryllium, or ultra-hard steel alloy, reinforced with super-strong carbon nanotubes, boron nanotubes, or diamond whiskers."
ReflecDesc = "Reflec is a light, highly-reflective armour of polished metallic fibers that reflects laser fire. It is useless against other attacks, but can be worn over other armour."
ReflexDesc = "Ballistic armour woven from para-aramids, polyethylene, or synthetic spider silk, soaked in a shear-thickening fluid"
AblativeNanoplasDesc = "Advanced ablative armour made of tailored carbon nanotubes."
NanocompositeDesc = "Ultra-strength carbon or boron nanotube-reinforced polymers."
BioplasDesc = "Bioplas is a strong, pseudo-alive smart matter material that is light and comfortable to wear."
TransparentBioplasDesc = "A transparent variant of bioplas. Provides no protection against laser fire."
NanoweaveDesc = "Similar to reflex armour, but reinforced for extra strength by woven carbon nanotubes."
MonocrysDesc = "A single-crystal weave of synthetic diamondoid fibers, also called 'nanocrystal'. Very light, but not particularly useful against beam weapons."
DiamondoidDesc = "Super-hard nano-fabricated materials such as diamondoid, ultra-hard fullerites, or cubic boron nitride."
EnergyClothDesc = "A light and easily-concealed armour made from a ballistic fibre similar to monocrys. Its hyperdense 'fabric' is resistant to nearly all forms of attack."
ExoticLaminateDesc = "Tougher armour than diamondoid, usually a complex laminate of ultra-hard materials and high-density exotic matter."
EssentialWoodDesc = "Wood shaped into the form of armour, then turned essential by casting the Essential Wood spell on it, giving it three times the hardness for the same weight."
SpidersilkDesc = "Silk fabric woven from spider's silk strands, making it incredibly light yet many times stronger than steel. Nearly impossible to tear, cut, or pierce."


### QUALITY & STYLING ###
  # Defines additional functions that modify armours for quality and styling, as well as some other quality-based features.

# NOT YET IMPLEMENTED

# These apply CFs, so they need to add these before the cost is calculated, but they modify DR, which needs to not affect the weight (and thus cost) calculation.
# Some also affect the weight. While all current ones multiply, I'd prefer a more robust method with a weight multiplier in the armour object.
# The armour.qualityGradeCount number is there to make the three quality grades mutually-exclusive. It's kind of placeholder.
# Maybe add keywords to the armour object itself, then have a keyword check during execution?

# The Stylish and Fashion Original functions are from Ultra-Tech, but Low-Tech provides more generic rules for styling on armour. Those should be used instead.

def Stylish(armour):
	armour.CF += 3.0
	armour.appendNotes("Stylish.")

def FashionOriginal(armour):
	armour.CF += 19.0
	armour.appendNotes("Fashion original.")

def Cheap(armour):
	armour.qualityGradeCount = 1
	armour.DR += -1.0
	armour.CF += -0.6
	armour.appendNotes("Cheap: can be worn comfortably by anyone of roughly the right size.")

def Fine(armour):
	armour.qualityGradeCount = 1
	armour.CF += 9.0
	armour.weight *= 0.75
	armour.appendNotes("Fine.")

def ExpertTailoring(armour):
	armour.qualityGradeCount = 1
	armour.CF += 5.0
	armour.weight *= 0.85
	armour.appendNotes("Expertly tailored: -1 to target chinks in armour.")

def MasterfulTailoring(armour):
	armour.qualityGradeCount = 1
	armour.CF += 29.0
	armour.weight *= 0.7
	armour.appendNotes("Masterfully tailored: -1 to target chinks in armour.")

def Fluted(armour):
	if armour.construction in [Plate,SegmentedPlate,Scale]:
		armour.CF += 4.0
		armour.weight *= 0.9
		armour.appendNotes("Fluted.")
	else:
		print("Warning: Tried to add fluting to an armour that cannot be fluted. No changes have been made.")

### OPTIONS & MODIFICATIONS ###
  # Defines additional functions that modify armours for options, accessories and attachments, as well as materials that don't have enough data to be a full-blown material above.

# NOT YET IMPLEMENTED

# Todo LT: mountain scale, butted mail, banded mail, jazerant, sliding rivets, duplex plate
# Todo FT: gothic plate
# Todo UT: buzz fabric (etc.?), vacuum-sealing, magnetised plates, provisions dispenser, waste relief, helmet w/o faceplates, biomonitor, IFF comm, psionic mind shield,
	 # near-miss indicator, desert environment system, microbot arteries, living metal

def ElvenMail(armour):
	if armour.construction == Mail:
		armour.CF += 3.0
		armour.keywords.remove("WeakToCrushing")
		armour.appendNotes("Elven mail.")
	else:
		print("Warning: Tried to add the elven mail quality to an armour that is not mail. No changes have been made.")

def ThievesMail(armour):
	if armour.construction == Mail:
		armour.CF += 3.0
		armour.appendNotes("Thieves' mail: Ignore weight for encumbrance purposes when making Climbing and Stealth rolls.")
	else:
		print("Warning: Tried to add the thieves' mail quality to an armour that is not mail. No changes have been made.")

def SpikedArmour(armour):
	armour.CF += 2.0
	armour.appendNotes("Spiked: Lets the wearer roll DX-4 to stab each foe in close combat with him for 1d-2 imp, once per turn, as a free action. Anyone who strikes him with an unarmed attack is hit immediately and automatically – and a bite, slam, or Constriction Attack means that attacker suffers maximum damage (4 points).")

def HighlyArticulated(armour):
	armour.CF += 19.0
	armour.appendNotes("Highly articulated: Attacks against chinks in armour use 2/3 DR, not half.")

def BeamAdaptive(armour,N):
	if armour.TL >= 11 and N == 1:
		armour.cost += armour.weight*1000.0
		armour.appendNotes("Beam-adaptive: can adapt to one beam type at a time to provide triple DR.")
	elif armour.TL >= 11 and N == 2:
		armour.cost += armour.weight*4000.0
		armour.appendNotes("Beam-adaptive: can adapt to two beam types at a time to provide triple DR.")
	elif armour.TL >= 11 and N == 3:
		armour.cost += armour.weight*9000.0
		armour.appendNotes("Beam-adaptive: can adapt to three beam types at a time to provide triple DR.")
	elif armour.TL >= 11 and N == 4:
		armour.cost += armour.weight*16000.0
		armour.appendNotes("Beam-adaptive: can adapt to four beam types at a time to provide triple DR.")

def Sealing(armour):
	if armour.TL >= 8:
		armour.cost += 5.0*armour.surfaceArea
		armour.appendNotes("Sealed.")
	elif armour.TL > 6:
		armour.cost += 10.0*armour.surfaceArea
		armour.appendNotes("Sealed.")
	else:
		print("Warning: Tried to add sealing to an armour of a TL too low to be sealed. No changes have been made.")

### ARMOUR CLASS ###
  # Defines the main armour class, along with its internal functions.

class Armour:
	def __init__(self, name = "BLANK NAME", TL = 0, DR = 0, surfaceArea = 0, material = ArmourMaterial(), construction = ArmourConstruction()):
		self.name = name
		self.TL = TL
		self.DR = DR
		self.surfaceArea = surfaceArea
		self.material = material
		self.construction = construction

		self.keywords = []
		self.keywords.extend(self.construction.keywords)
		self.keywords.extend(self.material.keywords)

		self.CF = 1.0
		self.notes = ""
		self.specDR = 0
		self.asterisk = ""
		self.flex = False
		self.errorCount = 0
	def execute(self):
		self.consistencyCheck()
		if self.errorCount < 1:
			self.keywordsCheck()
			self.donCalc()
			self.weightCalc()
			self.costCalc()
			self.LCCalc()
			self.output()
			self.verboseOutput()
		else:
			print("There were {} errors found with the input armour. Please look at the error message(s) above.".format(str(self.errorCount)))
	def appendNotes(self,AddedNotes):
		self.notes += AddedNotes + " "
	def consistencyCheck(self):
		if self.DR != 0:
			if self.DR < self.construction.minDR:
				self.DR = self.construction.minDR
				print("\nWarning: The input DR was lower than the construction type's minimum DR. The DR has been set to the minimum allowed value.\n")
			if self.DR > self.material.maxDR:
				self.DR = self.material.maxDR
				print("\nWarning: The input DR was higher than the material's maximum DR. The DR has been set to the maximum allowed value.\n")
		if self.DR == 0:
			self.errorCount += 1
			print("\nError: DR was set to zero.\n")
		if self.construction not in self.material.constructions:
			self.errorCount += 1
			print("\nError: The given material and construction type are incompatible.\n")
		if self.construction == Leather and TL == 0:
			self.errorCount += 1
			print("\nError: The layered fabric construction is TL1 for leather.\n")
		if self.material in [CheapIron,GoodIron,StrongSteel,HardSteel] and self.construction in [Plate,Solid] and self.TL < 4:		#This needs to account for helmets.
			self.errorCount += 1
			print("\nError: Plate or solid constructions are TL4 for iron and steel armour, apart from helmets.\n")
		if self.TL < self.construction.TL:
			self.errorCount += 1
			print("\nError: The given construction type was a higher TL than the armour.\n")
		if self.TL < self.material.TL:
			self.errorCount += 1
			print("\nError: The given material was a higher TL than the armour.\n")
	def keywordsCheck(self):
		if "Ballistic" in self.keywords:
			self.appendNotes("Split DR: provides full protection against piercing and cutting attacks and uses its reduced DR against all other types of damage.")
			self.specDR = self.DR*BallisticDRMult[self.material]
		if "Bio" in self.keywords:
			self.appendNotes("Split DR: provides full protection against burning and piercing attacks and uses its reduced DR against all other types of damage.")
			self.specDR = self.DR*3.0
		if "Combustible" in self.keywords:
			self.appendNotes("Combustible: if the armour is penetrated by burning damage, it may catch fire (see B433).")
		if "EnergyAblative" in self.keywords:
			self.appendNotes("Split DR: provides full protection against laser attacks and uses its reduced DR against all other types of damage.")
			self.appendNotes("The higher DR is semi-ablative, the lower DR is not.")
			self.specDR = self.DR*6.0
		if "FireResistant" in self.keywords:
			self.appendNotes("Split DR: provides full protection against burning attacks and uses its reduced DR against all other types of damage.")
			self.specDR = self.DR*4.0
		if "Flexible" in self.keywords and self.DR <= DRPerInch[self.material]*0.25:
			self.flex = True
			self.asterisk = "*"
		if "LaserOnly" in self.keywords:
			self.appendNotes("Split DR: provides full protection against laser attacks and none against any other types of damage.")
		if "ReactionsP2" in self.keywords:
			self.appendNotes("+2 to reactions.")
		if "ReactionsP3" in self.keywords:
			self.appendNotes("+3 to reactions.")
		if "SemiAblative" in self.keywords:
			self.appendNotes("DR is semi-ablative.")
		if "SilkBenefits" in self.keywords:
			self.appendNotes("+1 DR vs. cutting and impaling attacks. Negates the effect of barbed weapons.")
			self.appendNotes("+1 to First Aid to treat wounds inflicted through the armour.")
			self.appendNotes("Negates -2 in HT penalties from wound infection due to dirt in the wound.")
			self.appendNotes("Attacks penetrating the armour do not count for blood agent or contact poisons.")
		if "Transparent" in self.keywords:
			if str.casefold(input("This material can be transparent (double cost, no DR vs. visible-light lasers). Do you want a transparent material? Y/N")) == 'y':
				self.appendNotes("Transparent: No DR vs. visible-light lasers.")
				self.CF += 1.0
		if "HalfVsCrushing" in self.keywords:
			self.appendNotes("Split DR: provides full protection against crushing attacks and uses its reduced DR against all other types of damage.")
			self.specDR = self.DR/2.0
		if "WeakToImpaling" in self.keywords and self.material.TL <= 4:
			self.appendNotes("-1 DR vs. impaling.")
		if "WeakToCrushing" in self.keywords and self.construction == Scale and self.DR < 5:
			self.appendNotes("-1 DR vs. crushing.")
		if "WeakToCrushing" in self.keywords and self.construction == Mail:
			if self.DR <= 10:
				self.appendNotes("-2 DR vs. crushing.")
			elif self.DR > 10:
				self.appendNotes("-" + str(round(0.001+self.DR*0.2)) + "DR vs. crushing.")
	def donCalc(self):
		if self.flex == True:
			if self.material.TL >= 7:
				self.timeToDon = 3.0
			else:
				self.timeToDon = self.surfaceArea*self.construction.don*2.0/3.0
		else:
			self.timeToDon = self.surfaceArea*self.construction.don
	def weightCalc(self):
		self.weight = self.surfaceArea*self.material.WM*self.construction.CW*self.DR
	def costCalc(self):
		if self.TL >= 6 and self.material in [StrongSteel,HardSteel]:
			self.cost = self.CF*(self.weight*self.material.CM*self.construction.CC)/25.0
		elif self.TL >= 5 and self.material in [CheapBronze,GoodBronze,CheapIron,GoodIron,StrongSteel,HardSteel,Adamant,Orichalcum]:
			self.cost = self.CF*(self.weight*self.material.CM*self.construction.CC)/5.0
		else:
			self.cost = self.CF*(self.weight*self.material.CM*self.construction.CC)
	def LCCalc(self):
		pass				#LC calculation here. There's no LC calculation for Low-Tech armour, but there is for Ultra-Tech.
	def output(self):
		pass				#Output statblock here.
	def GCSOutput(self):
		pass				#HTML-formatted output block for GCS here.
	def verboseOutput(self):
		print("\nArmour Name: {}".format(self.name))
		if "Superscience" in self.material.keywords:
			print("TL: {}^".format(str(self.TL)))
		else:
			print("TL: {}".format(str(self.TL)))
		if "LaserOnly" in self.material.keywords or "HalfVsCrushing" in self.construction.keywords:
			print("DR: {}/{}{}".format(str(round(self.DR)),str(round(self.specDR)),self.asterisk))
		elif self.specDR == 0:
			print("DR: {}{}".format(str(round(self.DR)),self.asterisk))
		else:
			print("DR: {}/{}{}".format(str(round(self.specDR)),str(round(self.DR)),self.astrisk))
		print("Time to Don: {}".format(str(self.timeToDon)))
		print("Weight: {}".format(str(self.weight)))
		print("Cost: {}".format(str(self.cost)))
		print("Notes: {}".format(str(self.notes)))
		print("Material: {}".format(str(self.material.name)))
		print("Material TL: {}".format(str(self.material.TL)))
		print("Construction: {}".format(str(self.construction.name)))
		print("Total Surface Area: {}".format(str(self.surfaceArea)))
		print("Final Cost Factor: {}".format(str(self.CF)))
		print("Keywords: {}".format(str(self.keywords)))
		print("Quality Grade: {}".format("NOT IMPLEMENTED"))
		print("Special Features: {}".format("NOT IMPLEMENTED"))


### INPUT & CALCULATION ###
  # Takes input from the command line/shell for user-defined properties without having to alter the code to do it.
  # Then the input information us used to instantiate an armour object, and the armour.execute() method called, which calculates all properties and prints them.
  # If you add more hit locations, materials or constructions, make sure to add them to the information here, as it is currently very important that they be formatted correctly.

print("--GURPS ARMOUR GENERATOR--\n")

KeepGoing = True

while KeepGoing == True:

	TempName = input("Please enter the name of your armour:\n")

	TempTL = eval(input("Please enter the TL of your armour:\n"))

	print("""\nThe materials you can use are:
 TL0: Bone, Cloth, Horn, Leather, Silk, Wood
 TL1: CheapBronze, GoodBronze, Copper, Stone, Jade, GemJade
 TL2: CheapIron, GoodIron, Lead
 TL3: StrongSteel
 TL4: HardSteel
 TL6: Aluminium
 TL7: VeryHardSteel, Titanium
 TL8: Aramid
 TL9: Ablative, AdvMetallicLaminate, Reflec, Reflex
TL10: AblativeNanoplas, Nanocomposite, Bioplas, Nanoweave
TL11: Monocrys, Diamondoid
TL12: EnergyCloth, ExoticLaminate
 TL^: Adamant, EssentialWood, Orichalcum, Spidersilk

Please use the exact capitalisation, spacing and spelling. Not all materials are compatible with all constructions. If in doubt, use common sense, but an error message will be printed if they are incompatible.\n""")

	TempMaterial = eval(input("Please enter the material of your armour:\n"))

	print("\nThe construction types you can use are: Fabric, LayeredFabric, Scale, Mail, SegmentedPlate, Plate and Solid, OptimisedFabric and ImpactAbsorbing. Please use the exact capitalisation, spacing and spelling, otherwise the calculations may fail.\n")

	TempConstruction = eval(input("Please enter the construction of your armour:\n"))

	TempDR = eval(input("Please enter the DR of your armour:\n"))

	print("""The body areas you can use are: Head (which includes Skull, Face and Neck), Torso (which includes Chest, Abdomen and Groin), Arms (which includes Shoulders, UpperArms, Elbows and Forearms), Hands, Legs (which includes Thighs, Knees and Shins) and Feet.

You can use any combination of the hit locations and sub-locations, but be aware that there is currently no check to see whether you've entered the same area twice (e.g. Torso and Abdomen). Please use the exact capitalisation, spacing and spelling, and seperate locations with addition signs (+) if you are using more than one location.\n""")

	TempSA = eval(input("Please enter the areas your armour will cover:\n"))

	UserDefinedArmour = Armour(TempName,TempTL,TempDR,TempSA,TempMaterial,TempConstruction)
	UserDefinedArmour.execute()

	print("\n- - - - - - - - - - - - - - -\n")

	if str.casefold(input("Do you want to generate another armour? Type y to start again, or anything else to finish.\n")) == "y":
		continue
	else:
		KeepGoing = False
		break


### STORAGE ###
  # This is code that is mostly finished but not yet implemented for various reasons.

def MakeMaterialNameList(TL):
	Output = ""
	for each in MasterMaterialList:
		if each.TL == TL:
			Output += each.name + "; "
	if Output.endswith("; "):
		pass		#Delete the "; " from the end somehow
	return Output

def PrintAllMaterials():
	while i in range(0,TL+1):
		Line0 = "TL{}: {}".format(str(i),MakeMatNameList(i))

def PrintConstructions(TL,material):
	OutputList = []
	for each in material.constructions:
		if each.TL <= TL:
			Output += material.constructions.name + "; "
	if Output.endswith("; "):
		pass		#Delete the "; " from the end somehow
	return OutputList

class HitLocation:
	def __init__(self,SurfaceArea = 0.0, Subdivisions = []):
		self.surfaceArea = SurfaceArea
		self.subdiv = Subdivisions
		self.adjacent = []
	def adj(self,List = []):
		self.adjacent.extend(List)

def CreateHitLocations():

	Vitals = HitLocation(1.0,[])
	Groin = HitLocation(0.35,[])

	Skull = HitLocation(1.4,[])
	Face = HitLocation(0.7,[])
	Neck = HitLocation(0.35,[])
	Chest = HitLocation(5.25,[Vitals])
	Abdomen = HitLocation(1.75,[Groin])
	Shoulders = HitLocation(0.7,[])
	UpperArms = HitLocation(0.7,[])
	Elbows = HitLocation(0.35,[])
	Forearms = HitLocation(1.75,[])
	Hands = HitLocation(0.7,[])
	Thighs = HitLocation(3.15,[])
	Knees = HitLocation(0.35,[])
	Shins = HitLocation(3.5,[])
	Feet = HitLocation(0.7,[])

	Head = HitLocation(2.1,[Skull,Face])
	Torso = HitLocation(7.0,[Chest,Abdomen])
	Arms = HitLocation(3.5,[Shoulders,UpperArms,Elbows,Forearms])
	Legs = HitLocation(7.0,[Thighs,Knees,Shins])

	Skull.adj([Face])
	Face.adj([Skull,Neck])
	Neck.adj([Face,Chest])
	Chest.adj([Neck,Shoulders,Abdomen])
	Abdomen.adj([Chest,Thighs])
	Shoulders.adj([Chest,UpperArms])
	UpperArms.adj([Shoulders,Elbows])
	Elbows.adj([UpperArms,Forearms])
	Forearms.adj([Elbows,Hands])
	Hands.adj([Forearms])
	Thighs.adj([Abdomen,Knees])
	Knees.adj([Thighs,Shins])
	Shins.adj([Knees,Feet])
	Feet.adj([Shins])

	Head.adj([Neck])
	Torso.adj([Neck,Arms,Legs])
	Arms.adj([Torso,Hands])
	Legs.adj([Torso,Feet])

	#Directional *= 0.5
	#HalfCoverage *= 0.5
	#Skimpy *= 0.25

#LocationList = []

def SurfaceAreaSum(LocationList):
	total = 0.0
	for each in LocationList:
		total += each.surfaceArea
	return total

