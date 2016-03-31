from ClassLibrary import Configuration

BlankConfiguration = Configuration(
			name = "",
			accMult = 0,
			STMult = 0,
			bulkMult = 0,
			minBulk = 0,
                        damageMean = 0.0,
                        damageDeviation = 0.0,
			)

Beamer = Configuration(
			name = "Beamer",
			accMult = 0.5,
			STMult = 3.3,
			bulkMult = 1.0,
			minBulk = 0,
                        damageMean = 2.0,
                        damageDeviation = 0.5,
			)

Pistol = Configuration(
			name = "Pistol",
			accMult = 1.0,
			STMult = 3.3,
			bulkMult = 1.25,
			minBulk = 1,
                        damageMean = 3.0,
                        damageDeviation = 1.0,
			)

Rifle = Configuration(
			name = "Rifle",
			accMult = 2.0,
			STMult = 2.2,
			bulkMult = 1.5,
			minBulk = 3,
                        damageMean = 5.5,
                        damageDeviation = 1.5,
			)

Cannon = Configuration(
			name = "Cannon",
			accMult = 3.0,
			STMult = 2.4,
			bulkMult = 1.5,
			minBulk = 6,
                        damageMean = 12.0,
                        damageDeviation = 3.0,
			)
