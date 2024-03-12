import numpy as np
from load_image import ft_load_zoom


def check_var_int_or_float(var: int | float):
    """check if given var is int or float"""
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


def main():
    """take an image, print the zoomed version of an image"""
    print(ft_load_zoom('animal.jpeg'))


if __name__ == "__main__":
    main()
