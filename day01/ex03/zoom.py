import cv2
import numpy as np


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


def ft_load_zoom(path: str) -> list:
    """take an image, print the zoomed version of an image"""
    try:
        if not path.lower().endswith((".jpeg", ".jpg")):
            raise Exception("Image is not a jpeg or jpg")
        img = cv2.imread(path)
        if img is None:
            raise Exception("unreadable image")

        print("The shape of image is:", img.shape)
        print(img)

        zoom = img[125:500, 400:850, 0:1]

        cv2.imshow('image', zoom)
        cv2.waitKey(4000)
        cv2.destroyAllWindows()

        print("New shape after slicing:", zoom.shape)
        return zoom

    except Exception as e:
        print(e)
        return None


def main():
    """take an image, print the zoomed version of an image"""
    print(ft_load_zoom('animal.jpeg'))


if __name__ == "__main__":
    main()
