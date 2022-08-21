import cv2


def convert(img_loc):
    image = cv2.imread(img_loc)

    grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blur_gray_image = cv2.GaussianBlur(grey_image, (15, 15), 0)

    sketch_image = cv2.divide(grey_image, blur_gray_image, scale=256.0)

    return sketch_image
