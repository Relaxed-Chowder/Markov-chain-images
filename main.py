from PIL import Image
import os
import numpy
import time
import csv

# (hieght, width)
redProbability = numpy.zeros((257, 256))
greenProbability = numpy.zeros((257, 256))
blueProbability = numpy.zeros((257, 256))
alphaProbability = numpy.zeros((257, 256))

x = 0
directory = "inputed images"

for image in os.listdir(directory):
    redBefore = 0
    greenBefore = 0
    blueBefore = 0
    alphaBefore = 0
    Image.MAX_IMAGE_PIXELS = None
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
    start = time.time()
    for i in range(im.width):
        for j in range(im.height):
            rgba = im.getpixel((i, j))

            if channels == 1:
                rgba = [rgba, rgba, rgba, 255]
            elif channels <= 3:
                rgba = rgba + (255,)

            redProbability[redBefore+1][rgba[0]] += 1
            greenProbability[greenBefore+1][rgba[1]] += 1
            blueProbability[blueBefore+1][rgba[2]] += 1
            alphaProbability[alphaBefore+1][rgba[3]] += 1

            if (i, j) == (1,1):
                print("channels: " + str(channels))
                print("image: " + str(x) + " red: " + str(rgba))
                print()
                print()

            redBefore = rgba[0]
            greenBefore = rgba[1]
            blueBefore = rgba[2]
            alphaBefore = rgba[3]
            
    end = time.time()
    length = end - start
    print("completion took", length, "seconds")
    
for i in range(len(redProbability)):
    for j in range(len(redProbability[i])):
        if not(redProbability[i][j] > 0):
            print(str(i), str(j))

with open("redProbabilityCSV.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(redProbability)
with open("greenProbabilityCSV.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(greenProbability)
with open("blueProbabilityCSV.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(blueProbability)
with open("alphaProbabilityCSV.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(alphaProbability)

print(numpy.amax(redProbability))
print(x)
print("finished")
