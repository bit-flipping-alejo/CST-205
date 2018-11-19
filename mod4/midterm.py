# Ivan Alejandre
# Midterm Exami
# 11/17/18


# Main function to launch the filter functions:

def makeFilter():
  print("Please input your picture that you wish to add a filter to.")
  inputPicture = getPic()
  
  choice = input("Enter 1 for the CSUMB filter or 2 for the mirror dimension filter: ")
  
  if choice == 1:
    filteredPic = CSUMBify(inputPicture)
    show(filteredPic)
    writePictureTo(filteredPic, r"C://temp/CSUMBify.jpg")
  elif choice == 2:
    filteredPic = mirrorDimension(inputPicture)
    show(filteredPic)
    writePictureTo(filteredPic, r"C://temp/mirrorDimension.jpg")
  else:
    print("Invalid selection, ending program.")

# Function to grab picture from user selection

def getPic():
  return makePicture(pickAFile())

#/////////////////////
# School filter: /////
#/////////////////////

def CSUMBify(picture):
  # make the school colors to be passed into helper function
  schoolBlue = makeColor(0,42,78)
  schoolGreen = makeColor(18,90,55)
  
  # Define the width and height of the image
  picWidth = getWidth(picture)
  picHeight = getHeight(picture)
  
  # We want to make vertical stripped color hues on the image
  # 6 strips seems like a good amount :)
  # We also need to keep track of where we are on the x axis when
  # the loop executes. 
  
  workingWidth = picWidth/6
  
  # For each iteration, we pass the current picture to the hue function,
  # the width of the section, the starting point of the section, and the color
  # Each hue function passes back the picture and it is reassigned each iteration.
  for i in range(0,6):
    if i%2 == 0:
      picture = hueBlue(picture, workingWidth, (workingWidth * i))
    else:
      picture = hueGreen(picture, workingWidth, (workingWidth * i))
      
  # After we hued the picture, we're going to overlay the school logo in the top right corner
  logo = makePicture("C://temp//logo.jpg")
  
  picWithLogo = chromaCopy(logo, picture, picWidth, 0)
  
  # Overlay the school pride message on the bottom.
  prideMessage = makePicture("C://temp//pride.jpg")
  
  x = (picWidth - getWidth(prideMessage))/2
  finalPic = chromaCopy(prideMessage, picWithLogo, x, picHeight)
  
  # Return image to main function
  
  return finalPic
  
# School filter helper functions

def hueBlue(picture, sectionWidth, startLocation):
  picHeight = getHeight(picture)
  for x in range(startLocation, (startLocation + sectionWidth)):
    for y in range(0, picHeight):
      currentPixel = getPixel(picture, x, y)
      newRed = getRed(currentPixel) * 0.1
      newBlue = getBlue(currentPixel) * 0.8
      newGreen = getGreen(currentPixel) * 0.65
      newColor = makeColor(newRed, newGreen, newBlue)
      setColor(currentPixel, newColor)
  return picture
  
def hueGreen(picture, sectionWidth, startLocation):
  picHeight = getHeight(picture)
  for x in range(startLocation, (startLocation + sectionWidth)):
    for y in range(0, picHeight):
      currentPixel = getPixel(picture, x, y)
      newRed = getRed(currentPixel) * 0.2
      newBlue = getBlue(currentPixel) * 0.4
      newGreen = getGreen(currentPixel) * 0.9
      newColor = makeColor(newRed, newGreen, newBlue)
      setColor(currentPixel, newColor)
  return picture
  
def chromaCopy(source, target, targetX, targetY):
  sourceWidth = getWidth(source)
  sourceHeight = getHeight(source)
  targetWidth = getWidth(target)
  targetHeight = getHeight(target)
  pureWhite = makeColor(255,255,255)
  
  # need to consider if the user inputs the copy destination outside the bounds of the 
  # target dimensions. will position the image so the right and bottom edges of the source
  # image will align with the right and bottom edges of the target image
  if (targetX + sourceWidth) > targetWidth:
    targetX = targetWidth - sourceWidth -1
  if (targetY + sourceHeight) > targetHeight:
    targetY = targetHeight - sourceHeight -1
    
  # copy the image to the target destination
  for x in range (sourceWidth):
    # create a new variable so we add the source image to the right place on the target
    newX = (targetX + x)
    for y in range (sourceHeight):
      # grab the working pixel from the SOURCE image and declare the new Y coordinate on
      # the target image
      sourcePixel = getPixel(source, x, y)
      newY = (targetY + y)
      
      # we check if the current pixel's color is close to pure white, and if it is, don't do
      # anything and continue with the next iteration of the loop. Otherwise, copy the source
      # pixel to the target image
      if distance(pureWhite, getColor(sourcePixel)) < 50:
          continue
      else:
        targetPixel = getPixel(target, newX, newY)
        sourceColor = getColor(sourcePixel)
        setColor(targetPixel, sourceColor)
  
  return target

#////////////////////
# Unique filter /////
#////////////////////

def mirrorDimension(picture):
  # decalre some variables
  picWidth = getWidth(picture)
  mirrorText = makePicture("C://temp//mirrorText.jpg")
  
  # Make the image negative first
  print("Entering the mirror dimension...")
  negativePic = makeNegative(picture)
  
  # run the image through the mirror function
  finishedMirror = mirror(picture)
  
  # Now we overlay some text to mirrored picture. Find the difference in widths from the picture
  # and the mirror text image. Center the text based on that value
  startX = (picWidth - getWidth(mirrorText)) / 2
  
  print("Only opposites exist here.")
  finalPicture = chromaCopy(mirrorText, finishedMirror, startX, 0)
  
  # done modifying, so we pass it back to the main function
  return finalPicture

# Unique filter helper functions
def makeNegative(picture):
  # get picture and save pixel data
  picWidth = getWidth(picture)
  picHeight = getHeight(picture)
  
  # invert each pixel. Each color has a range of 0-255 and 0 is opposite of 255. So, 1 is opposite to 254, 
  # so on for each value and each pair works both ways.
  for x in range(0, picWidth):
    for y in range(0, picHeight):
      currentPixel = getPixel(picture, x, y)
      setRed(currentPixel, (255 - getRed(currentPixel)))
      setBlue(currentPixel, (255 - getBlue(currentPixel)))
      setGreen(currentPixel, (255 - getGreen(currentPixel)))
      
  # output back to parent function
  return picture

# Mirror along two vertical axes, each at the quarter line. So we mirror the first quarter to 
# the second, the third to the fourth
def mirror(picture):
  picHeight = getHeight(picture)
  picWidth = getWidth(picture)
  
  print("Delving deeper...")
  
  # do the first quarter
  for x in range (0, (picWidth/4)):
    for y in range (0, picHeight):
      pixelCurrent = getPixel(picture, x, y)
      newPix = getPixel(picture, ((picWidth/2) - x - 1), y)
      pixelColor = getColor(pixelCurrent)
      setColor(newPix, pixelColor)
  
  print("Even further in...")
  
  # do the third quarter
  for x in range(0, (picWidth/4)):
    for y in range (0, picHeight):
      pixelCurrent = getPixel(picture, ((picWidth/2) + x), y)
      newPix = getPixel(picture, (picWidth - x - 1), y)
      pixelColor = getColor(pixelCurrent)
      setColor(newPix, pixelColor)
  
  # pass the image back
  return picture
