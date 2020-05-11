Mouseomate V0.65
By Nekose


To use, run main.py with the image you would like to draw inside the 'images' folder. Images should ideally be vector-like, with limited shading or colorpallet (Although the program will attempt to monochrome any image given).

Required Modules:
* PyAutoGUI (maps mouse controls)
* numpy (creation of image array)
* Pillow (Image processing and manipulation)

Known issues:
* Output speed appears to be limited by the windows input buffer. You may need to wait till the program finishes running before the image apppears.

To Do:
* investigate better drawing algorithms (Line tracing with cv2.HoughLinesP()?)
