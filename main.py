from PIL import Image
import os
import numpy
import time
import csv
import random

# (hieght, width)
redProbability = numpy.zeros((257, 256))
greenProbability = numpy.zeros((257, 256))
blueProbability = numpy.zeros((257, 256))
alphaProbability = numpy.zeros((257, 256))

x = 0
directory = "inputed images"

print("type (1) for image creation. type (2) for marckov chain creation.")
print("if canont read it will make a marckov chain.")
number = int(input())

if number == 1:
    redProbabilityCSV = [[]]
    greenProbabilityCSV = [[]]
    blueProbabilityCSV = [[]]
    alphaProbabilityCSV = [[]]
    redBefore = 0
    greenBefore = 0
    blueBefore = 0
    alphaBefore = 0
    height = int(input("input hieght: "))
    width = int(input("input width: "))
    while (not isinstance(height, int)) and (not isinstance(width, int)):
        print("invalid inputs")
        height = int(input("input hieght: "))
        width = int(input("input width: "))
    
    redImage = numpy.zeros((height, width))
    greenImage = numpy.zeros((height, width))
    blueImage = numpy.zeros((height, width))
    alphaImage = numpy.zeros((height, width))
    with open("CSV" + "\\" + "redProbabilityCSV.csv",newline='') as my_csv:
        redProbabilityCSV = list(csv.reader(my_csv, delimiter=','))


    with open("CSV" + "\\" + "greenProbabilityCSV.csv",newline='') as my_csv:
        greenProbabilityCSV = list(csv.reader(my_csv, delimiter=','))

    with open("CSV" + "\\" + "blueProbabilityCSV.csv",newline='') as my_csv:
        blueProbabilityCSV = list(csv.reader(my_csv, delimiter=','))

    with open("CSV" + "\\" + "alphaProbabilityCSV.csv",newline='') as my_csv:
        alphaProbabilityCSV = list(csv.reader(my_csv, delimiter=','))

    for i in range(height):
        for j in range(width):
            dice = 0
            for k in redProbability[redBefore]:
                dice += int(k)
                print(k)

            random = random.randint(0, dice)
            kIndex = -1
            for k in redProbability[redBefore]:
                while random > 0:
                    random -= k
                    kIndex += 1

            redImage[i][j] = kIndex
                
                
            



else:
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
        for i in range(im.height):
            for j in range(im.width):
                rgba = im.getpixel((j, i))

                if channels == 1:
                    rgba = [rgba, rgba, rgba, 255]
                elif channels <= 3:
                    rgba = rgba + (255,)

                redProbability[redBefore][rgba[0]] += 1
                greenProbability[greenBefore][rgba[1]] += 1
                blueProbability[blueBefore][rgba[2]] += 1
                alphaProbability[alphaBefore][rgba[3]] += 1

                if (j, i) == (1,1):
                    print("channels: " + str(channels))
                    print("image: " + str(x) + " red: " + str(rgba))
                    print()
                    print()

                redBefore = rgba[0] + 1
                greenBefore = rgba[1] + 1
                blueBefore = rgba[2] + 1
                alphaBefore = rgba[3] + 1
                
        end = time.time()
        length = end - start
        print("completion took", length, "seconds")
        
    for i in range(len(redProbability)):
        for j in range(len(redProbability[i])):
            if not(redProbability[i][j] > 0):
                print(str(i), str(j))

    with open("CSV" + "\\" + "redProbabilityCSV.csv","w+") as my_csv:
        csvWriter = csv.writer(my_csv,delimiter=',')
        csvWriter.writerows(redProbability)
    with open("CSV" + "\\" + "greenProbabilityCSV.csv","w+") as my_csv:
        csvWriter = csv.writer(my_csv,delimiter=',')
        csvWriter.writerows(greenProbability)
    with open("CSV" + "\\" + "blueProbabilityCSV.csv","w+") as my_csv:
        csvWriter = csv.writer(my_csv,delimiter=',')
        csvWriter.writerows(blueProbability)
    with open("CSV" + "\\" + "alphaProbabilityCSV.csv","w+") as my_csv:
        csvWriter = csv.writer(my_csv,delimiter=',')
        csvWriter.writerows(alphaProbability)

    print(numpy.amax(redProbability))
    print(x)
    print("finished")
