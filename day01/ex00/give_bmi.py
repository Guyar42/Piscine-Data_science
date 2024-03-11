import numpy as np


def check_array_int_or_float(arr):
    """check if the elemts in the arr are int or float"""
    for elt in arr:
        if not (np.issubdtype(type(elt), np.integer) or
                np.issubdtype(type(elt), np.floating)):
            raise ValueError("elements or not int or float")


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """ with numpy, transforme the list into an np array
        doing just w * h, np calculate all value in the tab
        we have to return it casted as a list
    """
    try:
        if type(height) is not list or type(weight) is not list:
            raise ValueError("elements is not a list")
        h = np.array(height)
        w = np.array(weight)
        check_array_int_or_float(h)
        check_array_int_or_float(w)
        imc = w / (h ** 2)
        return imc.tolist()

    except ValueError as e:
        print("Value Error:", e)
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """ the [] in return say that function return a list
        the condition is true or false for each element in the list
        so it return a list of true or false
    """

    # lst = []
    # for elt in bmi:
    #     lst.append(elt > limit)
    # return lst
    if len(bmi) == 0:
        return None
    return [elt > limit for elt in bmi]

    # return [elt for elt in bmi if elt > limit]
    # different because it send the resultat that respect the condition


def main():
    """print a tab with true or false depending on if
    the bmi is superior of the limit"""
    height = (1.71, 1.15)
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()
