<<<<<<< HEAD
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
statement = "The last digit of {}".format(number) + " is {}".format(last_digit)
if last_digit > 5:
    statement+= " and is greater than 5 "
elif last_digit == 0:
    statement+= " and is 0 "
else:
    statement+= " and is less than 6 and not 0 "
statement+= "\n"

print(statement)
=======
#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE


last_digit = abs(number) % 10
if number < 0:
    last_digit = -last_digit
    print("Last digit of",number,"is",last_digit,end=" ")
else:
     print("Last digit of", number,"is",last_digit,end=" ")

if number > 5:
    print("and is greater than 5")
elif number == 0:
    print("and is 0")
else: 
    print("and is less than 6 and not 0")
    


>>>>>>> 572169f2e17c9b6127c6b23fec1b22cd663f2ab1

      