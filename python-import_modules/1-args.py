"""
import sys
if __name__ == "__main__":
    args = sys.argv[1:]
    num_args = len(args)
    if num_args == 0:
        print("0 arguments.")
    else:
        print(f"{num_args} argument{'s' if num_args > 1 else ''}:")
        for i, arg in enumerate(args, 1):
            print(f"{i}: {arg}")
"""

import sys

def print_arguments(argv):
    num_arguments = len(argv)
    if num_arguments == 0:
        print("Number of argument(s) : .")
        return
    
    plural_suffix = "s" if num_arguments > 1 else ""
    print(f"Number of argument{plural_suffix} : {num_arguments}.")
    
    for i, arg in enumerate(argv, 1):
        print(f"{i}: {arg}")

if __name__ == "__main__":
    print_arguments(sys.argv[1:])
