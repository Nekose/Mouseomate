import numpy
import pyautogui
import time

def closest_color(color, palette):

	r1, g1, b1 = color
	if r1 == 255 and g1 == 105 and b1 == 180:#Failsafe for last color drawn
		cc = r1, g1, b1
		return cc # (255, 105, 180)
	closest_dis = 10000
	cc = 0, 0, 0
	for r2, g2, b2 in palette:
		dis = ((r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2) ** 0.5
		if dis < closest_dis:
			closest_dis = dis
			cc = r2, g2, b2
	return cc
	

def change_color(color,app):
	if color == (255, 105, 180): #Failsafe, needs to be reworked, this should only be temporary
		i = 0
	else:
		i = palette[app][0].index(color)
		
	if app == "paint": 
		"""
		This system to change colors is suboptimal, as different screens have the buttons at different locations! 
		Using json data storage to store these would be better as different subroutines could access them, for example a color mapper.
		"""
		if i <= 9:
			x = i*22 + 878	  # Top row
			y = 58
		else:
			x = (i-10)*22 + 878	  # Bottom row
			y = 82
	else:
		raise ValueError("No color data found for application {}!".format(app))
	pyautogui.mouseUp()
	pyautogui.click(x=x, y=y)

# All color buttons for paint from left to right, top to bottom.
paints = ((0, 0, 0),(127,127,127),(136,0,21),(237,28,36),(255,127,39),(255,242,0),(34,177,76),(0,162,232),(63,72,204),(163,73,164),
		  (255, 255, 255),(195,195,195),(185,122,87),(255,174,201),(255,201,14),(239,228,176),(181,230,29),(153,217,234),(112,146,190),(200,191,231))	
		
palette = {"paint": [paints,paints[10]]}	# Key is the application name which is specified in main.py
		  
class Mouseomate(object):
	pyautogui.PAUSE = 0.00 #useful
	pyautogui.FAILSAFE = True

	@staticmethod
	def image_to_lines(image_array: numpy.array, offset:int, rsleep:int, lsleep:int, app:str) -> None:
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
			white = palette[app][1]
			alreadydrawing = [white,0,0] # Color, starting xoffset, offsets in that line
			row[-1] = [255,105,180] #Failsafe for last color drawn
			# Without it, the last color in a row would not be drawn as the script would skip it, needs fixing!
			for value in row:	
				closest = closest_color(value,palette[app][0])
				if closest == white:
					alreadydrawing[0] = closest
					xoffset += offset
					continue
					
				if alreadydrawing[0] == closest: # Is the current color the same color as the last one checked?
					alreadydrawing[2] += offset 
					xoffset += offset
					continue
			
				alreadydrawing[0] = closest # Define new color

				# Draw line with old color 
				pyautogui.mouseUp()
				pyautogui.moveTo(startpositionx + alreadydrawing[1], startpositiony) #Draw the full line of the last color
				pyautogui.mouseDown()
				pyautogui.dragTo(startpositionx + alreadydrawing[1] + alreadydrawing[2], startpositiony, duration=lsleep, button = 'left')
				pyautogui.mouseUp()
				
				# Define new values for next line
				alreadydrawing[1] = xoffset
				alreadydrawing[2] = 0
				
				# Change the color to the new color
				change_color(closest,app)
					
				time.sleep(lsleep)
				xoffset += offset

			pyautogui.mouseUp()
			change_color(white,app)
			startpositiony += offset
			pyautogui.mouseUp()
			pyautogui.moveTo(startpositionx, startpositiony)
			time.sleep(rsleep)
			# Might have overdone is with mouseUp(), but paint had some problems with recognizing the mouse and handeled it as if it were still drawing, creating some... interesting replications




