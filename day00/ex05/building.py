import sys
import string


def pars(argv):
    """
        parse each char of the string, and sum the corresponding variable
        then print
    """
    punctStr = string.punctuation
    count = sum(1 for c in argv)
    upper = sum(1 for c in argv if c.isupper())
    lower = sum(1 for c in argv if c.islower())
    digit = sum(1 for c in argv if c.isnumeric())
    space = sum(1 for c in argv if c.isspace())
    puncNb = sum(1 for c in argv if c in punctStr)

    print("The text contains ", count, "characters:")
    print(upper, "upper letters")
    print(lower, "lower letters")
    print(puncNb, " punctuation marks")
    print(space, "spaces")
    print(digit, "digits")


def main(argv):
    """
        look for the number of arg
        pars if it's 1 or 2
    """
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        elif len(sys.argv) == 1:
            print("What is the text to count?")
            inputStr = input()
            pars(inputStr)
        else:
            pars(sys.argv[1])
    except AssertionError as error:
        print("Assertion Error:", error)


if __name__ == "__main__":
    main(sys.argv)
