import time
from src.image_handler import Image_handler
from src.mouse_automate import Mouseomate
import os

os.chdir(".\images")

lsleep = 0.005 #adujust this to change pause time at end of line (recommend .002)
rsleep = 0.025 #adujust this to change pause time at end of row (recommend .025)
imagename = Image_handler.get_image()
handler = Image_handler(imagename)
resizevalue = int(input("What is the approximate pixel size of the input field?"))
offset = int(input("What is the approximate brush size in pixels? (1 for one to one drawing)"))
resizevalue = resizevalue / offset
handler.convert_bandw()
handler.resize(resizevalue)

handler.im.show()
returnkey = None
while returnkey == None:
    print("Preview image loaded. Enter to begin 3 second countdown to start, N to abort. Once image has started, pulling mouse to the upper left corner will abort the program.")
    returnkey = input()
    if returnkey == 'N' or returnkey =='n':
        exit()
    if returnkey == "I" or returnkey =="i":
        handler.invert(imagename)
        handler.convert_bandw()
        resizevalue = resizevalue / offset
        handler.resize(resizevalue)
        handler.im.show()
        returnkey = None

time.sleep(3)
array = handler.update_array()
Mouseomate.image_to_lines(array, offset, rsleep, lsleep)
repeat = 'Y'
while repeat == 'Y':
    repeat = input("Y to redraw after 3 sec pause, or enter to exit")
    if repeat == 'y' or repeat == 'Y':
        time.sleep(3)
        Mouseomate.image_to_lines(array, offset, rsleep, lsleep)
    else:
        exit()

