# import required modules
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps, ImageDraw, ImageFont
import os

# create functions


def on_closing():
    if messagebox.askokcancel("Exit the application.", "Want to quit the app?"):
        tk.destroy()


def selected():
    global img_path, img
    img_path = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          filetypes=[("Only photo", "*.jpg *.png"), ("All files", "*.*")])
    img = Image.open(img_path)
    width, height = img.size
    img = img.resize((round(width/3), round(height/3)), Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(img)
    canvas.create_image(450, 250, image=img1)
    canvas.image = img1


def selected_watermark():
    global wm_path, watermark, img, img_path, new_img, img2, img3
    img = Image.open(img_path)
    width, height = img.size
    wm_path = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          filetypes=[("Only photo", "*.jpg *.png"), ("All files", "*.*")])
    watermark = Image.open(wm_path).resize((round(width/2), round(width/2)), Image.ANTIALIAS)
    new_img = Image.new('RGBA', img.size, (0, 0, 0, 0))
    new_img.paste(img, (0, 0))
    new_img.paste(watermark, (0, 0), mask=watermark)
    img2 = new_img.resize((round(width / 3), round(height / 3)), Image.ANTIALIAS)
    img3 = ImageTk.PhotoImage(img2)
    canvas.create_image(450, 250, image=img3)
    canvas.image = img3


def save():
    global img_path, new_img, img1, img2, img3
    # file=None
    ext = img_path.split(".")[-1]
    file = asksaveasfilename(defaultextension=f".{ext}",
                             filetypes=[("All Files", "*.*"), ("PNG file", "*.png"), ("jpg file", "*.jpg")])
    rgb_img = new_img.convert('RGB')
    rgb_img.save(file)

# contrast border thumbnail

tk = Tk()
tk.protocol("WM_DELETE_WINDOW", on_closing)
tk.title("Watermark Photo Editor")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)

img1 = None
img2 = None
img3 = None

# create canvas to display image

canvas = Canvas(tk, width="900", height="600", bd=0, highlightthickness=0)
canvas.pack()

# create buttons

btn1 = Button(tk, text="Select Image", bg='grey', fg='black', font=('ariel 15'), relief=GROOVE, command=selected)
btn1.place(x=65, y=520)

btn2 = Button(tk, text="Select Watermark", bg='grey', fg='black', font=('ariel 15'), relief=GROOVE,
              command=selected_watermark)
btn2.place(x=255, y=520)

btn3 = Button(tk, text="Save", width=12, bg='grey', fg='black', font=('ariel 15'), relief=GROOVE, command=save)
btn3.place(x=490, y=520)

btn4 = Button(tk, text="Exit", width=12, bg='black', fg='white', font=('ariel 15'), relief=GROOVE,
              command=tk.destroy)
btn4.place(x=690, y=520)

tk.mainloop()