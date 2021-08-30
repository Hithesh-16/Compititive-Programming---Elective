# largestPerfectSquare(n) [10 pts]
# Write the function largestPerfectSquare(n) that takes a non-negative int n, and returns  the largest perfect
# square that is no larger than n. For example:
# assert(largestPerfectSquare(24) == 16)
# assert(largestPerfectSquare(25) == 25)
# assert(largestPerfectSquare(26) == 25)
# Hint: you may wish to use a similar approach to how you solved isPerfectSquare on the hw.
# Another hint: This can be written using just one or two lines of Python.

def largestperfectsquare(n):
	if isinstance(n, int) and n>=0:
		return n == (math.sqrt(n)**2)
  	elif isinstance(n, int) and  n<=0:
		  return False
  	elif isinstance(n, float):
		return False
  	elif n.isdigit():
		  n=int(n)
		  return n == (math.sqrt(n)**2)
	else:
		return False