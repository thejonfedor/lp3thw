
import random

min = random.randint(1,50) #set random minimum value for range
max = random.randint(51,1000) #set random maximum value for range
nums = range(min,max) #range of numbers in which we find all primes

def is_prime(num): # function to check if number is prime or not
    for x in range(2,num):
        if (num % x) == 0:
            return False
    return True

primes = list(filter(is_prime, nums)) #get a filtered list containing all primes in nums
countPrimes = len(primes) #how many primes are in the list?


print("\n#############\n")

print(f"There are", countPrimes, "prime numbers", "between", min, "and", max, "\n")
print(f"Here's a list of all the prime numbers in the above range:\n", primes)

print("\n#############\n")