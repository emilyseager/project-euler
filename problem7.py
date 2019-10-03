# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?
from math import sqrt
# def is_prime(n):
#     array_of_primes = []
#     for i in range(2, n):
#         for j in range(2, i):
#             if (i % j) == 0:
#                break
#         else:
#             array_of_primes.append(i)
#     return array_of_primes
# now we want the same function but we want to print if a number is prime - not all the prime numbers
def is_prime(n):
    for i in range(2, int(sqrt(n))+1):
        #print(i)
        if n % i == 0:
            return False
    return True

#now we want to find the 10,000st in the list

def nth_prime(n):
    number_of_primes = 0
    num = 1
    while number_of_primes < n:
        num = num + 1
        if is_prime(num):
            number_of_primes = number_of_primes + 1
    return num

print(nth_prime(10001))




