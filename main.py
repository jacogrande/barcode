# main application logic
# reading 1 frame per second based on code by Sparkiepandas
# https://stackoverflow.com/questions/51474421/extracting-frames-every-second-of-all-videos-in-folder
import cv2
import dominant_color as d
import numpy as np

scale_percent = 5 # percent of original size
count = 0
success = True
output_image = None
grayscale_image = None
frame_height=0
frame_width=0
grayscale=False
k=0
vidcap=None

def readFrame(vidcap):
  # get the current frame
  global success
  success, image = vidcap.read()
  if(success == False):
    return False
  # if this is the first frame of the second (assuming 24fps)
  if count % 24 == 0:
    print('read frame %d'%count)
    # convert the image to the hsv color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # get scaled down dimensions
    width = int(hsv_image.shape[1]*scale_percent/100)
    height = int(hsv_image.shape[0]*scale_percent/100)
    # find the dominant color
    dom_color = d.get_dominant_color(hsv_image, k, (width, height))

    # create a square showing dominant color of equal size to input image
    dom_color_hsv = np.full((frame_height, frame_width, 3), dom_color, dtype='uint8')
    #  convert to bgr color space for display
    dom_color_bgr = cv2.cvtColor(dom_color_hsv, cv2.COLOR_HSV2BGR)
    global output_image
    if output_image is None:
      # create a new image if there isn't one already
      output_image = dom_color_bgr
    else :
      # append the new frame to the end of the barcode
      output_image = np.hstack((output_image, dom_color_bgr))
    
    # repeat the process if grayscale is set to true
    if grayscale:
      grayscale_hsv = np.full((frame_height, frame_width, 3), (0,0,dom_color[2]), dtype='uint8')
      grayscale_bgr = cv2.cvtColor(grayscale_hsv, cv2.COLOR_HSV2BGR)
      global grayscale_image
      if grayscale_image is None:
        grayscale_image = grayscale_bgr
      else:
        grayscale_image = np.hstack((grayscale_image, grayscale_bgr))


def generate(input, kmeans, w, h, g):
  # configuration
  global vidcap
  vidcap = cv2.VideoCapture(input)
  global frame_width
  frame_width=w
  global frame_height
  frame_height=h
  global grayscale
  grayscale=g
  global k
  k=kmeans


  global count
  # loop through each frame of the inputted file
  while success:
    readFrame(vidcap)
    count += 1

  cv2.imwrite('./barcode.jpg', output_image)
  if grayscale:
    cv2.imwrite('./barcode_grayscale.jpg', grayscale_image)

