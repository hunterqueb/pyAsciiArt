import numpy as np
from PIL import Image
import sys

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

def translate(value, inputMax, outputMax):
    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value) / float(inputMax)

    # Convert the 0-1 range into a value in the right range.
    return int(valueScaled * outputMax)

ascii = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]

if __name__ == "__main__":
    imageName = sys.argv[1]
    if len(sys.argv) > 2:
        basewidth = int(sys.argv[2])
    else:
        basewidth = 300
    img = Image.open(imageName)
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    # resize image and save
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    img = np.array(img)
    gray = rgb2gray(img)    

    f = open("image.txt", "w")

    numAsciiChars = len(ascii)

    # 0 > 255
    # 0 > numAsciiChars

    grayConverted = np.zeros_like(gray)

    # translate the gray scale array to the translate gray scale so we can access the correct ascii character
    for i in range(len(gray[:,1])):
        for j in range(len(gray[1,:])):
            grayConverted[i,j]= translate(gray[i,j],255,numAsciiChars)

    grayConverted = grayConverted.astype(int)

    for i in range(len(gray[:,1])):
        f.write("\n")
        for j in range(len(gray[1,:])):
            string = ascii[grayConverted[i,j]]
            f.write(string)

    f.close()
