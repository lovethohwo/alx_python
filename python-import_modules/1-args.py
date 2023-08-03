
import sys

def print_argument(argv):
    num_args = len(argv)

    if num_args == 0:
        print("0 arguments.")
        print(":")
    else:
        print(f"{num_args} arguments{'s' if num_args > 1 else ''}:")
        for i, arg in enumerate(argv, 1):
            print(f"{i}: {arg}")

if __name__ == "__main__":
    args = sys.argv[1:]
    print_argument(args)

        
