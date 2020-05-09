from PIL import Image, ImageFilter
import numpy as np


class Image_handler(object):
    def __init__(self,image):
        self.im = Image.open(image)

    @staticmethod
    def get_image() -> str:
        path = input("what is the filename of the image?")
        return path

    def convert_bandw(self) -> None:
        self.im = self.im.convert(mode='1',dither=None)

    def blur_image(self):
        self.im = self.im.filter(filter=ImageFilter.BoxBlur(1))


    def resize(self,value:int) -> None:
        horizontalsize, verticalsize = self.im.size
        if horizontalsize > verticalsize:
            conversion = horizontalsize / value
            self.im = self.im.resize((int(horizontalsize / conversion), int(verticalsize / conversion)))
        else:
            conversion = verticalsize / value
            self.im = self.im.resize((int(horizontalsize / conversion), int(verticalsize / conversion)))

    def update_array(self) -> np.array:
        array = np.array(self.im)
        return array




