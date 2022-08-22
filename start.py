import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import ascify, sketchify, blockify

ascii_image_set = False
sketch_image_set = False
pixel_image_set = False


def magic_letter():
    global f_img
    global ascii_image, ascii_image_set, ascii_img_disp
    global h, w

    if ascii_image_set:
        f_img = ascii_image
    else:
        f_img = ascify.convert(img_loc=inp_filename)
        ascii_image = f_img
        ascii_image_set = True

    out_img = f_img.resize((w, h), Image.Resampling.LANCZOS)
    ascii_img_disp = ImageTk.PhotoImage(image=out_img)

    lbl_out_img.configure(image=ascii_img_disp)
    lbl_out_img.grid(row=2, column=1, sticky="nsew")
    btn_save.grid(row=3, column=1, sticky="nsew")


def magic_pencil():
    global f_img
    global pencil_sketch_image, sketch_image_set, sketch_image_display
    global h, w

    if sketch_image_set:
        f_img = pencil_sketch_image
    else:
        sk_img = sketchify.convert(img_loc=inp_filename)
        f_img = Image.fromarray(sk_img)
        pencil_sketch_image = f_img
        sketch_image_set = True

    out_img = f_img.resize((w, h), Image.Resampling.LANCZOS)
    sketch_image_display = ImageTk.PhotoImage(image=out_img)

    lbl_out_img.configure(image=sketch_image_display)
    lbl_out_img.grid(row=2, column=1, sticky="nsew")
    btn_save.grid(row=3, column=1, sticky="nsew")


def magic_block():
    global f_img
    global pixel_image, pixel_image_set, pixel_img_disp
    global h, w

    if pixel_image_set:
        f_img = pixel_image
    else:
        f_img = blockify.convert(img_loc=inp_filename)
        pixel_image = f_img
        pixel_image_set = True

    out_img = f_img.resize((w, h), Image.Resampling.LANCZOS)
    pixel_img_disp = ImageTk.PhotoImage(image=out_img)

    lbl_out_img.configure(image=pixel_img_disp)
    lbl_out_img.grid(row=2, column=1, sticky="nsew")
    btn_save.grid(row=3, column=1, sticky="nsew")


def upload():
    global image
    global inp_filename
    global ascii_image_set, sketch_image_set, pixel_image_set
    global h, w

    ascii_image_set = False
    sketch_image_set = False
    pixel_image_set = False

    f_types = [('All Files', '*'), ('Jpg Files', '*.jpg'), ('Png Files', '*.png')]
    inp_filename = filedialog.askopenfilename(filetypes=f_types)

    inp_img = Image.open(inp_filename)
    w, h = inp_img.size

    if h > 600:
        s = h / 600
        w = int(w / s)
        h = int(h / s)
    if w > 700:
        s = w / 700
        w = int(w / s)
        h = int(h / s)
    inp_img = inp_img.resize((w, h), Image.Resampling.LANCZOS)

    image = ImageTk.PhotoImage(image=inp_img)
    lbl_inp_img.configure(image=image)
    lbl_inp_img.grid(row=2, column=0, sticky="nsew")
    btn_sketch.grid(row=3, column=0, sticky="nsew")
    btn_ascii.grid(row=4, column=0, sticky="nsew")
    btn_pixel.grid(row=5, column=0, sticky="nsew")


def save_img():
    global f_img

    out_filename = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
    if not out_filename:
        return
    f_img.save(out_filename)


window = tk.Tk()
window.title("spyMonk ASCII Image Modification")
window.geometry("1200x1084")
window.rowconfigure([0, 1, 2, 3], weight=1)
window.columnconfigure([0, 1], weight=1)

lbl = tk.Label(master=window, text="Upload your Image 🖼", fg="Blue", font='Helvetica 32 bold', padx=200, pady=50)
lbl.grid(row=0, column=0, sticky="nsew")

lbl_inp_img = tk.Label(master=window)
lbl_out_img = tk.Label(master=window)

btn_upload = tk.Button(master=window, text="Upload Image", command=upload)
btn_upload.grid(row=1, column=0)

btn_ascii = tk.Button(master=window, text="ASCII Art", command=magic_letter)
btn_sketch = tk.Button(master=window, text="Sketch Art", command=magic_pencil)
btn_pixel = tk.Button(master=window, text="Pixel Art", command=magic_block)
btn_save = tk.Button(master=window, text="Save This Image", command=save_img)

window.mainloop()