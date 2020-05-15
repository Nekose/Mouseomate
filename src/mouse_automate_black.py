import numpy
import pyautogui
import time	  
class Mouseomate(object):
	pyautogui.PAUSE = 0.00 #useful
	pyautogui.FAILSAFE = True

	@staticmethod
	def image_to_lines(image_array: numpy.array, offset:int, rsleep:int, lsleep:int) -> None:
		"""
		Converts an image array to mouseclicks.
		:param image_array:
		A numpy array of bools, where False represents a click, and True represents no click.
		:param offset:
		An int which provides spacing between each pixel in image_array. Usefull to adjust for brush size used in whatever this will be outputting for.
		:param rlseep:
		int which designates how long in second the mouse will take drawing a line
		:param rsleep:
		int which designates how long in seconds to pause at end of row
		:return:
		"""
		startpositionx,startpositiony = pyautogui.position()
		for row in image_array:
			xoffset = 0
			alreadydrawing = False
			for value in row:
				if not value.all(): #Need to draw
					if alreadydrawing == True:
						xoffset += offset
					else:
						startline = startpositionx + xoffset
						alreadydrawing = True
						xoffset += offset
				if value.all(): #End of line aka. white begins
					if alreadydrawing == False:
						xoffset += offset
					else:
						pyautogui.moveTo(startline,startpositiony)
						pyautogui.dragTo(startpositionx + xoffset, startpositiony,duration=lsleep, button = 'left')
						time.sleep(lsleep)
						alreadydrawing = False
						xoffset += offset
			if not value.all():
				if alreadydrawing == True:
					pyautogui.moveTo(startline, startpositiony)
					pyautogui.dragTo(startpositionx + xoffset, startpositiony, duration=lsleep, button ='left')
					time.sleep(lsleep)
					xoffset += offset
			startpositiony += offset
			time.sleep(rsleep)
			