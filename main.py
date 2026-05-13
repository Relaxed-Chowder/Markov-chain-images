from PIL import Image
import os
import numpy
import time
import csv
import random

# (hieght, width)
redProbability = numpy.zeros((257, 256), dtype=int)
greenProbability = numpy.zeros((257, 256), dtype=int)
blueProbability = numpy.zeros((257, 256), dtype=int)
alphaProbability = numpy.zeros((257, 256), dtype=int)

x = 0
directory = "inputed images"


# red
def redLayer(height, width):
    redProbabilityCSV = []
    redBefore = 0
    clicks = 0
    redImage = numpy.zeros((height, width))
    with open("CSV/redProbabilityCSV.csv", newline='') as my_csv:
        redProbabilityCSV = [[int(value) for value in row] for row in csv.reader(my_csv)]
    
    for i in range(height):
        #print(str(redProbabilityCSV[redBefore]))
        #print()
        print(redBefore)
        print()
        for j in range(width):
            dice = 0
            for k in redProbabilityCSV[redBefore]:
                dice += int(k)

            randomness = random.randint(0, dice)
            kIndex = -1
            for k in redProbabilityCSV[redBefore]:
                if randomness <= 0:
                    break
                else:
                    randomness -= int(k)
                    kIndex += 1

            redImage[i][j] = kIndex
            redBefore = kIndex+1
            if redBefore > 255:
                clicks += 1
    print("clicks: " + str(clicks))
    return redImage

# green
def greenLayer(height, width):
    greenProbabilityCSV = []
    greenBefore = 0
    greenImage = numpy.zeros((height, width))
    with open("CSV/greenProbabilityCSV.csv", newline='') as my_csv:
        greenProbabilityCSV = [[int(value) for value in row] for row in csv.reader(my_csv)]
    
    for i in range(height):
        #print(str(greenProbabilityCSV[greenBefore]))
        for j in range(width):
            dice = 0
            for k in greenProbabilityCSV[greenBefore]:
                dice += int(k)

            randomness = random.randint(1, dice)
            kIndex = -1
            for k in greenProbabilityCSV[greenBefore]:
                if randomness <= 0:
                    break
                else:
                    randomness -= int(k)
                    kIndex += 1

            #print(greenBefore)
            #print()
            greenImage[i][j] = kIndex
            greenBefore = kIndex
    return greenImage

# blue
def blueLayer(height, width):
    blueProbabilityCSV = []
    blueBefore = 0
    blueImage = numpy.zeros((height, width))
    with open("CSV/blueProbabilityCSV.csv", newline='') as my_csv:
        blueProbabilityCSV = [[int(value) for value in row] for row in csv.reader(my_csv)]
    
    for i in range(height):
        #print(str(blueProbabilityCSV[blueBefore]))
        for j in range(width):
            dice = 0
            for k in blueProbabilityCSV[blueBefore]:
                dice += int(k)

            randomness = random.randint(1, dice)
            kIndex = -1
            for k in blueProbabilityCSV[blueBefore]:
                if randomness <= 0:
                    break
                else:
                    randomness -= int(k)
                    kIndex += 1

            #print(blueBefore)
            #print()
            blueImage[i][j] = kIndex
            blueBefore = kIndex
    return blueImage

# alpha
def alphaLayer(height, width):
    alphaProbabilityCSV = []
    alphaBefore = 0
    alphaImage = numpy.zeros((height, width))
    with open("CSV/alphaProbabilityCSV.csv", newline='') as my_csv:
        alphaProbabilityCSV = [[int(value) for value in row] for row in csv.reader(my_csv)]
    
    for i in range(height):
        #print(str(alphaProbabilityCSV[alphaBefore]))
        for j in range(width):
            dice = 0
            for k in alphaProbabilityCSV[alphaBefore]:
                dice += int(k)

            randomness = random.randint(1, dice)
            kIndex = -1
            for k in alphaProbabilityCSV[alphaBefore]:
                if randomness <= 0:
                    break
                else:
                    randomness -= int(k)
                    kIndex += 1

            #print(alphaBefore)
            #print()
            alphaImage[i][j] = kIndex
            alphaBefore = kIndex+1
    return alphaImage


def imageCreate(redImage, greenImage, blueImage, alphaImage):
    pass






print("type (1) for image creation. type (2) for marckov chain creation.")
print("if canont read it will make a marckov chain.")
number = int(input())

if number == 1:
    height = int(input("input hieght: "))
    width = int(input("input width: "))
    while (not isinstance(height, int)) and (not isinstance(width, int)):
        print("invalid inputs")
        height = int(input("input hieght: "))
        width = int(input("input width: "))
    
    imageStart = time.time()
    print("processing...")
    redImage = redLayer(height, width)
    greenImage = greenLayer(height, width)
    blueImage = blueLayer(height, width)
    alphaImage = alphaLayer(height, width)
    #imageCreate(redImage, greenImage, blueImage, alphaImage)
    imageEnd = time.time()
    length = imageEnd - imageStart
    print("finished! time took: " + str(length) + " seconds")
        


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
                    rgba = [int(rgba), int(rgba), int(rgba), 255]
                elif channels == 2:
                    rgba = [int(rgba[0]), int(rgba[0]), int(rgba[0]), int(rgba[1])]
                elif channels == 3:
                    rgba = rgba + (255,)

                redProbability[redBefore][int(rgba[0])] += 1
                greenProbability[greenBefore][int(rgba[1])] += 1
                blueProbability[blueBefore][int(rgba[2])] += 1
                alphaProbability[alphaBefore][int(rgba[3])] += 1

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
        k = 0
        for j in range(len(redProbability[i])):
            if redProbability[i][j] == 0:
                k += 1
            if k == 50:
                print(str(i) + " " + str(j))

    with open("CSV" + "\\" + "redProbabilityCSV.csv","w+",newline="") as my_csv:
        csvWriter = csv.writer(my_csv,delimiter=',')
        csvWriter.writerows(redProbability)
    with open("CSV" + "\\" + "greenProbabilityCSV.csv","w+",newline="") as my_csv:
        csvWriter = csv.writer(my_csv,delimiter=',')
        csvWriter.writerows(greenProbability)
    with open("CSV" + "\\" + "blueProbabilityCSV.csv","w+",newline="") as my_csv:
        csvWriter = csv.writer(my_csv,delimiter=',')
        csvWriter.writerows(blueProbability)
    with open("CSV" + "\\" + "alphaProbabilityCSV.csv","w+",newline="") as my_csv:
        csvWriter = csv.writer(my_csv,delimiter=',')
        csvWriter.writerows(alphaProbability)

    print(numpy.amax(redProbability))
    print(x)
    print("finished")
