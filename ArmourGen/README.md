# GURPS Armour Generator

## About

This program automates the process and calculations from the article *Eidetic Memory: Low-Tech Armour Design* by David L. Pulver, published in **_Pyramid #3/52: Low-Tech II_**. It expands upon the original system somewhat, adding the materials from **_GURPS Ultra-Tech_** which were not in the article, as well as essential wood and several armour options from **_GURPS Low-Tech_** (although these are currently non-functional). All values used for new materials were obtained from doing the armour creation calculations backwards on items from Ultra-Tech, so are totally consistent with those statistics.

## Use

This program must be run using a Python shell or interpreter that is compatible with Python 3.1 or greater. A compatible interpreter can be downloaded from the [official Python website](ttps://www.python.org/downloads/).

## Planned Changes
- Added the new materials from *Eidetic Memory: Cutting Edge Armor Design* from **_Pyramid #3/85_**.
- Add the meteoric iron, dragonbone and dragonhide materials from **_GURPS Dungeon Fantasy_**
- Plaintext output of statistics, formatted similarly to the armour tables in GURPS books.
- An easier-to-use way to select hit locations, rather than just totalling up their surface area from an input expression.
- Change logic so that helmets made from steel or iron plate are allowed before TL4.
- Allow the creation of complex armour - two distinct pieces (construction and material) layered or connected together.
- Legality Class calculation (this is tricky, since no guidelines exist for Low-Tech armours).
- HTML output of statistics, formatted to work with GURPS Character Sheet (http://gurpscharactersheet.com/).
- Random generation of armour properties, constrained by an input TL.
- Graphical user interface
- Compilation into an executable, so the program can be distributed and run without having to install Python and an interpreter.

## Known Issues

- Making iron or steel plate helmets below TL4 will always fail, even though this is allowed by the article as written. An error message will say that iron or steel plate must be TL4 or higher. This is due to the limitations of the system used for selecting hit locations and will be fixed when a more robust solution for armour locations has been implemented. In the meantime, the easiest workaround is to use iron or steel of your desired TL, then set the armour's TL to 4, since this doesn't directly modify anything. Don't set the TL any higher, since at TL5+ the cost of iron and steel is reduced.
- Legality Class is not calculated for any armour. This is due to a lack of concrete rules on this before TL9.
- Quality grades and special armour features (e.g. butted mail, fluting, etc.) are present in the code but not useable through the main interface.
