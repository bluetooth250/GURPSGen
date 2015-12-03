# GURPSGen

## About
In this repository I keep and work on several different generators for **_GURPS 4e_** from Steve Jackson Games'. Most are in various stages of not-quite-finished but some are functional, if incomplete.

## Legal Information
GURPS is a trademark of Steve Jackson Games, and its rules and art are copyrighted by Steve Jackson Games. All rights are reserved by Steve Jackson Games. This game aid is the original creation of Tom Coates and is released for free distribution, and not for resale, under the permissions granted in the [Steve Jackson Games Online Policy](http://www.sjgames.com/general/online_policy.html).

While I don't know whether I am permitted to add a Creative Commons license to my work in addition to the required Steve Jackson Games legal notice, I would like anyone who looks at or modifies this sourcecode to act in the spirit of the [Attribution-NonCommercial-ShareAlike (BY-NC-SA)](https://creativecommons.org/licenses/by-nc-sa/4.0/) version of the Creative Commons license.

## Current Generators

#### ArmourGen
An automation of the rules from *Eidetic Memory: Low-Tech Armour Design* and *Eidetic Memory: Cutting Edge Armour Design* from **_Pyramid #3/52_** and **_Pyramid #3/85_**, respectively. The rules have been expanded upon where necessary to make the generator more complete, generic and customisable. Eventually, the program will also be able to randomly generate armours from input parameters and constraints.

*Status: Functional but incomplete*

#### EnergyWeaponGen
An automation of the rules from *Eidetic Memory: Blaster & Laser Design* from **_Pyramid #3/37_**. The rules have been expanded upon to make the generator more complete, generic and customisable. Eventually, the program will also be able to randomly generate armours from input parameters and constraints.

*Status: Functional (?) but incomplete*

#### GunGen
An automation of the projectile weapon creation rules from the much-maligned **_GURPS 3e Vehicles_** to create custom projectile weapons. Eventually, the program will also be able to randomly generate armours from input parameters and constraints.

*Status: Nonfunctional skeleton*

#### MeleeWeaponGen
Will generate melee weapons, including both Low-Tech and Ultra-Tech options.

*Status: Nonfunctional skeleton*

#### TreasureGen
Will generate miscellaneous treasure according to the rules in **_Dungeon Fantasy 8: Treasure Tables_**: coins, spices, fabrics, statues, idols, paintings, vases, pots, containers, drinks, food, etc.

*Status: Partially functional but untested*

## Planned Generators

#### BowGen
Will generate bows, according to the rules in *The Deadly Spring* from **_Pyramid #3/33_**.

#### CargoGen
Will generate cargo lots and passengers according to the rules in **_Spaceships 2: Traders, Liners, and Transports_**.

#### EnchantGen
Will generate enchantments according to the rules in **_Dungeon Fantasy 8: Treasure Tables_**, allowing them to be passed to other generators.

## Development Information
All code is written in Python 3.5.0, and needs at least Python 3.1+ to run (I think).

The code is written in British English. This only affects spellings but they are small changes that may be easy to miss. Some examples are:
- *Armour* instead of *armor*
- *Aluminium* instead of *aluminum*
- *Magnetised* instead of *magnetized*
- *Optimised* instead of *optimized*

All units are in GURPS' preferred Imperial/Customary units, which notably includes:
- Surface area: square feet (sqft) 
- Weight/mass: pounds (lbs)
