import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import ascify
import numpy as np

def magic():
    global ascii_img
    global f_img
    f_img = ascify.convert(img_loc=inp_filename)
    img_arr = np.asarray(f_img, dtype=np.uint8)
    out_img = Image.fromarray(img_arr)
    width = lbl_inp_img.winfo_width()
    height = lbl_inp_img.winfo_height()
    out_img = out_img.resize((width, height), Image.Resampling.LANCZOS)
    ascii_img = ImageTk.PhotoImage(image=out_img)
    lbl_out_img.configure(image=ascii_img)
    lbl_out_img.grid(row=2, column=1, sticky="nsew")
    btn_sav.grid(row=3, column=1, sticky="nsew")

def upload():
    global image
    global inp_filename
    f_types = [('All Files', '*'), ('Jpg Files', '*.jpg'), ('Png Files', '*.png')]
    inp_filename = filedialog.askopenfilename(filetypes=f_types)
    image = ImageTk.PhotoImage(file=inp_filename)
    lbl_inp_img.configure(image=image)
    lbl_inp_img.grid(row=2,column=0, sticky="nsew")
    btn_ask.grid(row=3, column=0, sticky="nsew")


def save_img():
    out_filename = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
    if not out_filename:
        return
    f_img.save(out_filename)


## TO DO:
# def inv_img():



window = tk.Tk()
window.title("spyMonk Image Modification")

window.rowconfigure([0, 1, 2, 3], weight=1)
window.columnconfigure([0, 1], weight=1)

lbl = tk.Label(master=window, text="Upload your Image", fg="RED")
lbl.grid(row=0,column=0, sticky="nsew")

lbl_inp_img = tk.Label(master=window)
lbl_out_img = tk.Label(master=window)

btn_upload = tk.Button(master=window, text="Upload Image", command=upload)
btn_upload.grid(row=1,column=0)

btn_ask = tk.Button(master=window, text="ASCIFY", command=magic)
btn_sav = tk.Button(master=window, text="Save", command=save_img)
# btn_invert = tk.Button(master=window, text="Save", command=inv_img)

window.mainloop()