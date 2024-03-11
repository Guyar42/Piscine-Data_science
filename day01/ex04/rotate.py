
from load_image import ft_load_zoom
import cv2
import numpy


def ft_tranpose(img: list) -> list:
    print("the shape of image is", img.shape)
    print(img)
    img = [
            [img[j][i] for j in range(len(img))]
            for i in range(len(img[0])-1, -1, -1)
        ]
    img = numpy.array(img)
    print("New shape after Transpose:", img.shape)
    print(img)
    cv2.imshow('image', img)
    cv2.waitKey(4000)
    cv2.destroyAllWindows()

    return img


def main():
    """take an image, print the zoomed version of an image"""
    ft_tranpose(ft_load_zoom('animal.jpeg'))


if __name__ == "__main__":
    main()