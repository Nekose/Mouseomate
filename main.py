import time
import sys
import os

cwd = os.getcwd()
sys.path.append(cwd+'/src')

from image_handler import Image_handler
from mouse_automate import Mouseomate


os.chdir("images")


lsleep = 0.005 #adujust this to change pause time at end of line (recommend .002)
rsleep = 0.025 #adujust this to change pause time at end of row (recommend .025)
imagename = Image_handler.get_image()
handler = Image_handler(imagename)
resizevalue = int(input("What is the approximate pixel size you would like to output?"))
offset = int(input("What is the approximate brush size in pixels? (1 for one to one drawing)"))
resizevalue = resizevalue / offset
handler.convert_bandw()
handler.resize(resizevalue)

handler.im.show()
returnkey = None
while returnkey == None:
    print("Preview image loaded. Enter to begin 3 second countdown to start, N to abort. Once image has started, pulling mouse to the upper left corner will abort the program.")
    returnkey = input()
    returnkey = returnkey.lower()
    if returnkey == 'n':
        exit()
    if returnkey == 'i':
        handler.invert(imagename)
        handler.convert_bandw()
        resizevalue = resizevalue / offset
        handler.resize(resizevalue)
        handler.im.show()
        returnkey = None

time.sleep(3)
array = handler.update_array()
Mouseomate.image_to_lines(array, offset, rsleep, lsleep)
repeat = 'y'
while repeat == 'y':
    repeat = input("Y to redraw after 3 sec pause, or enter to exit")
    repeat = repeat.lower()
    if repeat == 'y':
        time.sleep(3)
        Mouseomate.image_to_lines(array, offset, rsleep, lsleep)
    else:
        exit()

