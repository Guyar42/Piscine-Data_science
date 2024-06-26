import cv2


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
