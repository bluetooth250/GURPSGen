from ClassLibrary import BeamType

# Keyword definitions:
	# Affliction - this beam causes an affliction, rather than inflicting damage.
	# Laser - this beam is a laser.
	# NoIncendiary - this beam cannot start fires.
	# NoShotgun - this beam cannot be a shotgun or scatterbeam.
	# NotTightbeam - this beam inflicts normal burning damage, not tight-beam burning damage.
	# PulseCapable - this beam is a laser capable of firing in a pulsed mode.
	# StunCapable - this beam can optionally have an alternate nonlethal stunning mode.
	# Superscience - this beam requires superscience.
	# Tunable - this beam has a further selection for what type of neurostun effect it delivers.

BlankBeam = BeamType(
			name = "",			#
			TL = 0,				#
			E = 0.0,			#
			divisor = 0,			#
			baseAcc = 0,			#
			damageType = "",		#
			Rb = 0,				#
			shotCapacity = 0,		#
			Bc = 0,				#
			baseLC = 0,			#
			diceMult = 1.0,			#
			keywords = []			#
			)


## Beam Types from the Pyramid article ##

Blaster = BeamType(
			name = "Blaster",
			TL = 11,
			E = 3.0,
			divisor = 5,
			baseAcc = 5,
			damageType = "burn sur",
			Rb = 32,
			shotCapacity = 1080,
			Bc = 2000,
			baseLC = 3,
			diceMult = 1.0,
			keywords = ["StunCapable"]
			)

Force = BeamType(
			name = "Force beam",
			TL = 10,
			E = 4.0,
			divisor = 1,
			baseAcc = 6,
			damageType = "cr dbkb",
			Rb = 11,
			shotCapacity = 2160,
			Bc = 500,
			baseLC = 4,
			diceMult = 1.5,
			keywords = ["NoShotgun","Superscience"]
			)

Graser = BeamType(
			name = "Graser",
			TL = 12,
			E = 3.0,
			divisor = 10,
			baseAcc = 6,
			damageType = "burn",
			Rb = 6000,
			shotCapacity = 1800,
			Bc = 1500,
			baseLC = 3,
			diceMult = 1.0,
			keywords = ["Laser","PulseCapable"]
			)

Graviton = BeamType(
			name = "Graviton",
			TL = 11,
			E = 1.5,
			divisor = 1000,
			baseAcc = 6,
			damageType = "cr",
			Rb = 100,
			shotCapacity = 225,
			Bc = 2000,
			baseLC = 3,
			diceMult = 0.5,
			keywords = ["NoShotgun","Superscience"]
			)

Laser = BeamType(
			name = "Laser",
			TL = 10,
			E = 3.0,
			divisor = 2,
			baseAcc = 6,
			damageType = "burn",
			Rb = 40,
			shotCapacity = 1800,
			Bc = 500,
			baseLC = 3,
			diceMult = 1.0,
			keywords = ["Laser","PulseCapable"]
			)

Neutral = BeamType(
			name = "Neutral particle beam",
			TL = 11,
			E = 3.0,
			divisor = 1,
			baseAcc = 5,
			damageType = "burn rad sur",
			Rb = 32,
			shotCapacity = 270,
			Bc = 3000,
			baseLC = 3,
			diceMult = 1.0,
			keywords = []
			)

Pulsar = BeamType(
			name = "Pulsar",
			TL = 12,
			E = 6.0,
			divisor = 3,
			baseAcc = 5,
			damageType = "cr ex rad sur",
			Rb = 8,
			shotCapacity = 17280,
			Bc = 3000,
			baseLC = 2,
			diceMult = 2.0,
			keywords = []
			)

Rainbow = BeamType(
			name = "Rainbow laser",
			TL = 11,
			E = 3.0,
			divisor = 3,
			baseAcc = 6,
			damageType = "burn",
			Rb = 56,
			shotCapacity = 1800,
			Bc = 500,
			baseLC = 3,
			diceMult = 1.0,
			keywords = ["Laser"]
			)

Xray = BeamType(
			name = "X-ray laser",
			TL = 11,
			E = 3.0,
			divisor = 5,
			baseAcc = 6,
			damageType = "burn",
			Rb = 2000,
			shotCapacity = 1800,
			Bc = 1000,
			baseLC = 3,
			diceMult = 1.0,
			keywords = ["Laser","PulseCapable"]
			)

## Additional Beam Types from Ultra-Tech ##
	# EMP, neural, sonic screamer and sonic stun weapons need identical E and shotCapacity. E and Bc differ between configurations and the only way to make UT-like weapons is with per-configuration E and Bc, or fiddle factors.
        # Force beams are half as heavy as they should be (so half as expensive). Shots is slightly under half of what it should be. Range is 1/3.

