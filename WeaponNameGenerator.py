### Random weapon name generator ###

## This behaviour is unintended but cool, preserve it:
#	MK89 Diamondback09
#	MM175 MantisPR
#	KT210 Pilum2–1

import random

FullLetterList = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
CoolLetterList = ["B","D","J","K","L","M","N","P","T","X"]
EndingLetterList = ["A","B","C","D","E","I","K","X","a","b","c","d","e","i"]
NumberList = ["1","2","3","4","5","6","7","8","9","0"]
DashList = ["-","–","—"]
GreekList = ["Γ","Δ","Θ","Λ","Π","Σ","Φ","Ψ","Ω","β","γ","δ","ε","ζ","η","θ","λ","μ","ξ","π","ρ","ψ","ω"]
WordList = ["Acolyte","Aftershock","Alpha","Argus","Armageddon","Avalanche","Avenger","Bandit","Banshee","Blackstar","Blackstorm","Blizzard","Brawler","Breaker","Bulldog","Burn","Cain","Carnifex","Cataclysm","Challenger","Chevalier","Claymore","Cobra","Comet","Crossfire","Crusader","Cyclone","Dawn","Diamondback","Disciple","Eagle","Earthquake","Echo","Eclipse","Edge","Ember","Equaliser","Eviscerator","Executioner","Falcon","Firestarter","Firestorm","Flux","Fury","Gargoyle","Gladius","Gorgon","Hammer","Harpoon","Harpy","Harrier","Hawkeye","Helix","Hornet","Hurricane","Hydra","Incisor","Indra","Infinity","Intervention","Jackalope","Jaeger","Javelin","Judgement","Justice","Karpov","Katana","Kessler","Knight","Kovalyov","Lancer","Legionnaire","Lightning","Locust","Mantis","Matador","Mattock","Meteor","Midnight","Mirage","Naginata","Nova","Ogre","Omega","Orbit","Paladin","Pendulum","Penetrator","Phalanx","Phantom","Pilum","Pinnacle","Piranha","Predator","Pugio","Pulse","Punisher","Python","Raider","Raptor","Rattlesnake","Razer","Reaper","Reckoner","Revenant","Rhino","Sabre","Savage","Scimitar","Scorpion","Scutum","Shuriken","Sokolov","Spatha","Spitfire","Stalker","Stiletto","Sting","Stinger","Storm","Striker","Supernova","Sweeper","Talon","Terminator","Thunder","Tiebreaker","Titan","Tornado","Torrent","Tremour","Trinity","Tsunami","Tunguska","Twister","Typhoon","Valiant","Valkyrie","Venom","Vindicator","Viper","Volkov","Vortex","Widow","Wildfire","Wolf","Wraith"]

#These have been added to the master wordlist, so they just need to be added to the sorted wordlists below.
NewList = ["Midnight","Challenger","Sweeper","Justice","Tiebreaker","Mirage","Dawn","Reckoner","Intervention"]

#These haven't been added to the master wordlist or anywhere else.
NewNewList = ["Guardian","Hydra","Liberator","Phantom","Titan","Ursa"]

AnimalList = ["Bulldog","Cobra","Diamondback","Eagle","Falcon","Hawkeye","Harrier","Hornet","Jackalope","Jaeger","Locust","Mantis","Piranha","Predator","Python","Raptor","Rattlesnake","Rhino","Scorpion","Sting","Viper","Widow","Wolf"]
BiblicalList = ["Alpha","Cain","Omega","Paladin","Trinity"]
DisasterList = ["Aftershock","Armageddon","Avalanche","Blackstorm","Blizzard","Cataclysm","Cyclone","Earthquake","Firestorm","Hurricane","Lightning","Storm","Thunder","Tornado","Torrent","Tremour","Tsunami","Twister","Typhoon","Wildfire"]
FightingList = ["Bandit","Brawler","Chevalier","Crusader","Knight","Legionnaire","Matador","Paladin","Raider","Stalker","Warrior"]
FireList = ["Burn","Ember","Firestarter","Firestorm","Wildfire"]
GreekAlphabetList = ["Alpha","Beta","Gamma","Delta","Epsilon","Zeta","Eta","Theta","Iota","Kappa","Lambda","Mu","Nu","Omicron","Pi","Rho","Sigma","Tau","Upsilon","Phi","Chi","Psi","Omega"]
GrecoRomanList = ["Argus","Carnifex","Gladius","Gorgon","Hydra","Javelin","Legionaire","Phalanx","Pilum","Pugio","Scutum","Spatha","Titan"]
RussianList = ["Avtomat","Karpov","Kovalyov","Sokolov","Tunguska","Volkov"]
ScienceList = ["Blackstar","Comet","Darkstar","Echo","Eclipse","Flux","Infinity","Magnetar","Meteor","Nova","Orbit","Pendulum","Pulsar","Quasar","Supernova","Vortex"]
SpiritList = ["Banshee","Fury","Gargoyle","Harpy","Ogre","Phantom","Reaper","Revenant","Valkyrie","Widow","Wraith"]
WeaponList = ["Claymore","Edge","Gladius","Hammer","Harpoon","Javelin","Katana","Lance","Naginata","Pilum","Sabre","Scimitar","Shuriken","Stiletto"]

