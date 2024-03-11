import sys


def ft_filter(func, lst):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""

    return (x for x in lst if func(x) is True)


def ft_is_upper(s: str) -> bool:
    """check if the str is upper"""
    return s.isupper()


def main():
    sys.argv
    """ print the return of the filter"""

    lst = ["ABON", "b", "C", "d"]

    print(list(ft_filter(ft_is_upper, lst)))
    print(list(ft_filter(ft_is_upper, lst)))
    original = filter.__doc__
    copy = ft_filter.__doc__
    print(copy)  # output: docstring
    print(original == copy)  # output: True


if __name__ == "__main__":
    main()
