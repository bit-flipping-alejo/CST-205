# Ivan Alejandre
# Fall CST 205 Module 2 Lab 5
# 11/6/2018
#
# =============================================================================

# Need to import the random library for some functions used in problem 2
import random

# Most common functions on top
def getPic():
  return makePicture(pickAFile())

def saveImage(pic):
  file = r"C:\\Temp\newImage.jpg"
  writePictureTo(pic, file)
  
# Warm up problem
def centerImage():
  # obtain image from user
  source = getPic()
  
  # get dimensions of selected image
  picWidth = getWidth(source)
  picHeight = getHeight(source)
  
  # make the empty destination picture twice the size of the original with a 
  # white background
  newPic = makeEmptyPicture(picWidth*2, picHeight*2, white)
  
  # we place the top left anchor as half the width and height of the source
  targetX = picWidth/2
  targetY = picHeight/2
  
  # for each pixel, grab the pixel data from the source and the destination
  # set destination color the same as source
  for x in range (0, picWidth):
    for y in range (0, picHeight):
      currentPixel = getPixel(source, x, y)
      newPixel = getPixel(newPic, x + targetX, y + targetY)
      pixelColor = getColor(currentPixel)
      setColor(newPixel, pixelColor)
  
  return newPic

# Problem 1
def pyCopy(source, target, targetX, targetY):
  # get the dimensions of both images
  sourceWidth = getWidth(source)
  sourceHeight = getHeight(source)
  targetWidth = getWidth(target)
  targetHeight = getHeight(target)
 
  # need to consider if the user inputs the copy destination outside the bounds of the 
  # target dimensions. will position the image so the right and bottom edges of the source
  # image will align with the right and bottom edges of the target image
  if (targetX + sourceWidth) > targetWidth:
    targetX = targetWidth - sourceWidth -1
  if (targetY + sourceHeight) > targetHeight:
    targetY = targetHeight - sourceHeight -1
    
  # copy the image to the target destination
  for x in range (sourceWidth):
    # places the copied image where the user wants it to start
    newX = (targetX + x)
    
    for y in range (sourceHeight):
      # grabs source pixel data and copies it to target pixel
      sourcePixel = getPixel(source, x, y)
      newY = (targetY + y)
      targetPixel = getPixel(target, newX, newY)
      sourceColor = getColor(sourcePixel)
      setColor(targetPixel, sourceColor)
  
  # returns the final image (target)
  return target
  
# Problem 2: This is a compilation of functions from this week and last. I've 
# taken what I consider the crazier functions and included them here. In addition,
# I've modified each function to accept a parameter and return the picture.

def mirrorLeft(pic):
  picHeight = getHeight(pic)
  picWidth = getWidth(pic)
  
  for x in range (0, picWidth/2):
    for y in range (0, picHeight):
      pixelCurrent = getPixel(pic, x, y)
      newPix = getPixel(pic, (picWidth - x - 1), y)
      pixelColor = getColor(pixelCurrent)
      setColor(newPix, pixelColor)
  
  return pic

def mirrorRight(pic):
  picHeight = getHeight(pic)
  picWidth = getWidth(pic)
  
  for x in range (picWidth/2, picWidth):
    for y in range (0, picHeight):
      currentPixel = getPixel(pic, x, y)
      newPixel = getPixel(pic, (picWidth - x), y)
      pixelColor = getColor(currentPixel)
      setColor(newPixel, pixelColor)
  
  return pic
  
def mirrorTop(pic):
  picHeight = getHeight(pic)
  picWidth = getWidth(pic)
  
  for x in range(0, picWidth):
    for y in range(0, picHeight/2):
      currentPixel = getPixel(pic, x, y)
      newPixel = getPixel(pic, x, picHeight - y - 1)
      pixelColor = getColor(currentPixel)
      setColor(newPixel, pixelColor)
      
  return pic
  
def mirrorBottom(pic):
  picHeight = getHeight(pic)
  picWidth = getWidth(pic)
  
  for x in range(0, picWidth):
    for y in range(picHeight/2, picHeight):
      currentPixel = getPixel(pic, x, y)
      newPixel = getPixel(pic, x, picHeight - y)
      pixelColor = getColor(currentPixel)
      setColor(newPixel, pixelColor)
      
  return pic
  
# A note regarding this function: I added a random number generator so each time
# this is called, a different image is produced. Each pass it'll generate a number 
# then call that particular function.
def doubleMirror(pic):
  picHeight = getHeight(pic)
  picWidth = getWidth(pic)
  
  
  for x in range(0, 2):
    randomFlip = random.randint(1,5)
    
    if x == 1:
      if randomFlip == 1:
        secondMirror = mirrorTop(firstMirror)
      elif randomFlip == 2:
        secondMirror = mirrorBottom(firstMirror)
      elif randomFlip == 3:
        secondMirror = mirrorLeft(firstMirror)
      else:
        secondMirror = mirrorRight(firstMirror)
    else:
      if randomFlip == 1:
        firstMirror = mirrorTop(pic) 
      elif randomFlip == 2:
        firstMirror = mirrorBottom(pic)
      elif randomFlip == 3:
        firstMirror = mirrorLeft(pic)
      else:
        firstMirror = mirrorRight(pic)
      
  return secondMirror
  
