"""
This code will not work without Python 3 and Pillow installed on the host machine,
ensure both are installed before running the script.
"""

from PIL import Image, ImageEnhance
import os

#Pillow Procedure
def whiteout(im):
    image = Image.open(im).convert("RGBA")

    decontrast = ImageEnhance.Contrast(image)
    image_decontrast = decontrast.enhance(0)
    whiteout = ImageEnhance.Brightness(image_decontrast)
    image_filtered = whiteout.enhance(10000000000000)
    decolor = ImageEnhance.Color(image_filtered)
    image_filtered = decolor.enhance(0)

    image_filtered.save(im)


#Recursive Loop
def findall(dir):
    os.chdir(dir)
    for f in os.listdir("."):
        if f.endswith(".png"):
            whiteout(f)
        elif f.find(".") == -1:
            findall(f)
    os.chdir("..")

#Call
findall(".")
print("Images Whitened")
input("")
