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

      