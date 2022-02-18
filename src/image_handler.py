from PIL import Image, ImageFilter, ImageOps
import numpy as np
from easygui import fileopenbox

class Image_handler(object):
	def __init__(self,image):
		self.im = Image.open(image)

	@staticmethod
	def get_image() -> str:
		"""
		Ask's users the name of the file to be used
		:return:
		a string of the file name
		"""
		path = fileopenbox()
		return path

	def convert_bandw(self,mode) -> None:
		"""
		converts image to a black and white bit per pixel image
		:return:
		"""
		if mode == "color":
			self.im = self.im.convert(mode='RGB',dither=None)
		elif mode == "black":
			self.im = self.im.convert(mode='1',dither=None)

	def invert(self,image) -> None:
		"""
		Returns a color inverted image file
		:return:
		"""
		self.im = ImageOps.invert(Image.open(image))

	def resize(self,value:int) -> None:
		"""
		resizes image to fit withing an X by X square
		:param value:
		Size of the square input field
		:return:
		"""
		horizontalsize, verticalsize = self.im.size
		if horizontalsize > verticalsize:
			conversion = horizontalsize / value
			self.im = self.im.resize((int(horizontalsize / conversion), int(verticalsize / conversion)))
		else:
			conversion = verticalsize / value
			self.im = self.im.resize((int(horizontalsize / conversion), int(verticalsize / conversion)))

	def update_array(self) -> np.array:
		"""
		Converts image into a numpy array of bools
		:return:
		"""
		array = np.array(self.im)
		return array




