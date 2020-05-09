from src.image_handler import Image_handler
from src.mouse_automate import Mouseomate

handler = Image_handler('dickbutt.jpg')
handler.convert_bandw()
handler.resize(150)
array = handler.update_array()
Mouseomate.image_to_clicks(array,2)
