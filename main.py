import time
from src.image_handler import Image_handler
from src.mouse_automate import Mouseomate

offset = 2 #adjust this value if brush size is to large, minimum value of 1
handler = Image_handler(Image_handler.get_image())
resizevalue = int(input("What is the approximate pixel size of the input field?"))
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
time.sleep(3)
array = handler.update_array()
Mouseomate.image_to_clicks(array,offset)

