# pyAsciiArt
little python program to convert an image to ascii art

## Using

be sure to have numpy installed

in order to convert an image, run in your terminal

$ python main.py NAME_OF_IMAGE OPTIONAL_WIDTH_OF_RESULT

where NAME_OF_IMAGE is the total name of the image including the file extension, can include total path to image on disk and OPTIONAL_WIDTH_OF_RESULT is the pixel/character width of the resultant image. if not used, defaults to 300. If you want to see your results in your terminal, I recommend setting the width to the size of your terminal.

the final result is saved in a text file in the same directory as main.py.

you can then display your image in the terminal by running

$ cat image.txt

an example converted image is provided.

## Example

![](example.png)
