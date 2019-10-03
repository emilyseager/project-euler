import random
import string


def random_array(size=28, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))


print(random_array())
print(len(random_array()))


# now we need to make 100 copies of the string


def hundred_copies(n, length):
    output_array = [] * n
    for i in range(0, n):
        output_array.append(random_array())
    return output_array


# print(hundred_copies(100,28))

def prob_five():
    if random.randint(0, 99) <= 5:
        return True
    return False


# print(prob_five(5))

def single_char():
    letter = random.choice(string.ascii_letters)
    return letter.lower()


# def replacing_characters(num):
# if prob_five(num):


def search_through_string():
    output_array = hundred_copies(100, 28)
    for i in range(0, 99):
        array = output_array[i]
        print(array + " old ")
        for j in range(0, 28):
            if prob_five():
                list1 = list(array)
                list1[j] = single_char()
                array = ''.join(list1)
                print(array + " new ")
        output_array[i] = array
    return output_array


search_through_string()
#Compare each new string with the target string
# “METHINKS IT IS LIKE A WEASEL”, and give each a score
# (the number of letters in the string that are correct and in the correct position).
