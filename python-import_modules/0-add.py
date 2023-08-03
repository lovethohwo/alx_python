# Importing add function from another file
from add_0 import add

def outcome():
    a = 1
    b = 2
    total = add(a,b)
    print("{} + {} = {}".format(a,b, total))

if __name__ == "__main__":
    outcome()


