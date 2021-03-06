# GURPS Energy Weapon Generator

## Outline
This is a Python3 program that automates the rules from the article *Eidetic Memory: Blaster & Laser Design* from **_Pyramid #3/37_**. Input is via text-based interface in the Python shell and output is a text block in the python shell with an option for XML data written to a GCS equipment file. When inputting informating, please take care to spell and format input exactly as given in the prompts, as there is currently little to no error handling or correction for incorrect inputs.

## Features
All functionality from the article is represented in this file, with the exception of beam cannon. In addition, other features have either been added, are in development, or are planned. These include:
* Blue-green and ultraviolet high-energy lasers
* Pulse lasers, including dual-mode beam/pulse lasers
* Scatterbeams ("beam shotguns") including weapons switchable between normal and scatterbeam modes
* Nonrechargeable power cells
* Cheap, Expensive, Hotshotted, Disguised, Styled, Rugged, Fine/Very Fine (Accurate) and Fine/Very Fine (Reliable) weapons
* Weapon accessories
* Beam types from Ultra-Tech not represented in the article (currently: electrolasers, microwave disruptors, neural beams, sonic screamers, sonic stun beams, plasma flamers, plasma guns)
* Randomly generated beam weapons

## Random Generation
The program is also capable of generating a random beam weapon based on an input TL. This feature is *nearly* complete; currently everything but the name, rate of fire, number/kind of power cells and qualities/features are randomised. As other features are added and verified to be working, the random generator will be updated to include them.

## GURPS Character Sheet Output Format
The program is able to automatically write the properties of beam weapons (whether designed or generated) into the XML format that GURPS Character Sheet uses. Currently this is done after a weapon's stats are calculated, with a yes/no prompt from the user. The object is written to the file called BeamGen.eqp in the same folder as the main file. Moving this file from the EnergyWeaponGen folder will cause this functionality to break. To add these objects to your characters or main GCS libraries, it is recommended that you use GCS' file dialogue to open BeamGen.eqp, then copy the weapons you want to character sheets or custom equipment libraries that are saved in the normal locations GCS uses.

## Known Bugs
### Article
* The number of shots a weapon could fire was prone to inaccuracies due to the complicated nature of adjusting power cell capacity based on TL. Although **_Ultra-Tech_** does mention an increase in power cell capacity per TL, this behaviour is not represented or even mentioned in the statistics for beam weapons, so it has been removed for now, using power cell capacities that are static and based on the TL at the weapon's introduction. It may be re-added in the future, especially if increased shot capacity by TL is confirmed as an intended feature by the designers.
* Trying to create copies of weapons from **_Ultra-Tech_** will provide results that are not exactly the same, though the variations are small, typically around 0.2lbs or $100 off. This was acknowledged by the author of the original article.
* Rifles using rainbow laser, X-ray laser or graser beams have about half the range of equivalent weapons in **_Ultra-Tech_**. This has been fixed with a 'fiddle factor' that is marked clearly in the code.

### Program
* Although the program allows you to generate several weapons in succession, keywords are not cleared between weapons. So making one cheap weapon followed by an expensive weapon will produce a weapon that is both cheap and expensive. For the time being, restart the program between uses.
* Neural, sonic screamer and sonic stun beam weapons have weights and costs totally incongruous with those listed in **_Ultra-Tech_**. This is due to the properties for these weapons varying significantly between each weapon configuration. The only way to fix this would be to define the properties separately per configuration.
* When writing weapons that have linked or alternate fire modes (electrolasers, dual-mode beam/pulse lasers and dual-mode scatterbeams) to a GCS file, only the primary firing mode is added.
