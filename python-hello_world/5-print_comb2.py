for number in range(100):
<<<<<<< HEAD
    print("{:02d}".format(number), end=', ')
print("\n")
=======
    print("{:02d}".format(number), end=", " if number < 99 else '\n')
>>>>>>> 572169f2e17c9b6127c6b23fec1b22cd663f2ab1
