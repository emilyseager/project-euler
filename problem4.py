# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
def palindrome_number(x):
    x = str(x)
    reversedstring = x[::-1]
    if x == reversedstring:
        return True


def largest_palindrome():
    find_palindrome = []
    for a in range(100, 999):
        for b in range(100, 999):
            product = str(a * b)
            if palindrome_number(product):
                find_palindrome.append(a * b)
    return find_palindrome


print(max(largest_palindrome()))
# palindrome_array = []
# for a in range(100, 999):
# for b in range(100, 999):
# product = str(b * a)
# if str(product) == str(product[::-1]):
##palindrome_array.append(b * a)
# print(max(palindrome_array))
