import pyautogui
class Mouseomate(object):
    pyautogui.PAUSE = 0.00
    pyautogui.FAILSAFE = True

    @staticmethod
    def image_to_clicks(image_array,offset):
        startpositionx,startpositiony = pyautogui.position()
        for row in image_array:
            xoffset = 0
            for value in row:
                if value == False:
                    pyautogui.click(interval=.03)
                    startpositionx += offset
                    pyautogui.moveTo(startpositionx, startpositiony, duration=0)
                    xoffset += offset
                elif value == True:
                    startpositionx += offset
                    pyautogui.moveTo(startpositionx, startpositiony, duration=0)
                    xoffset += offset
            startpositiony += offset
            startpositionx -= xoffset
            pyautogui.moveRel(startpositionx, startpositiony, duration=0)



