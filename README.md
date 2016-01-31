# OpenCVLabJam
Necessary source files and resources for the Iowa State Spring 2016 OpenCV Lab Jam

## Setup
### Installing OpenCV
Follow [this link](http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_setup/py_setup_in_windows/py_setup_in_windows.html#install-opencv-python-in-windows) to install the OpenCV Libraries in Windows.

Follow [this link](http://docs.opencv.org/2.4/doc/tutorials/introduction/linux_install/linux_install.html) to install the OpenCV libraries in Linux.

Follow [this link](http://www.pyimagesearch.com/2015/06/15/install-opencv-3-0-and-python-2-7-on-osx/) to install the OpenCV libraries in OS X.

If you are using the yum package manager (Fedora or other relative distros), the following command should successfully install OpenCV:

`sudo yum install numpy opencv*`

This may not give you access to the latest OpenCV version like building from source, so there may be compatibility issues involved.  It's worth a shot to try.

### Install a Python Editor
You can use whatever editor you want for this.  I would recommend [PyCharm](https://www.jetbrains.com/pycharm/).  Visual Studio and XCode are also great options.

## Color Filtering
Try running color-filtering/color.py and see what happens.  Follow [this link](https://en.wikipedia.org/wiki/HSL_and_HSV) to learn more about HSV image parameters.

**Make sure you hit escape to exit the program.  Don't hit X in the corner of the window.  Some GUI features are messed up (at least on linux)**

What we are doing is a very simple image processing technique known as thresholding.  Some parts of the image are within the desired parameters, and are thresholded to a 1 (White pixel) while those outside our desired parameters are thrown out and set to 0 (black pixels.)  This is very helpful for finding parts of an image that are a certain color.  You are seeing a bitmasked output by default, so the original image is overlaid with the "white" or high thresholded pixels.

**First Step:** Have your program hardcoded to select only one cartridge on startup.

**Free cookie:** Using [OpenCV contours](http://docs.opencv.org/master/dd/d49/tutorial_py_contour_features.html#gsc.tab=0), draw a rectangle around whichever pokemon cartridge your settings are selecting.

## Face Detection
Now change to the face-detect directory and try out face detection using:

`python face.py <image name> haarcascade_frontalface_default.xml`

[Here's some good info on haar cascade classifiers](http://docs.opencv.org/master/d7/d8b/tutorial_py_face_detection.html#gsc.tab=0).  Face detection is a very advanced subject and using machine learning to recognize faces has been proven to be an effective solution.  We are utilizing training done by professionals to help us.

**Thankless Task:** Use haarcascade_eye.xml as a second classifier to detect eyes in the images given.  Draw rectangles around the eyes.