Electrolaser = BeamType(
			name = "Electrolaser",
			TL = 9,
			E = 2.5,
			divisor = 2,
			baseAcc = 4,
			damageType = "aff",
			Rb = 22.5,
			shotCapacity = 2300,
			Bc = 1000,
			baseLC = 4,
			diceMult = 1.0,
			keywords = ["Affliction","NoShotgun"]
			)

EMP = BeamType(
			name = "EMP beam",
			TL = 9,
			E = 4.0,
			divisor = 1,
			baseAcc = 6,
			damageType = "aff",
			Rb = 5,
			shotCapacity = 1780,
			Bc = 500,
			baseLC = 2,
			diceMult = 1.0,
			keywords = ["Affliction","NoShotgun","Projector"]
			)

Neural = BeamType(
			name = "Neural beam",
			TL = 11,
			E = 4.0,
			divisor = 1,
			baseAcc = 6,
			damageType = "aff",
			Rb = 5,
			shotCapacity = 1780,
			Bc = 2000,
			baseLC = 4,
			diceMult = 1.0,
			keywords = ["Affliction","NoShotgun","Superscience","Tunable"]
			)

PlasmaFlamer = BeamType(
			name = "Plasma flamer",
			TL = 9,
			E = 2.75,
			divisor = 1,
			baseAcc = 3,
			damageType = "burn",
			Rb = 4,
			shotCapacity = 1792,
			Bc = 500,
			baseLC = 3,
			diceMult = 1.0,
			keywords = ["Jet","NoShotgun","NotTightbeam","Projector","Superscience"]
			)

PlasmaGun = BeamType(
			name = "Plasma gun",
			TL = 11,
			E = 8.3,
			divisor = 2,
			baseAcc = 4,
			damageType = "burn ex",
			Rb = 13.33,
			shotCapacity = 16750,
			Bc = 2000,
			baseLC = 3,
			diceMult = 1.0,
			keywords = ["Superscience"]
			)

SonicScreamer = BeamType(
			name = "Sonic screamer",
			TL = 9,
			E = 2.8,
			divisor = 1,
			baseAcc = 3,
			damageType = "cor",
			Rb = 4,
			shotCapacity = 1780,
			Bc = 1000,
			baseLC = 4,
			diceMult = 1.0,
			keywords = ["NoShotgun","Projector","Superscience"]
			)

SonicStun = BeamType(
			name = "Sonic stun",
			TL = 10,
			E = 2.35,	#2.8,
			divisor = 5,
			baseAcc = 3,
			damageType = "aff",
			Rb = 6.6,
			shotCapacity = 1780,
			Bc = 500,
			baseLC = 4,
			diceMult = 1.0,
			keywords = ["Affliction","NoShotgun"]
			)

## Custom Beam Types ##

Cryobeamer = BeamType(
			name = "Cryobeamer",
			TL = 10,
			E = 3.0,
			divisor = 1,
			baseAcc = 6,
			damageType = "burn",
			Rb = 40,
			shotCapacity = 1800,
			Bc = 500,
			baseLC = 3,
			diceMult = 1.0,
			keywords = ["NoIncendiary","PulseCapable"]
			)

CyclonicBeam = BeamType(
			name = "Cyclonic particle beam",
			TL = 10,
			E = 0.0,			# TO DO
			divisor = 0,			# TO DO
			baseAcc = 0,			# TO DO
			damageType = "imp",
			Rb = 0,				# TO DO
			shotCapacity = 0,		# TO DO
			Bc = 0,				# TO DO
			baseLC = 3,
			diceMult = 1.0,
			keywords = ["NoShotgun","Superscience"]
			)

ElectronBeam = BeamType(
			name = "Electron beam",
			TL = 10,
			E = 2.5,
			divisor = 1,
			baseAcc = 4,
			damageType = "burn sur",
			Rb = 22.5,
			shotCapacity = 1150,
			Bc = 1000,
			baseLC = 4,
			diceMult = 1.0,
			keywords = ["NoShotgun","StunCapable"]
			)

Lightning = BeamType(
			name = "Lightning Gun",
			TL = 7,
			E = 2.5,
			divisor = 1,
			baseAcc = 4,
			damageType = "burn sur",
			Rb = 22.5,
			shotCapacity = 1150,
			Bc = 1000,
			baseLC = 4,
			diceMult = 1.0,
			keywords = ["NoShotgun","StunCapable","Superscience"]
			)

PlasmaBeam = BeamType(					# Possibly increase divisor to 2 or 3. Bc needs to be changed to account for increased usefulness.
			name = "Plasma beam",
			TL = 10,
			E = 2.75,
			divisor = 1,
			baseAcc = 4,
			damageType = "burn",
			Rb = 4,
			shotCapacity = 1792,
			Bc = 500,
			baseLC = 3,
			diceMult = 1.0,
			keywords = ["NoShotgun","NotTightbeam","Superscience"]
			)


