from . import image_handler
import numpy as np
import pyautogui
class Mouseomate(object):
    pyautogui.PAUSE = 0
    pyautogui.FAILSAFE = True

    @staticmethod
    def image_to_clicks(image_array):
        for row in image_array:
            xoffset = 0
            for value in row:
                if value == True:
                    pyautogui.click()
                    pyautogui.dragRel(2, 0, duration=0)
                    xoffset += 2
                else:
                    pyautogui.dragRel(2, 0, duration=0)
                    xoffset += 2
            pyautogui.dragRel(-xoffset, 2, duration=0)

