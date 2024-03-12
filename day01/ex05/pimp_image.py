from load_image import ft_load
import cv2
import numpy as np


def ft_invert(img: np.array) -> np.array:
    """invert the color of the image"""
    try:
        if len(img) == 0:
            raise Exception("Invert received an empty img")
        inverted = 255 - img

        cv2.imshow('image', inverted)
        cv2.waitKey(4000)
        cv2.destroyAllWindows()
        return inverted
    except Exception as e:
        print(e)
        return None


def ft_red(img: np.array) -> np.array:
    """put red filter on the image"""
    try:
        if len(img) == 0:
            raise Exception("ft_red error: ")
        B, G, R = cv2.split(img)
        red_img = cv2.merge((np.zeros_like(R), np.zeros_like(G), R))
        cv2.imshow('image', red_img)
        cv2.waitKey(4000)
        cv2.destroyAllWindows()
        red_img = np.array(red_img)
        return img
    except Exception as e:
        print(e)
        return (None)


def ft_green(img: np.array) -> np.array:
    """put green filter on the image"""
    try:
        if len(img) == 0:
            raise Exception("ft_green error: ")
        B, G, R = cv2.split(img)
        green_img = cv2.merge((np.zeros_like(G), G, np.zeros_like(B)))
        cv2.imshow('image', green_img)
        cv2.waitKey(4000)
        cv2.destroyAllWindows()
        green_img = np.array(green_img)
        return img
    except Exception as e:
        print(e)
        return (None)


def ft_blue(img: np.array) -> np.array:
    """put blue filter on the image"""
    try:
        if len(img) == 0:
            raise Exception("ft_blue error: ")
        B, G, R = cv2.split(img)
        blue_img = cv2.merge((B, np.zeros_like(B), np.zeros_like(B)))
        cv2.imshow('image', blue_img)
        cv2.waitKey(4000)
        cv2.destroyAllWindows()
        blue_img = np.array(blue_img)
        return img
    except Exception as e:
        print(e)
        return (None)


def ft_grey(img: np.array) -> np.array:
    """put grey filter on the image"""
    try:
        strlen = len(img)
        if strlen == 0:
            raise Exception("ft_grey error: ")
        img_cp = img
        for i in img_cp:
            for j in i:
                grey = j[1] / 3 + j[0] / 3 + j[2] / 3
                j[1] = grey
        img_grey = img[:, :, 1:-1]
        cv2.imshow('image', img_grey)
        cv2.waitKey(4000)
        cv2.destroyAllWindows()
        return img
    except Exception as e:
        print(e)
        return (None)


def main():
    """load an image and then show it with filter"""
    arr = np.array(ft_load('landscape.jpeg'))
    ft_invert(arr)
    ft_red(arr)
    ft_green(arr)
    ft_blue(arr)
    ft_grey(arr)


if __name__ == "__main__":
    main()
