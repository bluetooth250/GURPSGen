#Generate whether firearm or EM gun
#Generate modifiers:
    #Dice modifer
    #Accuracy modifier
    #Range modifier
    #Weight modifier
    #RoF modifier
    #Shots capacity modifier
    #Bulk (based on weight?)
    #Recoil (based on weight and dice?)
#Generate CF of all modifiers
#Generate accesories
#Generate loaded ammo:
    #Incendiary rounds - add inc modifier, x1.5 CPS
    #Tracer rounds - add inc modifier, allows a +1 to shooting after long bursts, x1.5 CPS

import random
CF = 1.0

TL = 10
if TL == 9:
    WeaponList
elif TL == 10;

#   #   #

#Firearms
    #Pistols
HeavyPistol = {'DamageDice':3.0,'Divisor':1,'DamageType':'pi+','Acc':2,'HalfRange':180.0,'FullRange':2000.0,'Weight':2.5,'AmmoWeight':0.7,'RoF':3,'RoF2':1,'Shots':20,'Reload':3,'ST':10,'Bulk':-3,'Rcl':3,'Cost':540.0,'LC':3,'Ammo':'10mmCLP'}
HoldoutPistol = {'DamageDice':2.0,'Divisor':1,'DamageType':'pi','Acc':1,'HalfRange':100.0,'FullRange':1200.0,'Weight':1.0,'AmmoWeight':0.2,'RoF':3,'RoF2':1,'Shots':18,'Reload':3,'ST':6,'Bulk':-1,'Rcl':2,'Cost':240.0,'LC':3,'Ammo':'7.5mmCLP'}
MagnumPistol = {'DamageDice':4.25,'Divisor':1,'DamageType':'pi++','Acc':2,'HalfRange':235.0,'FullRange':2600.0,'Weight':3.0,'AmmoWeight':1.0,'RoF':3,'RoF2':1,'Shots':9,'Reload':3,'ST':11,'Bulk':-2,'Rcl':4,'Cost':870.0,'LC':3,'Ammo':'15mmCLP'}
MediumPistol = {'DamageDice':2.5,'Divisor':1,'DamageType':'pi','Acc':2,'HalfRange':150.0,'FullRange':1900.0,'Weight':2.0,'AmmoWeight':0.5,'RoF':3,'RoF2':1,'Shots':30,'Reload':3,'ST':9,'Bulk':-2,'Rcl':2,'Cost':450.0,'LC':3,'Ammo':'7.5mmCLP'}
    #SMGs
MachinePistol = {'DamageDice':,'Divisor':,'DamageType':,'Acc':,'HalfRange':,'FullRange':,'Weight':,'AmmoWeight':,'RoF':,'RoF2':,'Shots':,'Reload':,'ST':,'Bulk':,'Rcl':,'Cost':,'LC':,'Ammo':}
PDW = {'DamageDice':,'Divisor':,'DamageType':,'Acc':,'HalfRange':,'FullRange':,'Weight':,'AmmoWeight':,'RoF':,'RoF2':,'Shots':,'Reload':,'ST':,'Bulk':,'Rcl':,'Cost':,'LC':,'Ammo':}
UrbanAssault = {'DamageDice':,'Divisor':,'DamageType':,'Acc':,'HalfRange':,'FullRange':,'Weight':,'AmmoWeight':,'RoF':,'RoF2':,'Shots':,'Reload':,'ST':,'Bulk':,'Rcl':,'Cost':,'LC':,'Ammo':}
    #Rifles
