from PIL import Image
import os
import numpy

# (hieght, width)
Probability = numpy.zeros((257, 257))


x = 0
directory = "inputed images"

for image in os.listdir(directory):
    channels = -1
    im = Image.open(directory + "\\" + image, "r")
    channelRgba = im.getpixel((0, 0))
    if isinstance(channelRgba, int):
        channels = 1
    elif isinstance(channelRgba, tuple):
        channels = len(channelRgba)

    print(type(channelRgba))
    print(image)
    x += 1
    for i in range(im.width):
        for j in range(im.height):
            rgba = im.getpixel((i, j))

            if channels == 1:
                rgba = [rgba, rgba, rgba, 255]
            elif channels <= 3:
                rgba = rgba + (255,)

            if (i%27, j%27) == (1,1) and x == 2:
                print("channels: " + str(channels))
                print("image: " + str(x) + " red: " + str(rgba))
                print()
                print()
            
            

print(x)
