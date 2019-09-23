from math import sqrt

def is_prime(n):
    for a in range(2, int(sqrt(n))+1):
        print(a)
        if n % a == 0:
            return False
    return True

def max_prime_factor(x):
     max_primes = []
     for i in range(2, int(sqrt(x))):
         if x % i == 0:
             if is_prime(i):
                  max_primes.append(i)
             if is_prime(x/i):
                 max_primes.append(i)
     return max_primes

#print(max_prime_factor(13195))

print(is_prime(64))