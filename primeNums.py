
nums = range(1,30) # print(list(nums))

def is_prime(num): # function to check if number is prime or not
    for x in range(2,num):
        if (num % x) == 0:
            return False
    return True

primes = list(filter(is_prime, nums))

print("#############")
print(" ")
print(f"These are all the prime numbers between", nums, ":", primes)
print(" ")
print("#############")