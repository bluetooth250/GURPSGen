
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
		<notes>{cells}/{shots} shots. {notes}</notes>
		<categories>
			<category>Missile Weapon</category>
			<category>Weaponry</category>
		</categories>
	</equipment>
</equipment_list>"""


	if weapon.cellNum == 1:
		CellString = weapon.powerCell.name
	else:
		CellString = str(weapon.cellNum)+weapon.powerCell.name)

	OutputRangedWeapon1 = RangedWeaponTemplate.format(damage=weapon.getDamageString(),ST=weapon.getSTString(),Acc=weapon.getAccString(),rangestring=weapon.getRangeString(),RoF=weapon.getRoFString(),shots=weapon.shots,bulk=weapon.getBulkString(),recoil=(str(weapon.recoil)),skill=weapon.configuration.name)
	if "SecondaryMode" in weapon.keywords:
		OutputRangedWeapon2 = RangedWeaponTemplate.format(damage=weapon.getAltDamageString(),ST=weapon.getSTString(),Acc=weapon.getAccString(),rangestring=weapon.getAltRangeString(),RoF=weapon.getRoFString(),shots=weapon.shots,bulk=weapon.getBulkString(),recoil=(str(weapon.recoil)),skill=weapon.configuration.name)
	else:
		OutputRangedWeapon2 = ""

	OutputObject = EquipmentTemplate.format(name=weapon.name,TL=weapon.getTLString(),LC=weapon.LC,cost=weapon.cost,weight=weapon.fullWeight,weap1=OutputRangedWeapon1,weap2=OutputRangedWeapon2,cells=CellString,shots=weapon.shots,notes=weapon.notes)

	with open("BeamGen.eqp","r+") as TargetFile:
		TempStorage = TargetFile.read()
		StartPoint = TempStorage.find("</equipment_list>")
		TargetFile.seek(StartPoint,0)
		TargetFile.write(OutputObject)
	print("Saved to GCS equipment file.")

