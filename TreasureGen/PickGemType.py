import random

def EncrustWithGem(OtherObject):
	EncrustedGem = PickGem()
	OtherObject.cost += EncrustedGem.cost
	OtherObject.appendNotes("Set with a " + str(EncrustedGem.carats) + "-carat " + str.lowercase(EncrustedGem.name) + " worth $" + str(EncrustedGem.cost) + ".")
	#NB:  This should probably EITHER add the cost, or give the extra cost in notes. Both may be confusing.

#All of this below should be wrapped up into a function called PickGem
class Gem:
	def __init__(self):
		class GemMaterial:
			def __init__(self,name,valuemod,num1,num2):
				self.name = name
				self.valuemod = valuemod
				self.num1 = num1
				self.num2 = num2

		Bigger = GemMaterial("Bigger",0.0,[1],[1,2])
		Agate = GemMaterial("Agate",5.0,[1],[3])
		Azurite = GemMaterial("",10.0,[1],[4])
		Chalcedony = GemMaterial("Chalcedony",10.0,[1],[5])
		Haematite = GemMaterial("Haematite",5.0,[1],[6])

		Jade = GemMaterial("Jade",20.0,[2],[1])
		Jet = GemMaterial("Jet",10.0,[2],[2])
		Magnetite = GemMaterial("Magnetite",5.0,[2],[3])
		Malachite = GemMaterial("Malachite",15.0,[2],[4])
		Obsidian = GemMaterial("Obsidian",2.0,[2],[5])
		Quartz = GemMaterial("Quartz",15.0,[2],[6])

		Amber = GemMaterial("Amber",25.0,[3],[1])
		Amethyst = GemMaterial("Amethyst",30.0,[3],[2])
		Calcite = GemMaterial("Calcite",20.0,[3],[3])
		Sard = GemMaterial("Sard",25.0,[3],[4])
		Coral = GemMaterial("Coral",20.0,[3],[5])
		LapisLazuli = GemMaterial("Lapis lazuli",25.0,[3],[6])

		Onyx = GemMaterial("Onyx",20.0,[4],[1])
		Tourmaline = GemMaterial("Tourmaline",25.0,[4],[2])
		Turquoise = GemMaterial("Turquoise",20.0,[4],[3])
		Aquamarine = GemMaterial("Aquamarine",30.0,[4],[4])
		Beryl = GemMaterial("Beryl",30.0,[4],[5])
		Bloodstone = GemMaterial("Bloodstone",30.0,[4],[6])

		CatsEye = GemMaterial("Cat's eye",30.0,[5],[1])
		Emerald = GemMaterial("Emerald",35.0,[5],[2])
		Garnet = GemMaterial("Garnet",35.0,[5],[3])
		Iolite = GemMaterial("Iolite",30.0,[5],[4])
		Moonstone = GemMaterial("Moonstone",30.0,[5],[5])
		Opal = GemMaterial("Opal",35.0,[5],[6])

		Pearl = GemMaterial("Pearl",35.0,[6],[1])
		Peridot = GemMaterial("Peridot",30.0,[6],[2])
		Ruby = GemMaterial("Ruby",35.0,[6],[3])
		Sapphire = GemMaterial("Sapphire",35.0,[6],[4])
		Topaz = GemMaterial("Topaz",35.0,[6],[5])
		Diamond = GemMaterial("Diamond",40.0,[6],[6])

		GemMaterialList = [Bigger,Agate,Azurite,Chalcedony,Haematite,Jade,Jet,Magnetite,Malachite,Obsidian,Quartz,Amber,Amethyst,Calcite,Sard,Coral,LapisLazuli,Onyx,Tourmaline,Turquoise,Aquamarine,Beryl,Bloodstone,CatsEye,Emerald,Garnet,Iolite,Moonstone,Opal,Pearl,Peridot,Ruby,Sapphire,Topaz,Diamond]

		Dice1 = random.randint(1,6)
		Dice2 = random.randint(1,6)
		self.carats = (random.randint(1,6)+random.randint(1,6))/4

		for each in GemMaterialList:
			if Dice1 in each.num1 and Dice2 in each.num2:
				if each == Bigger:
					self.carats += random.randint(1,6)
					pass		#needs to re-roll, but double size.
				self.material = each
			
		self.cost = (self.carats**2 + 4*self.carats)*self.material.valuemod

a = Gem()
print(str(a.material.name))
print(str(a.carats))
print(str(a.cost))
