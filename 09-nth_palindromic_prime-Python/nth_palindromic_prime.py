# Write the function fun_nth_palindromic_prime(n) that takes 
# a non-negative int n and returns the nth palindromic Prime, 
# which is a palidrome number such that 
# it is also a prime. 

# For example, 313 is a palindrome and it is prime 
# so 313 is an palindrome Prime. fun_nth_palindrome_prime(0) 
# returns 2

def isPrime(n):
	for i in range(2,int(n**0.5)+1):
		if n%i==0:
			return False
	return True
    
def revNumber(num):
	rn = 0
	while(num!=0):
		rm = num%10
		rn = rn*10 + rm
		num = num//10
	return rn

def isPalindrome(num):
	rnum = revNumber(num)
	return (num == rnum)

def nthPalindromicPrime(x):
	cou = -1
	num=2
	while(cou!=x):
		if isPrime(num) and isPalindrome(num):
			cou = cou+1
		num = num+1
	return num-1
        
	

# print(nthPalindromicPrime(int(input())))