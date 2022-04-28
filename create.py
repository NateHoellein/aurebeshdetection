import cv2
from imageutils import *
import glob

BACKGROUNDS_DIR = 'backgrounds'
OUTPUT_DIR = 'output'
FONTS_DIR = 'fonts'

backgrounds = glob.glob("{0}/**/**".format(BACKGROUNDS_DIR), recursive=True)

backgrounds = random.sample(backgrounds, 10)

for b in backgrounds:

    resized_image = resizeBackground(b, (640, 640))

    fonts = getfonts(FONTS_DIR)

    paths = list(map(lambda p: os.path.join(FONTS_DIR, p), fonts))
    randomSplit = random.randint(1,4)

    x = 10
    y = 10
    biggestFont = 0
    for f in fonts:
        size = random.randint(40, 120)
        contours,box = getContours("{0}/{1}".format(FONTS_DIR, f), (size, size))
        if box[0] > biggestFont:
            biggestFont = box[0]
        for c in contours:
            print("drawing at: {0} {1} width {2}".format(x, y, box[0]))
            imageThirds = box[0] // 3
            if x + imageThirds + imageThirds > 640:
                print("two-thirds of the image: {0}".format(x + imageThirds +
                                                            imageThirds))
                x = 10
                y += biggestFont

            cv2.drawContours(resized_image,
                             contours, -1,
                             color=(255, 255, 255),
                             thickness=cv2.FILLED,
                             offset=(x, y))
            cv2.rectangle(resized_image,
                          (x, y),
                          (x + box[0], y + box[0]),
                          (255,0,0),2)
        x += box[0]
        if x > 640:
            x = 10
            y += biggestFont

    cv2.imshow("Markedup", resized_image)
    cv2.waitKey()

cv2.destroyAllWindows()
