import os
import cv2

with open('labels/0a1d6ac2-b650-4b59-a9bb-4925143aa4c6.txt', 'r') as f:
    lines = f.readlines()

image = cv2.imread('images/0a1d6ac2-b650-4b59-a9bb-4925143aa4c6.jpg')
h, w, _ = image.shape
print(image.shape)
newimage = cv2.imread('images/0a1d6ac2-b650-4b59-a9bb-4925143aa4c6.jpg')
for l in lines:
    contents = l.split(" ")
    print(contents)
    x = float(contents[1]) * w
    width = float(contents[3]) * w
    y = float(contents[2]) * h
    height = float(contents[4]) * h

    newx = x - (width/2)
    newy = y - (height/2)
    print(newx, newy, width, height)
    cv2.rectangle(newimage,
                  (int(newx), int(newy)),
                  (int(newx + width), int(newy + height)),
                  (0,255,0),2)


cv2.imshow('Generated', image)
cv2.imshow('Annotated', newimage)
cv2.waitKey()
cv2.destroyAllWindows()


