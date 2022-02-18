Mouseomate V0.8, Now with Color!

Original Code by Nekose

Color Implementation and GUI by Quadrum1

formating contributions by Logistic-bot


To use, run main.py. The image you would like to draw must be inside the 'images' folder. 

To switch between color or BW, change the mode variable near the top of main. If using color, specify the program you would like to draw with to specify color controls. (currently only supports MS Paint)

If running in black and white, images should ideally be vector-like, with limited shading or colorpallet (Although the program will attempt to monochrome any image given).

***
Example Of Use:

* After running, a prompt will ask which file to open. Once open a dialog box will appear asking for the following:

What is the approximate pixel size you would like to output?> 500
What is the approximate brush size in pixels? (Use 1 for one to one drawing)>? 1

* Once the parameters have been provided, the following message will be displayed:

Preview image loaded. Enter to begin 3 second countdown to start, N to abort. Once image has started, pulling mouse to the upper left corner will abort the program.

* Hitting enter will start a 3 second countdown, afterwhich the program will take control of the mouse, using the current position as the upper left corner of the image.

***

Known issues:
* Output speed appears to be limited by the windows input buffer. You may need to wait till the program finishes running before the image apppears. If you have CPU speed issues, you can try increasing "lsleep" and "rsleep" values at the top of main.py.

To Do:
* investigate better drawing algorithms (Line tracing with cv2.HoughLinesP()?)
