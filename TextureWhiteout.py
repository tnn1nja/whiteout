from PIL import Image, ImageEnhance
import os

#Pillow method
def whiteout(im):
    image = Image.open(im).convert("RGBA")

    decontrast = ImageEnhance.Contrast(image)
    image_decontrast = decontrast.enhance(0)
    whiteout = ImageEnhance.Brightness(image_decontrast)
    image_filtered = whiteout.enhance(10000000000000)
    decolor = ImageEnhance.Color(image_filtered)
    image_filtered = decolor.enhance(0)

    image_filtered.save(im)


#Loop
def findall(dir):
    os.chdir(dir)
    for f in os.listdir("."):
        if f.endswith(".png"):
            whiteout(f)
        if not f.endswith(".png") and not f.endswith(".mcmeta") and not f.endswith(".json")\
             and not f.endswith(".properties") and not f.endswith(".zip") and not f.endswith(".ini"):
            findall(f)
    os.chdir("..")

findall(".")
print("Images Whitened")
input("")