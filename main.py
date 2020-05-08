from src.image_handler import Image_handler
from src.mouse_automate import Mouseomate
from PIL import Image
import numpy as np

#im = Image.open()
handler = Image_handler('emoji.png')
handler.convert_bandw()
handler.resize(300)
handler.im.show()
array = handler.update_array()
Mouseomate.image_to_clicks(array)
