import time
from src.image_handler import Image_handler
from src.mouse_automate import Mouseomate

offset = 1 #adjust this value if brush size is to large, minimum value of 1
imagename = Image_handler.get_image()
handler = Image_handler(imagename)
resizevalue = int(input("What is the approximate pixel size of the input field?"))
resizevalue = resizevalue / offset
handler.convert_bandw()
handler.resize(resizevalue)

handler.im.show()
returnkey = None
while returnkey == None:
    print("Preview image loaded. Enter to begin 3 second countdown to start, I to invert colors, N to abort. Once image has started, pulling mouse to the upper left corner will abort the program.")
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
Mouseomate.image_to_clicks(array,offset)

