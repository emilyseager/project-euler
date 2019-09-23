n1 = 1
n2 = 2
var = 0

total_sum = 0
while var <= 4000000:
    var = n2
    if var % 2 == 0:
       total_sum = total_sum + var
    var = n1 + n2
    n1 = n2
    n2 = var

print (total_sum)



