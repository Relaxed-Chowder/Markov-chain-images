from PIL import Image
import os

x = 0
directory = "inputed images"

for image in os.listdir(directory):
    im = Image.open(directory + "\\" + image, "r")
    print(image)
    x += 1
    for i in range(im.width):
        for j in range(im.height):
            rgba = im.getpixel((i, j))
            if (i, j) == (1,1):
                print("image: " + str(x) + " red: " + str(rgba))

print(x)