#This is for armour, not weapons.
ArmourList = ["Plastron","Heater","Scutum","Buckler","Aspis","Phalanx","Tortuga","Mycenene","Dendra","Mempo","Galea","Casis","Lorica","Jazerant","Kazaghand","Hamata","Segmentata","Aketon","Pourpoint","Jack","Bezaint","Hauberk","Haubergeon","Thracian","Duplex","Berserker","Colossus","Duellist","Explorer","Gladiator","Guardian","Hydra","Liberator","Mantis","Onyx","Phantom","Phoenix","Predator","Scorpion","Survivor","Titan","Ursa","Kestrel","Ajax","Shade"]


def SerialCode(Name):
	if len(Name) > 1 and Name.endswith(" ") == False:
		Name += " "
	#if Normal != True:
	#	Max = random.randint(2,8)
	#else:
	#	Max = random.randint(2,3)
	Max = random.randint(2,8)
	for each in range(1,Max+1):
		if len(Name) == 0 or len(Name) >= Max+1 or Name.endswith("-") == True:
			Name += random.choice(random.choice([FullLetterList,NumberList]))
		else:
			Name += random.choice(random.choice([FullLetterList,NumberList,"-"]))	
	if Name.endswith("-") == True:
		Name += random.choice(random.choice([FullLetterList,NumberList]))
	return Name

def Designation(Name):
	if len(Name) > 1 and Name.endswith(" ") == False:
		Name += " "
	Max = random.randint(1,3)
	for each in range(1,Max+1):
		Name += random.choice(CoolLetterList)
	Name += random.choice(["","-"])
	Name += str(random.randint(1,299))
	if random.random() >= 0.8:
		Name += random.choice(EndingLetterList)
	return Name

def NickName(Name):
	if len(Name) > 1 and Name.endswith(" ") == False:
		Name += " "
	Name += random.choice(WordList)
	return Name

def Mark(Name):
	if len(Name) > 1 and Name.endswith(" ") == False:
		Name += " "
	Name += random.choice(["Mark","Mk","Mk."])
	if "Mark" in Name:		#does this work?
		Name += " "
	else:
		random.choice([""," "])
	Name += str(random.randint(1,5))
	return Name

def Brand(Name):
	if len(Name) > 1 and Name.endswith(" ") == False:
		Name += " "
	pass
	return Name

def VersionNum(Name):
	if len(Name) > 1 and Name.endswith(" ") == False:
		Name += " "
	pass
	return Name

def RomanNumeral(i):
	numeral_map = tuple(zip(
		(1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
		('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
	))
	result = []
	for integer, numeral in numeral_map:
		count = i // integer
		result.append(numeral * count)
		i -= integer * count
	return ''.join(result)

def RomanModel(Name):
	if len(Name) > 1 and Name.endswith(" ") == False:
		Name += " "
	Name += random.choice(WordList)
	Name += random.choice([" ","-"])
	Name += RomanNumeral(random.randint(1,25))
	if random.random() >= 0.75:
		Name  += random.choice(EndingLetterList)
	return Name

###

#Name types:		D-Nk, D-Nk-Mk, D-Nk-V, D-Nk-Gk, D-Nk-S, Nk-Ro, Br-SD
 # Designation, Nickname 		e.g. XTX-5 Guardian
 # Designation, Nickname, Mark 		e.g. XTX-5 Guardian Mark 2
 # Designation, Nickname, Version	e.g. XTX-5 Guardian v5.4
 # Designation, Nickname, Greek		e.g. XTX-5 Guardian Gamma
 # Designation, Nickname, Serial 	e.g. XTX-5 Guardian 056-AS2
 # Nickname, Roman numeral		e.g. Guardian-VII
 # Brand, Short Designation 		e.g. Caliburn M65e

Name = ""

def D_Nk(Name):
	Name = Designation(Name)
	Name = NickName(Name)
	return Name

def D_Nk_Mk(Name):
	Name = Designation(Name)
	Name = NickName(Name)
	Name = Mark(Name)
	return Name

def D_Nk_V(Name):
	Name = Designation(Name)
	Name = NickName(Name)
	Name = VersionNum(Name)		#Not implemented
	return Name

def D_Nk_Gk(Name):
	Name = Designation(Name)
	Name = NickName(Name)
	Name += " " + random.choice(GreekAlphabetList)
	return Name

def D_Nk_S(Name):
	Name = Designation(Name)
	Name = NickName(Name)
	Name = SerialCode(Name)
	return Name

def Nk_Ro(Name):
	Name = RomanModel(Name)
	return Name

def Br_SD(Name):
	Name = Brand(Name)		#Not implemented
	Name = Designation(Name)
	return Name

##

Name = random.choice([D_Nk(Name),D_Nk_Mk(Name),D_Nk_V(Name),D_Nk_Gk(Name),D_Nk_S(Name),Nk_Ro(Name),Br_SD(Name)])
print(Name)
