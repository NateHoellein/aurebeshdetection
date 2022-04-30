import cv2
from imageutils import *
import glob
import uuid

OUTPUT_DIR = 'output'
FONTS_DIR = 'fonts'
IMAGES_DIR = 'images'
LABELS_DIR = 'labels'
labelIndex = list(fontmap.values())


#backgrounds = random.sample(backgrounds, 10)

for i in range(21):

    image = np.zeros([640,640,1],dtype=np.uint8)
    image[:] = 0 

    fonts = getfonts(FONTS_DIR)

    paths = list(map(lambda p: os.path.join(FONTS_DIR, p), fonts))
    randomSplit = random.randint(1,4)

    x = random.randint(10, 600)
    y = random.randint(10, 600)
    color = (255,255,255)

    if random.randint(1,2) %2 == 0:
        coordinates = drawVerticle(image, x, y, fonts, color, 0, [])
    else:
        coordinates = drawHorizontal(image, x, y, fonts, color, 0, [])

    fileID = uuid.uuid4()
    cv2.imwrite("{0}/{1}.jpg".format(IMAGES_DIR, fileID), image)
    with open("{0}/{1}.txt".format(LABELS_DIR, fileID), 'w') as f:
        for c in coordinates:
            label = c[0]
            x = c[1]
            y = c[2]
            w = c[3]
            h = c[4]
            x_center = (float(x) + (w / 2)) / 640
            y_center = (float(y) + (h / 2)) / 640
            width = w / 640
            height = h / 640
            index = labelIndex.index(label)
            f.write("{0} ".format(index))
            f.write("{0} ".format(x_center))
            f.write("{0} ".format(y_center))
            f.write("{0} ".format(width))
            f.write("{0} \n".format(height))

    #cv2.imshow("Markedup", image)
    #cv2.waitKey()

#cv2.destroyAllWindows()

