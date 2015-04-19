#!/usr/bin/python

import sys
from PIL import Image, ImageFilter
from path import Path

# Take the path to the image file as an argument
imgPath = Path(sys.argv[1])
print imgPath, imgPath.basename()

# We first apply the CONTOUR filter to get the contours
# Then convert the image to black n white
# Traverse the pixels to get max and min positions of Black
img = Image.open(imgPath)
contourImg = img.filter(ImageFilter.CONTOUR)
binaryImg = contourImg.convert("1")
rows, cols = binaryImg.size

imgData = binaryImg.load()
edgeDataX = []
edgeDataY = []

print "Image size = (%d,%d)" % (rows, cols)

for x in xrange(rows):
    for y in xrange(cols):
        if imgData[x,y] == 0:
            edgeDataX.append(x)
            edgeDataY.append(y)

print "\nEdge Points of cropped image: "

print (min(edgeDataX), min(edgeDataY)), (max(edgeDataX), max(edgeDataY))
print "croppig image.."

croppedImg = img.crop((min(edgeDataX), min(edgeDataY), max(edgeDataX), max(edgeDataY)))
croppedImgPath = imgPath.dirname() / imgPath.namebase + "_cropped.jpg"
print "\nCropped Image saved at : " + croppedImgPath
croppedImg.save(croppedImgPath)

croppedImg.show()
