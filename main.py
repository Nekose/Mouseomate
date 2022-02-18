import time
import sys
import os
from easygui import multenterbox

cwd = os.getcwd()
sys.path.append(cwd+'/src')

from image_handler import Image_handler
from mouse_automate_black import Mouseomate as Mouseomate_black
from mouse_automate_color import Mouseomate as Mouseomate_color

mode = "black" # "color", "black"
app = "paint" # What application are you drawing with?

os.chdir("images")


lsleep = 0.002 #adujust this to change pause time at end of line (recommend .002)
rsleep = 0.025 #adujust this to change pause time at end of row (recommend .025)
imagename = Image_handler.get_image()
handler = Image_handler(imagename)
message = "Resizevalue: What is the approximate pixel size you would like to output?\nOffset: What is the approximate brush size in pixels? (1 for one to one drawing)"
resizevalue, offset = multenterbox(message,"Mouseomate", ["Resizevalue","Offset"])
resizevalue = int(resizevalue) if resizevalue else 100
offset = int(offset) if offset else 1
resizevalue = resizevalue / offset
handler.convert_bandw(mode)
handler.resize(resizevalue)
	
handler.im.show()
returnkey = None
while returnkey == None:
	print("Preview image loaded. Enter to begin 3 second countdown to start, N to abort. Once image has started, pulling mouse to any corner will abort the program.")
	returnkey = input()
	returnkey = returnkey.lower()
	if returnkey == 'n':
		exit()
	if returnkey == 'i':
		handler.invert(imagename)
		handler.convert_bandw(mode)
		resizevalue = resizevalue / offset
		handler.resize(resizevalue)
		handler.im.show()
		returnkey = None

time.sleep(3)
array = handler.update_array()
if mode == "color":
	Mouseomate_color.image_to_lines(array, offset, rsleep, lsleep, app)
elif mode == "black":
	Mouseomate_black.image_to_lines(array, offset, rsleep, lsleep)
		
repeat = 'y'
while repeat == 'y':
	repeat = input("Y to redraw after 3 sec pause, or enter to exit")
	repeat = repeat.lower()
	if repeat == 'y':
		time.sleep(3)
		if mode == "color":
			Mouseomate_color.image_to_lines(array, offset, rsleep, lsleep, app)
		elif mode == "black":
			Mouseomate_black.image_to_lines(array, offset, rsleep, lsleep)
	else:
		exit()

