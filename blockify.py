import cv2
import numpy as np
from PIL import Image, ImageDraw


def convert(img_loc):
    image = cv2.imread(img_loc)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    height, width, garbage = image.shape

    length = 10

    num_cols = int(width / length)
    num_rows = int(height / length)

    out_width = length * num_cols
    out_height = length * num_rows

    out_img = Image.new("RGB", (out_width, out_height))
    draw = ImageDraw.Draw(out_img)

    for i in range(int(num_rows)):
        for j in range(int(num_cols)):
            partial_image = image[int(i * length):   min(int((i + 1) * length), height),
                            int(j * length):   min(int((j + 1) * length), width),
                            :]

            partial_avg_color = np.sum(np.sum(partial_image, axis=0), axis=0) / (length * length)
            partial_avg_color = tuple(partial_avg_color.astype(np.int32).tolist())

            draw.rectangle((int(j * length), int(i * length), min(int((j + 1) * length), width),
                            min(int((i + 1) * length), height)), fill=partial_avg_color)

    cropped_img = out_img.getbbox()
    f_img = out_img.crop(cropped_img)
    return f_img
