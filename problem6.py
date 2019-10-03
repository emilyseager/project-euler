


def sum_of_squares(n):
    sum = 0
    for i in range(1, n+1):
        s = i**2
        sum = sum + s
        #print(i)
    return sum

print(sum_of_squares(100))

def square_of_sums(n):
    sum1 = []
    for i in range(1, n+1):
        #print(i)
        q = (i-1) + 1
        sum1.append(q)
    sum2 = sum(sum1)
    sum3 = (sum2)**2
    #print(sum2)
    return sum3
print(square_of_sums(100))

result = square_of_sums(100)-sum_of_squares(100)
print(result)
