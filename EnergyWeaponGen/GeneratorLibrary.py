from ClassLibrary import Generator

BlankGenerator = Generator(
			name = "",
			minRoF = 0,
			maxRoF = 0,
			G = 0,
			Gc = 0,
			)

SingleShot = Generator(
			name = "Single shot",
			minRoF = 1,
			maxRoF = 1,
			G = 1.0,
			Gc = 1.0,
			)

SemiAuto = Generator(
			name = "Semi-automatic",
			minRoF = 2,
			maxRoF = 3,
			G = 1.25,
			Gc = 1.0,
			)

LightAuto = Generator(
			name = "Light automatic",
			minRoF = 4,
			maxRoF = 10,
			G = 1.25,
			Gc = 2.0,
			)

HeavyAuto = Generator(
			name = "Heavy automatic",
			minRoF = 11,
			maxRoF = 20,
			G = 2.0,
			Gc = 2.0,
			)
