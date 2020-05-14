Mouseomate V0.7
By Nekose

Contributions by Qaudrum1 and Logistic-bot


To use, run main.py. The image you would like to draw must be inside the 'images' folder. Images should ideally be vector-like, with limited shading or colorpallet (Although the program will attempt to monochrome any image given).

***
Example Of Use:

what is the filename of the image?> mona.jpg

What is the approximate pixel size you would like to output?> 500

What is the approximate brush size in pixels? (Use 1 for one to one drawing)>? 1

Preview image loaded. Enter to begin 3 second countdown to start, N to abort. Once image has started, pulling mouse to the upper left corner will abort the program.

***

Required Modules:
* PyAutoGUI (maps mouse controls)
* numpy (creation of image array)
* Pillow (Image processing and manipulation)

Known issues:
* Output speed appears to be limited by the windows input buffer. You may need to wait till the program finishes running before the image apppears. If you have CPU speed issues, you can try increasing "lsleep" and "rsleep" values at the top of main.py.

To Do:
* investigate better drawing algorithms (Line tracing with cv2.HoughLinesP()?)