AntiMateriel = {'DamageDice':,'Divisor':,'DamageType':,'Acc':,'HalfRange':,'FullRange':,'Weight':,'AmmoWeight':,'RoF':,'RoF2':,'Shots':,'Reload':,'ST':,'Bulk':,'Rcl':,'Cost':,'LC':,'Ammo':}
AssaultCarbine = {'DamageDice':,'Divisor':,'DamageType':,'Acc':,'HalfRange':,'FullRange':,'Weight':,'AmmoWeight':,'RoF':,'RoF2':,'Shots':,'Reload':,'ST':,'Bulk':,'Rcl':,'Cost':,'LC':,'Ammo':}
GatlingCarbine = {'DamageDice':,'Divisor':,'DamageType':,'Acc':,'HalfRange':,'FullRange':,'Weight':,'AmmoWeight':,'RoF':,'RoF2':,'Shots':,'Reload':,'ST':,'Bulk':,'Rcl':,'Cost':,'LC':,'Ammo':}
HuntingRifle = {'DamageDice':,'Divisor':,'DamageType':,'Acc':,'HalfRange':,'FullRange':,'Weight':,'AmmoWeight':,'RoF':,'RoF2':,'Shots':,'Reload':,'ST':,'Bulk':,'Rcl':,'Cost':,'LC':,'Ammo':}
PayloadRifle = {'DamageDice':,'Divisor':,'DamageType':,'Acc':,'HalfRange':,'FullRange':,'Weight':,'AmmoWeight':,'RoF':,'RoF2':,'Shots':,'Reload':,'ST':,'Bulk':,'Rcl':,'Cost':,'LC':,'Ammo':}
StormCarbine = {'DamageDice':,'Divisor':,'DamageType':,'Acc':,'HalfRange':,'FullRange':,'Weight':,'AmmoWeight':,'RoF':,'RoF2':,'Shots':,'Reload':,'ST':,'Bulk':,'Rcl':,'Cost':,'LC':,'Ammo':}
StormRifle = {'DamageDice':,'Divisor':,'DamageType':,'Acc':,'HalfRange':,'FullRange':,'Weight':,'AmmoWeight':,'RoF':,'RoF2':,'Shots':,'Reload':,'ST':,'Bulk':,'Rcl':,'Cost':,'LC':,'Ammo':}
    #Shotguns
CivilianShotgun = {'DamageDice':,'Divisor':,'DamageType':,'Acc':,'HalfRange':,'FullRange':,'Weight':,'AmmoWeight':,'RoF':,'RoF2':,'Shots':,'Reload':,'ST':,'Bulk':,'Rcl':,'Cost':,'LC':,'Ammo':}
CloseAssaultWeapon = {'DamageDice':,'Divisor':,'DamageType':,'Acc':,'HalfRange':,'FullRange':,'Weight':,'AmmoWeight':,'RoF':,'RoF2':,'Shots':,'Reload':,'ST':,'Bulk':,'Rcl':,'Cost':,'LC':,'Ammo':}
ShotgunPistol = {'DamageDice':,'Divisor':,'DamageType':,'Acc':,'HalfRange':,'FullRange':,'Weight':,'AmmoWeight':,'RoF':,'RoF2':,'Shots':,'Reload':,'ST':,'Bulk':,'Rcl':,'Cost':,'LC':,'Ammo':}
UnderbarrelShotgun = {'DamageDice':,'Divisor':,'DamageType':,'Acc':,'HalfRange':,'FullRange':,'Weight':,'AmmoWeight':,'RoF':,'RoF2':,'Shots':,'Reload':,'ST':,'Bulk':,'Rcl':,'Cost':,'LC':,'Ammo':}


#Electromagnetic Guns



#   #   #

WeaponName = {'DamageDice':,'Divisor':,'DamageType':,'Acc':,'HalfRange':,'FullRange':,'Weight':,'AmmoWeight':,'RoF':,'RoF2':,'Shots':,'Reload':,'ST':,'Bulk':,'Rcl':,'Cost':,'LC':,'Ammo':}



if ETC = 'y':
    DamageDice = DamageDice*1.5
    HalfRange = HalfRange*1.5
    FullRange = FullRange*1.5
    CF = CF+1.0

if LPST = 'y'
    Shots = Shots*1.5
    CF = CF+0.5



#   #   #
