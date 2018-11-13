# Ivan Alejandre
# Line Art Function

import os

def getPic():
  return makePicture(pickAFile())
  
def lineArt(pic):
  threshold = 20
  for x in range(0, getWidth(pic)):
    # if we're at the rightmost column, don't check right pixel
    if x == (getWidth(pic) - 1):
      # if we're at the bottom right pixel, just change to white. No pixels to compare.
      if (y + 1) == getHeight(pic):
        setColor(pixel, white)
      
      # grab bottom pixel and its luminance
      else:
        pixelBottom = getPixel(pic, x, (y + 1))
        luminanceBottom = (getRed(pixelBottom) + getBlue(pixelBottom) + getGreen(pixelBottom)) / 3
        #luminanceBottom = (getRed(pixelBottom) * 0.299) + (getBlue(pixelBottom) * 0.587) + (getGreen(pixelBottom) * 0.114)
      
        # check the luminance difference and change its color
        if abs(luminance - luminanceBottom) > threshold:
          setColor(pixel, black)
        else:
          setColor(pixel, white)
        
    # for all other columns, check the right pixel AND bottom pixel UNLESS we're at the bottom pixel, then only check
    # the right pixel
    else:
      for y in range(0, getHeight(pic)):
        # grab current pixel and its luminance
        pixel = getPixel(pic, x, y)
        luminance = (getRed(pixel) * 0.299) + (getBlue(pixel) * 0.587) + (getGreen(pixel) * 0.114)
      
        # if we reach the bottom of the column, just compare the right pixel and modify
        if y + 1 == getHeight(pic):
          # grab right pixel and its luminance
          pixelRight = getPixel(pic, x + 1, y)
          luminanceRight = (getRed(pixelBottom) + getBlue(pixelBottom) + getGreen(pixelBottom)) / 3
          #luminanceRight = (getRed(pixelRight) * 0.299) + (getBlue(pixelRight) * 0.587) + (getGreen(pixelRight) * 0.114)
          
          # change the working pixel's color
          if abs(luminance - luminanceRight) > threshold:
            setColor(pixel, black)
          else:
            setColor(pixel, white)
          
        else:
          # grab right and bottom pixel and their luminances
          pixelBottom = getPixel(pic, x, y + 1)
          pixelRight = getPixel(pic, x + 1, y)
          luminanceBottom = (getRed(pixelBottom) + getBlue(pixelBottom) + getGreen(pixelBottom)) / 3
          luminanceRight = (getRed(pixelBottom) + getBlue(pixelBottom) + getGreen(pixelBottom)) / 3
          #luminanceBottom = (getRed(pixelBottom) * 0.299) + (getBlue(pixelBottom) * 0.587) + (getGreen(pixelBottom) * 0.114)
         # luminanceRight = (getRed(pixelRight) * 0.299) + (getBlue(pixelRight) * 0.587) + (getGreen(pixelRight) * 0.114)
          
          # change to black if BOTH right and lower pixel are over threshold
          if abs(luminance - luminanceRight) > threshold and abs(luminance - luminanceBottom) > threshold:
            setColor(pixel, black)
          else:
            setColor(pixel, white)
  
  return pic

def makeLineArt():
  pic = getPic()
  
  file = r"C://temp/lineArt.jpg"
  
  writePictureTo(lineArt(pic), file)