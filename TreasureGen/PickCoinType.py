
#Everything should be wrapped up in a PickCoin() function, within which is the Coin class, which during instantiation calls the other functions as methods to create the whole coin.

# # #

def PickCoinMaterial():
	class CoinMaterial:
		def __init__(self,name = "",costPerPound = 0.0,num1 = 0,num2 = 0):
			self.name = name
			self.costPerPound = costPerPound
			self.num1 = num1
			self.num2 = num2

	Copper = CoinMaterial("Copper",62.5,[1],[1,2,3])
	Bronze = CoinMaterial("Bronze",62.5,[1],[4,5])
	Brass = CoinMaterial("Brass",62.5,[1],[6])
	Billon = CoinMaterial("Billon",531.25,[2],[1,2])
	Silver = CoinMaterial("Silver",1000.0,[2],[3,4])
	Tumbaga = CoinMaterial("Tumbaga",3100.00,[2],[5])
	Electrum = CoinMaterial("Electrum",10500.0,[2],[6])
	Gold = CoinMaterial("Gold",20000.0,[3],[1,2,3])
	Platinum = CoinMaterial("Platinum",38400.0,[3],[4])
	Iron = CoinMaterial("Iron",6.9,[3],[5,6])
	Lead = CoinMaterial("Lead",4.3,[4],[1,2])
	Gemstone = CoinMaterial("Gemstone",5152714.40,[4],[3])			#Needs to generate a gem
	Antler = CoinMaterial("Antler",0.0,[4],[4])
	Bone = CoinMaterial("Bone",0.0,[4],[5])
	Ivory = CoinMaterial("Ivory",0.0,[4],[6])
	Resin = CoinMaterial("Resin",0.0,[5],[1])
	Shell = CoinMaterial("Shell",0.0,[5],[2])
	Wood = CoinMaterial("Wood",0.0,[5],[3])
	Marble = CoinMaterial("Marble",0.0,[5],[4])
	Glass = CoinMaterial("Glass",0.0,[5],[5])
	Porcelain = CoinMaterial("Porcelain",0.0,[5],[6])
	Soapstone = CoinMaterial("Soapstone",0.0,[6],[1])
	Gypsum = CoinMaterial("Gypsum",0.0,[6],[2])
	MeteoricIron = CoinMaterial("Meteoric iron",138.0,[6],[3,4])
	Orichalcum = CoinMaterial("Orichalcum",1875.0,[6],[5])
	Implausible = CoinMaterial("Implausible material: ",0.0,[6],[6])	#Generates an implausible material

	CoinMaterialList = [Copper,Bronze,Brass,Billon,Silver,Tumbaga,Electrum,Gold,Platinum,Iron,Lead,Gemstone,Antler,Bone,Ivory,Resin,Shell,Wood,Marble,Glass,Porcelain,Soapstone,Gypsum,MeteoricIron,Orichalcum,Implausible]

	Dice1 = random.randint(1,6)
	Dice2 = random.randint(1,6)

	for each in CoinMaterialList:
		if Dice1 in each.num1 and Dice2 in each.num2:
			if each == Gemstone:
				pass		#special case - generate a gemstone from another function
			if each == Implausible:
				pass		#special case - generate an implausible material from another function
			return each

# # #

def PickCoinShape():
	class CoinShape:
		def __init__(self,name = "",num1 = 0,num2 = 0):
			self.name = name
			self.num1 = num1
			self.num2 = num2

	Oval = CoinShape("Oval",[1,2],[1,2])
	Crescent = CoinShape("Crescent",[1,2],[3,4])
	Semicircle = CoinShape("Semi-circle",[1,2],[5,6])
	
	KnifeKey = CoinShape("Knife/key",[3,4],[1,2])
	Spade = CoinShape("Spade",[3,4],[3,4])
	Fan = CoinShape("Fan",[3,4],[5,6])
	
	Polygonal = CoinShape("Polygonal: ",[5,6],[1,2])
	ScallopedLobed = CoinShape("Scalloped/lobed: ",[5,6],[3,4])
	Wedge = CoinShape("Wedged",[5,6],[5,6])

	CoinShapeList = [Oval,Crescent,Semicircle,KnifeKey,Spade,Fan,Polygonal,ScallopedLobed,Wedge]

	Dice1 = random.randint(1,6)
	Dice2 = random.randint(1,6)

	for each in CoinShapeList:
		if Dice1 in each.num1 and Dice2 in each.num2:
			if each == Polygonal:
				sides = random.randint(1,6) + 2
				each.name += str(sides) + " sides"
			if each == ScallopedLobed:
				sides = random.randint(1,6) + 2
				each.name += str(sides) + " sides"
			return each

# # #

def PickCoinCondition():
	class CoinCondition:
		def __init__(self,name = "",num1 = 0,num2 = 0):
			self.name = name
			self.num1 = num1
			self.num2 = num2

	Rough = CoinCondition("Rough",[1,2],[1,2])
	Worn = CoinCondition("Worn",[1,2],[3,4])
	Clipped = CoinCondition("Clipped",[1,2],[5,6])
	Marked = CoinCondition("Marked",[3,4],[1,2])
	Pierced = CoinCondition("Pierced",[3,4],[3,4])
	Cupped = CoinCondition("Cupped",[3,4],[5,6])
	Hollow = CoinCondition("Hollow",[5,6],[1,2])
	Sharpened = CoinCondition("Sharpened",[5,6],[3,4])
	Overstruck = CoinCondition("Overstruck",[5,6],[5,6])

	CoinConditionList = [Rough,Worn,Clipped,Marked,Pierced,Cupped,Hollow,Sharpened,Overstruck]

	Dice1 = random.randint(1,6)
	Dice2 = random.randint(1,6)

	for each in CoinConditionList:
		if Dice1 in each.num1 and Dice2 in each.num2:
			return each


# # #


import random

class CoinObject:
	def __init__(self):
		self.material = PickCoinMaterial()
		self.shape = PickCoinShape()
		self.condition = PickCoinCondition()
		#self.decoration = PickDecoration()

		print(self.material.name + ", " + self.shape.name + ", " + self.condition.name)

a = CoinObject()


