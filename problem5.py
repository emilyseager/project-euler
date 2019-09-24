# 2520 is the smallest number that can be divided by each of the
# numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


# begin with brute force approach
# make a function that checks if some number num is divisible by numbers 1 to 20

def divisibleupto20(val):
    for i in range(1, 21):
        if val % i != 0:
           return False
    return True


# make a loop that check all numbers up to infinity until we find the smallest number
# divisble by all these numbers

val = 20
while True:
    if divisibleupto20(val):
        break
    else:
        val += 1
print(val)



# once this is working then test with prime factorisation approach
