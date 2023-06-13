
nums = range(1,100)
# print(list(nums))

def is_prime(num):
    for x in range(2,num):
        if (num % x) == 0:
            return False
    return True

primes = list(filter(is_prime, nums))

print(primes)