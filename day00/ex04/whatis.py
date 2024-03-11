import sys

lenargv = len(sys.argv)

try:
    if lenargv > 2:
        raise AssertionError("more than one arugment is provided")
except AssertionError as error:
    print("AssertionError :", error)
else:
    if lenargv != 1:
        try:
            first = int(sys.argv[1])
            if (first % 2) == 0:
                print(first, "is even number")
            else:
                print(first, "is odd number")	
        except ValueError:
            print("AssertionError: argument is not an integer")