def lessRed(pic):
  percLessRed = float(random.randint(0,101))
  
  if percLessRed == 0:
    return pic
    
  sourceWidth = getWidth(pic)
  sourceHeight = getHeight(pic)
  
  for x in range(0, sourceWidth):
    for y in range(0, sourceHeight):
      pix = getPixel(pic, x, y)
      pixRedCt = getRed(pix)
      setRed(pix, pixRedCt * (1.0 - percLessRed))
  
  return pic

def moreRed(pic):
  sourceWidth = getWidth(pic)
  sourceHeight = getHeight(pic)
  newPercTot = 1 + (random.randint(0,101) / 100.0)
  for x in range(0, sourceWidth):
    for y in range(0, sourceHeight):
      pix = getPixel(pic, x, y)
      pixRed = getRed(pix)
      newRedVal = floor(pixRed * newPercTot)
      if (newRedVal > 255):
        setRed(pix, 255)
      else:
        setRed(pix, newRedVal)
        
  return pic

def roseColoredGlasses(pic):
  sourceWidth = getWidth(pic)
  sourceHeight = getHeight(pic)
  
  for x in range(0, sourceWidth):
    for y in range(0, sourceHeight):
      pix = getPixel(pic, x, y)
      newRed = getRed(pix) * 1.1
      newBlue = getBlue(pix) * 0.8
      newGreen = getGreen(pix) * 0.5
    
      if newRed > 255:
        setRed(pix, 255)
      else:
        setRed(pix, newRed)
      
      setBlue(pix, newBlue)
      setGreen(pix, newGreen)
  
  return pic

def betterBnW(pic):  
  sourceWidth = getWidth(pic)
  sourceHeight = getHeight(pic)
 
  for x in range(0, sourceWidth):
    for y in range(0, sourceHeight):
      pix = getPixel(pic, x, y)
      
      redColor = getRed(pix) * 0.299
      blueColor = getBlue(pix) * 0.587
      greenColor = getGreen(pix) * 0.114
      
      luminance = (redColor + blueColor + greenColor)
      
      setRed(pix, luminance)
      setBlue(pix, luminance)
      setGreen(pix, luminance)
    
  return pic
  
# This function is here to make the collage creation process random.
# Instead of hardcoding each pass, it will execute a random function
# and pass back the altered image
def transmog(source):
  selection = random.randint(0, 12)
  print("augment: %d") % selection
  if selection == 1:
    return mirrorLeft(source)
  elif selection == 2:
    return mirrorRight(source)
  elif selection == 3:
    return mirrorTop(source)
  elif selection == 4:
    return mirrorBottom(source)
  elif selection == 5:
    return doubleMirror(source)
  elif selection == 6:
    return lessRed(source)
  elif selection == 7:
    return moreRed(source)
  elif selection == 8:
    return roseColoredGlasses(source)
  elif selection == 9:
    return betterBnW(source)
  else:
    return source

# This is it. This function will continue to prompt the user for images for the
# collage. After each image is inputted, the script will alter the image randomly,
# then copy it to the target picture. There are some logic statements to maximize
# coverage, but it will hardly ever fill all the way to the bottom.
def makeCollage():
  # initiate some variables needed
  targetX = 0
  targetY = 0
  smallerHeight = 3300
  x = 0
  
  # make the empty picture destination
  target = makeEmptyPicture(2550, 3300, black)
  
  while True:
    # shows the user how many loops they've gone through and the current anchor location
    print("iteration: %d" % x)
    print("targetX: %d" % targetX)
    print("targetY: %d" % targetY)
    
    # prompt the user for the image. Then returns to the console which augmentation it chose
    # 
    source = transmog(getPic())
    
    # get the width and height of the current image
    sourceWidth = getWidth(source)
    sourceHeight = getHeight(source)
    
    # set next row height
    if (sourceHeight < smallerHeight):
      smallerHeight = sourceHeight
    
    # if the image is too wide, move the anchor to the left to accomadate,
    # copy the image, then reset to the next row
    if (targetX + sourceWidth) > 2550:
      targetX = 2550 - sourceWidth
      target = pyCopy(source, target, targetX, targetY)
      targetX = 0
      targetY = targetY + smallerHeight
    # otherwise just copy it and move the anchor
    else:
      target = pyCopy(source, target, targetX, targetY)
      targetX = targetX + sourceWidth
    
    # if the next image is and the bottom of the page, end the loop
    if (targetY + sourceHeight) > 3300:
      break   
    
    # up the current iteration
    x += 1
    
  saveImage(target)