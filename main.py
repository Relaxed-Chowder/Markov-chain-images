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
    counter = 1
    click = 0
    redImage = numpy.zeros((height, width))
    with open("CSV/redProbabilityCSV.csv", newline='') as my_csv:
        redProbabilityCSV = [[int(value) for value in row] for row in csv.reader(my_csv)]
    
    for i in range(height):
        for j in range(width):
            if (j, i) == (0, 0):
                number = random.choices(list(range(0,256)), weights = redProbabilityCSV[0])
            
            number = random.choices(list(range(0,256)), weights = redProbabilityCSV[redBefore+1], k = height*width)

            redImage[i][j] = int(number[counter])
            redBefore = int(number[counter])
            #print(redBefore)
            #print()

    return redImage

# green
def greenLayer(height, width):
    greenProbabilityCSV = []
    greenBefore = 0
    counter = 1
    greenImage = numpy.zeros((height, width))
    with open("CSV/greenProbabilityCSV.csv", newline='') as my_csv:
        greenProbabilityCSV = [[int(value) for value in row] for row in csv.reader(my_csv)]
    
    for i in range(height):
        for j in range(width):
            if (j, i) == (0, 0):
                number = random.choices(list(range(0,256)), weights = greenProbabilityCSV[0])
            
            number = random.choices(list(range(0,256)), weights = greenProbabilityCSV[greenBefore+1], k = height*width)

            greenImage[i][j] = int(number[counter])
            greenBefore = int(number[counter])
            #print(greenBefore)
            #print()

    return greenImage

# blue
def blueLayer(height, width):
    blueProbabilityCSV = []
    blueBefore = 0
    counter = 1
    blueImage = numpy.zeros((height, width))
    with open("CSV/blueProbabilityCSV.csv", newline='') as my_csv:
        blueProbabilityCSV = [[int(value) for value in row] for row in csv.reader(my_csv)]
    
    for i in range(height):
        for j in range(width):
            if (j, i) == (0, 0):
                number = random.choices(list(range(0,256)), weights = blueProbabilityCSV[0])
            
            number = random.choices(list(range(0,256)), weights = blueProbabilityCSV[blueBefore+1], k = height*width)

            blueImage[i][j] = int(number[counter])
            blueBefore = int(number[counter])
            #print(blueBefore)
            #print()

    return blueImage

# alpha
def alphaLayer(height, width):
    alphaProbabilityCSV = []
    alphaBefore = 0
    counter = 1
    alphaImage = numpy.zeros((height, width))
    with open("CSV/alphaProbabilityCSV.csv", newline='') as my_csv:
        alphaProbabilityCSV = [[int(value) for value in row] for row in csv.reader(my_csv)]
    
    for i in range(height):
        for j in range(width):
            if (j, i) == (0, 0):
                number = random.choices(list(range(0,256)), weights = alphaProbabilityCSV[0])
            
            number = random.choices(list(range(0,256)), weights = alphaProbabilityCSV[alphaBefore+1], k = height*width)

            alphaImage[i][j] = int(number[counter])
            alphaBefore = int(number[counter])
            print(alphaBefore)
            print()

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

