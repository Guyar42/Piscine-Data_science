import cv2


def ft_load(path: str) -> list:
    try:
        if not path.lower().endswith((".jpeg", ".jpg")):
            raise Exception("Image is not a jpeg or jpg")
        img = cv2.imread(path)
        if img is None:
            raise Exception("unreadable image")

        cv2.imshow('image', img)
        cv2.waitKey(4000)
        cv2.destroyAllWindows()

        print("The shape of image is:", img.shape)
        return img
    except Exception as e:
        print(e)
        return None


def main():
    print(ft_load('landscape.jpeg'))


if __name__ == "__main__":
    main()
