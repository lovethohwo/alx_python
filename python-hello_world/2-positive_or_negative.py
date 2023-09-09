#word = "Holberton"
'''l=len(word)
print("First 3 letters: {}".format(word[0 : 3]))
print("Last 2 letters: {}".format(word[-2:]))
print("middle word: {}".format(word[1:-1]))
'''
import random

number = random.randint(-10, 10)

if number < 0:
    print("{} : is negative.".format(number))
elif number == 0:
    print("{} : is zero.".format(number))
else:
    print("{} : is positive.".format(number))

      