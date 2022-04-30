import cv2
import random
import os
import numpy as np

FONTS_DIR = 'fonts'

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

def drawVerticle(image, x, y, fonts, biggestFont, coordinates):

    if len(fonts) == 0:
        return coordinates
    f = fonts[0]
    fonts = np.delete(fonts, 0)

    size = random.randint(40, 120)
    contours,box = getContours("{0}/{1}".format(FONTS_DIR, f), (size, size))
    if box[0] > biggestFont:
        biggestFont = box[0]
    for c in contours:
        print("drawing at: {0} {1} width {2}".format(x, y, box[0]))
        imageThirds = box[0] // 3
        twoThirds = imageThirds + imageThirds
        if x + twoThirds > 640:
            print("\tX two-thirds of the image: {0}".format(x + twoThirds))
            x = 10
            y += biggestFont

        if y + twoThirds > 640:
            print("\tY two-thirds of the image: {0}".format(y + twoThirds))
            y = 10
            x += biggestFont

        cv2.drawContours(image,
                         contours, -1,
                         color=(255, 255, 255),
                         thickness=cv2.FILLED,
                         offset=(x, y))
        cv2.rectangle(image,
                      (x, y),
                      (x + box[0], y + box[0]),
                      (255,0,0),2)

    s = getCharacter(f)
    coordinates.append((s, x, y, box[0], box[1]))
    x += box[0]
    if x > 640:
        x = 10
        y += biggestFont

    return drawVerticle(image, x, y, fonts, biggestFont, coordinates)


def drawHorizontal(image, x, y, fonts, biggestFont, coordinates):

    if len(fonts) == 0:
        return coordinates
    f = fonts[0]
    fonts = np.delete(fonts, 0)

    size = random.randint(40, 120)
    contours,box = getContours("{0}/{1}".format(FONTS_DIR, f), (size, size))
    if box[0] > biggestFont:
        biggestFont = box[0]
    for c in contours:
        print("horizontal drawing at: {0} {1} width {2}".format(x, y, box[0]))
        imageThirds = box[0] // 3
        twoThirds = imageThirds + imageThirds
        if x + twoThirds > 640:
            print("\tX two-thirds of the image: {0}".format(x + twoThirds))
            x = 10
            y += biggestFont

        if y + twoThirds > 640:
            print("\tY two-thirds of the image: {0}".format(y + twoThirds))
            y = 10
            x += biggestFont

        cv2.drawContours(image,
                         contours, -1,
                         color=(255, 255, 255),
                         thickness=cv2.FILLED,
                         offset=(x, y))
        cv2.rectangle(image,
                      (x, y),
                      (x + box[0], y + box[0]),
                      (255,0,0),2)
    s = getCharacter(f)
    coordinates.append((s, x, y, box[0], box[1]))
    y += box[0]
    if y > 640:
        y = 10
        x += biggestFont

    return drawHorizontal(image, x, y, fonts, biggestFont, coordinates)

fontmap = {
    'aurek':'a',
    'besh':'b',
    'cresh':'c',
    'dorn':'d',
    'esk':'e',
    'forn':'f',
    'grek':'g',
    'herf':'h',
    'isk':'i',
    'jenth':'j',
    'krill':'k',
    'lenth':'l',
    'mern':'m',
    'nern':'n',
    'osk':'o',
    'peth':'p',
    'qek':'q',
    'resh':'r',
    'senth':'s',
    'trill':'t',
    'usk':'u',
    'vev':'v',
    'wesk':'w',
    'xesh':'x',
    'yirt':'y',
    'zerek':'z'
}

def getCharacter(path):
    fontpath = os.path.split(path)
    file = fontpath[1]
    name = file.split('_')
    character = name[0]
    return fontmap[character]
