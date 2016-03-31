
def AppendToGCSFile(weapon):

	RangedWeaponTemplate = """		<ranged_weapon>
			<damage>{damage}</damage>
			<strength>{ST}</strength>
			<accuracy>{Acc}</accuracy>
			<range>{rangestring}</range>
			<rate_of_fire>{RoF}</rate_of_fire>
			<shots>{shots}</shots>
			<bulk>{bulk}</bulk>
			<recoil>{recoil}</recoil>
			<default>
				<type>DX</type>
				<modifier>-4</modifier>
			</default>
			<default>
				<type>Skill</type>
				<name>Beam Weapons</name>
				<specialization>{skill}</specialization>
				<modifier>0</modifier>
			</default>
			<default>
				<type>Skill</type>
				<name>Beam Weapons</name>
				<modifier>-4</modifier>
			</default>
			<default>
				<type>Skill</type>
				<name>Guns</name>
				<specialization>{skill}</specialization>
				<modifier>-4</modifier>
			</default>
		</ranged_weapon>"""


	EquipmentTemplate = """	<equipment version="3">
		<quantity>1</quantity>
		<description>{name}</description>
		<tech_level>{TL}</tech_level>
		<legality_class>{LC}</legality_class>
		<value>{cost}</value>
		<weight>{weight} lb</weight>
		<reference></reference>
		{weap1}
		{weap2}
		<notes>{cellshots} shots. {notes}</notes>
		<categories>
			<category>Missile Weapon</category>
			<category>Weaponry</category>
		</categories>
	</equipment>
</equipment_list>"""

	if weapon.cellNum > 1 and weapon.powerCell.name in ["D","E","F"]:
		CellShotsString = "{} external {} cells.".format(str(weapon.cellNum),weapon.powerCell.name)
	elif weapon.cellNum > 1 and weapon.powerCell.name not in ["D","E","F"]:
		CellShotsString = "External {} cell.".format(weapon.powerCell.name)
	elif weapon.cellNum == 1 and weapon.powerCell.name in ["D","E","F"]:
		CellShotsString = "{}/{} shots.".format(weapon.powerCell.name, weapon.shots)
	elif weapon.cellNum == 1 and weapon.powerCell.name not in ["D","E","F"]:
		CellShotsString = "{}/{} shots.".format(str(weapon.cellNum)+weapon.powerCell.name, weapon.shots)

	OutputRangedWeapon1 = RangedWeaponTemplate.format(damage=weapon.getDamageString(),ST=weapon.getSTString(),Acc=weapon.getAccString(),rangestring=weapon.getRangeString(),RoF=weapon.getRoFString(),shots=weapon.shots,bulk=weapon.getBulkString(),recoil=(str(weapon.recoil)),skill=weapon.configuration.name)
	if "SecondaryMode" in weapon.keywords:
		OutputRangedWeapon2 = RangedWeaponTemplate.format(damage=weapon.getAltDamageString(),ST=weapon.getSTString(),Acc=weapon.getAccString(),rangestring=weapon.getAltRangeString(),RoF=weapon.getRoFString(),shots=weapon.shots,bulk=weapon.getBulkString(),recoil=(str(weapon.recoil)),skill=weapon.configuration.name)
	else:
		OutputRangedWeapon2 = ""

	OutputObject = EquipmentTemplate.format(name=weapon.name,TL=weapon.getTLString(),LC=weapon.LC,cost=weapon.cost,weight=weapon.fullWeight,weap1=OutputRangedWeapon1,weap2=OutputRangedWeapon2,cellshots=CellShotsString,notes=weapon.notes)

	with open("BeamGen.eqp","r+") as TargetFile:
		TempStorage = TargetFile.read()
		StartPoint = TempStorage.find("</equipment_list>")
		TargetFile.seek(StartPoint,0)
		TargetFile.write(OutputObject)
	print("Saved to GCS equipment file.")


def DiceRounder(Dice):
	"""Takes a dice number in decimal format and returns it in a string in dice+adds format."""
	IntDice = int(Dice)
	Fraction = Dice-int(Dice)
	if Dice > 12.0:
		return ("6dx" + str(round(Dice/6)))
	if Dice >= 1.0 and Dice <= 12.0:
		if Fraction >= 0.85:
			IntDice = IntDice+1
			Adds = ""
		elif Fraction >= 0.65:
			IntDice = IntDice+1
			Adds = "-1"
		elif Fraction >= 0.43:
			Adds = "+2"
		elif Fraction >= 0.15:
			Adds = "+1"
		else:
			Adds = ""
		return (str(IntDice) + "d" + Adds)
	if Dice < 1.0:
		IntDice = 1
		if Dice >=0.96:
			Adds = ''
		elif Dice >= 0.76:
			Adds = '-1'
		elif Dice >= 0.57:
			Adds = '-2'
		elif Dice >= 0.43:
			Adds = '-3'
		elif Dice >= 0.33:
			Adds = '-4'
		else:
			Adds = '-5'
		return (str(IntDice) + 'd' + Adds)


def BeamFix(BeamType,Configuration):	#From input, we know beam type and config. E varies by config only, whereas Bc varies by both? Need to double check that
	"""Takes the beam type's name (as a string) and the weapon configuration, to use the right properties for beam types whose properties vary by configuration"""

	if BeamType in [EMP,Neural,SonicScreamer,SonicStun]:
		EMPBcDict = {Beamer:0.0,Pistol:0.0,Rifle:0.0}
		NeuralBcDict = {Beamer:0.0,Pistol:0.0,Rifle:0.0}
		SonicScreamerBcDict = {Beamer:0.0,Pistol:0.0,Rifle:0.0}
		SonicStunBcDict = {Beamer:0.0,Pistol:0.0,Rifle:0.0}
		BcDict = {EMP:{EMPBcDict},Neural:{NeuralBcDict},SonicScreamer:{SonicScreamerBcDict},SonicStun:{SonicStunBcDict}}
		BeamType.Bc = BcDict[BeamType][Configuration]

		EDict = {Beamer:0.0,Pistol:0.0,Rifle:0.0}
		BeamType.E = EDict[Configuration]
	else:
		pass
