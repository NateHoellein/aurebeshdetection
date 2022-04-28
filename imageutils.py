import cv2
import random
import os
import numpy as np

def resizeBackground(file, size):
    image = cv2.imread(file)
    return cv2.resize(image, size)

def getfonts(path):
        sampleSize = random.randint(7,15)
        fontFiles = [f for f in os.listdir(path) if not f.startswith('.')]
        fonts = random.sample(fontFiles, sampleSize)
        return fonts

def getContours(path, size):
    if not os.path.exists(path):
        print("path {0} not valid".format(path))
        return

    letter = cv2.imread(path)

    gray = cv2.cvtColor(letter,cv2.COLOR_RGB2GRAY)
    crop_rows = gray[~np.all(gray == 255, axis=1), :]
    cropped_image = crop_rows[:, ~np.all(crop_rows == 255, axis=0)]

    letter = cv2.resize(cropped_image, size)
    print("FONT BOX " + path)
    print(letter.shape)
    #cv2.imshow("font", letter)
    #cv2.waitKey()
    #cv2.destroyAllWindows()
    _,thresh = cv2.threshold(letter, np.mean(cropped_image), 255, cv2.THRESH_BINARY_INV)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contours, letter.shape


def drawWithBoundingBox(backgroundImage, path, size, color, offSet):
    contours = getContours(path, size)
    updatedbackground = cv2.drawContours(backgroundImage, contours,-1, color=color,
                                         thickness=cv2.FILLED, offset=offSet)
    minx,miny,maxx,maxy = getBoundingBox(contours, backgroundImage)
    #cv2.rectangle(backgroundImage,
    #              (minx+offSet[0],miny+offSet[1]),(maxx+offSet[0],maxy+offSet[1]),(255,0,0),2)
    return minx+offSet[0],miny+offSet[1],maxx+offSet[0],maxy+offSet[1]
