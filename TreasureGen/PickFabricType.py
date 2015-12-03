def PickFabricType(ClothObject):
	class FabricType:
		def __init__(self,name = "",desc = "",CF = 0.0,num1 = [],num2 = []):
			self.name = name
			self.desc = desc
			self.CF =  CF
			self.num1 = num1
			self.num2 = num2

	PlainWeave = FabricType("Plain weave","",0.0,[1],[1,2,3])
	BasketWeave = FabricType("Basket weave","",0.1,[1],[4,5,6])
	Twill = FabricType("Twill","",0.1,[2],[1,2,3])
	Cambric = FabricType("Cambric","",0.1,[2],[4,5,6])
	Canvas = FabricType("Canvas","",0.1,[3],[1,2,3])
	Gauze = FabricType("Gauze","",0.3,[3],[4,5,6])
	Grogram = FabricType("Grogram","",0.5,[4],[1,2])
	Crinoline = FabricType("Crinoline","",0.1,[4],[3])
	Taffeta = FabricType("Taffeta","",4.0,[4],[4])
	Chiffon = FabricType("Chiffon","",0.5,[4],[5])
	DoubleWeave = FabricType("Double weave","",15.0,[4],[6])
	Organdy = FabricType("Organdy","",0.0,[5],[1])
	Organza = FabricType("Organza","",2.5,[5],[2])
	Satin = FabricType("Satin","",14.0,[5],[3])
	Sateen = FabricType("Sateen","",10.0,[5],[4])
	Brocade = FabricType("Brocade","",16.0,[5],[5])
	Damask = FabricType("Damask","",20.0,[5],[6])
	Lame = FabricType("Lamé","",22.0,[6],[1])
	Jamdani = FabricType("Jamdani","",4.0,[6],[2])
	Velvet = FabricType("Velvet","",0.5,[6],[3])
	Corduroy = FabricType("Corduroy","",0.75,[6],[4])
	DoubleVelvet = FabricType("Double velvet","",8.0,[6],[5])
	Samite = FabricType("Samite","",5.0,[6],[6])

	FabricTypeList = [PlainWeave,BasketWeave,Twill,Cambric,Canvas,Gauze,Grogram,Crinoline,Taffeta,Chiffon,DoubleWeave,Organdy,Organza,Satin,Sateen,Brocade,Damask,Lame,Jamdani,Velvet,Corduroy,DoubleVelvet,Samite]

	Dice1 = random.randint(1,6)
	Dice2 = random.randint(1,6)

	for each in FabricTypeList:
		if Dice1 in each.num1 and Dice2 in each.num2:
			ClothObject.CF += each.CF
			ClothObject.appendNotes(str(each.name) + ".")
			break
