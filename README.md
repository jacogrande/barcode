# barcode

![color barcode example](https://github.com/jacogrande/barcode/blob/master/fantastic_planet.jpg)
*The color barcode of René Laloux's classic animated science fiction film "Fantastic Planet"*

Barcode is a tool that generates color barcodes for inputted video files. 1 frame will be read per second of the video, and that frame's dominant color will be added to the barcode image until the video is over.

## Installation

Clone **barcode** into your development environment:

```
git clone git@github.com:jacogrande/barcode
```

Navigate to the project directory:

```
cd barcode
```

### Dependencies

Make sure you have [python 3 installed on your machine](https://www.python.org/downloads/) (this will also install pip3 on your machine, which you'll need next)

Now, download the required python libraries ([opencv-python](https://pypi.org/project/opencv-python/), [numpy](https://numpy.org/), [sklearn](https://scikit-learn.org/stable/)):

```
pip3 install opencv-python numpy sklearn
```

*Common Errors:* pip may require you to install the opencv-python package with the --user flair

## Generating Barcodes

To run Barcode:

```
python3 barcode.py -i <inputfile> [-k <kmeans>] [-f <frameInterval>] [-w <frameWidth>] [-h <frameHeight] [-g] [-m]
```

### Arguments

* **-i <inputfile**: The path to the video file you'd like to create a barcode of.
* **-k <kmeans>** *(optional)*: The number of k-mean clusters to create per frame *(defaults to 10)*.
* **-f <frameInterval>** *(optional)*: The time (in seconds) between frames *(defaults to 1 second)*.
* **-w <frameWidth>** *(optional)*: The width of each inidividual barcode strip in pixels *(defaults to 1)*.
* **-h <frameHeight>** *(optional)*: The height of each inidividual barcode strip in pixels *(defaults to 2000)*.
* **-g** *(optional)*: Grayscale parameter. If included, a grayscale version of the barcode will also be created.
* **-m** *(optional)*: See the manual

## Recommendations

* Dimension settings:
  * For videos 1 - 2 hours long, don't alter the dimensions.
  * For videos 2+ hours long, set the frame height to 3000.
  * For videos shorter than an hour, set the frame width anywhere between 2 and 100.
* Raising the number of k-mean clusters yields increasingly similar results while dramatically decreasing performance.
* Don't worry if you see a ConvergenceWarning, this just means that there aren't as many colors in a frame as there are k-mean clusters.
* **WARNING**: Barcodes may take over an hour to complete.

Feel free to send me what you make at prowelljackson@gmail.com
