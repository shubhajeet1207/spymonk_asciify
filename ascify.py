import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageOps, ImageFont

# Characters used for Mapping to Pixels
Character = {
    "standard": "@%#*+=-:. ",
    "complex": "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
}


def get_data(mode):
    font = ImageFont.truetype("fonts/DejaVuSansMono.ttf", size=20)
    scale = 2
    char_list = Character[mode]
    return char_list, font, scale


# Making Background Black or White
bg = "black"
if bg == "black":
    bg_code = (255,255,255)
elif bg == "white":
    bg_code = (0,0,0)

# Getting the character List, Font and Scaling characters for square Pixels
(char_list, font, scale) = get_data("complex")
num_chars = len(char_list)
num_cols = 300

# Reading Input Image
img = cv2.imread("./input_images/testing_image.jpg")

# Run to see the read input
# cv2.imshow('inputAsRead', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Converting Color Image to Grayscale
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Run to see the converted input
# cv2.imshow('inputafterBGR2GRAY', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Extracting height and width from Image
height, width, garbage = img.shape

# Defining height and width of each cell/pixel
cell_w = width/num_cols
cell_h = scale*cell_w
num_rows = int(height/cell_h)

# Calculating Height and Width of the output Image
char_width, char_height = font.getsize("A")
out_width = char_width*num_cols
out_height = scale*char_height*num_rows

# Making a new Image using PIL
out_img = Image.new("RGB", (out_width, out_height), bg_code)
draw = ImageDraw.Draw(out_img)

# Run to open a window of the created blank image
# out_img.show()

# Mapping the Characters for i in range(num_rows): min_h = min(int((i+1)*cell_h), height) row_pix = int(i*cell_h)
# line = "".join([char_list[min(int(np.mean(img[row_pix:min_h, int(j*cell_w):min(int((j+1)*cell_w),
# width)])/255*num_chars), num_chars-1)] for j in range(num_cols)]) + "\n"

# # Draw string at a given position (x,y)
#     draw.text((0, (i+char_height)*25), line, fill = 255-bg_code, font = font)

# Mapping Characters for RGB
for i in range(num_rows):
    for j in range(num_cols):
        partial_image = img[int(i*cell_h):min(int((i+1)*cell_h), height), int(j*cell_w):min(int((j+1)*cell_w), width), :]
        partial_avg_color = np.sum(np.sum(partial_image, axis=0), axis=0)/(cell_h*cell_w)
        partial_avg_color = tuple(partial_avg_color.astype(np.int32).tolist())
        c = char_list[min(int((int(np.mean(partial_image))*num_chars)/255), num_chars-1)]
        draw.text((j*char_width, i*char_height), c, fill = partial_avg_color, font = font)

# Inverting Image and removing excess borders
if bg == "white":
    cropped_img = ImageOps.invert(out_img).getbbox()
elif bg == "black":
    cropped_img = out_img.getbbox()

# Saving the new Image
out_img = out_img.crop(cropped_img)
out_img.save("./output_images/testing_output.jpg")