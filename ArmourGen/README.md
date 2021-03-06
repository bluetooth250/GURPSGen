# GURPS Armour Generator

## Outline
This is a Python3 program that automates the rules from the article *Eidetic Memory: Low-Tech Armour Design* from **_Pyramid #3/52: Low-Tech II_**. Input is via text-based interface in the Python shell and output is a text block in the python shell. When inputting informating, please take care to spell and format input exactly as given in the prompts, as there is currently little to no error handling or correction for incorrect inputs.

## Features
All functionality from the article is represented in this file. In addition, other features have either been added, are in development, or are planned. These include:
* New materials from *Eidetic Memory: Cutting Edge Armor Design* from **_Pyramid #3/85_**
* Metoric iron, dragonbone and dragonhide materials from **_GURPS Dungeon Fantasy_** and essential wood from **_GURPS Magic_**
* Materials from **_GURPS Ultra-Tech_**
* Armour features and quality grades from **_GURPS Low-Tech_**
* Complex armour creation - distinct pieces with different constructions and materials layered or connected together
* Randomly generated armour pieces, constrained by an input TL.
* Automatic output of statistics into XML format for GURPS Character Sheet

## Known Bugs

* Iron or steel plate can be used for helmets before TL4 but the program cannot currently check for this, so trying to make iron and steel helmets at TL3 will fail. This will be fixed when a more robust solution for tracking armour locations has been implemented. In the meantime, the easiest workaround is to use iron or steel of your desired TL, then set the armour to TL4. This doesn't directly modify anything but don't set the TL any higher, since at TL5+ the cost of iron and steel is reduced.
* Legality Class is not calculated for any armour. There are no concrete rules on this before TL9, so until those can be determined this will remain.
