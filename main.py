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

ascii = "@%#0*+=-;:'._ "[::-1]

if __name__ == "__main__":
    # get args
    imageName = sys.argv[1]
    if len(sys.argv) > 2:
        basewidth = int(sys.argv[2])
    else:
        basewidth = 150
    
    f = open("image.txt", "w")

    # image processing:
    # open image
    img = Image.open(imageName)
    # calculated new height based on new width 
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    # resize image and save
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    # convert image to numpy array, this is of the form [:,:,3]
    img = np.array(img)
    # convert 3d array to 2d array in gray scale
    gray = rgb2gray(img)    

    NUM_ASCII_CHARS = len(ascii)

    grayConverted = np.zeros_like(gray).astype(int)

    # translate the gray scale array to the translate gray scale so we can access the correct ascii character and then writes to file in same loop
    for i in range(len(gray[:,1])):
        # for every new line write to file new line character
        f.write("\n")
        for j in range(len(gray[1,:])):
            # for every pixel in a horizontal line:
            # convert the gray scale pixel to an integer corresponding to the total ascii string
            grayConverted = translate(gray[i,j],255,NUM_ASCII_CHARS)

            string = ascii[grayConverted]
            # then write the sting to the file
            f.write(string + ' ')

    f.close()
