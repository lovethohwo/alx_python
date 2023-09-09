<<<<<<< HEAD
for tens_digit in range(10):
    for ones_digit in range(tens_digit + 1, 10):
        print("{:02d}".format(tens_digit * 10 + ones_digit), end=', ')
print("\n")
=======
#!/usr/bin/python3

for i in range(10):
    for j in range(i + 1, 10):
        if i == 8 and j == 9:
            print("{:02d}".format(i * 10 + j))
        else:
            print("{:02d}, ".format(i * 10 + j), end="")
>>>>>>> 572169f2e17c9b6127c6b23fec1b22cd663f2ab1
