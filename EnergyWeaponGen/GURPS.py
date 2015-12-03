
def DiceRounder(x):
	"""Takes a dice number in decimal format and returns it in a string in dice+adds format."""
	IntDice = int(Dice)
	Fraction = Dice-int(Dice)
	if Dice > 12.0:
		return ("6d x " + str(round(Dice/6)))
	if Dice >= 1.0 and Dice <= 12.0:
		if Fraction >= 0.85:
			IntDice = IntDice+1
			Adds = ""
		elif Fraction >= 0.65:
			IntDice = IntDice+1
			Adds = "-1"
		elif Fraction >= 0.43:
			Adds = "+2"
		elif Fraction >= 0.15:
			Adds = "+1"
		else:
			Adds = ""
		return (str(IntDice) + "d" + Adds)
	if Dice < 1.0:
		IntDice = 1
		if Dice >=0.96:
			Adds = ''
		elif Dice >= 0.76:
			Adds = '-1'
		elif Dice >= 0.57:
			Adds = '-2'
		elif Dice >= 0.43:
			Adds = '-3'
		elif Dice >= 0.33:
			Adds = '-4'
		else:
			Adds = '-5'
		return (str(IntDice) + 'd' + Adds)

def Nd6(N):
	"""Takes an integer as an argument then rolls that many six-sided dice and returns the total."""
	result = 0
	for i in  range(1,N+1):
		result = result + random.randint(1,6)
	return result

def NdM(N,M):
	"""Takes two integers N and M as arguments then rolls N dice with M sides and returns the total."""
	result = 0
	for i in range(1,N+1):
		result = result + random.randint(1,M)
	return result

def SuccessRoll(sk,mod):
	"""Takes a skill and a modifier as arguments then performs a Success Test, returning boolean for success or failure"""
	roll = Nd6(3)
	if roll <= sk+mod:
		return True
	else:
		return False

def SuccessMargin(sk,mod):
	"""Takes a skill and a modifier as arguments then performs a Success Test, returning the margin of success or failure as an integer"""
	roll = Nd6(3)
	return sk+mod-roll

def QuickContest(sk1,mod1,sk2,mod2):		#Technically, quick contests also require knowledge of whether both players succeeded or failed individually. Fix this?
	"""Takes two skills and modifers as arguments then performs a Quick Conteest, returning the winner and their margin of success or failure in a dictionary."""
	result1= SuccessMargin(sk1,mod1)
	result2 = SuccessMargin(sk2,mod2)
	if result1 > result2:
		return {"Winner":1,"Margin":result2-result1}
	elif result2 > result1:
		return {"Winner":2,"Margin":result1-result2}
	elif result1 == result2:
		return {"Winner":0,"Margin":0}
	else:
		return 0

def QuickContestString(sk1,mod1,sk2,mod2):
	"""Takes two skills and modifers as arguments then performs a Quick Conteest, returning the winner and their margin of success or failure as a string."""
	result1= SuccessMargin(sk1,mod1)
	result2 = SuccessMargin(sk2,mod2)
	if result1 > result2:
		return ("Player 1 won by " + str(result2-result1))
	elif result2 > result1:
		return ("Player 2 won by " + str(result1-result2))
	elif result1 == result2:
		return "Player 1 and 2 tied."
	else:
		return "Something went wrong"



#
