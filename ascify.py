import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageOps, ImageFont
import os

Characters = {
    "standard": "@%#*+=-:. ",
    "complex": "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
}


def get_data(mode):
    font_filename = "DejaVuSansMono"
    font = ImageFont.truetype(os.path.dirname(__file__) + "/fonts/" + font_filename + ".ttf", size=20)
    char_list = Characters[mode]
    return char_list, font


def convert(img_loc):
    (char_list, font) = get_data("complex")
    num_chars = len(char_list)
    num_cols = 300
    scale = 2

    image = cv2.imread(img_loc)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    height, width, garbage = image.shape

    cell_w = width / num_cols
    cell_h = scale * cell_w
    num_rows = int(height / cell_h)

    char_width, char_height = font.getsize("A")
    out_width = char_width * num_cols
    out_height = char_height * num_rows

    out_img = Image.new("RGB", (out_width, out_height), (255, 255, 255))
    draw = ImageDraw.Draw(out_img)

    for i in range(int(num_rows)):
        for j in range(int(num_cols)):
            partial_image = image[int(i * cell_h):   min(int((i + 1) * cell_h), height),
                            int(j * cell_w):   min(int((j + 1) * cell_w), width),
                            :]

            partial_avg_color = np.sum(np.sum(partial_image, axis=0), axis=0) / (cell_h * cell_w)
            partial_avg_color = tuple(partial_avg_color.astype(np.int32).tolist())

            c = char_list[min(int((int(np.mean(partial_image)) * num_chars) / 255), num_chars - 1)]

            draw.text((j * char_width, i * char_height), c, fill=partial_avg_color, font=font)

    cropped_img = out_img.getbbox()
    f_img = out_img.crop(cropped_img)

    return f_img