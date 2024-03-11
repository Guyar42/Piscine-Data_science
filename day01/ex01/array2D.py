import numpy as np


def check_var_int_or_float(var: int | float):
    if (not isinstance(var, (int)) and
            not isinstance(var, float)):
        raise ValueError("is not an int or a float")


def check_array_int_or_float(arr):
    """check if the elemts in the arr are int or float"""
    for elt in arr:
        for x in elt:
            if not (np.issubdtype(type(x), np.integer) or
                    np.issubdtype(type(x), np.floating)):
                raise ValueError("elements in the list are not int or float")


def slice_me(family: list, start: int | float, end: int | float) -> list:
    try:
        if type(family) is not list:
            raise ValueError("is not a list")
        check_array_int_or_float(family)
        check_var_int_or_float(start)
        check_var_int_or_float(end)
        arr = np.array(family)
        print("My shape is :", arr.shape)
        lst = family[start:end]
        arr = np.array(lst)
        print("My new shape is :", arr.shape)

        return lst
    except ValueError as e:
        print("ValueError:", e)
        return []


def main():
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))


if __name__ == "__main__":
    main()
