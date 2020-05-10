import numpy
import pyautogui
import time
class Mouseomate(object):
    pyautogui.PAUSE = 0.00 #useful
    pyautogui.FAILSAFE = True

    @staticmethod
    def image_to_clicks(image_array: numpy.array,offset:int) -> None:
        """
        Converts an image array to mouseclicks.
        :param image_array:
        A numpy array of bools, where False represents a click, and True represents no click.
        :param offset:
        An int which provides spacing between each pixel in image_array. Usefull to adjust for brush size used in whatever this will be outputting for.
        :return:
        """
        startpositionx,startpositiony = pyautogui.position()
        for row in image_array:
            xoffset = 0
            alreadydrawing = False
            for value in row:
                if value == False: #Need to draw
                    if alreadydrawing == True:
                        xoffset += offset
                    else:
                        startline = startpositionx + xoffset
                        alreadydrawing = True
                        xoffset += offset
                if value == True: #End of line
                    if alreadydrawing == False:
                        xoffset += offset
                    else:
                        pyautogui.moveTo(startline,startpositiony)
                        pyautogui.dragTo(startpositionx + xoffset, startpositiony, button = 'left')
                        alreadydrawing = False
                        xoffset += offset
            time.sleep(.025)
            startpositiony += offset




