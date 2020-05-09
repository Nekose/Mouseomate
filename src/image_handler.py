from PIL import Image, ImageFilter
import numpy as np


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
        path = input("what is the filename of the image?")
        return path

    def convert_bandw(self) -> None:
        """
        converts image to a black and white bit per pixel image
        :return:
        """
        self.im = self.im.convert(mode='1',dither=None)

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




